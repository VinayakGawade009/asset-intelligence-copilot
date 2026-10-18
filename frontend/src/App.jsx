import React, { useState, useEffect, useRef, useCallback } from 'react'
import { Sidebar } from './components/Sidebar.jsx'
import { UserPickerModal } from './components/Sidebar.jsx'
import { AssistantMessage, LoadingState, ErrorState, CitationDrawer } from './components/Message.jsx'
import { getToday, EXAMPLE_QUERIES } from './utils.js'
import { getUsers, getChats, getChatDetail, postChat } from './api.js'

// ============================================================
//  EmptyChat
// ============================================================
function EmptyChat({ userName, onQuery }) {
  const firstName = userName?.split(' ')[0] ?? 'there'
  return (
    <div className="empty-chat">
      <div className="empty-greeting">Hello, {firstName}.</div>
      <div className="empty-hint">
        Ask me anything about your wells, inspections, maintenance, or compliance records.
      </div>
      <div className="example-cards">
        {EXAMPLE_QUERIES.map((q, i) => (
          <button key={i} className="example-card" onClick={() => onQuery(q.text)}>
            <div className="example-card-label">{q.label}</div>
            <div className="example-card-text">{q.text}</div>
          </button>
        ))}
      </div>
      <div className="teach-hint">
        You can also teach me — submit a correction on any response to update my knowledge.
      </div>
    </div>
  )
}

// ============================================================
//  UserMessage
// ============================================================
function UserMessage({ text, userName }) {
  const label = userName ? `OPERATOR // ${userName.toUpperCase()}` : 'OPERATOR'
  return (
    <div className="user-msg-wrap">
      <div className="user-msg">
        <div className="user-msg-header">
          <span className="user-msg-label">{label}</span>
        </div>
        <div className="user-msg-text">{text}</div>
      </div>
    </div>
  )
}

