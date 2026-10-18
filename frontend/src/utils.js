// Utility: get initials from name
export function initials(name) {
  if (!name) return '?'
  return name.split(' ').map(w => w[0]).slice(0, 2).join('').toUpperCase()
}

// Utility: format role string
export function formatRole(role) {
  if (!role) return ''
  return role.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

// Detect ID-like tokens in markdown text (WELL-XXXX, INS-XXXX-XXXX, MNT-..., REG-..., CTX-...)
const ID_PATTERN = /\b(WELL-\d{4}|INS-\d{4}-\d{4}|MNT-\d{4}-\d{3}|REG-\d{4}-\d{3}|CTX-\d{4}-\d{3}|CLAIM-\d{4}-[a-z0-9]+)\b/g

export function extractIds(text) {
  if (!text) return []
  const matches = [...text.matchAll(ID_PATTERN)]
  return [...new Set(matches.map(m => m[0]))]
}

// Heatmap color interpolation: 0 → heat-low → heat-mid → heat-high
export function heatColor(value, max) {
  if (max === 0) return { bg: '#1A222D', text: '#5B6675' }
  const t = Math.min(value / max, 1)
  if (t === 0) return { bg: '#1A222D', text: '#5B6675' }
  if (t <= 0.5) {
    // #1A222D → #FBBF24
    const s = t * 2
    const r = Math.round(26 + (251 - 26) * s)
    const g = Math.round(34 + (191 - 34) * s)
    const b = Math.round(45 + (36 - 45) * s)
    const textLight = s > 0.6
    return {
      bg: `rgb(${r},${g},${b})`,
      text: textLight ? '#0B0F14' : '#E6EDF3'
    }
  } else {
    // #FBBF24 → #F43F5E
    const s = (t - 0.5) * 2
    const r = Math.round(251 + (244 - 251) * s)
    const g = Math.round(191 + (63 - 191) * s)
    const b = Math.round(36 + (94 - 36) * s)
    return { bg: `rgb(${r},${g},${b})`, text: '#FFFFFF' }
  }
}

// Get tone CSS class
export function toneClass(tone) {
  const map = { ok: 'ok', warning: 'warning', critical: 'critical', unconfirmed: 'unconfirmed', neutral: 'neutral' }
  return map[tone] ?? 'neutral'
}

// Get today string from VITE_TODAY env or dynamic date
export function getToday() {
  return import.meta.env.VITE_TODAY ?? new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' })
}

// Pinned users (shown at top of user picker if configured)
export const PINNED_USER_IDS = []

// Example queries for empty state
export const EXAMPLE_QUERIES = [
  { label: 'Area Status', text: 'Which wells in Northeast Block 8 are not producing oil right now, and why? Show them in a table.' },
  { label: 'Downtime Ranking', text: 'Which 3 wells in Northeast Block 7 had the most downtime in the last 4 months? Show a bar chart.' },
  { label: 'Spills Map', text: 'Show on a map every well in Northeast Block 8 with a real spill in the last 90 days.' },
  { label: 'Spills Heatmap', text: 'Show a heatmap of spills by geographic area and month.' },
]
