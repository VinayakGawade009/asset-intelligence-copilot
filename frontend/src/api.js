// API client — reads VITE_API_URL from env (default: http://localhost:8000)
const BASE = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

export async function getUsers() {
  const r = await fetch(`${BASE}/api/users`)
  if (!r.ok) throw new Error(`HTTP ${r.status}`)
  return r.json()
}

export async function getChats(userId) {
  const url = userId ? `${BASE}/api/chats?user_id=${encodeURIComponent(userId)}` : `${BASE}/api/chats`
  const r = await fetch(url)
  if (!r.ok) throw new Error(`HTTP ${r.status}`)
  return r.json()
}

export async function getChatDetail(chatId) {
  const r = await fetch(`${BASE}/api/chats/${encodeURIComponent(chatId)}`)
  if (!r.ok) throw new Error(`HTTP ${r.status}`)
  return r.json()
}

export async function postChat(userId, chatId, message) {
  const r = await fetch(`${BASE}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: userId, chat_id: chatId ?? null, message }),
    signal: AbortSignal.timeout(180_000), // 180 s
  })
  if (!r.ok) {
    const text = await r.text().catch(() => '')
    throw new Error(`HTTP ${r.status}${text ? ': ' + text : ''}`)
  }
  return r.json()
}
