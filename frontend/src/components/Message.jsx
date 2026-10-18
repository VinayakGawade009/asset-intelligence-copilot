import React, { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { FlagBanner, Chip } from './Primitives.jsx'
import { VisualRenderer } from './Visuals.jsx'
import { extractIds } from '../utils.js'

// Regex to find ID tokens in markdown text for inline chip rendering
const ID_RE = /\b(WELL-\d{4}|INS-\d{4}-\d{4}|MNT-\d{4}-\d{3}|REG-\d{4}-\d{3}|CTX-\d{4}-\d{3}|CLAIM-\d{4}-[a-z0-9]+)\b/g

function InlineChipText({ text, citations, onChipClick }) {
  const parts = []
  let last = 0
  let m
  ID_RE.lastIndex = 0
  while ((m = ID_RE.exec(text)) !== null) {
    if (m.index > last) parts.push(text.slice(last, m.index))
    parts.push(<Chip key={`${m[0]}-${m.index}`} id={m[0]} citations={citations} onChipClick={onChipClick} />)
    last = m.index + m[0].length
  }
  if (last < text.length) parts.push(text.slice(last))
  return <>{parts}</>
}

// Custom renderer that injects chips for ID tokens
function makeMarkdownComponents(citations, onChipClick) {
  function processNode(children) {
    if (!children) return null
    const arr = React.Children.toArray(children)
    return arr.flatMap((child, i) => {
      if (typeof child === 'string') {
        return [<InlineChipText key={i} text={child} citations={citations} onChipClick={onChipClick} />]
      }
      return [child]
    })
  }

  return {
    p: ({ children }) => <p>{processNode(children)}</p>,
    strong: ({ children }) => <strong style={{ fontWeight: 600, color: 'var(--cyan)' }}>{processNode(children)}</strong>,
    li: ({ children }) => <li>{processNode(children)}</li>,
  }
}

// ============================================================
//  LoadingState
// ============================================================
const STEPS = ['Choosing a tool', 'Querying the records', 'Writing the answer', 'Checking citations', 'Verifying flags']

export function LoadingState({ elapsed }) {
  const stepIdx = Math.floor((elapsed / 8) % STEPS.length)
  return (
    <div className="loading-state">
      <div className="loading-dots">
        <div className="loading-dot" />
        <div className="loading-dot" />
        <div className="loading-dot" />
      </div>
      <div style={{ flex: 1 }}>
        <div className="loading-text">Working on it…</div>
        <div className="loading-step">{STEPS[stepIdx]}</div>
        <div className="loading-timer">{elapsed}s elapsed</div>
      </div>
    </div>
  )
}

// ============================================================
//  ErrorState
// ============================================================
export function ErrorState({ message, detail, onRetry }) {
  const [showDetail, setShowDetail] = useState(false)
  return (
    <div className="error-state">
      <div className="error-title">⚠ Request failed</div>
      <div className="error-msg">
        {message.includes('Failed to fetch') || message.includes('NetworkError') || message.includes('Unable to connect')
          ? 'Cannot reach the server. Please check that the backend is running.'
          : message}
      </div>
      <div style={{ display: 'flex', gap: 8, marginTop: 8, flexWrap: 'wrap' }}>
        <button className="btn-retry" onClick={onRetry}>↺ Retry</button>
        {detail && (
          <button
            className="btn-secondary"
            style={{ fontSize: 12 }}
            onClick={() => setShowDetail(d => !d)}
          >
            {showDetail ? 'Hide details' : 'Show details'}
          </button>
        )}
      </div>
      {showDetail && detail && (
        <div className="error-details">{detail}</div>
      )}
    </div>
  )
}

// ============================================================
//  CitationDrawer
// ============================================================
export function CitationDrawer({ citation, flags = [], onClose }) {
  if (!citation) return null
  const relatedFlags = flags.filter(f => f.source_ids?.includes(citation.id))

  function handleCopyId() {
    navigator.clipboard?.writeText(citation.id).catch(() => {})
  }

  const KIND_ICONS = {
    inspection: '🔍',
    maintenance: '🔧',
    regulatory: '📋',
    note: '📝',
    document: '📄',
  }

  return (
    <div className="drawer-overlay" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="drawer">
        <div className="drawer-header">
          <span className="drawer-title">Record Detail</span>
          <button className="btn-icon" onClick={onClose} style={{ padding: '4px 6px' }}>✕</button>
        </div>
        <div className="drawer-body">
          <div className="drawer-kind">
            <span style={{ fontSize: 20 }}>{KIND_ICONS[citation.kind] ?? '📎'}</span>
            <span className="drawer-kind-badge">{citation.kind}</span>
          </div>
          <div className="drawer-id">{citation.id}</div>
          <div className="drawer-label">{citation.label}</div>
          <div className="drawer-detail">{citation.detail}</div>

          {relatedFlags.length > 0 && (
            <div className="drawer-flags">
              <div className="drawer-flags-title">Flags referencing this record</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                {relatedFlags.map((f, i) => (
                  <FlagBanner key={i} flag={f} />
                ))}
              </div>
            </div>
          )}

          <button className="btn-copy-id" onClick={handleCopyId}>
            <span>⎘</span> Copy ID
          </button>
        </div>
      </div>
    </div>
  )
}

// ============================================================
//  CorrectionModal
// ============================================================
export function CorrectionModal({ response, onClose, onSubmit }) {
  const [field, setField] = useState('')
  const [original, setOriginal] = useState('')
  const [corrected, setCorrected] = useState('')
  const [reason, setReason] = useState('')
  const [scope, setScope] = useState('this_well')

  function handleSubmit(e) {
    e.preventDefault()
    if (!corrected.trim()) return
    const target = scope === 'all_type'
      ? `all wells of this type`
      : response?.visual?.well_id ?? 'this record'
    const msg = `The ${field || 'value'} for ${target} is wrong; the correct value is ${corrected}${reason ? ` because ${reason}` : ''}.`
    onSubmit(msg)
    onClose()
  }

  return (
    <div className="modal-overlay" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="modal">
        <div className="modal-header">
          <span style={{ fontSize: 15, fontWeight: 600 }}>Correct this response</span>
          <button className="btn-icon" onClick={onClose} style={{ padding: '4px 6px' }}>✕</button>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="modal-body">
            <div>
              <label className="field-label">Field / what is wrong</label>
              <input
                className="field-input"
                placeholder="e.g. producing status, wellhead temperature"
                value={field}
                onChange={e => setField(e.target.value)}
              />
            </div>
            <div>
              <label className="field-label">Original value (from response)</label>
              <input
                className="field-input"
                placeholder="What the copilot said"
                value={original}
                onChange={e => setOriginal(e.target.value)}
              />
            </div>
            <div>
              <label className="field-label">Corrected value *</label>
              <input
                className="field-input"
                placeholder="The correct value"
                value={corrected}
                required
                onChange={e => setCorrected(e.target.value)}
              />
            </div>
            <div>
              <label className="field-label">Reason (optional)</label>
              <textarea
                className="field-textarea"
                placeholder="Why is this wrong?"
                value={reason}
                onChange={e => setReason(e.target.value)}
              />
            </div>
            <div>
              <label className="field-label">Scope</label>
              <select className="field-select" value={scope} onChange={e => setScope(e.target.value)}>
                <option value="this_well">This well only</option>
                <option value="all_type">All wells of this type</option>
              </select>
            </div>
          </div>
          <div className="modal-footer">
            <button type="button" className="btn-secondary" onClick={onClose}>Cancel</button>
            <button type="submit" className="btn-primary">Send correction</button>
          </div>
        </form>
      </div>
    </div>
  )
}

// ============================================================
//  AssistantMessage
// ============================================================
export function AssistantMessage({ response, onChipClick, onSendMessage }) {
  const [thumbs, setThumbs] = useState(null)
  const [copied, setCopied] = useState(false)
  const [showCorrection, setShowCorrection] = useState(false)

  if (!response) return null
  const { answer, visual, citations = [], flags = [], meta } = response

  function handleCopy() {
    navigator.clipboard?.writeText(answer).catch(() => {})
    setCopied(true)
    setTimeout(() => setCopied(false), 1500)
  }

  function handleCorrection(msg) {
    onSendMessage?.(msg)
  }

  const mdComponents = makeMarkdownComponents(citations, onChipClick)

  const footerText = [
    meta?.model,
    meta?.latency_ms ? `${(meta.latency_ms / 1000).toFixed(1)} s` : null,
    meta?.tool_calls?.length ? `tools: ${meta.tool_calls.join(', ')}` : null,
  ].filter(Boolean).join(' · ')

  return (
    <>
      <div className="assistant-msg">
        {/* Header */}
        <div className="assistant-msg-header">
          <div className="assistant-msg-brand">
            <div className="assistant-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
              </svg>
            </div>
            <div>
              <div className="assistant-title">Asset Intelligence Copilot</div>
              <div className="assistant-subtitle">ASSET INTELLIGENCE ENGINE</div>
            </div>
          </div>
        </div>

        {/* Answer text — always first, never empty gap */}
        <div className="answer-text">
          {answer && answer.trim()
            ? <ReactMarkdown components={mdComponents}>{answer}</ReactMarkdown>
            : <p style={{ color: 'var(--text-secondary)', fontStyle: 'italic' }}>The copilot returned an empty response. Please try rephrasing your question.</p>
          }
        </div>

        {/* Visual */}
        {visual && (
          <VisualRenderer
            visual={visual}
            citations={citations}
            onChipClick={onChipClick}
            onSendMessage={onSendMessage}
          />
        )}

        {/* Flag banners */}
        {flags.length > 0 && (
          <div className="flags-list">
            {flags.map((flag, i) => (
              <FlagBanner key={i} flag={flag} citations={citations} onChipClick={onChipClick} />
            ))}
          </div>
        )}

        {/* Citation chips strip */}
        {citations.length > 0 && (
          <div>
            <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10, textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--text-tertiary)', marginBottom: 6 }}>
              REFERENCED RECORDS
            </div>
            <div className="chips-strip">
              {citations.map(cit => (
                <button
                  key={cit.id}
                  className="chip"
                  onClick={() => onChipClick?.(cit)}
                  title={cit.label}
                >
                  {cit.id}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="msg-footer">
          <div className="msg-footer-meta">{footerText}</div>
          <div className="msg-actions" style={{ display: 'flex', alignItems: 'center', gap: 4, flexWrap: 'wrap' }}>
            <button className={`btn-icon ${copied ? 'active' : ''}`} onClick={handleCopy} title="Copy answer">
              {copied ? '✓' : '⎘'} Copy
            </button>
            <button
              className={`btn-icon ${thumbs === 'up' ? 'active' : ''}`}
              onClick={() => setThumbs(t => t === 'up' ? null : 'up')}
              title="Good response"
            >
              👍
            </button>
            <button
              className={`btn-icon ${thumbs === 'down' ? 'active' : ''}`}
              onClick={() => setThumbs(t => t === 'down' ? null : 'down')}
              title="Bad response"
            >
              👎
            </button>
            <button className="btn-correct" onClick={() => setShowCorrection(true)}>
              ✏ Correct this
            </button>
          </div>
        </div>
      </div>

      {showCorrection && (
        <CorrectionModal
          response={response}
          onClose={() => setShowCorrection(false)}
          onSubmit={handleCorrection}
        />
      )}
    </>
  )
}
