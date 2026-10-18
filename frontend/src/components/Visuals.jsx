import React, { useMemo } from 'react'
import { heatColor } from '../utils.js'

// ============================================================
//  StatusCard
// ============================================================
export function StatusCard({ visual, citations = [], onChipClick }) {
  if (!visual) return null
  const { well_id, name, area, well_type, producing, headline, recorded_status, metrics = [], badges = [], last_inspection } = visual
  const stale = recorded_status === 'active' && !producing

  return (
    <div className="visual-card">
      <div className="visual-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span className="t-mono-tag text-cyan">{well_id}</span>
          {well_type && <span className="t-mono-tag" style={{ color: 'var(--text-tertiary)' }}>{well_type}</span>}
        </div>
        <span className={`tone-badge ${producing ? 'ok' : 'warning'}`}>
          {producing ? 'PRODUCING' : 'SHUT IN'}
        </span>
      </div>
      <div className="visual-body">
        <div className="status-card-headline">
          <span style={{ fontSize: 20, fontWeight: 600, fontFamily: 'var(--font-mono)' }}>{name || well_id}</span>
        </div>
        {area && <div className="status-card-area">{area}</div>}
        <div style={{ fontSize: 18, fontWeight: 600, marginBottom: 12, color: producing ? 'var(--ok-base)' : 'var(--warning-base)' }}>
          {headline}
        </div>

        {metrics.length > 0 && (
          <div className="status-card-metrics">
            {metrics.map((m, i) => (
              <div key={i} className="metric-tile">
                <div className="metric-tile-label">{m.label}</div>
                <div style={{ marginTop: 4 }}>
                  <span className="t-display">{m.value}</span>
                  <span className="metric-tile-unit">{m.unit}</span>
                </div>
              </div>
            ))}
          </div>
        )}

        {badges.length > 0 && (
          <div className="status-card-badges">
            {badges.map((b, i) => (
              <span key={i} className={`tone-badge ${b.tone || 'neutral'}`}>{b.text}</span>
            ))}
          </div>
        )}

        <div className="status-card-recorded">
          Recorded status: <span className={stale ? 'status-card-stale' : ''}>{recorded_status}</span>
          {stale && <span className="status-card-stale"> — out of date</span>}
        </div>

        {last_inspection && (
          <div className="status-card-inspection" style={{ marginTop: 8 }}>
            <span style={{ color: 'var(--text-secondary)', fontSize: 12 }}>Last inspection:</span>
            <button
              className="chip"
              onClick={() => {
                const cit = citations.find(c => c.id === last_inspection.id)
                if (cit) onChipClick?.(cit)
              }}
            >
              {last_inspection.id}
            </button>
            <span style={{ fontSize: 12, color: 'var(--text-secondary)' }}>{last_inspection.date} · {last_inspection.by}</span>
          </div>
        )}
      </div>
    </div>
  )
}

// ============================================================
//  DataTable
// ============================================================
const ID_RE = /^(WELL-\d{4}|INS-\d{4}-\d{4}|MNT-\d{4}-\d{3}|REG-\d{4}-\d{3}|CTX-\d{4}-\d{3}|CLAIM-\d{4}-[a-z0-9]+)$/

