# UI Contract

## Endpoints
- GET  /api/users -> [{user_id, name, role, team}]
- GET  /api/chats?user_id=U-201 -> [{chat_id, title, updated_at}]
- GET  /api/chats/{chat_id} -> {chat_id, messages: [{role: "user"|"assistant", text, response?}]}
- POST /api/chat  body: {user_id, chat_id | null, message}  -> ChatResponse

## ChatResponse
{
  "chat_id": "string",
  "answer": "markdown string",
  "visual": Visual | null,
  "citations": [{"id": "INS-0001-0203", "kind": "inspection|maintenance|regulatory|note|document", "label": "short title", "detail": "one-line excerpt"}],
  "flags": [{"kind": "conflict|overdue|unconfirmed|correction_applied|no_cause", "text": "string", "source_ids": ["CTX-0001-003"]}],
  "meta": {"model": "gemma-4-26b-a4b-it", "latency_ms": 0, "tool_calls": ["well_status"]}
}

## Visual (one of, selected by "type")
- status_card:
  {"type":"status_card","well_id":"WELL-0001","name":"","area":"","well_type":"T200","producing":false,
   "headline":"Not producing oil","recorded_status":"active",
   "metrics":[{"label":"Wellhead above air","value":3.2,"unit":"°C"}],
   "badges":[{"text":"Planned shut-in","tone":"warning"}],
   "last_inspection":{"id":"INS-0001-0203","date":"2026-10-15","by":"Ryan Brooks"}}
- table:
  {"type":"table","title":"","columns":[{"key":"well","label":"Well"}],"rows":[{"well":"WELL-0164"}]}
- line_chart:
  {"type":"line_chart","title":"","x":["2026-07-23"],"x_label":"","y_label":"°C",
   "series":[{"name":"Wellhead","values":[0]},{"name":"Air","values":[0]}],
   "markers":[{"x":"2026-10-08","label":"Not producing"}]}
- bar_chart:
  {"type":"bar_chart","title":"","categories":["WELL-0121"],"unit":"days",
   "series":[{"name":"Downtime","values":[49]}]}
- map:
  {"type":"map","title":"","center":{"lat":0,"lon":0},
   "pins":[{"label":"WELL-0151","lat":0,"lon":0,"detail":"4.5 bbl, 24 Sep 2026","tone":"critical"}]}
- heatmap:
  {"type":"heatmap","title":"","rows":["Northeast Block 7"],"cols":["Jan","Feb"],
   "values":[[5,3]],"unit":"spills"}

tone is one of: ok | warning | critical | unconfirmed | neutral.