// ============================================================
//  App
// ============================================================
export default function App() {
  // Data
  const [users, setUsers] = useState([])
  const [currentUser, setCurrentUser] = useState(null)
  const [chats, setChats] = useState([])
  const [activeChatId, setActiveChatId] = useState(null)
  const [messages, setMessages] = useState([]) // [{role, text, response?, status?, error?}]

  // UI state
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [elapsed, setElapsed] = useState(0)
  const [errorMsg, setErrorMsg] = useState(null)
  const [errorDetail, setErrorDetail] = useState(null)
  const [pendingMsg, setPendingMsg] = useState(null)
  const [openCitation, setOpenCitation] = useState(null)
  const [showUserPicker, setShowUserPicker] = useState(false)

  const threadRef = useRef(null)
  const timerRef = useRef(null)
  const inputRef = useRef(null)

  // Load users on mount
  useEffect(() => {
    getUsers()
      .then(us => {
        setUsers(us)
        // Default to first user in list
        const defaultUser = us[0] ?? null
        setCurrentUser(defaultUser)
      })
      .catch(err => {
        console.error('Failed to load users:', err)
      })
  }, [])

  // Load chats when user changes
  useEffect(() => {
    if (!currentUser) return
    setActiveChatId(null)
    setMessages([])
    setErrorMsg(null)
    getChats(currentUser.user_id)
      .then(setChats)
      .catch(err => console.error('Failed to load chats:', err))
  }, [currentUser])

  // Auto-scroll to bottom
  useEffect(() => {
    if (threadRef.current) {
      threadRef.current.scrollTop = threadRef.current.scrollHeight
    }
  }, [messages, isLoading])

  // Loading timer
  useEffect(() => {
    if (isLoading) {
      setElapsed(0)
      timerRef.current = setInterval(() => setElapsed(e => e + 1), 1000)
    } else {
      clearInterval(timerRef.current)
    }
    return () => clearInterval(timerRef.current)
  }, [isLoading])

  // Send a message
  const sendMessage = useCallback(async (text, chatId = activeChatId) => {
    if (!text?.trim() || !currentUser) return
    const msgText = text.trim()

    // Optimistic user message
    setMessages(ms => [...ms, { role: 'user', text: msgText }])
    setInputValue('')
    setIsLoading(true)
    setErrorMsg(null)
    setErrorDetail(null)
    setPendingMsg({ text: msgText, chatId })

    try {
      const resp = await postChat(currentUser.user_id, chatId, msgText)
      setMessages(ms => [
        ...ms,
        { role: 'assistant', text: resp.answer, response: resp }
      ])
      setActiveChatId(resp.chat_id)

      // Refresh chats list
      getChats(currentUser.user_id).then(setChats).catch(() => {})
    } catch (err) {
      const msg = err.message ?? 'Unknown error'
      setErrorMsg(msg)
      setErrorDetail(err.stack ?? null)
      // Keep user message but show error
    } finally {
      setIsLoading(false)
      setPendingMsg(null)
    }
  }, [activeChatId, currentUser])

  // Retry last failed message
  function handleRetry() {
    if (!pendingMsg) return
    setMessages(ms => ms.slice(0, -0)) // keep user message
    sendMessage(pendingMsg.text, pendingMsg.chatId)
  }

  // Open a past chat
  async function handleChatSelect(chat) {
    setActiveChatId(chat.chat_id)
    setMessages([])
    setErrorMsg(null)
    try {
      const detail = await getChatDetail(chat.chat_id)
      setMessages(detail.messages.map(m => ({
        role: m.role,
        text: m.text,
        response: m.response ?? null,
      })))
    } catch (err) {
      setErrorMsg(err.message)
    }
  }

  // New chat
  function handleNewChat() {
    setActiveChatId(null)
    setMessages([])
    setErrorMsg(null)
    setInputValue('')
    inputRef.current?.focus()
  }

  // User switch
  function handleUserSelect(user) {
    setCurrentUser(user)
    setShowUserPicker(false)
  }

  // Form submit
  function handleSubmit(e) {
    e.preventDefault()
    sendMessage(inputValue)
  }

  // Collect all citations from all messages for drawer lookup
  const allCitations = messages.flatMap(m => m.response?.citations ?? [])
  const allFlags = messages.flatMap(m => m.response?.flags ?? [])

  const today = getToday()

  return (
    <div className="app-shell">
      {/* Sidebar */}
      <Sidebar
        users={users}
        currentUser={currentUser}
        chats={chats}
        activeChatId={activeChatId}
        onNewChat={handleNewChat}
        onChatSelect={handleChatSelect}
        onUserPickerOpen={() => setShowUserPicker(true)}
      />

      {/* Main area */}
      <div className="main-area">
        {/* Header */}
        <header className="app-header">
          <span className="header-title">Asset Intelligence Copilot</span>
          <div className="header-meta">
            <div className="header-badge">
              <span className="icon">📅</span>
              Today: {today}
            </div>
            {currentUser && (
              <div className="header-badge" style={{ color: 'var(--text-primary)' }}>
                <span style={{ width: 8, height: 8, borderRadius: '50%', background: 'var(--ok-base)', display: 'inline-block' }} />
                {currentUser.name}
              </div>
            )}
          </div>
        </header>

        {/* Thread */}
        <div className="thread-container" ref={threadRef}>
          <div className="thread-inner">
            {messages.length === 0 && !isLoading && !errorMsg ? (
              <EmptyChat userName={currentUser?.name} onQuery={sendMessage} />
            ) : (
              messages.map((msg, i) => (
                <React.Fragment key={i}>
                  {msg.role === 'user' ? (
                    <UserMessage text={msg.text} userName={currentUser?.name} />
                  ) : (
                    <AssistantMessage
                      response={msg.response}
                      onChipClick={setOpenCitation}
                      onSendMessage={sendMessage}
                    />
                  )}
                </React.Fragment>
              ))
            )}

            {/* Loading state */}
            {isLoading && <LoadingState elapsed={elapsed} />}

            {/* Error state */}
            {errorMsg && !isLoading && (
              <ErrorState
                message={errorMsg}
                detail={errorDetail}
                onRetry={handleRetry}
              />
            )}
          </div>
        </div>

        {/* Input bar */}
        <div className="input-bar">
          <div className="input-bar-inner">
            <form className="input-form" onSubmit={handleSubmit}>
              <span style={{ color: 'var(--cyan)', flexShrink: 0 }}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round">
                  <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>
                </svg>
              </span>
              <input
                ref={inputRef}
                className="input-field"
                placeholder={isLoading ? 'Waiting for response…' : 'Ask about wells, inspections, maintenance, or compliance…'}
                value={inputValue}
                onChange={e => setInputValue(e.target.value)}
                disabled={isLoading || !currentUser}
                onKeyDown={e => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault()
                    handleSubmit(e)
                  }
                }}
              />
              <button className="btn-send" type="submit" disabled={isLoading || !inputValue.trim() || !currentUser}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.5} strokeLinecap="round" strokeLinejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"/>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"/>
                </svg>
              </button>
            </form>
          </div>
        </div>
      </div>

      {/* Citation drawer */}
      {openCitation && (
        <CitationDrawer
          citation={openCitation}
          flags={allFlags}
          onClose={() => setOpenCitation(null)}
        />
      )}

      {/* User picker modal */}
      {showUserPicker && (
        <UserPickerModal
          users={users}
          currentUser={currentUser}
          onSelect={handleUserSelect}
          onClose={() => setShowUserPicker(false)}
        />
      )}
    </div>
  )
}
