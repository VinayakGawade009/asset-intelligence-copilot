import React, { useState, useEffect } from 'react'
import { initials, formatRole, PINNED_USER_IDS } from '../utils.js'

// ============================================================
//  UserPickerModal
// ============================================================
export function UserPickerModal({ users, currentUser, onSelect, onClose }) {
  const pinned = PINNED_USER_IDS.map(id => users.find(u => u.user_id === id)).filter(Boolean)
  const others = users.filter(u => !PINNED_USER_IDS.includes(u.user_id))

  return (
    <div className="modal-overlay" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="user-picker-modal">
        <div className="modal-header">
          <span style={{ fontSize: 15, fontWeight: 600 }}>Switch user</span>
          <button className="btn-icon" onClick={onClose} style={{ padding: '4px 6px' }}>✕</button>
        </div>
        <div className="user-picker-body">
          <div className="pinned-label">Pinned</div>
          {pinned.map(u => (
            <UserCard key={u.user_id} user={u} active={u.user_id === currentUser?.user_id} onSelect={onSelect} />
          ))}
          {others.length > 0 && (
            <>
              <div className="pinned-label" style={{ marginTop: 8 }}>All users</div>
              {others.map(u => (
                <UserCard key={u.user_id} user={u} active={u.user_id === currentUser?.user_id} onSelect={onSelect} />
              ))}
            </>
          )}
        </div>
        <div className="user-picker-privacy">
          🔒 Your chats are private. Corrections are shared.
        </div>
      </div>
    </div>
  )
}

function UserCard({ user, active, onSelect }) {
  return (
    <div className={`user-card ${active ? 'active' : ''}`} onClick={() => onSelect(user)}>
      <div className="user-avatar">{initials(user.name)}</div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div className="user-name">{user.name}</div>
        <div className="user-meta">{formatRole(user.role)}</div>
        <div className="user-team">{user.team}</div>
      </div>
      {active && (
        <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--cyan)' }}>ACTIVE</span>
      )}
    </div>
  )
}

// ============================================================
//  Sidebar
// ============================================================
export function Sidebar({ users, currentUser, chats, activeChatId, onNewChat, onChatSelect, onUserPickerOpen }) {
  return (
    <aside className="sidebar">
      {/* Brand */}
      <div className="sidebar-brand">
        <div className="sidebar-brand-icon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round">
            <polyline points="16 18 22 12 16 6"/>
            <polyline points="8 6 2 12 8 18"/>
          </svg>
        </div>
        <div>
          <div className="sidebar-brand-name">Asset Intelligence</div>
          <div className="sidebar-brand-sub">Copilot · Oil Field Operations</div>
        </div>
      </div>

      {/* User picker trigger */}
      <div className="sidebar-user" onClick={onUserPickerOpen} role="button" tabIndex={0}
        onKeyDown={e => e.key === 'Enter' && onUserPickerOpen()}>
        <div className="sidebar-user-row">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1, minWidth: 0 }}>
            <div className="sidebar-user-avatar">
              {currentUser ? initials(currentUser.name) : '?'}
            </div>
            <div style={{ minWidth: 0 }}>
              <div className="sidebar-user-name truncate">{currentUser?.name ?? 'Select user'}</div>
              <div className="sidebar-user-role truncate">{currentUser ? formatRole(currentUser.role) : ''}</div>
            </div>
          </div>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--text-tertiary)" strokeWidth={2}>
            <polyline points="6 9 12 15 18 9"/>
          </svg>
        </div>
        {currentUser && (
          <div className="sidebar-user-team" style={{ marginLeft: 40, fontSize: 11 }}>{currentUser.team}</div>
        )}
        <div className="sidebar-privacy">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          Private chats · Corrections shared
        </div>
      </div>

      {/* New chat */}
      <div className="sidebar-new-chat">
        <button className="btn-new-chat" onClick={onNewChat}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          New chat
        </button>
      </div>

      {/* Recent chats */}
      <div className="sidebar-chats-label">Recent chats</div>
      <nav className="sidebar-nav">
        {chats.length === 0 && (
          <div style={{ padding: '8px 12px', color: 'var(--text-tertiary)', fontSize: 12, fontFamily: 'var(--font-mono)' }}>
            No chats yet
          </div>
        )}
        {chats.map(chat => (
          <button
            key={chat.chat_id}
            className={`sidebar-nav-item ${chat.chat_id === activeChatId ? 'active' : ''}`}
            onClick={() => onChatSelect(chat)}
          >
            <span className="sidebar-nav-item-title">{chat.title ?? 'Untitled'}</span>
            {chat.updated_at && (
              <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--text-tertiary)', marginTop: 2 }}>
                {chat.updated_at.slice(0, 10)}
              </span>
            )}
          </button>
        ))}
      </nav>
    </aside>
  )
}