export function DataTable({ visual, citations = [], onChipClick }) {
  if (!visual) return null
  const { title, columns = [], rows = [] } = visual
  const [sortKey, setSortKey] = React.useState(null)
  const [sortDir, setSortDir] = React.useState('asc')

  const sortedRows = useMemo(() => {
    if (!sortKey) return rows
    return [...rows].sort((a, b) => {
      const av = a[sortKey] ?? ''
      const bv = b[sortKey] ?? ''
      const n = parseFloat(av) - parseFloat(bv)
      if (!isNaN(n)) return sortDir === 'asc' ? n : -n
      return sortDir === 'asc'
        ? String(av).localeCompare(String(bv))
        : String(bv).localeCompare(String(av))
    })
  }, [rows, sortKey, sortDir])

  function toggleSort(key) {
    if (sortKey === key) setSortDir(d => d === 'asc' ? 'desc' : 'asc')
    else { setSortKey(key); setSortDir('asc') }
  }

  if (!rows.length) return (
    <div className="visual-fallback">
      <span>No data returned for this query.</span>
    </div>
  )

  return (
    <div className="visual-card">
      {title && <div className="visual-header"><span className="visual-title">{title}</span></div>}
      <div className="data-table-wrap">
        <table className="data-table">
          <thead>
            <tr>
              {columns.map(col => (
                <th key={col.key} onClick={() => toggleSort(col.key)}>
                  {col.label}
                  {sortKey === col.key && <span className="sort-icon">{sortDir === 'asc' ? '▲' : '▼'}</span>}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sortedRows.map((row, ri) => (
              <tr key={ri}>
                {columns.map(col => {
                  const val = row[col.key]
                  const isId = val && ID_RE.test(String(val))
                  const cit = isId ? citations.find(c => c.id === val) : null
                  return (
                    <td key={col.key}>
                      {isId ? (
                        <button className="chip" onClick={() => cit && onChipClick?.(cit)}>{val}</button>
                      ) : (
                        val ?? '—'
                      )}
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

// ============================================================
//  LineChart
// ============================================================
import {
  ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ReferenceLine, ReferenceArea, Legend
} from 'recharts'

function LineChartTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null
  return (
    <div className="chart-tooltip">
      <div className="chart-tooltip-label">{label}</div>
      {payload.map(p => (
        <div key={p.name} style={{ color: p.stroke, fontFamily: 'var(--font-mono)', fontSize: 12 }}>
          {p.name}: <strong>{p.value}</strong>
        </div>
      ))}
    </div>
  )
}

export function LineChartVisual({ visual }) {
  if (!visual) return null
  const { title, x = [], x_label, y_label, series = [], markers = [] } = visual

  // Build chart data
  const data = x.map((xv, i) => {
    const point = { x: xv }
    series.forEach(s => { point[s.name] = s.values[i] ?? null })
    return point
  })

  const colors = { Wellhead: 'var(--wellhead-orange)', Air: 'var(--ambient-cyan)' }
  const defaultColors = ['var(--wellhead-orange)', 'var(--ambient-cyan)', '#A78BFA', '#34D399']

  // Tick formatter: show every 30th date label
  const tickStep = Math.max(1, Math.floor(x.length / 8))
  const formatTick = (v, i) => (i % tickStep === 0 ? v.slice(0, 7) : '')

  return (
    <div className="visual-card">
      {title && <div className="visual-header"><span className="visual-title">{title}</span></div>}
      <div style={{ padding: '16px 16px 8px' }}>
        <div className="chart-container">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={data} margin={{ top: 8, right: 20, left: 0, bottom: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border-hairline)" vertical={false} />
              <XAxis
                dataKey="x"
                tickFormatter={formatTick}
                tick={{ fill: 'var(--text-secondary)', fontSize: 10, fontFamily: 'var(--font-mono)' }}
                axisLine={{ stroke: 'var(--border)' }}
                tickLine={false}
                label={x_label ? { value: x_label, position: 'insideBottom', offset: -10, fill: 'var(--text-secondary)', fontSize: 11 } : undefined}
              />
              <YAxis
                tick={{ fill: 'var(--text-secondary)', fontSize: 10, fontFamily: 'var(--font-mono)' }}
                axisLine={false}
                tickLine={false}
                label={y_label ? { value: y_label, angle: -90, position: 'insideLeft', fill: 'var(--text-secondary)', fontSize: 11 } : undefined}
              />
              <Tooltip content={<LineChartTooltip />} />
              <Legend
                iconSize={8}
                wrapperStyle={{ fontSize: 11, fontFamily: 'var(--font-mono)', color: 'var(--text-secondary)' }}
              />
              {markers.map((m, i) => (
                <ReferenceLine
                  key={i}
                  x={m.x}
                  stroke="var(--critical-base)"
                  strokeDasharray="4 2"
                  label={{ value: m.label, fill: 'var(--critical-base)', fontSize: 10, dy: -6 }}
                />
              ))}
              {series.map((s, i) => (
                <Line
                  key={s.name}
                  type="monotone"
                  dataKey={s.name}
                  stroke={colors[s.name] ?? defaultColors[i % defaultColors.length]}
                  dot={false}
                  strokeWidth={2}
                  connectNulls
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}

// ============================================================
//  BarChart
// ============================================================
import { BarChart, Bar, Cell } from 'recharts'

export function BarChartVisual({ visual }) {
  if (!visual) return null
  const { title, categories = [], unit, series = [] } = visual

  // Build data
  const mainSeries = series[0] ?? { name: '', values: [] }
  const data = categories.map((cat, i) => ({
    cat,
    value: mainSeries.values[i] ?? 0,
  }))
  const maxVal = Math.max(...data.map(d => d.value), 1)

  return (
    <div className="visual-card">
      {title && <div className="visual-header"><span className="visual-title">{title}</span></div>}
      <div style={{ padding: '16px 16px 8px' }}>
        <div className="bar-chart-container">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data} layout="vertical" margin={{ top: 4, right: 60, left: 80, bottom: 4 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border-hairline)" horizontal={false} />
              <XAxis
                type="number"
                tick={{ fill: 'var(--text-secondary)', fontSize: 10, fontFamily: 'var(--font-mono)' }}
                axisLine={{ stroke: 'var(--border)' }}
                tickLine={false}
                label={unit ? { value: unit, position: 'insideBottom', offset: -4, fill: 'var(--text-secondary)', fontSize: 11 } : undefined}
              />
              <YAxis
                type="category"
                dataKey="cat"
                width={75}
                tick={{ fill: 'var(--text-secondary)', fontSize: 11, fontFamily: 'var(--font-mono)' }}
                axisLine={false}
                tickLine={false}
              />
              <Tooltip
                content={({ active, payload }) => {
                  if (!active || !payload?.length) return null
                  return (
                    <div className="chart-tooltip">
                      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 12, color: 'var(--text-primary)' }}>
                        {payload[0]?.payload?.cat}: <strong>{payload[0]?.value}</strong> {unit}
                      </div>
                    </div>
                  )
                }}
              />
              <Bar dataKey="value" radius={[0, 2, 2, 0]} label={{ position: 'right', fill: 'var(--text-secondary)', fontSize: 11, fontFamily: 'var(--font-mono)', formatter: (v) => `${v} ${unit ?? ''}` }}>
                {data.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={entry.value === maxVal ? 'var(--critical-base)' : 'var(--ambient-cyan)'}
                    fillOpacity={0.8}
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}

// ============================================================
//  Map
// ============================================================
import { MapContainer, TileLayer, CircleMarker, Popup, useMap } from 'react-leaflet'

const TONE_COLORS = {
  ok: '#34D399',
  warning: '#FBBF24',
  critical: '#F43F5E',
  unconfirmed: '#A78BFA',
  neutral: '#94A3B8',
}

function FitBounds({ pins }) {
  const map = useMap()
  React.useEffect(() => {
    if (pins.length === 0) return
    const lats = pins.map(p => p.lat)
    const lons = pins.map(p => p.lon)
    const bounds = [[Math.min(...lats), Math.min(...lons)], [Math.max(...lats), Math.max(...lons)]]
    if (bounds[0][0] === bounds[1][0] && bounds[0][1] === bounds[1][1]) {
      map.setView([bounds[0][0], bounds[0][1]], 12)
    } else {
      map.fitBounds(bounds, { padding: [32, 32] })
    }
  }, [pins, map])
  return null
}

export function MapVisual({ visual }) {
  if (!visual) return null
  const { title, center, pins = [] } = visual

  const centerPos = center && center.lat !== 0 ? [center.lat, center.lon] : [34.05, -118.24]

  // Collect tone types for legend
  const tones = [...new Set(pins.map(p => p.tone))]

  return (
    <div className="visual-card">
      {title && <div className="visual-header"><span className="visual-title">{title}</span></div>}
      <div style={{ padding: 16 }}>
        <div className="map-container">
          <MapContainer
            center={centerPos}
            zoom={10}
            style={{ height: '100%', width: '100%', background: 'var(--canvas)', borderRadius: 6 }}
            zoomControl={true}
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='© <a href="https://openstreetmap.org">OpenStreetMap</a>'
              style={{ filter: 'invert(1) hue-rotate(180deg) brightness(0.7) contrast(0.9)' }}
              className="dark-tiles"
            />
            <FitBounds pins={pins} />
            {pins.map((pin, i) => (
              <CircleMarker
                key={i}
                center={[pin.lat, pin.lon]}
                radius={8}
                pathOptions={{
                  color: TONE_COLORS[pin.tone] ?? TONE_COLORS.neutral,
                  fillColor: TONE_COLORS[pin.tone] ?? TONE_COLORS.neutral,
                  fillOpacity: 0.85,
                  weight: 2,
                }}
              >
                <Popup>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: 12, background: 'var(--surface-2)', color: 'var(--text-primary)', border: 'none' }}>
                    <div style={{ fontWeight: 600 }}>{pin.label}</div>
                    {pin.detail && <div style={{ color: 'var(--text-secondary)', marginTop: 4 }}>{pin.detail}</div>}
                  </div>
                </Popup>
              </CircleMarker>
            ))}
          </MapContainer>
        </div>
        {/* Legend */}
        {tones.length > 0 && (
          <div style={{ display: 'flex', gap: 12, marginTop: 8, flexWrap: 'wrap' }}>
            {tones.map(tone => (
              <div key={tone} style={{ display: 'flex', alignItems: 'center', gap: 4, fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--text-secondary)' }}>
                <div style={{ width: 10, height: 10, borderRadius: '50%', background: TONE_COLORS[tone] ?? TONE_COLORS.neutral }} />
                {tone}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

// ============================================================
//  Heatmap
// ============================================================
export function HeatmapVisual({ visual, onSendMessage }) {
  if (!visual) return null
  const { title, rows = [], cols = [], values = [], unit } = visual

  // Compute stats
  const allVals = values.flat().filter(v => v != null)
  const maxVal = Math.max(...allVals, 1)
  const rowTotals = values.map(row => row.reduce((a, b) => a + (b ?? 0), 0))
  const highestRow = rowTotals.indexOf(Math.max(...rowTotals))
  const lowestRow = rowTotals.indexOf(Math.min(...rowTotals))

  return (
    <div className="visual-card">
      {title && <div className="visual-header"><span className="visual-title">{title}</span></div>}
      <div className="visual-body">
        {/* Summary stats */}
        <div className="heatmap-summary">
          <div className="heatmap-stat">Total: <span>{allVals.reduce((a, b) => a + b, 0)} {unit}</span></div>
          {rows[highestRow] && <div className="heatmap-stat">Highest: <span>{rows[highestRow]}</span> ({rowTotals[highestRow]} {unit})</div>}
          {rows[lowestRow] !== rows[highestRow] && rows[lowestRow] && (
            <div className="heatmap-stat">Lowest: <span>{rows[lowestRow]}</span> ({rowTotals[lowestRow]} {unit})</div>
          )}
        </div>

        {/* Grid */}
        <div className="heatmap-grid">
          {/* Header */}
          <div className="heatmap-header-row">
            <div className="heatmap-row-label" style={{ fontSize: 10, textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--text-tertiary)' }}>Area</div>
            {cols.map(col => (
              <div key={col} className="heatmap-col-header">{col}</div>
            ))}
            <div style={{ width: 48, textAlign: 'center', fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--cyan)', textTransform: 'uppercase' }}>Total</div>
          </div>

          {/* Rows */}
          {rows.map((row, ri) => (
            <div key={ri} className="heatmap-row">
              <div className="heatmap-row-label">
                <span title={row}>{row}</span>
              </div>
              {cols.map((col, ci) => {
                const val = values[ri]?.[ci] ?? 0
                const { bg, text } = heatColor(val, maxVal)
                return (
                  <button
                    key={ci}
                    className="heatmap-cell"
                    style={{ background: bg, color: text }}
                    onClick={() => onSendMessage?.(`Show the spills for ${row} in ${col}`)}
                    title={`${row} · ${col}: ${val} ${unit ?? ''}`}
                  >
                    {val}
                  </button>
                )
              })}
              <div className="heatmap-total-col">{rowTotals[ri]}</div>
            </div>
          ))}
        </div>

        {/* Legend */}
        <div className="heatmap-legend">
          <span>0</span>
          <div className="heatmap-legend-ramp" />
          <span>{maxVal} {unit}</span>
        </div>
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--text-tertiary)', marginTop: 8 }}>
          Click any cell to query filtered incident records.
        </div>
      </div>
    </div>
  )
}

// ============================================================
//  VisualRenderer — switch on visual.type
// ============================================================
export function VisualRenderer({ visual, citations = [], onChipClick, onSendMessage }) {
  if (!visual) return null

  try {
    switch (visual.type) {
      case 'status_card':
        return <StatusCard visual={visual} citations={citations} onChipClick={onChipClick} />
      case 'table':
        return <DataTable visual={visual} citations={citations} onChipClick={onChipClick} />
      case 'line_chart':
        return <LineChartVisual visual={visual} />
      case 'bar_chart':
        return <BarChartVisual visual={visual} />
      case 'map':
        return <MapVisual visual={visual} />
      case 'heatmap':
        return <HeatmapVisual visual={visual} onSendMessage={onSendMessage} />
      default:
        return (
          <div className="visual-fallback">
            <span>⚠ Unknown visual type: <code>{visual.type}</code></span>
          </div>
        )
    }
  } catch (err) {
    return (
      <div className="visual-fallback">
        <span>⚠ Could not render visual: {err.message}</span>
      </div>
    )
  }
}
