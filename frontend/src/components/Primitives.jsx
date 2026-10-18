import React from 'react'
import { toneClass } from '../utils.js'

// --- ToneBadge ---
export function ToneBadge({ tone, text }) {
  return (
    <span className={`tone-badge ${toneClass(tone)}`}>
      <ToneIcon tone={tone} size={12} />
      {text}
    </span>
  )
}

// --- ToneIcon (inline SVG icons via lucide-react pattern) ---
export function ToneIcon({ tone, size = 14 }) {
  const s = size
  const props = { width: s, height: s, viewBox: '0 0 24 24', fill: 'none', strokeWidth: 2, stroke: 'currentColor', strokeLinecap: 'round', strokeLinejoin: 'round' }
  if (tone === 'ok') return (
    <svg {...props}><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
  )
  if (tone === 'warning') return (
    <svg {...props}><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>
  )
  if (tone === 'critical') return (
    <svg {...props}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>
  )
  if (tone === 'unconfirmed') return (
    <svg {...props}><circle cx="12" cy="12" r="10"/><line x1="12" x2="12.01" y1="8" y2="8"/><path d="M12 12v4"/></svg>
  )
  return (
    <svg {...props}><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="16"/><line x1="12" x2="12.01" y1="12" y2="12"/></svg>
  )
}

// --- FlagKind icon ---
export function FlagKindIcon({ kind, size = 14 }) {
  const s = size
  const p = { width: s, height: s, viewBox: '0 0 24 24', fill: 'none', strokeWidth: 2, stroke: 'currentColor', strokeLinecap: 'round', strokeLinejoin: 'round' }
  if (kind === 'conflict') return <svg {...p}><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>
  if (kind === 'overdue') return <svg {...p}><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
  if (kind === 'unconfirmed') return <svg {...p}><circle cx="12" cy="12" r="10"/><line x1="12" x2="12.01" y1="8" y2="8"/><path d="M12 12v4"/></svg>
  if (kind === 'correction_applied') return <svg {...p}><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
  // no_cause
  return <svg {...p}><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>
}

const FLAG_LABELS = {
  conflict: 'CONFLICT',
  overdue: 'OVERDUE',
  unconfirmed: 'UNCONFIRMED',
  correction_applied: 'CORRECTION APPLIED',
  no_cause: 'NO CAUSE IDENTIFIED',
}

// --- FlagBanner ---
export function FlagBanner({ flag, citations = [], onChipClick }) {
  const kind = flag.kind
  return (
    <div className={`flag-banner ${kind}`}>
      <span className={`flag-icon ${kind}`}><FlagKindIcon kind={kind} size={14} /></span>
      <div style={{ flex: 1 }}>
        <div className="flag-label">{FLAG_LABELS[kind] ?? kind}</div>
        <div className="flag-text">{flag.text}</div>
        {flag.source_ids?.length > 0 && (
          <div className="flag-chips">
            {flag.source_ids.map(id => {
              const cit = citations.find(c => c.id === id)
              return (
                <button
                  key={id}
                  className="chip"
                  onClick={() => cit && onChipClick?.(cit)}
                  title={cit?.label ?? id}
                >
                  {id}
                </button>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}

// --- Chip (inline entity tag) ---
export function Chip({ id, citations = [], onChipClick }) {
  const cit = citations.find(c => c.id === id)
  return (
    <button
      className="chip"
      style={{ fontSize: 11, padding: '1px 6px' }}
      onClick={() => cit && onChipClick?.(cit)}
      title={cit?.label ?? id}
    >
      {id}
    </button>
  )
}
