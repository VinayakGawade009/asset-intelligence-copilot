UI Document of Asset Intelligence Copilot

1. Design.md
```
---
name: Asset Intelligence Console
colors:
surface: '#0e141c'
surface-dim: '#0e141c'
surface-bright: '#343a42'
surface-container-lowest: '#090f16'
surface-container-low: '#161c24'
surface-container: '#1a2028'
surface-container-high: '#242a33'
surface-container-highest: '#2f353e'
on-surface: '#dde3ee'
on-surface-variant: '#bdc8d1'
inverse-surface: '#dde3ee'
inverse-on-surface: '#2b3139'
outline: '#87929a'
outline-variant: '#3e484f'
surface-tint: '#7bd0ff'
primary: '#8ed5ff'
on-primary: '#00354a'
primary-container: '#38bdf8'
on-primary-container: '#004965'
inverse-primary: '#00668a'
secondary: '#45dfa4'
on-secondary: '#003825'
secondary-container: '#00bd85'
on-secondary-container: '#00452e'
tertiary: '#ffbcbf'
on-tertiary: '#67001b'
tertiary-container: '#ff929a'
on-tertiary-container: '#8c0028'
error: '#ffb4ab'
on-error: '#690005'
error-container: '#93000a'
on-error-container: '#ffdad6'
primary-fixed: '#c4e7ff'
primary-fixed-dim: '#7bd0ff'
on-primary-fixed: '#001e2c'
on-primary-fixed-variant: '#004c69'
secondary-fixed: '#68fcbf'
secondary-fixed-dim: '#45dfa4'
on-secondary-fixed: '#002114'
on-secondary-fixed-variant: '#005137'
tertiary-fixed: '#ffdadb'
tertiary-fixed-dim: '#ffb2b7'
on-tertiary-fixed: '#40000d'
on-tertiary-fixed-variant: '#92002a'
background: '#0e141c'
on-background: '#dde3ee'
surface-variant: '#2f353e'
typography:
display-telemetry:
fontFamily: IBM Plex Mono
fontSize: 28px
fontWeight: '600'
lineHeight: 34px
letterSpacing: -0.01em
headline-panel:
fontFamily: IBM Plex Sans
fontSize: 20px
fontWeight: '600'
lineHeight: 28px
letterSpacing: -0.01em
headline-panel-mobile:
fontFamily: IBM Plex Sans
fontSize: 18px
fontWeight: '600'
lineHeight: 24px
body-prose:
fontFamily: IBM Plex Sans
fontSize: 16px
fontWeight: '400'
lineHeight: 24px
body-prose-medium:
fontFamily: IBM Plex Sans
fontSize: 16px
fontWeight: '500'
lineHeight: 24px
body-spec:
fontFamily: IBM Plex Sans
fontSize: 14px
fontWeight: '400'
lineHeight: 20px
body-spec-mono:
fontFamily: IBM Plex Mono
fontSize: 14px
fontWeight: '500'
lineHeight: 20px
label-metric:
fontFamily: IBM Plex Sans
fontSize: 12px
fontWeight: '600'
lineHeight: 16px
letterSpacing: 0.04em
label-mono-tag:
fontFamily: IBM Plex Mono
fontSize: 12px
fontWeight: '500'
lineHeight: 16px
rounded:
sm: 0.125rem
DEFAULT: 0.25rem
md: 0.375rem
lg: 0.5rem
xl: 0.75rem
full: 9999px
spacing:
gutter: 1.5rem
margin: 1.5rem
space-xs: 0.25rem
space-sm: 0.5rem
space-md: 1rem
space-lg: 1.25rem
space-xl: 1.5rem
---

## Brand & Style

The design system establishes a high-contrast, calm, technical command-center environment tailored for oil-field operators, petroleum technicians, and supervisory field engineers operating in control vans, harsh daylight, and low-light field command units.

### Philosophy & Character
- **Industrial Precision:** The visual language rejects consumer software tropes. It eliminates conversational fluff, AI sparkles, magic wands, pastel bubbles, and decorative gradient meshes in favor of structural clarity, high-contrast readability, and low cognitive load under operational stress.
- **Arm's-Length Readability:** Visual hierarchy prioritizes scanning from a distance of one meter on ruggedized displays and desktop terminal arrays (optimized for 1440px target viewports).
- **Redundant Status Encoding:** In high-risk operational environments, color cannot act alone. Critical alerts and state indicators always couple chromatic signals with standardized technical iconography and explicit textual state descriptions.
- **Tone:** Terse, objective, factual, engineering-grade. Copy avoids pleasantries and focuses on parameter metrics, delta calculations, maintenance flags, and direct evidentiary records.

## Colors

Visual hierarchy is built on a strict stepped luminance ladder. Surfaces step upward from deep ambient control backgrounds to functional interactive layers.

### Baseline Canvas & Tonal Hierarchy
- **Canvas Base (`#0B0F14`):** Deepest console void. Background for master shell layout, navigation rails, and backdrop framing.
- **Surface Level 1 (`#121820`):** Default panel and card baseline. Houses report streams, log readouts, and primary telemetry containers.
- **Surface Level 2 (`#1A222D`):** Elevated modules, nested telemetry plates, table header bands, and user prompt containers.
- **Border Structural (`#263140`):** Outer perimeter 1px borders for cards, inputs, and section boundaries.
- **Hairline / Dividers (`#1E2733`):** Internal horizontal rules, data grid rows, and subtle modular splits.

### Text & Readability Tiers
- **Text Primary (`#E6EDF3`):** High-contrast optical white for primary telemetry readings, summary reports, and active headings.
- **Text Secondary (`#8B98A8`):** Muted slate for metadata, metric units, technical attributes, and secondary timestamps.
- **Text Tertiary / Disabled (`#5B6675`):** Subdued contrast for inactive controls, de-emphasized grid axes, and unconfigured telemetry slots.

### Interactive & Accent Color
- **Signal Cyan (`#38BDF8`):** System accent color. Applied strictly to interactive affordances, selected tab rails, focus rings, link citations, telemetry line overlays, and left border rails of intelligence reports.

### Operational Status Matrix
Status styling combines a solid semantic base, a 12% tinted alpha fill (`1F`), and a matching 1px border (`40`):
- **Normal / OK:** Base `#34D399` | Fill `rgba(52, 211, 153, 0.12)` | Border `rgba(52, 211, 153, 0.25)`
- **Warning / Alert:** Base `#FBBF24` | Fill `rgba(251, 191, 36, 0.12)` | Border `rgba(251, 191, 36, 0.25)`
- **Critical / Alarm:** Base `#F43F5E` | Fill `rgba(244, 63, 94, 0.12)` | Border `rgba(244, 63, 94, 0.25)`
- **Telemetry Gap / Unconfirmed:** Base `#A78BFA` | Fill `rgba(167, 139, 250, 0.12)` | Border `1px dashed rgba(167, 139, 250, 0.40)`
- **Neutral / Standby:** Base `#94A3B8` | Fill `rgba(148, 163, 184, 0.12)` | Border `rgba(148, 163, 184, 0.25)`

### Telemetry & Chart Series
- **Wellhead Pressure & Temperature:** `#FB923C` (Technical Orange)
- **Ambient & Flow Telemetry:** `#38BDF8` (Signal Cyan)
- **Bar Series:** Base `#38BDF8` with anomaly peaks dynamically painted in `#F43F5E`.
- **Thermal Heatmap Ramp:** Linear stepping from `#1A222D` (baseline null/0) to `#FBBF24` (elevated) to `#F43F5E` (exceedance/max).

## Typography

The type system is divided cleanly between structured linguistic communication and tabular engineering readouts.

### Font Role Allocation
- **Primary Interface & Report Typography:** `IBM Plex Sans`. Delivers neutral, highly legible sans-serif glyphs engineered for complex digital interfaces. Weights used are strictly limited to `400` (Regular), `500` (Medium), and `600` (Semi-Bold).
- **Quantitative, Telemetry, and Identifiers:** `IBM Plex Mono`. Applied to operational record tags (wells, inspections, valves), telemetry floats, pressure ratings, SI units, and chronological timestamps. Tabular figures (`tnum`) must remain enabled across all data grids to prevent horizontal jitter during real-time streaming updates.

### Usage Standards
- **Uppercase Labels:** `label-metric` must be styled in uppercase with tracking set to `+0.04em` to optimize legibility on low-brightness screens.
- **Metric Grouping:** All big telemetry displays (`display-telemetry`) must bind numerical values directly to their corresponding metric unit (`body-spec-mono` or `label-metric`) placed inline or stacked below, colored in `Text Secondary` (`#8B98A8`).

## Layout & Spacing

The system runs on a strict 4px base increment grid. Content is organized around a dual-pane or tri-pane desktop architecture calibrated for 1440px wide operational dashboards.

### Grid & Canvas Structure
- **Desktop Target (1440px+):** Fixed full-height viewport canvas (`100vh`) with fixed global navigation rail (64px width), an asset/wellhead selector column (320px width), and an elastic report/telemetry split canvas (adaptive flex fill with `1.5rem` / 24px inner margins).
- **Gutter & Module Distribution:** Columns and adjacent panels utilize a constant 24px (`1.5rem`) gutter. Structural cards within a module use a 16px (`1rem`) gap.
- **Vertical Rhythm:**
- `space-xs` (4px): Micro offsets between metric values and engineering units.
- `space-sm` (8px): Icon-to-text spacing, chip padding, and compact table cell vertical padding.
- `space-md` (16px): Standard internal card padding, telemetry metric tile spacing.
- `space-lg` (20px): Deep panel internal padding for high-density analysis cards.
- `space-xl` (24px): Boundary separations between primary assistant reports and diagnostic panels.

### Responsive Behavior (1024px to 1440px+)
- Below 1280px, the asset/wellhead selector column collapses into an off-canvas drawer with an explicit toggle button.
- Report output and telemetry inspection views convert from side-by-side split view into a stacked two-tier layout with persistent query bar docked at the bottom.

## Elevation & Depth

Depth in this system is strictly planar and non-tactile.

### Shadow Policy
- **Zero Drop Shadows:** Ambient, soft, or colored drop shadows are prohibited (`box-shadow: none`). In operational industrial interfaces, diffused blur shadows create visual murkiness and decrease interface contrast.

### Planar Depth Model
Depth is established exclusively through surface stepping paired with architectural 1px borders:
1. **Canvas Tier (0dp):** Color `#0B0F14` — Base foundation.
2. **Structural Tier (1dp):** Color `#121820` bounded by 1px border `#263140` — Main report surfaces, side panels, log displays.
3. **Elevated Functional Tier (2dp):** Color `#1A222D` bounded by 1px border `#263140` — User query plates, interactive form fields, telemetry sub-cards, table head rails.
4. **Active/Focus Overlay:** Element retains `#1A222D` background and updates border to 1px solid Signal Cyan (`#38BDF8`) with zero outer spread.

## Shapes

The interface utilizes a disciplined, low-radius geometric contour vocabulary that emphasizes stability and structural alignment.

### Geometry Specifications
- **Cards, Modules, Input Containers:** Radius 10px (`rounded-lg` override: `10px`). Provides clean structural framing without round consumer softens.
- **Operational Badges, Telemetry Chips, Metric Tags:** Radius 6px. Compact, snug contours around monospaced identifiers.
- **Interactive Action Buttons:** Radius 6px.
- **Divider Rails & Status Dots:** Pure 90-degree squared geometry, with the exception of status circular pips (border-radius 9999px).

## Components

### 1. Assistant Report Modules (System Output)
- **Structure:** Full-width structural block seated on Surface 1 (`#121820`) with 1px border (`#263140`). Never styled as a bubble.
- **Identification:** Features an uninterrupted 2px solid Signal Cyan (`#38BDF8`) left border rail.
- **Header:** System title ("ASSET INTELLIGENCE ENGINE"), status timestamp, and confidence telemetry rendered in `IBM Plex Mono` (12px, `#8B98A8`).
- **Body:** Markdown summary text in `body-prose` (`#E6EDF3`). Data tables, parameter summaries, and diagnostic graphs sit nested inside elevated plates (`#1A222D`).

### 2. User Query Plates (Operator Prompt)
- **Structure:** Right-aligned or right-indented compact plate. Maximum width 75% of stream canvas.
- **Surface:** Surface 2 (`#1A222D`) with 1px border (`#263140`) and 10px corner radius.
- **Typography:** `body-spec` (`#E6EDF3`) paired with a monospaced user tag ("OPERATOR // CREW-A") in `#8B98A8`.

### 3. Record Citation Chips & Entity Tags
- **Application:** Displaying well IDs, maintenance tickets, and inspection codes (e.g., `WELL-0001`, `INS-0001-0203`, `MNT-0001-032`).
- **Styling:** Rendered in `IBM Plex Mono` (12px, weight 500). Background fill `rgba(56, 189, 248, 0.08)`, text `#38BDF8`, border 1px solid `rgba(56, 189, 248, 0.25)`.
- **States:** Hover elevates background to `rgba(56, 189, 248, 0.16)` with mouse pointer; active click triggers inspection drawer.

### 4. Status Indicator Badges
- **Triple-Redundancy Principle:** Every status display must render:
1. Solid semantic color dot or icon stroke.
2. 16px geometric line icon (`check-circle2`, `alert-triangle`, `shield-alert`, `activity`).
3. Terse uppercase text label.
- **Examples:**
- *Normal:* `#34D399` + `check-circle2` + "NORMAL OPERATING"
- *Warning:* `#FBBF24` + `alert-triangle` + "PLANNED SHUT-IN"
- *Critical:* `#F43F5E` + `shield-alert` + "CRITICAL EXCEEDANCE"
- *Gap:* `#A78BFA` + `help-circle` + "TELEMETRY GAP" (dashed border)

### 5. Telemetry Metric Readout Tiles
- **Structure:** Surface 2 (`#1A222D`) with 1px border (`#263140`), 16px padding.
- **Top Row:** Metric label in `label-metric` (`#8B98A8`) with redundant status pill right-aligned.
- **Primary Value:** `display-telemetry` in `IBM Plex Mono` (`#E6EDF3`), followed by unit designation in 14px mono (`#8B98A8`).
- **Footer:** Baseline delta or threshold range indicator rendered as a hairline comparison bar.

### 6. Interactive Input Terminal (Prompt Field)
- **Container:** Grounded dock panel on `#121820`, top hairline divider `#263140`.
- **Input Field:** Height 48px, background `#1A222D`, border 1px solid `#263140`, radius 10px. Text in `IBM Plex Sans` (14px, `#E6EDF3`).
- **Focus State:** 1px border color transitions to `#38BDF8`. No outer glow ring.
- **Affordance:** Right-aligned action cluster with terminal execute button: solid background `#38BDF8`, text `#0B0F14`, weight 600, radius 6px.

### 7. Telemetry & Data Grids
- **Header Row:** Background `#1A222D`, bottom hairline `#1E2733`. Typography: `label-metric` (12px, uppercase, `#8B98A8`).
- **Body Rows:** Alternating row striping disabled. Row divider: 1px hairline `#1E2733`.
- **Numbers & Units:** Right-aligned `IBM Plex Mono` with tabular figure setting enabled.
```

2. 2026_spills_by_area_and_month_heatmap_asset_intelligence
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config = { darkMode: "class", theme: { extend: { "colors": { "on-primary-fixed": "#001e2c", "surface-variant": "#2f353e", "on-primary": "#00354a", "primary-fixed-dim": "#7bd0ff", "surface-bright": "#343a42", "primary": "#8ed5ff", "tertiary-fixed-dim": "#ffb2b7", "surface-container-low": "#161c24", "outline-variant": "#3e484f", "surface-dim": "#0e141c", "on-error-container": "#ffdad6", "secondary-container": "#00bd85", "on-error": "#690005", "surface-container": "#1a2028", "on-tertiary-fixed-variant": "#92002a", "secondary-fixed-dim": "#45dfa4", "outline": "#87929a", "secondary-fixed": "#68fcbf", "surface": "#0e141c", "tertiary-fixed": "#ffdadb", "on-secondary": "#003825", "error": "#ffb4ab", "surface-container-highest": "#2f353e", "background": "#0e141c", "on-tertiary-fixed": "#40000d", "inverse-on-surface": "#2b3139", "on-primary-fixed-variant": "#004c69", "on-secondary-fixed-variant": "#005137", "on-secondary-fixed": "#002114", "inverse-primary": "#00668a", "error-container": "#93000a", "surface-container-high": "#242a33", "on-secondary-container": "#00452e", "on-background": "#dde3ee", "tertiary": "#ffbcbf", "on-surface": "#dde3ee", "secondary": "#45dfa4", "on-tertiary": "#67001b", "tertiary-container": "#ff929a", "on-tertiary-container": "#8c0028", "primary-fixed": "#c4e7ff", "primary-container": "#38bdf8", "surface-tint": "#7bd0ff", "inverse-surface": "#dde3ee", "surface-container-lowest": "#090f16", "on-primary-container": "#004965", "on-surface-variant": "#bdc8d1" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-lg": "1.25rem", "space-md": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "gutter": "1.5rem", "space-sm": "0.5rem", "margin": "1.5rem" }, "fontFamily": { "body-spec": [ "IBM Plex Sans" ], "label-mono-tag": [ "IBM Plex Mono" ], "body-prose-medium": [ "IBM Plex Sans" ], "label-metric": [ "IBM Plex Sans" ], "body-spec-mono": [ "IBM Plex Mono" ], "headline-panel": [ "IBM Plex Sans" ], "headline-panel-mobile": [ "IBM Plex Sans" ], "body-prose": [ "IBM Plex Sans" ], "display-telemetry": [ "IBM Plex Mono" ] }, "fontSize": { "body-spec": [ "14px", { "lineHeight": "20px", "fontWeight": "400" } ], "label-mono-tag": [ "12px", { "lineHeight": "16px", "fontWeight": "500" } ], "body-prose-medium": [ "16px", { "lineHeight": "24px", "fontWeight": "500" } ], "label-metric": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "body-spec-mono": [ "14px", { "lineHeight": "20px", "fontWeight": "500" } ], "headline-panel": [ "20px", { "lineHeight": "28px", "letterSpacing": "-0.01em", "fontWeight": "600" } ], "headline-panel-mobile": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ], "body-prose": [ "16px", { "lineHeight": "24px", "fontWeight": "400" } ], "display-telemetry": [ "28px", { "lineHeight": "34px", "letterSpacing": "-0.01em", "fontWeight": "600" } ] } } } };</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface antialiased"><aside class="fixed left-0 top-0 h-full w-64 bg-surface-container-low flex flex-col justify-between py-space-md px-3 z-50 border-r border-surface-container-high"><div class="flex flex-col gap-space-md"><div class="flex items-center gap-2 px-2 py-1"><div class="w-8 h-8 rounded bg-surface-container flex items-center justify-center border border-outline-variant text-primary"><span class="material-symbols-outlined text-[18px]">terminal</span></div><span class="font-label-mono-tag text-label-mono-tag text-primary font-semibold tracking-wider uppercase">ASSET INTEL</span></div><button class="w-full flex items-center justify-center gap-2 py-2 px-3 rounded bg-primary/10 hover:bg-primary/20 border border-primary/30 text-primary font-body-spec text-[13px] font-semibold transition-colors"><span class="material-symbols-outlined text-[18px]">add</span><span class="">+ New chat</span></button><div class="flex flex-col gap-1 mt-2"><span class="font-label-metric text-[11px] text-on-surface-variant uppercase tracking-wider px-2 py-1">Recent chats</span><a href="#" class="px-2.5 py-1.5 rounded hover:bg-surface-container text-on-surface font-body-spec text-[13px] truncate transition-colors">WELL-0001 status and last inspection</a><a href="#" class="px-2.5 py-1.5 rounded hover:bg-surface-container text-on-surface font-body-spec text-[13px] truncate transition-colors">Northeast Block 8 not producing</a><a href="#" class="px-2.5 py-1.5 rounded hover:bg-surface-container text-on-surface font-body-spec text-[13px] truncate transition-colors">Block 7 downtime, top 3</a><a href="#" class="px-2.5 py-1.5 rounded hover:bg-surface-container text-on-surface font-body-spec text-[13px] truncate transition-colors">WELL-0001 spills, last 4 years</a><a href="#" class="px-2.5 py-1.5 rounded hover:bg-surface-container text-on-surface font-body-spec text-[13px] truncate transition-colors">Pump jack root-cause wells</a></div></div><div class="flex items-center gap-2 px-2 pt-space-sm border-t border-surface-container-high"><div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold text-xs shrink-0"><span class="material-symbols-outlined text-[18px]">person</span></div><div class="flex flex-col truncate"><span class="text-[13px] font-semibold text-on-surface truncate">Michael Turner</span><span class="text-[11px] text-on-surface-variant font-label-mono-tag">Weekly Inspections</span></div></div></aside><div class="pl-64 min-h-screen flex flex-col"><header class="fixed top-0 left-64 right-0 h-14 bg-surface-container-lowest/95 backdrop-blur-md z-40 border-b border-surface-container-high"><div class="w-full h-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] text-on-surface font-semibold">2026 Spills by Area and Month</span></div><div class="flex items-center gap-space-md"><div class="inline-flex items-center gap-1.5 px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-label-mono-tag text-on-surface-variant"><span class="material-symbols-outlined text-[14px] text-primary">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="inline-flex items-center gap-1.5 px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-label-mono-tag text-on-surface"><span class="material-symbols-outlined text-[14px] text-primary">account_circle</span><span class="">Michael Turner</span></div></div></div></header><main class="w-full pt-14 bg-surface-container-lowest flex-1"><div class="flex flex-col w-full"><div class="w-full max-w-[1280px] mx-auto px-space-xl py-space-lg flex flex-col gap-space-lg"><div class="flex flex-col items-end w-full"><div class="w-full max-w-[780px] bg-surface-container p-space-md rounded-xl border border-outline-variant flex flex-col gap-space-sm"><div class="flex items-center justify-between w-full font-label-mono-tag text-label-mono-tag text-on-surface-variant"><div class="flex items-center gap-space-sm"><span class="material-symbols-outlined text-[16px] text-primary">person</span><span class="text-on-surface font-semibold tracking-wide">OPERATOR QUERY // (CONSOLE-04)</span></div><span class="">14:34:10 UTC</span></div><p class="font-body-prose text-body-prose text-on-surface font-normal">Show a heatmap of 2026 spills by geographic area and month.</p><div class="flex items-center gap-space-xs pt-1 flex-wrap font-label-mono-tag text-[11px]"><span class="px-space-sm py-0.5 rounded bg-surface-container-low text-primary border border-primary/20 tracking-wider">#SPILL-ANALYTICS</span><span class="px-space-sm py-0.5 rounded bg-surface-container-low text-primary border border-primary/20 tracking-wider">#HEATMAP-MATRIX</span><span class="px-space-sm py-0.5 rounded bg-surface-container-low text-on-surface-variant border border-outline-variant">WINDOW: YTD-2026</span><span class="px-space-sm py-0.5 rounded bg-surface-container-low text-secondary border border-secondary/20">WEEKLY INSPECTIONS</span></div></div></div><div class="w-full max-w-[880px] bg-surface-container-low rounded-xl border border-outline-variant border-l-[3px] border-l-primary-container p-space-lg flex flex-col gap-space-lg relative"><div class="flex items-start justify-between pb-space-md border-b border-surface-container-high"><div class="flex items-center gap-space-md"><div class="w-9 h-9 rounded bg-surface-container flex items-center justify-center border border-primary/30 text-primary"><span class="material-symbols-outlined text-[20px]">smart_toy</span></div><div class="flex flex-col"><div class="flex items-center gap-space-sm"><span class="font-headline-panel text-headline-panel text-on-surface">Asset Intelligence Copilot</span><span class="font-label-mono-tag text-label-mono-tag px-2 py-0.5 rounded bg-surface-container text-primary font-medium tracking-wide">CORE-V4</span></div><div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-on-surface-variant mt-0.5"><span class="">INCIDENT ANALYTICS // SPATIAL-TEMPORAL HEATMAP</span></div></div></div><div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-on-surface-variant"><span class="">14:34:12 UTC</span></div></div><div class="font-body-prose text-body-prose text-on-surface leading-relaxed">Across 4 active operating sectors in 2026 YTD, <strong class="text-primary font-semibold">141 confirmed spills</strong> were recorded. <strong class="text-tertiary-container font-semibold">Southwest Block 24 exhibited the highest incidence with 43 spills</strong>, peaking in January (7 spills) and April (6 spills). Northeast Block 8 showed the sharpest decrease, dropping to <strong class="text-secondary font-semibold">0 spills in August and October</strong> based on weekly inspections. Note: Each block has 50 wells.</div><div class="grid grid-cols-2 md:grid-cols-4 gap-space-md"><div class="bg-surface-container p-space-md rounded border border-outline-variant flex flex-col justify-between"><div class="flex items-center justify-between font-label-metric text-label-metric text-on-surface-variant uppercase"><span class="">TOTAL 2026 SPILLS</span><span class="material-symbols-outlined text-[16px] text-primary">water_loss</span></div><div class="my-space-sm flex items-baseline gap-space-xs"><span class="font-display-telemetry text-display-telemetry text-on-surface">141</span><span class="font-body-spec-mono text-body-spec-mono text-on-surface-variant">CASES</span></div><div class="font-label-mono-tag text-[11px] text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">check_circle</span><span class="">WEEKLY AUDITED SET</span></div></div><div class="bg-surface-container p-space-md rounded border border-error/30 flex flex-col justify-between"><div class="flex items-center justify-between font-label-metric text-label-metric text-on-surface-variant uppercase"><span class="">HIGHEST INCIDENCE</span><span class="material-symbols-outlined text-[16px] text-error">warning</span></div><div class="my-space-sm flex flex-col"><span class="font-display-telemetry text-display-telemetry text-error">43</span><span class="font-body-spec text-[13px] text-on-surface font-semibold tracking-tight">SW BLK 24</span></div><div class="font-label-mono-tag text-[11px] text-tertiary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">location_on</span><span class="">50 WELLS MONITORED</span></div></div><div class="bg-surface-container p-space-md rounded border border-outline-variant flex flex-col justify-between"><div class="flex items-center justify-between font-label-metric text-label-metric text-on-surface-variant uppercase"><span class="">LOWEST INCIDENCE</span><span class="material-symbols-outlined text-[16px] text-secondary">check_circle</span></div><div class="my-space-sm flex flex-col"><span class="font-display-telemetry text-display-telemetry text-secondary">26</span><span class="font-body-spec text-[13px] text-on-surface font-semibold tracking-tight">NE BLK 8</span></div><div class="font-label-mono-tag text-[11px] text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">location_on</span><span class="">50 WELLS MONITORED</span></div></div><div class="bg-surface-container p-space-md rounded border border-outline-variant flex flex-col justify-between"><div class="flex items-center justify-between font-label-metric text-label-metric text-on-surface-variant uppercase"><span class="">EXCLUSIONS</span><span class="material-symbols-outlined text-[16px] text-primary">filter_alt</span></div><div class="my-space-sm flex items-baseline gap-space-xs"><span class="font-display-telemetry text-display-telemetry text-on-surface">19</span><span class="font-body-spec-mono text-body-spec-mono text-on-surface-variant">REMOVED</span></div><div class="font-label-mono-tag text-[11px] text-on-surface-variant flex items-center gap-1"><span class="material-symbols-outlined text-[14px] text-secondary">check</span><span class="">WEEKLY AUDIT VERIFIED</span></div></div></div><div class="bg-surface-container-lowest rounded-lg border border-outline-variant p-space-lg flex flex-col gap-space-md"><div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-space-sm pb-space-sm border-b border-surface-container-high"><div class="flex items-center gap-space-sm"><span class="material-symbols-outlined text-primary text-[20px]">grid_view</span><span class="font-headline-panel text-[16px] leading-[22px] text-on-surface font-semibold">2026 spills by area and month</span></div><div class="flex items-center gap-space-sm"><span class="font-label-mono-tag text-label-mono-tag px-space-sm py-0.5 rounded bg-surface-container text-primary font-semibold tracking-widest uppercase border border-outline-variant">MATRIX // 4×10</span></div></div><div class="w-full overflow-x-auto pb-space-sm"><div class="min-w-[800px] flex flex-col gap-1"><div class="flex items-center"><div class="w-[190px] shrink-0 font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase px-space-sm">OPERATING SECTOR</div><div class="flex items-center gap-[4px] flex-1"><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">JAN</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">FEB</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">MAR</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">APR</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">MAY</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">JUN</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">JUL</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">AUG</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">SEP</div><div class="w-[56px] text-center font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase">OCT</div></div><div class="w-[74px] shrink-0 text-center font-label-mono-tag text-label-mono-tag text-primary uppercase pl-2 border-l border-surface-container-high">TOTAL</div></div><div class="flex items-center group hover:bg-surface-container-low/50 rounded py-1 transition-colors"><div class="w-[190px] shrink-0 font-body-spec text-[13px] text-on-surface font-medium truncate pr-2">Southwest Block 23</div><div class="flex items-center gap-[4px] flex-1"><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#e11d48] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">6</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#2b3b33] text-[#CBD5E1] font-display-telemetry text-[15px] flex items-center justify-center font-bold">2</button></div><div class="w-[74px] shrink-0 pl-2 border-l border-surface-container-high flex justify-center"><div class="w-[56px] h-[44px] rounded-[6px] bg-surface-container border border-outline-variant text-on-surface font-display-telemetry text-[15px] flex items-center justify-center font-semibold">35</div></div></div><div class="flex items-center group hover:bg-surface-container-low/50 rounded py-1 transition-colors relative"><div class="w-[190px] shrink-0 font-body-spec text-[13px] text-on-surface font-medium truncate pr-2 flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-error"></span><span class="">Southwest Block 24</span></div><div class="flex items-center gap-[4px] flex-1 relative"><div class="relative"><button class="w-[56px] h-[44px] rounded-[6px] bg-[#F43F5E] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold shadow-sm ring-2 ring-primary focus:outline-none cursor-pointer">7</button></div><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#ea580c] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">5</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#e11d48] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">6</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#ea580c] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">5</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#ea580c] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">5</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#1e2c38] text-[#94A3B8] font-display-telemetry text-[15px] flex items-center justify-center font-bold">1</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#ea580c] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">5</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#2b3b33] text-[#CBD5E1] font-display-telemetry text-[15px] flex items-center justify-center font-bold">2</button></div><div class="w-[74px] shrink-0 pl-2 border-l border-surface-container-high flex justify-center"><div class="w-[56px] h-[44px] rounded-[6px] bg-error-container/40 border border-error text-tertiary-container font-display-telemetry text-[15px] flex items-center justify-center font-bold tracking-tight">43</div></div></div><div class="flex items-center group hover:bg-surface-container-low/50 rounded py-1 transition-colors"><div class="w-[190px] shrink-0 font-body-spec text-[13px] text-on-surface font-medium truncate pr-2">Northeast Block 7</div><div class="flex items-center gap-[4px] flex-1"><button class="w-[56px] h-[44px] rounded-[6px] bg-[#ea580c] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">5</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#2b3b33] text-[#CBD5E1] font-display-telemetry text-[15px] flex items-center justify-center font-bold">2</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#e11d48] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">6</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#e11d48] text-white font-display-telemetry text-[15px] flex items-center justify-center font-bold">6</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#2b3b33] text-[#CBD5E1] font-display-telemetry text-[15px] flex items-center justify-center font-bold">2</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#1e2c38] text-[#94A3B8] font-display-telemetry text-[15px] flex items-center justify-center font-bold">1</button></div><div class="w-[74px] shrink-0 pl-2 border-l border-surface-container-high flex justify-center"><div class="w-[56px] h-[44px] rounded-[6px] bg-surface-container border border-outline-variant text-on-surface font-display-telemetry text-[15px] flex items-center justify-center font-semibold">37</div></div></div><div class="flex items-center group hover:bg-surface-container-low/50 rounded py-1 transition-colors"><div class="w-[190px] shrink-0 font-body-spec text-[13px] text-on-surface font-medium truncate pr-2 flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span><span class="">Northeast Block 8</span></div><div class="flex items-center gap-[4px] flex-1"><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#4d431c] text-[#FDE68A] font-display-telemetry text-[15px] flex items-center justify-center font-bold">3</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#2b3b33] text-[#CBD5E1] font-display-telemetry text-[15px] flex items-center justify-center font-bold">2</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#d97706] text-[#090f16] font-display-telemetry text-[15px] flex items-center justify-center font-bold">4</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#1A222D] border border-outline-variant text-[#64748B] font-display-telemetry text-[15px] flex items-center justify-center font-bold">0</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#1e2c38] text-[#94A3B8] font-display-telemetry text-[15px] flex items-center justify-center font-bold">1</button><button class="w-[56px] h-[44px] rounded-[6px] bg-[#1A222D] border border-outline-variant text-[#64748B] font-display-telemetry text-[15px] flex items-center justify-center font-bold">0</button></div><div class="w-[74px] shrink-0 pl-2 border-l border-surface-container-high flex justify-center"><div class="w-[56px] h-[44px] rounded-[6px] bg-surface-container border border-outline-variant text-on-surface font-display-telemetry text-[15px] flex items-center justify-center font-semibold">26</div></div></div></div></div><div class="flex flex-col sm:flex-row sm:items-center justify-between gap-space-md pt-space-sm border-t border-surface-container-high"><div class="flex flex-col gap-1.5"><div class="flex items-center justify-between font-label-mono-tag text-[11px] text-on-surface-variant uppercase"><span class="">COLOR RAMP // SPILLS PER MONTH</span><span class="">0 (NONE) ➔ 7 (PEAK)</span></div><div class="flex items-center gap-1"><div class="flex items-center h-4 rounded overflow-hidden border border-outline-variant"><div class="w-7 h-full bg-[#1A222D] flex items-center justify-center font-label-mono-tag text-[9px] text-slate-400">0</div><div class="w-7 h-full bg-[#1e2c38] flex items-center justify-center font-label-mono-tag text-[9px] text-slate-400">1</div><div class="w-7 h-full bg-[#2b3b33] flex items-center justify-center font-label-mono-tag text-[9px] text-slate-300">2</div><div class="w-7 h-full bg-[#4d431c] flex items-center justify-center font-label-mono-tag text-[9px] text-amber-200">3</div><div class="w-7 h-full bg-[#d97706] flex items-center justify-center font-label-mono-tag text-[9px] text-black font-bold">4</div><div class="w-7 h-full bg-[#ea580c] flex items-center justify-center font-label-mono-tag text-[9px] text-white">5</div><div class="w-7 h-full bg-[#e11d48] flex items-center justify-center font-label-mono-tag text-[9px] text-white">6</div><div class="w-7 h-full bg-[#F43F5E] flex items-center justify-center font-label-mono-tag text-[9px] text-white font-bold">7</div></div></div></div><div class="font-label-mono-tag text-[11px] text-on-surface-variant max-w-[340px] flex items-start gap-1.5"><span class="material-symbols-outlined text-[16px] text-primary shrink-0 mt-0.5">touch_app</span><span class="">Click any cell to query filtered incident records.</span></div></div></div><div class="flex flex-col gap-space-sm pt-space-xs"><div class="font-label-metric text-label-metric text-on-surface-variant uppercase flex items-center gap-1.5"><span class="material-symbols-outlined text-[15px] text-primary">menu_book</span><span class="">REFERENCED RECORDS</span></div><div class="flex items-center gap-space-xs flex-wrap font-label-mono-tag text-label-mono-tag"><span class="inline-flex items-center gap-1 px-space-sm py-1 rounded bg-primary/10 border border-primary/30 text-primary font-body-spec-mono text-[12px]"><span class="material-symbols-outlined text-[14px]">table_rows</span><span class="">INS-2026-001</span></span><span class="inline-flex items-center gap-1 px-space-sm py-1 rounded bg-primary/10 border border-primary/30 text-primary font-body-spec-mono text-[12px]"><span class="material-symbols-outlined text-[14px]">receipt_long</span><span class="">REG-2026-002</span></span><span class="inline-flex items-center gap-1 px-space-sm py-1 rounded bg-primary/10 border border-primary/30 text-primary font-body-spec-mono text-[12px]"><span class="material-symbols-outlined text-[14px]">description</span><span class="">DOC-2026-003</span></span></div></div><div class="pt-space-md border-t border-surface-container-high font-label-mono-tag text-[11px] text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</div></div><div class="w-full max-w-[880px] bg-surface-container-low border border-outline-variant rounded-xl p-space-sm flex items-center gap-space-sm mt-space-xs"><div class="flex items-center justify-center pl-space-sm text-primary"><span class="material-symbols-outlined text-[20px]">terminal</span></div><input class="bg-transparent border-0 flex-1 font-body-spec text-body-spec text-on-surface placeholder:text-outline focus:outline-none" placeholder="Query additional block telemetry, isolate containment failure causes, or filter by volume..." type="text" value=""><button class="w-9 h-9 rounded bg-primary-container text-on-primary-container flex items-center justify-center hover:bg-primary transition-colors"><span class="material-symbols-outlined text-[20px]">arrow_forward</span></button></div></div></div></main></div>

</body></html>
```

3. asset_intelligence_copilot_console
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"outline-variant":"#3e484f","primary":"#8ed5ff","on-secondary-fixed-variant":"#005137","primary-container":"#38bdf8","surface-container":"#1a2028","surface-bright":"#343a42","on-error-container":"#ffdad6","surface":"#0e141c","on-secondary":"#003825","inverse-primary":"#00668a","error-container":"#93000a","tertiary":"#ffbcbf","primary-fixed":"#c4e7ff","secondary-fixed":"#68fcbf","on-error":"#690005","outline":"#87929a","on-secondary-fixed":"#002114","on-tertiary-container":"#8c0028","secondary-fixed-dim":"#45dfa4","on-tertiary-fixed-variant":"#92002a","surface-variant":"#2f353e","surface-tint":"#7bd0ff","on-primary-fixed":"#001e2c","on-tertiary":"#67001b","surface-container-highest":"#2f353e","surface-container-high":"#242a33","surface-container-low":"#161c24","on-surface":"#dde3ee","tertiary-fixed":"#ffdadb","background":"#0e141c","inverse-surface":"#dde3ee","on-primary-fixed-variant":"#004c69","on-primary-container":"#004965","on-surface-variant":"#bdc8d1","primary-fixed-dim":"#7bd0ff","on-secondary-container":"#00452e","surface-dim":"#0e141c","on-background":"#dde3ee","tertiary-fixed-dim":"#ffb2b7","error":"#ffb4ab","on-primary":"#00354a","inverse-on-surface":"#2b3139","tertiary-container":"#ff929a","surface-container-lowest":"#090f16","on-tertiary-fixed":"#40000d","secondary-container":"#00bd85","secondary":"#45dfa4"},borderRadius:{DEFAULT:"0.125rem",lg:"0.25rem",xl:"0.5rem",full:"0.75rem"},spacing:{"space-lg":"1.25rem","space-xl":"1.5rem","space-xs":"0.25rem","space-md":"1rem",margin:"1.5rem",gutter:"1.5rem","space-sm":"0.5rem"},fontFamily:{"body-spec":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"body-prose-medium":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel-mobile":["IBM Plex Sans"],"display-telemetry":["IBM Plex Mono"],"headline-panel":["IBM Plex Sans"]},fontSize:{"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}}</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low border-r border-outline-variant z-40 flex flex-col justify-between select-none"><div class="flex flex-col flex-1 min-h-0"><div class="p-space-md border-b border-outline-variant"><div class="flex items-center gap-space-sm mb-space-xs"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="font-headline-panel text-headline-panel tracking-tight text-on-surface">Asset Intelligence</span></div><div class="font-label-mono-tag text-label-mono-tag uppercase tracking-wider text-outline">OIL FIELD · 200 WELLS (50/BLOCK) · 4 BLOCKS</div></div><div class="p-space-md border-b border-outline-variant bg-surface-container-low"><div class="flex items-center justify-between"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono text-primary font-bold">MT</div><div class="flex flex-col min-w-0"><div class="font-body-spec-mono text-body-spec-mono text-on-surface truncate leading-tight">Michael Turner</div><div class="font-label-mono-tag text-label-mono-tag text-outline truncate">Production Supervisor</div></div></div><span class="material-symbols-outlined text-outline-variant text-[18px]">expand_more</span></div><div class="mt-space-sm pt-space-xs border-t border-outline-variant flex items-center justify-between text-outline"><span class="font-label-mono-tag text-label-mono-tag truncate">Northeast Production</span><div class="flex items-center gap-space-xs text-outline"><span class="material-symbols-outlined text-[14px]">lock</span><span class="font-label-mono-tag text-label-mono-tag text-[10px]">Private</span></div></div></div><div class="p-space-md"><a class="w-full flex items-center justify-center gap-space-sm py-space-sm px-space-md rounded-lg border border-primary-container text-primary-container hover:bg-surface-container hover:text-primary transition-colors font-body-spec-mono text-body-spec-mono" data-path="copilot-workspace" href="#"><span class="material-symbols-outlined text-[18px]">add</span><span class="">New chat</span></a></div><div class="px-space-md pt-space-xs pb-space-xs"><div class="font-label-mono-tag text-label-mono-tag uppercase text-outline tracking-wider">RECENT CHATS</div></div><nav class="flex-1 overflow-y-auto px-space-xs py-space-xs space-y-space-xs" data-active-classes="bg-surface-container text-primary border-l-2 border-primary-container"><a aria-current="page" class="flex flex-col px-space-md py-space-sm rounded-lg transition-colors bg-surface-container text-primary border-l-2 border-primary-container" href="#"><span class="font-body-spec-mono text-body-spec-mono truncate">WELL-0001 status and last inspection</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec-mono text-body-spec-mono truncate">Northeast Block 8 not producing</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec-mono text-body-spec-mono truncate">Block 7 downtime, top 3</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec-mono text-body-spec-mono truncate">WELL-0001 spills, last 4 years</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec-mono text-body-spec-mono truncate">Pump jack root-cause wells</span></a></nav></div></aside><div class="pl-[296px] min-h-screen flex flex-col"><header class="fixed top-0 left-[296px] right-0 h-14 bg-surface-container-low border-b border-outline-variant z-30 flex items-center justify-between px-space-lg"><div class="flex items-center gap-space-sm font-headline-panel text-headline-panel tracking-tight text-on-surface"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="">Asset Intelligence</span></div><div class="flex items-center gap-space-sm"><div class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container-high border border-outline-variant text-outline font-body-spec-mono text-label-mono-tag"><span class="material-symbols-outlined text-[15px] text-outline">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-2 px-2.5 py-1 rounded bg-surface-container border border-outline-variant text-on-surface font-body-spec text-label-mono-tag"><span class="w-2 h-2 rounded-full bg-secondary"></span><span class="font-medium text-on-surface">Michael Turner</span></div></div></header><main class="relative pt-14 w-full flex-1 bg-surface-container-lowest"><div class="flex flex-col w-full h-[calc(100vh-3.5rem)] overflow-hidden font-body-spec text-on-surface">
<div class="flex flex-1 h-full min-h-0 relative bg-surface-container-lowest">
<!-- PRIMARY COPILOT FLUID WORKSPACE (Centered 880px Thread Engine) -->
<div class="flex-1 flex flex-col min-w-0 h-full bg-surface">
<!-- SLIM TOP TELEMETRY BAR -->

<!-- SCROLLABLE OPERATIONAL CHAT STREAM (Max 880px target) -->
<div class="flex-1 overflow-y-auto px-8 py-6 space-y-6" id="threadStream">
<div class="max-w-[880px] mx-auto w-full space-y-6">
<!-- SECTION TIMESTAMP DIVIDER -->
<div class="flex items-center justify-center gap-3 my-2 select-none">
<div class="h-px bg-outline-variant flex-1"></div>
<span class="font-label-mono-tag text-[11px] uppercase tracking-widest text-outline bg-surface px-2">INCIDENT LOG VERIFICATION</span>
<div class="h-px bg-outline-variant flex-1"></div>
</div>
<!-- TURN 1: USER MESSAGE PLATE -->
<div class="flex justify-end w-full">
<div class="max-w-[620px] bg-surface-container rounded-lg border border-outline-variant p-4 space-y-2">
<div class="flex items-center justify-between border-b border-outline-variant pb-2">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary text-[15px]">person</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline tracking-wider uppercase">OPERATOR // MICHAEL TURNER (U-201)</span>
</div>
<span class="font-body-spec-mono text-[11px] text-outline">14:22:04 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface leading-relaxed">
Is <button class="inline-flex items-center px-1.5 py-0.5 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container font-body-spec-mono text-label-mono-tag hover:bg-primary-container/20 transition-colors align-baseline">WELL-0001</button> producing oil right now? When was it last inspected, and by whom? Show me its current operational status card.
</p>
</div>
</div>
<!-- TURN 2: ASSISTANT REPORT BLOCK (Zero-Fluff Technical Console Card) -->
<div class="w-full bg-surface-container-low border border-outline-variant border-l-[3px] border-l-primary-container rounded-r-lg p-6 space-y-5"><div class="flex items-center justify-between border-b border-outline-variant pb-3 text-outline"><div class="flex items-center gap-2.5"><div class="w-6 h-6 rounded bg-primary-container/10 border border-primary-container/40 flex items-center justify-center text-primary-container"><span class="material-symbols-outlined text-[15px]">model_training</span></div><span class="font-body-prose-medium text-body-spec font-medium text-on-surface">Asset Intelligence Copilot</span><span class="text-outline text-xs">/</span><span class="font-label-mono-tag text-label-mono-tag text-outline">WEEKLY INSPECTIONS</span></div><div class="flex items-center gap-3 font-label-mono-tag text-[11px]"><span class="flex items-center gap-1 text-outline"><span class="material-symbols-outlined text-[13px]">timer</span> 1.4s query time</span><span class="h-3 w-px bg-outline-variant"></span><span class="text-secondary">WEEKLY INSPECTIONS</span><span class="h-3 w-px bg-outline-variant"></span><span class="text-outline">14:22:08 UTC</span></div></div><div class="space-y-2"><div class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-secondary"></span><h3 class="font-headline-panel text-body-prose-medium text-on-surface font-semibold">WELL-0001 is ACTIVE &amp; PRODUCING</h3></div><p class="font-body-prose text-body-spec text-on-surface-variant leading-relaxed">Weekly inspection confirmed normal stroke frequency and steady flowline pressure. The asset was last visually cleared during physical rounds 19 days ago by Field Inspector <span class="text-on-surface font-medium">Jessica Reed</span> (badge <span class="font-body-spec-mono text-outline text-xs">U-203</span>) with zero critical flags.</p></div><div class="grid grid-cols-1 md:grid-cols-4 gap-3"><div class="bg-surface-container rounded border border-outline-variant p-3 space-y-1"><div class="flex items-center justify-between text-outline"><span class="font-label-metric text-[11px] uppercase tracking-wider">Flowline Pressure</span><span class="material-symbols-outlined text-secondary text-[14px]">trending_up</span></div><div class="flex items-baseline gap-1"><span class="font-display-telemetry text-headline-panel text-on-surface font-semibold">1,428</span><span class="font-body-spec-mono text-label-mono-tag text-outline">PSI</span></div><div class="flex items-center justify-between text-[11px] font-body-spec-mono pt-1 border-t border-outline-variant/60 text-secondary"><span class="">Δ +12 PSI vs avg</span><span class="text-outline">NOMINAL</span></div></div><div class="bg-surface-container rounded border border-outline-variant p-3 space-y-1"><div class="flex items-center justify-between text-outline"><span class="font-label-metric text-[11px] uppercase tracking-wider">Gross Liquid Rate</span><span class="material-symbols-outlined text-secondary text-[14px]">check_circle</span></div><div class="flex items-baseline gap-1"><span class="font-display-telemetry text-headline-panel text-on-surface font-semibold">342.6</span><span class="font-body-spec-mono text-label-mono-tag text-outline">BFPD</span></div><div class="flex items-center justify-between text-[11px] font-body-spec-mono pt-1 border-t border-outline-variant/60 text-outline"><span class="">Target: 340.0</span><span class="text-secondary">OPTIMAL</span></div></div><div class="bg-surface-container rounded border border-outline-variant p-3 space-y-1"><div class="flex items-center justify-between text-outline"><span class="font-label-metric text-[11px] uppercase tracking-wider">Pump Efficiency</span><span class="material-symbols-outlined text-secondary text-[14px]">speed</span></div><div class="flex items-baseline gap-1"><span class="font-display-telemetry text-headline-panel text-on-surface font-semibold">91.4</span><span class="font-body-spec-mono text-label-mono-tag text-outline">%</span></div><div class="flex items-center justify-between text-[11px] font-body-spec-mono pt-1 border-t border-outline-variant/60 text-outline"><span class="">Fillage: 94.2%</span><span class="text-secondary">BALANCED</span></div></div><div class="bg-surface-container rounded border border-outline-variant p-3 space-y-1"><div class="flex items-center justify-between text-outline"><span class="font-label-metric text-[11px] uppercase tracking-wider">Last Inspection</span><span class="material-symbols-outlined text-primary-container text-[14px]">verified</span></div><div class="flex items-baseline gap-1"><span class="font-display-telemetry text-headline-panel text-on-surface font-semibold">27 Sep</span><span class="font-body-spec-mono text-label-mono-tag text-outline">2026</span></div><div class="flex items-center justify-between text-[11px] font-body-spec-mono pt-1 border-t border-outline-variant/60 text-outline truncate"><span class="">Inspector: J. Reed</span><span class="text-primary-container">PASS</span></div></div></div><div class="bg-surface-container rounded border border-outline-variant p-4 space-y-3"><div class="flex items-center justify-between border-b border-outline-variant pb-2"><div class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-[16px]">stacked_line_chart</span><span class="font-label-metric text-label-metric text-on-surface uppercase tracking-wider">DYNAMOMETER CARDS // WEEKLY RUN PROFILE</span></div><span class="font-label-mono-tag text-[11px] text-outline">STROKE: 144 IN · 8.2 SPM</span></div><div class="grid grid-cols-1 lg:grid-cols-3 gap-4 pt-1"><div class="lg:col-span-2 h-36 bg-surface-container-low rounded border border-outline-variant/70 p-2 relative flex flex-col justify-between"><div class="flex justify-between items-center text-[10px] font-body-spec-mono text-outline px-1"><span class="">POLISHED ROD LOAD (LBS x 1,000)</span><span class="text-secondary">PEAK: 24.8k LBS // MIN: 7.2k LBS</span></div><div class="w-full flex-1 flex items-center justify-center"><svg class="w-full h-24 overflow-visible" fill="none" preserveAspectRatio="none" viewBox="0 0 460 90"><line stroke="#242a33" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="460" y1="20" y2="20"></line><line stroke="#242a33" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="460" y1="50" y2="50"></line><line stroke="#242a33" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="460" y1="80" y2="80"></line><path d="M 40 70 L 90 24 C 180 20, 360 22, 410 25 L 420 68 C 340 76, 120 74, 40 70 Z" fill="rgba(56, 189, 248, 0.05)" stroke="#3e484f" stroke-dasharray="3 3" stroke-width="1.2"></path><path d="M 44 68 L 92 26 C 185 23, 355 24, 408 27 L 416 66 C 335 73, 122 72, 44 68 Z" fill="rgba(69, 223, 164, 0.08)" stroke="#45dfa4" stroke-width="1.8"></path></svg></div><div class="flex justify-between items-center text-[10px] font-body-spec-mono text-outline px-1"><span class="">POSITION: 0" (BOTTOM OF STROKE)</span><span class="">144" (TOP OF STROKE)</span></div></div><div class="flex flex-col justify-between bg-surface-container-high rounded p-3 text-xs space-y-2 border border-outline-variant/60"><div class="space-y-1.5"><div class="font-label-metric text-[11px] text-outline uppercase tracking-wider">CARTRIDGE DIAGNOSTICS</div><div class="flex items-center gap-2 text-on-surface"><span class="material-symbols-outlined text-secondary text-[16px]">check_circle</span><span class="font-medium">Normal Liquid Load</span></div><p class="font-body-spec text-[12px] text-on-surface-variant leading-tight">No gas interference, fluid pound, or mechanical friction detected on sucker rod string.</p></div><div class="pt-2 border-t border-outline-variant text-[11px] font-body-spec-mono text-outline flex justify-between"><span class="">STROKE DURATION:</span><span class="text-on-surface">7.31 sec</span></div></div></div></div><div class="pt-3 border-t border-outline-variant flex flex-wrap items-center justify-between gap-3 text-xs"><div class="flex items-center gap-2 flex-wrap"><span class="font-label-mono-tag text-label-mono-tag text-outline uppercase">EVIDENCE CITATIONS:</span><button class="record-chip inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container font-body-spec-mono text-[11px] hover:bg-primary-container/20 transition-all cursor-pointer" data-record="INS-0001-0203"><span class="material-symbols-outlined text-[13px]">assignment_turned_in</span><span class="">INS-0001-0203</span></button><button class="record-chip inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container font-body-spec-mono text-[11px] hover:bg-primary-container/20 transition-all cursor-pointer" data-record="MNT-0001-032"><span class="material-symbols-outlined text-[13px]">build</span><span class="">MNT-0001-032</span></button><button class="record-chip inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container font-body-spec-mono text-[11px] hover:bg-primary-container/20 transition-all cursor-pointer" data-record="REG-0001-002"><span class="material-symbols-outlined text-[13px]">policy</span><span class="">REG-0001-002</span></button></div></div><div class="pt-2 border-t border-outline-variant/60 font-body-spec-mono text-[11px] text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</div></div>
<!-- DYNAMIC STREAM EXTENSION CONTAINER (for user interaction responses) -->
<div class="space-y-6" id="dynamicResponses"></div>
</div>
</div>
<!-- PINNED BOTTOM COMPOSER DOCK (880px Centered) -->
<div class="border-t border-outline-variant bg-surface-container-low shrink-0 px-8 py-3 w-full"><div class="max-w-[880px] mx-auto w-full space-y-2.5"><div class="flex items-center gap-2 overflow-x-auto pb-0.5 no-scrollbar"><span class="font-label-mono-tag text-[10px] uppercase text-outline shrink-0 tracking-wider">QUERY ACCELERATORS:</span><button class="query-prompt-btn px-2.5 py-1 rounded-md bg-surface-container border border-outline-variant text-outline hover:text-primary-container hover:border-primary-container transition-colors font-body-spec text-[12px] whitespace-nowrap shrink-0 flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">search</span><span class="">Wells not producing in Northeast Block 8</span></button><button class="query-prompt-btn px-2.5 py-1 rounded-md bg-surface-container border border-outline-variant text-outline hover:text-primary-container hover:border-primary-container transition-colors font-body-spec text-[12px] whitespace-nowrap shrink-0 flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">opacity</span><span class="">Spills by area and month, 2026</span></button><button class="query-prompt-btn px-2.5 py-1 rounded-md bg-surface-container border border-outline-variant text-outline hover:text-primary-container hover:border-primary-container transition-colors font-body-spec text-[12px] whitespace-nowrap shrink-0 flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">gavel</span><span class="">Which rules has WELL-0001 broken?</span></button></div><div class="h-14 rounded-lg bg-surface border border-outline-variant focus-within:border-primary-container focus-within:ring-1 focus-within:ring-primary-container/40 flex items-center px-4 gap-3 transition-all"><span class="material-symbols-outlined text-outline text-[20px] select-none">terminal</span><input autocomplete="off" class="flex-1 bg-transparent border-0 outline-none text-on-surface placeholder:text-outline font-body-spec text-body-spec min-w-0" id="promptInput" placeholder="Ask about a well, a block, a spill or a repair..." type="text"><div class="flex items-center"><button class="w-9 h-9 rounded bg-primary-container hover:bg-primary text-surface-container-lowest flex items-center justify-center transition-colors font-semibold" id="sendPromptBtn" title="Execute Query"><span class="material-symbols-outlined text-[20px]">arrow_forward</span></button></div></div></div></div>
</div>
<!-- RIGHT AUDIT / RECORD SLIDE-OVER DRAWER (420px Fixed) -->
<div class="w-[420px] border-l border-outline-variant bg-surface-container-low flex flex-col h-full shrink-0 transition-transform duration-200 ease-in-out" id="recordDrawer">
<!-- Drawer Header -->
<div class="h-14 border-b border-outline-variant px-5 flex items-center justify-between bg-surface-container-low shrink-0">
<div class="flex items-center gap-2 min-w-0">
<span class="material-symbols-outlined text-primary-container text-[20px]">folder_open</span>
<span class="font-headline-panel text-body-prose-medium text-on-surface truncate">Evidence Audit Ledger</span>
</div>
<div class="flex items-center gap-2">
<span class="px-2 py-0.5 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container font-body-spec-mono text-[11px]" id="currentRecordTag">INS-0001-0203</span>
<button class="w-7 h-7 rounded hover:bg-surface-container-high text-outline hover:text-on-surface flex items-center justify-center transition-colors" id="closeDrawerBtn">
<span class="material-symbols-outlined text-[18px]">close</span>
</button>
</div>
</div>
<!-- Drawer Content Stream -->
<div class="flex-1 overflow-y-auto p-5 space-y-5">
<!-- Record Header Card -->
<div class="bg-surface-container rounded-lg border border-outline-variant p-4 space-y-3"><div class="flex items-center justify-between border-b border-outline-variant pb-2"><span class="font-label-mono-tag text-label-mono-tag text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">check_circle</span> VERIFIED RECORD</span><span class="font-body-spec-mono text-[11px] text-outline">REV 1.0</span></div><div><div class="font-headline-panel text-body-prose-medium text-on-surface font-semibold">Q3 Comprehensive Wellhead Inspection</div><div class="font-label-mono-tag text-[12px] text-outline pt-0.5">Asset Target: WELL-0001 · North Block · Pad-A</div></div><div class="grid grid-cols-2 gap-2 pt-2 border-t border-outline-variant/60 font-body-spec-mono text-xs"><div><span class="text-outline block text-[10px] uppercase">Inspection Timestamp</span><span class="text-on-surface">2026-09-27 10:14 CST</span></div><div><span class="text-outline block text-[10px] uppercase">Inspector Signature</span><span class="text-on-surface">J. Reed (U-203)</span></div><div><span class="text-outline block text-[10px] uppercase">Protocol</span><span class="text-on-surface">WEEKLY VERIFIED</span></div><div><span class="text-outline block text-[10px] uppercase">HSE Compliance</span><span class="text-secondary font-medium">100% CLEAR</span></div></div></div>
<!-- Physical Inspection Checklist Details -->
<div class="space-y-2">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric text-outline uppercase tracking-wider">CHECKLIST TELEMETRY &amp; ATTRIBUTES</span>
<span class="font-label-mono-tag text-[10px] text-secondary">6/6 VERIFIED</span>
</div>
<div class="bg-surface-container rounded border border-outline-variant divide-y divide-outline-variant text-xs">
<div class="p-3 flex items-start justify-between gap-3">
<div>
<span class="font-body-prose-medium text-on-surface block">Stuffing Box &amp; Polish Rod Packoff</span>
<span class="text-outline text-[11px]">Zero hydrocarbons detected at seal face. Cone packing replaced 40d ago.</span>
</div>
<span class="px-2 py-0.5 rounded bg-secondary/10 border border-secondary/30 text-secondary font-label-mono-tag text-[10px]">PASS</span>
</div>
<div class="p-3 flex items-start justify-between gap-3">
<div>
<span class="font-body-prose-medium text-on-surface block">Master &amp; Wing Gate Valves</span>
<span class="text-outline text-[11px]">Cycled 2 full turns to verify free travel. Flange bolts torqued to 340 ft-lb.</span>
</div>
<span class="px-2 py-0.5 rounded bg-secondary/10 border border-secondary/30 text-secondary font-label-mono-tag text-[10px]">PASS</span>
</div>
<div class="p-3 flex items-start justify-between gap-3">
<div>
<span class="font-body-prose-medium text-on-surface block">Flowline Ultrasonic Wall Gauge</span>
<span class="text-outline text-[11px]">Wall thickness 0.380 in vs nominal 0.400 in (5% erosion, within tolerance).</span>
</div>
<span class="px-2 py-0.5 rounded bg-secondary/10 border border-secondary/30 text-secondary font-label-mono-tag text-[10px]">PASS</span>
</div>
<div class="p-3 flex items-start justify-between gap-3">
<div>
<span class="font-body-prose-medium text-on-surface block">Secondary Containment Berm</span>
<span class="text-outline text-[11px]">Dry liner integrity verified; no pooling liquids or salt crust residue.</span>
</div>
<span class="px-2 py-0.5 rounded bg-secondary/10 border border-secondary/30 text-secondary font-label-mono-tag text-[10px]">PASS</span>
</div>
</div>
</div>
<!-- Field Inspector Notes & Photo Stamp -->
<div class="bg-surface-container rounded border border-outline-variant p-4 space-y-3">
<div class="flex items-center justify-between border-b border-outline-variant pb-2">
<span class="font-label-metric text-label-metric text-outline uppercase tracking-wider">FIELD OPERATOR LOG EXTRACT</span>
<span class="material-symbols-outlined text-[16px] text-outline">description</span>
</div>
<p class="font-body-spec text-xs text-on-surface-variant leading-relaxed">
"Arrived 09:45 AM. Ambient temperature 74°F. Visual check shows zero vibration on casing head. Flowing casing pressure registered 42 PSI (normal). Fluid level shot indicates pump intake at 7,420 ft TVD with 480 ft pump submergence. Lubricator reservoir topped with Grade ISO VG 220 oil. Ready for continued continuous lift."
</p>
<div class="pt-2 border-t border-outline-variant flex items-center justify-between text-[11px] font-body-spec-mono text-outline"><span class="text-primary-container font-body-spec-mono text-[11px]">SIGN-OFF VALIDATED</span></div>
</div>
<!-- Related Work Orders Ledger -->
<div class="space-y-2">
<span class="font-label-metric text-label-metric text-outline uppercase tracking-wider">ATTACHED WORK ORDERS</span>
<div class="bg-surface-container-high rounded p-3 border border-outline-variant flex items-center justify-between text-xs">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary-container text-[18px]">engineering</span>
<div>
<span class="font-body-prose-medium text-on-surface block">MNT-0001-032 Valve Lube</span>
<span class="text-outline text-[11px]">Completed by T. Hughes</span>
</div>
</div>
<span class="font-body-spec-mono text-[11px] text-outline">12d ago</span>
</div>
</div>
</div>
<!-- Drawer Footer Action -->

</div>
</div>
</div>
<!-- CLIENT MICRO-INTERACTIONS LOGIC -->
<script>
(function initIndustrialConsole() {
const threadStream = document.getElementById('threadStream');
const dynamicResponses = document.getElementById('dynamicResponses');
const promptInput = document.getElementById('promptInput');
const sendPromptBtn = document.getElementById('sendPromptBtn');
const recordChips = document.querySelectorAll('.record-chip');
const recordDrawer = document.getElementById('recordDrawer');
const closeDrawerBtn = document.getElementById('closeDrawerBtn');
const inspectDrawerBtn = document.getElementById('inspectDrawerBtn');
const currentRecordTag = document.getElementById('currentRecordTag');
const queryButtons = document.querySelectorAll('.query-prompt-btn');

// Drawer toggles
let isDrawerOpen = true;
function setDrawer(open) {
isDrawerOpen = open;
if (open) {
recordDrawer.classList.remove('hidden');
} else {
recordDrawer.classList.add('hidden');
}
}

if (closeDrawerBtn) {
closeDrawerBtn.addEventListener('click', () => setDrawer(false));
}
if (inspectDrawerBtn) {
inspectDrawerBtn.addEventListener('click', () => setDrawer(!isDrawerOpen));
}

// Record inspection interaction
recordChips.forEach(chip => {
chip.addEventListener('click', (e) => {
const recordId = chip.getAttribute('data-record') || 'INS-0001-0203';
if (currentRecordTag) currentRecordTag.textContent = recordId;
setDrawer(true);
});
});

// Query Accelerator Buttons
queryButtons.forEach(btn => {
btn.addEventListener('click', () => {
const queryText = btn.querySelector('span:last-child').textContent.trim();
if (promptInput) {
promptInput.value = queryText;
promptInput.focus();
}
});
});

// Execution of prompt
function executeQuery() {
if (!promptInput) return;
const text = promptInput.value.trim();
if (!text) return;

const userTime = new Date().toTimeString().split(' ')[0];

// Append User Message
const userNode = document.createElement('div');
userNode.className = "flex justify-end w-full";
userNode.innerHTML = `
<div class="max-w-[620px] bg-surface-container rounded-lg border border-outline-variant p-4 space-y-2">
<div class="flex items-center justify-between border-b border-outline-variant pb-2">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary text-[15px]">person</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline tracking-wider uppercase">OPERATOR // MICHAEL TURNER (U-201)</span>
</div>
<span class="font-body-spec-mono text-[11px] text-outline">${userTime} UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface leading-relaxed">${escapeHtml(text)}</p>
</div>
`;
dynamicResponses.appendChild(userNode);

// Append System Processing Node
const sysNode = document.createElement('div');
sysNode.className = "w-full bg-surface-container-low border border-outline-variant border-l-[3px] border-l-primary-container rounded-r-lg p-6 space-y-4";
sysNode.innerHTML = `
<div class="flex items-center justify-between border-b border-outline-variant pb-3 text-outline">
<div class="flex items-center gap-2.5">
<div class="w-6 h-6 rounded bg-primary-container/10 border border-primary-container/40 flex items-center justify-center text-primary-container">
<span class="material-symbols-outlined text-[15px]">model_training</span>
</div>
<span class="font-body-prose-medium text-body-spec font-medium text-on-surface">Asset Intelligence Copilot</span>
<span class="text-outline text-xs">/</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">CROSS-BLOCK TELEMETRY AUDIT</span>
</div>
<div class="flex items-center gap-2 font-label-mono-tag text-[11px] text-secondary">
<span class="w-1.5 h-1.5 rounded-full bg-secondary animate-pulse"></span>
<span>SCAN COMPLETE · 0.9s</span>
</div>
</div>
<div class="space-y-2">
<div class="font-headline-panel text-body-prose-medium text-on-surface font-semibold">Query Evaluated: Multi-Vector Scan</div>
<p class="font-body-spec text-body-spec text-on-surface-variant leading-relaxed">
Correlated target parameter against 200 field transmitters across Blocks 1 through 4. No emergency ESD or threshold breach logged for requested criteria in the current 12-hour operational shift.
</p>
</div>
<div class="bg-surface-container rounded border border-outline-variant p-3 flex items-center justify-between text-xs font-body-spec-mono">
<span class="text-outline">DATABASE TARGETS CHECKED: [SCADA_HISTORIAN_B3, EPA_NOTIFICATIONS_2026]</span>
<span class="text-primary-container">0 EXCEEDANCES</span>
</div>
`;
dynamicResponses.appendChild(sysNode);

promptInput.value = '';
if (threadStream) {
setTimeout(() => {
threadStream.scrollTop = threadStream.scrollHeight;
}, 50);
}
}

function escapeHtml(string) {
return String(string).replace(/[&<>"'`=\/]/g, function (s) {
return {
'&': '&amp;',
'<': '&lt;',
'>': '&gt;',
'"': '&quot;',
"'": '&#39;',
'/': '&#x2F;',
'`': '&#x60;',
'=': '&#x3D;'
}[s];
});
}

if (sendPromptBtn) {
sendPromptBtn.addEventListener('click', executeQuery);
}
if (promptInput) {
promptInput.addEventListener('keydown', (e) => {
if (e.key === 'Enter') {
e.preventDefault();
executeQuery();
}
});
}

})();
</script></main></div>

</body></html>
```


4. assistant_message_component_asset_intelligence
```
<!DOCTYPE html><html lang="en" class="dark"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Asset Intelligence - Assistant Message Component Spec</title>
<!-- Google Fonts: IBM Plex Sans & IBM Plex Mono -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&amp;family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest"></script>
<script>
tailwind.config = {
darkMode: 'class',
theme: {
extend: {
colors: {
bg: '#0B0F14',
surface: '#121820',
'raised-surface': '#1A222D',
border: '#263140',
hairline: '#1E2733',
'primary-text': '#E6EDF3',
'secondary-text': '#8B98A8',
'disabled-text': '#5B6675',
'signal-cyan': '#38BDF8',
'status-ok': '#34D399',
'status-warn': '#FBBF24',
'status-crit': '#F43F5E',
'status-unconfirmed': '#A78BFA',
'status-neutral': '#94A3B8',
},
fontFamily: {
sans: ['"IBM Plex Sans"', 'sans-serif'],
mono: ['"IBM Plex Mono"', 'monospace'],
}
}
}
}
</script>
<style>
body {
background-color: #0B0F14;
color: #E6EDF3;
font-family: 'IBM Plex Sans', sans-serif;
}
.mono-num {
font-family: 'IBM Plex Mono', monospace;
font-variant-numeric: tabular-nums;
}
/* Custom tooltip styling */
.has-tooltip:hover .tooltip-box {
opacity: 1;
visibility: visible;
transform: translateY(-4px);
}
</style>
</head>
<body class="min-h-screen p-6 md:p-12 flex flex-col items-center justify-start antialiased selection:bg-[#38BDF8]/20 selection:text-[#38BDF8]">

<!-- Context / Component Stage Header -->
<header class="w-full max-w-[880px] mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#263140] pb-4"><div>
<div class="flex items-center gap-2 mb-1">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded text-[11px] font-mono tracking-wider uppercase bg-[#1A222D] text-[#38BDF8] border border-[#263140]">
<i data-lucide="cpu" class="w-3.5 h-3.5 stroke-[1.5]"></i> Component Spec // AI-MSG-REPORT
</span>
</div>
<h1 class="text-lg font-semibold tracking-tight text-[#E6EDF3]">Assistant Operational Report</h1>
</div>
<div class="flex items-center gap-2 font-mono text-xs text-[#8B98A8]">
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-[#121820] border border-[#263140] text-[#E6EDF3]">
<i data-lucide="calendar" class="w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]"></i> Today: 17 Oct 2026
</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-[#121820] border border-[#263140] text-[#E6EDF3]">
<i data-lucide="user" class="w-3.5 h-3.5 stroke-[1.5] text-[#34D399]"></i> Michael Turner
</span>
</div></header>

<!-- Query Context Visual (User Question Plate) -->
<div class="w-full max-w-[880px] mb-4 flex justify-end">
<div class="max-w-[620px] rounded-[10px] bg-[#1A222D] border border-[#263140] px-4 py-3 text-sm text-[#E6EDF3] leading-relaxed shadow-sm">
<div class="flex items-center justify-between gap-4 mb-1">
<span class="text-[11px] font-mono uppercase tracking-wider text-[#8B98A8] flex items-center gap-1.5">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="user" aria-hidden="true" class="lucide lucide-user w-3 h-3 stroke-[1.5]"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> Operator Query
</span>
<span class="text-[11px] font-mono text-[#5B6675]">14:28:11 UTC</span>
</div>
<p class="">
Which rules has <span class="inline-flex items-center px-1.5 py-0.2 rounded bg-[#38BDF8]/10 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium cursor-pointer hover:bg-[#38BDF8]/20 transition-colors">WELL-0001</span> broken in the last 12 months, and what is still open?
</p>
</div>
</div>

<!-- MAIN COMPONENT: Assistant Message Report Block (880px wide) -->
<main class="w-full max-w-[880px] bg-[#121820] border border-[#263140] rounded-[10px] p-5 relative transition-all shadow-xl" style="border-left: 2px solid #38BDF8;">

<!-- TOP FLAGS AREA: Stacked Operational Banners -->
<section class="flex flex-col gap-2.5 mb-5" aria-label="Top Flags Area">

<!-- Flag 1: OVERDUE (Critical) -->
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#F43F5E]/[0.12] border border-[#F43F5E] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#F43F5E] flex items-center justify-center">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="alert-octagon" aria-hidden="true" class="lucide lucide-alert-octagon w-4 h-4 stroke-[1.5]"><path d="M12 16h.01"></path><path d="M12 8v4"></path><path d="M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#F43F5E] flex-shrink-0">OVERDUE</span>
<span class="text-[#E6EDF3] leading-tight font-normal truncate">SR-03 clean-up verification was due 10 Aug 2026 and is still open.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a href="#REG-0001-003" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="scale" aria-hidden="true" class="lucide lucide-scale w-3 h-3 stroke-[1.5]"><path d="M12 3v18"></path><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"></path><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M7 21h10"></path></svg> REG-0001-003
</a>
</div>
</article>

<!-- Flag 2: OVERDUE (Critical) -->
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#F43F5E]/[0.12] border border-[#F43F5E] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#F43F5E] flex items-center justify-center">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="alert-octagon" aria-hidden="true" class="lucide lucide-alert-octagon w-4 h-4 stroke-[1.5]"><path d="M12 16h.01"></path><path d="M12 8v4"></path><path d="M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#F43F5E] flex-shrink-0">OVERDUE</span>
<span class="text-[#E6EDF3] leading-tight font-normal truncate">RC-04 notice of violation response was due 30 Jul 2026. No response recorded.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a href="#REG-0001-002" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="scale" aria-hidden="true" class="lucide lucide-scale w-3 h-3 stroke-[1.5]"><path d="M12 3v18"></path><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"></path><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M7 21h10"></path></svg> REG-0001-002
</a>
</div>
</article>

<!-- Flag 3: CORRECTION APPLIED (Neutral) -->
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#94A3B8]/[0.12] border border-[#94A3B8] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#94A3B8] flex items-center justify-center">
<!-- Pencil check icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="file-check-2" aria-hidden="true" class="lucide lucide-file-check-2 w-4 h-4 stroke-[1.5]"><path d="M10.5 22H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.706.706l3.588 3.588A2.4 2.4 0 0 1 20 8v6"></path><path d="M14 2v5a1 1 0 0 0 1 1h5"></path><path d="m14 20 2 2 4-4"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#94A3B8] flex-shrink-0">CORRECTION APPLIED</span>
<span class="text-[#E6EDF3] leading-tight font-normal truncate">INS-0001-0070 (7 Mar 2024) was corrected to rainwater and is excluded.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a href="#CTX-0001-001" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="sticky-note" aria-hidden="true" class="lucide lucide-sticky-note w-3 h-3 stroke-[1.5]"><path d="M21 9a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 15 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2z"></path><path d="M15 3v5a1 1 0 0 0 1 1h5"></path></svg> CTX-0001-001
</a>
</div>
</article>

</section>

<!-- ANSWER BODY: 16px, line-height 1.55, Rendered Markdown Content -->
<section class="text-[16px] text-[#E6EDF3] leading-[1.55] space-y-4 mb-6">

<!-- Lead Sentence -->
<p class="font-normal text-[#E6EDF3] tracking-tight">
<span class="inline-flex items-center px-1.5 py-0.2 rounded bg-[#38BDF8]/10 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-sm font-medium mr-1">WELL-0001</span> broke <strong class="font-semibold text-white">4 rules</strong>, all tied to the <span class="font-mono text-[15px] font-medium text-[#E6EDF3]">11 Jun 2026</span> spill of <span class="font-mono text-[15px] font-medium text-[#E6EDF3]">6.8 bbl</span>. <strong class="text-[#F43F5E] font-semibold mono-num">USD 5,000</strong> in fines are still open.
</p>

<!-- Protocol Bullet List -->
<ul class="space-y-2.5 my-3 pl-1">
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] mt-[10px] flex-shrink-0"></span>
<div>
<span class="font-mono font-bold text-white tracking-wide">SR-01:</span>
<span class="text-[#E6EDF3]"> reported after <span class="font-mono font-medium text-[#F43F5E]">41 hours</span> against a <span class="font-mono text-[#8B98A8]">24-hour</span> limit; notice of violation with a <span class="font-mono font-medium text-[#F43F5E]">USD 5,000</span> fine, <span class="text-[#F43F5E] font-medium">still open</span>.</span>
</div>
</li>
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] mt-[10px] flex-shrink-0"></span>
<div>
<span class="font-mono font-bold text-white tracking-wide">SR-02:</span>
<span class="text-[#E6EDF3]"> contained after about <span class="font-mono font-medium text-[#FBBF24]">7 hours</span> against a <span class="font-mono text-[#8B98A8]">4-hour</span> limit.</span>
</div>
</li>
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] mt-[10px] flex-shrink-0"></span>
<div>
<span class="font-mono font-bold text-white tracking-wide">SR-03:</span>
<span class="text-[#E6EDF3]"> clean-up verification due <span class="font-mono text-white">10 Aug 2026</span>, <span class="text-[#F43F5E] font-medium">still open</span>.</span>
</div>
</li>
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] mt-[10px] flex-shrink-0"></span>
<div>
<span class="font-mono font-bold text-white tracking-wide">RC-04:</span>
<span class="text-[#E6EDF3]"> response due <span class="font-mono text-white">30 Jul 2026</span>, <span class="text-[#F43F5E] font-medium">none recorded</span>.</span>
</div>
</li>
</ul>

<!-- Sub-section: Open Actions, Not Yet Breaches -->
<div class="pt-2">
<h4 class="font-bold text-sm text-[#E6EDF3] tracking-wide mb-2 flex items-center gap-2">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="clock-alert" aria-hidden="true" class="lucide lucide-clock-alert w-4 h-4 text-[#FBBF24] stroke-[1.5]"><path d="M12 6v6l4 2"></path><path d="M20 12v5"></path><path d="M20 21h.01"></path><path d="M21.25 8.2A10 10 0 1 0 16 21.16"></path></svg>
Open actions, not yet breaches
</h4>
<ul class="space-y-2 pl-1 text-[15px] text-[#8B98A8]">
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#8B98A8] mt-[9px] flex-shrink-0"></span>
<span class="">Root-cause analysis due on the flowline (<span class="font-mono text-xs text-[#E6EDF3] bg-[#1A222D] px-1.5 py-0.5 rounded border border-[#263140]">3 corrective repairs in 12 months</span>);</span>
</li>
<li class="flex items-start gap-2.5">
<span class="w-1.5 h-1.5 rounded-full bg-[#8B98A8] mt-[9px] flex-shrink-0"></span>
<span class="">Planned shut-in from <span class="font-mono text-xs text-[#E6EDF3]">7 Oct</span> not yet in the maintenance system.</span>
</li>
</ul>
</div>

</section>

<!-- CITATIONS STRIP: Sources (6) with Tooltips and Kind Icons -->
<section class="border-t border-[#1E2733] pt-3.5 mb-4" aria-label="Citations Strip">
<div class="flex items-center gap-2 mb-2.5">
<span class="text-[11px] font-mono font-semibold tracking-wider uppercase text-[#8B98A8] flex items-center gap-1.5">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="file-text" aria-hidden="true" class="lucide lucide-file-text w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]"><path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"></path><path d="M14 2v5a1 1 0 0 0 1 1h5"></path><path d="M10 9H8"></path><path d="M16 13H8"></path><path d="M16 17H8"></path></svg>
SOURCES (6)
</span>
<span class="text-[11px] text-[#5B6675]">· Hover citation to preview audit record</span>
</div>

<div class="flex flex-wrap items-center gap-2">

<!-- Source 1: REG-0001-001 (regulatory) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="scale" aria-hidden="true" class="lucide lucide-scale w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M12 3v18"></path><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"></path><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M7 21h10"></path></svg>
REG-0001-001
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#38BDF8] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Regulatory Incident Dossier</span>
<span class="">11 JUN 2026</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">Spill notice: 6.8 bbl crude discharge on Wellhead Pad-A. Initial notification delayed.</p>
</div>
</div>

<!-- Source 2: REG-0001-002 (regulatory) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="scale" aria-hidden="true" class="lucide lucide-scale w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M12 3v18"></path><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"></path><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M7 21h10"></path></svg>
REG-0001-002
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#F43F5E] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Violation Penalty Notice</span>
<span class="">USD 5,000 FINE</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">Notice of Violation RC-04: Formal response was legally due 30 Jul 2026. Delinquent status.</p>
</div>
</div>

<!-- Source 3: REG-0001-003 (regulatory) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="scale" aria-hidden="true" class="lucide lucide-scale w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M12 3v18"></path><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"></path><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"></path><path d="M7 21h10"></path></svg>
REG-0001-003
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#F43F5E] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Remediation Order</span>
<span class="">OPEN AUDIT</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">SR-03 clean-up verification sign-off mandated within 60 days of containment. Due 10 Aug 2026.</p>
</div>
</div>

<!-- Source 4: MNT-0001-032 (maintenance) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="wrench" aria-hidden="true" class="lucide lucide-wrench w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.106-3.105c.32-.322.863-.22.983.218a6 6 0 0 1-8.259 7.057l-7.91 7.91a1 1 0 0 1-2.999-3l7.91-7.91a6 6 0 0 1 7.057-8.259c.438.12.54.662.219.984z"></path></svg>
MNT-0001-032
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#38BDF8] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Work Order · Workover</span>
<span class="">18 JUL 2026</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">Flowline gasket replacement and polish rod packoff repacking following minor pressure surge.</p>
</div>
</div>

<!-- Source 5: CTX-0001-003 (note) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="sticky-note" aria-hidden="true" class="lucide lucide-sticky-note w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M21 9a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 15 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2z"></path><path d="M15 3v5a1 1 0 0 0 1 1h5"></path></svg>
CTX-0001-003
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#8B98A8] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Shift Handover Note</span>
<span class="">U-203 REED</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">Field supervisor remarks confirming pending EPA environmental filing and Berm soil survey sample.</p>
</div>
</div>

<!-- Source 6: DOC-SR-SOP (document: Spill Response SOP) -->
<div class="relative has-tooltip">
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] hover:border-[#38BDF8]/60 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium transition-all group">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="file-code" aria-hidden="true" class="lucide lucide-file-code w-3.5 h-3.5 stroke-[1.5] text-[#38BDF8]/80 group-hover:text-[#38BDF8]"><path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"></path><path d="M14 2v5a1 1 0 0 0 1 1h5"></path><path d="M10 12.5 8 15l2 2.5"></path><path d="m14 12.5 2 2.5-2 2.5"></path></svg>
DOC-SR-SOP
</button>
<div class="tooltip-box pointer-events-none absolute bottom-full right-0 sm:left-0 mb-2 w-72 bg-[#1A222D] border border-[#263140] rounded-[8px] p-2.5 text-xs text-[#E6EDF3] opacity-0 invisible transition-all z-20 shadow-2xl">
<div class="font-mono text-[10px] text-[#34D399] uppercase tracking-wider mb-1 flex items-center justify-between">
<span class="">Standard Operating Procedure</span>
<span class="">REV 4.2</span>
</div>
<p class="text-[11px] text-[#8B98A8] leading-tight">Corporate EHS Manual §4.1: Basin Spill Escalation Timelines &amp; Notification Protocols.</p>
</div>
</div>

</div>
</section>

<!-- FOOTER META LINE: Execution Metadata & Interaction Controls -->
<footer class="border-t border-[#1E2733] pt-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">

<!-- Execution Metadata -->
<div class="flex items-center gap-2 font-mono text-[11px] text-[#8B98A8] overflow-x-auto"><span class="inline-flex items-center gap-1 text-[#E6EDF3] font-medium">
<i data-lucide="sparkles" class="w-3 h-3 text-[#38BDF8]"></i> gemma-4-26b-a4b-it
</span>
<span class="text-[#5B6675]">-</span>
<span class="text-[#34D399] mono-num">1.4 s</span>
<span class="text-[#5B6675]">-</span>
<span class="text-[#8B98A8]">tools: well_status</span></div>

<!-- Action Buttons -->
<div class="flex items-center gap-1.5 self-end sm:self-auto flex-shrink-0">
<!-- Copy Button -->
<button title="Copy message content" class="p-1.5 rounded-[6px] text-[#8B98A8] hover:text-[#E6EDF3] hover:bg-[#1A222D] border border-transparent hover:border-[#263140] transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="copy" aria-hidden="true" class="lucide lucide-copy w-4 h-4 stroke-[1.5]"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>
</button>
<!-- Thumbs Up -->
<button title="Helpful report" class="p-1.5 rounded-[6px] text-[#8B98A8] hover:text-[#34D399] hover:bg-[#1A222D] border border-transparent hover:border-[#263140] transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="thumbs-up" aria-hidden="true" class="lucide lucide-thumbs-up w-4 h-4 stroke-[1.5]"><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"></path><path d="M7 10v12"></path></svg>
</button>
<!-- Thumbs Down -->
<button title="Report discrepancy" class="p-1.5 rounded-[6px] text-[#8B98A8] hover:text-[#F43F5E] hover:bg-[#1A222D] border border-transparent hover:border-[#263140] transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="thumbs-down" aria-hidden="true" class="lucide lucide-thumbs-down w-4 h-4 stroke-[1.5]"><path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22a3.13 3.13 0 0 1-3-3.88Z"></path><path d="M17 14V2"></path></svg>
</button>
<!-- Divider -->
<div class="w-[1px] h-4 bg-[#263140] mx-1"></div>
<!-- Correct This Button -->
<button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#E6EDF3] hover:text-[#38BDF8] border border-[#263140] font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="edit-3" aria-hidden="true" class="lucide lucide-edit-3 w-3.5 h-3.5 stroke-[1.5]"><path d="M13 21h8"></path><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"></path></svg> Correct this
</button>
</div>

</footer>

</main>

<!-- SECTION: Flag Variants Documentation & Showcase -->
<section class="w-full max-w-[880px] mt-10 pt-6 border-t border-[#263140]" aria-labelledby="flag-variants-heading">

<div class="flex items-center justify-between mb-4">
<div class="flex items-center gap-2">
<h3 id="flag-variants-heading" class="text-xs font-mono font-semibold uppercase tracking-wider text-[#8B98A8]">
Flag Variants
</h3>
<span class="text-[11px] text-[#5B6675]">· Operational indicator banners specified by the design system</span>
</div>
<span class="text-[11px] font-mono text-[#8B98A8]">3 STATES PRESENTED</span>
</div>

<div class="flex flex-col gap-3">

<!-- Variant 1: CONFLICT (Warning - Amber) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#FBBF24]"></span>
CONFLICT FLAG (Warning State · 12% Tinted Fill · 1px Solid Border)
</span>
<span class="text-[#5B6675]">split-arrows icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#FBBF24]/[0.12] border border-[#FBBF24] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#FBBF24] flex items-center justify-center">
<!-- split-arrows icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="git-fork" aria-hidden="true" class="lucide lucide-git-fork w-4 h-4 stroke-[1.5]"><circle cx="12" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><circle cx="18" cy="6" r="3"></circle><path d="M18 9v2c0 .6-.4 1-1 1H7c-.6 0-1-.4-1-1V9"></path><path d="M12 12v3"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#FBBF24] flex-shrink-0">CONFLICT</span>
<span class="text-[#E6EDF3] leading-tight font-normal">Inspection note 'Pump jack not moving.' (Tyler Hughes) disagrees with the corrected reading of 41.0 C. Please confirm.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a href="#INS-0164-0205" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="clipboard-check" aria-hidden="true" class="lucide lucide-clipboard-check w-3 h-3 stroke-[1.5]"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"></rect><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><path d="m9 14 2 2 4-4"></path></svg> INS-0164-0205
</a>
</div>
</article>
</div>

<!-- Variant 2: UNCONFIRMED (Violet - Dashed Border) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#A78BFA]"></span>
UNCONFIRMED FLAG (Violet State · 12% Tinted Fill · 1px DASHED Border)
</span>
<span class="text-[#5B6675]">question icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#A78BFA]/[0.12] text-xs" style="border: 1px dashed #A78BFA;">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#A78BFA] flex items-center justify-center">
<!-- question icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="help-circle" aria-hidden="true" class="lucide lucide-help-circle w-4 h-4 stroke-[1.5]"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><path d="M12 17h.01"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#A78BFA] flex-shrink-0">UNCONFIRMED</span>
<span class="text-[#E6EDF3] leading-tight font-normal">Tyler Hughes says WELL-0175 is running fine. The 15 Oct inspection shows 0.4 C above air. Kept on record, awaiting confirmation.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a href="#INS-0175-0205" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="clipboard-check" aria-hidden="true" class="lucide lucide-clipboard-check w-3 h-3 stroke-[1.5]"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"></rect><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><path d="m9 14 2 2 4-4"></path></svg> INS-0175-0205
</a>
</div>
</article>
</div>

<!-- Variant 3: NO CAUSE (Neutral - Empty Circle Icon) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#94A3B8]"></span>
NO CAUSE FLAG (Neutral State · 12% Tinted Fill · 1px Solid Border)
</span>
<span class="text-[#5B6675]">empty-circle icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#94A3B8]/[0.12] border border-[#94A3B8] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#94A3B8] flex items-center justify-center">
<!-- empty-circle icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="circle" aria-hidden="true" class="lucide lucide-circle w-4 h-4 stroke-[1.5]"><circle cx="12" cy="12" r="10"></circle></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#94A3B8] flex-shrink-0">NO CAUSE</span>
<span class="text-[#E6EDF3] leading-tight font-normal">No recorded reason for the stop at WELL-0175. Suggest a field check.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] text-[#8B98A8] border border-[#263140] font-mono text-[11px]">
Suggest field check
</span></div>
</article>
</div>

</div>
</section>

<!-- Technical Spec Footer -->
<footer class="w-full max-w-[880px] mt-8 text-center text-xs font-mono text-[#5B6675] pb-8 border-t border-[#1E2733] pt-4 flex flex-col sm:flex-row justify-between items-center gap-2">
<div class="">ASSET INTELLIGENCE COPILOT · DESIGN SYSTEM REV 1.0</div>
<div class="text-[#8B98A8]">IBM PLEX SANS &amp; MONO · 4PX SYSTEM · NO DROP SHADOWS</div>
</footer>

<script>
// Initialize Lucide icons
lucide.createIcons();
</script>

</body></html>
```

5. assistant_message_loading_state_asset_intelligence
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"outline-variant":"#3e484f","primary":"#8ed5ff","on-secondary-fixed-variant":"#005137","primary-container":"#38bdf8","surface-container":"#1a2028","surface-bright":"#343a42","on-error-container":"#ffdad6","surface":"#0e141c","on-secondary":"#003825","inverse-primary":"#00668a","error-container":"#93000a","tertiary":"#ffbcbf","primary-fixed":"#c4e7ff","secondary-fixed":"#68fcbf","on-error":"#690005","outline":"#87929a","on-secondary-fixed":"#002114","on-tertiary-container":"#8c0028","secondary-fixed-dim":"#45dfa4","on-tertiary-fixed-variant":"#92002a","surface-variant":"#2f353e","surface-tint":"#7bd0ff","on-primary-fixed":"#001e2c","on-tertiary":"#67001b","surface-container-highest":"#2f353e","surface-container-high":"#242a33","surface-container-low":"#161c24","on-surface":"#dde3ee","tertiary-fixed":"#ffdadb","background":"#0e141c","inverse-surface":"#dde3ee","on-primary-fixed-variant":"#004c69","on-primary-container":"#004965","on-surface-variant":"#bdc8d1","primary-fixed-dim":"#7bd0ff","on-secondary-container":"#00452e","surface-dim":"#0e141c","on-background":"#dde3ee","tertiary-fixed-dim":"#ffb2b7","error":"#ffb4ab","on-primary":"#00354a","inverse-on-surface":"#2b3139","tertiary-container":"#ff929a","surface-container-lowest":"#090f16","on-tertiary-fixed":"#40000d","secondary-container":"#00bd85","secondary":"#45dfa4"},borderRadius:{DEFAULT:"0.125rem",lg:"0.25rem",xl:"0.5rem",full:"0.75rem"},spacing:{"space-lg":"1.25rem","space-xl":"1.5rem","space-xs":"0.25rem","space-md":"1rem",margin:"1.5rem",gutter:"1.5rem","space-sm":"0.5rem"},fontFamily:{"body-spec":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"body-prose-medium":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel-mobile":["IBM Plex Sans"],"display-telemetry":["IBM Plex Mono"],"headline-panel":["IBM Plex Sans"]},fontSize:{"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}}</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low border-r border-outline-variant z-40 flex flex-col justify-between select-none"><div class="flex flex-col flex-1 min-h-0"><div class="p-space-md border-b border-outline-variant"><div class="flex items-center gap-space-sm mb-space-xs"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="font-headline-panel text-headline-panel tracking-tight text-on-surface">Asset Intelligence</span></div><div class="font-label-mono-tag text-label-mono-tag uppercase tracking-wider text-outline">WEEKLY INSPECTION RECORDS</div></div><div class="p-space-md border-b border-outline-variant bg-surface-container-low"><div class="flex items-center justify-between"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono text-primary font-bold">MT</div><div class="flex flex-col min-w-0"><div class="font-body-spec-mono text-body-spec-mono text-on-surface truncate leading-tight">Michael Turner</div><div class="font-label-mono-tag text-label-mono-tag text-outline truncate">Production Supervisor</div></div></div><span class="material-symbols-outlined text-outline-variant text-[18px]">expand_more</span></div><div class="mt-space-sm pt-space-xs border-t border-outline-variant flex items-center justify-between text-outline"><span class="font-label-mono-tag text-label-mono-tag truncate">Northeast Production</span><div class="flex items-center gap-space-xs text-outline"><span class="material-symbols-outlined text-[14px]">lock</span><span class="font-label-mono-tag text-label-mono-tag text-[10px]">Private</span></div></div></div><div class="p-space-md"><a class="w-full flex items-center justify-center gap-space-sm py-space-sm px-space-md rounded-lg border border-primary-container text-primary-container hover:bg-surface-container hover:text-primary transition-colors font-body-spec-mono text-body-spec-mono" data-path="copilot-workspace" href="#"><span class="material-symbols-outlined text-[18px]">add</span><span class="">New chat</span></a></div><div class="px-space-md pt-space-xs pb-space-xs"><div class="font-label-mono-tag text-label-mono-tag uppercase text-outline tracking-wider">Recent chats</div></div><nav class="flex-1 overflow-y-auto px-space-xs py-space-xs space-y-space-xs" data-active-classes="bg-surface-container text-primary border-l-2 border-primary-container"><a class="flex items-center px-space-md py-space-sm rounded-lg bg-surface-container text-primary border-l-2 border-primary-container transition-colors" href="#"><span class="font-body-spec text-sm truncate">WELL-0001 status and last inspection</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-sm truncate">Northeast Block 8 not producing</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-sm truncate">Block 7 downtime, top 3</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-sm truncate">WELL-0001 spills, last 4 years</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-sm truncate">Pump jack root-cause wells</span></a></nav></div><div class="p-space-md border-t border-outline-variant bg-surface-container-lowest"><div class="flex items-center justify-between text-outline font-label-mono-tag text-xs"><span class="">Weekly Inspection Records</span></div></div></aside><div class="pl-[296px] min-h-screen flex flex-col"><header class="fixed top-0 left-[296px] right-0 h-14 bg-surface-container-low border-b border-outline-variant z-30 flex items-center justify-between px-space-lg"><div class="flex items-center gap-space-sm font-headline-panel text-body-prose-medium text-on-surface"><span class="material-symbols-outlined text-primary-container text-[20px]">chat</span><span class="">Asset Intelligence Chat</span></div><div class="flex items-center gap-space-md"><div class="px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-label-mono-tag text-outline flex items-center gap-1.5"><span class="material-symbols-outlined text-[15px] text-primary">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-space-sm px-2.5 py-1 rounded-full bg-surface-container border border-outline-variant"><div class="w-6 h-6 rounded-full bg-primary flex items-center justify-center font-body-spec-mono text-xs text-on-primary font-bold">MT</div><span class="font-body-spec text-xs text-on-surface font-medium">Michael Turner</span></div></div></header><main class="relative pt-14 w-full flex-1 bg-surface-container-lowest"><div class="flex flex-col w-full">
<div class="relative w-full min-h-[calc(100vh-3.5rem)] flex flex-col justify-between bg-surface-container-lowest text-on-surface">
<!-- Top Context & Filter Rail -->
<section class="w-full bg-surface-container-low border-b border-outline-variant px-space-lg py-space-sm flex flex-wrap items-center justify-between gap-space-md select-none"><div class="flex items-center gap-space-xs font-label-mono-tag text-label-mono-tag text-outline"><span class="">TARGET:</span><span class="px-space-xs py-0.5 rounded bg-primary/10 border border-primary/30 text-primary font-medium">WELL-0001</span></div></section>
<!-- Chat Stream Scrollport (Centered 880px Workspace) -->
<div class="flex-1 w-full max-w-[880px] mx-auto px-space-md lg:px-0 py-space-xl space-y-space-xl">
<!-- 1. Operator Query Block (Indented / Aligned to Right Flow) -->
<div class="flex flex-col items-end w-full space-y-space-xs">
<div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-outline"><span class="text-on-surface-variant font-medium">OPERATOR</span><span class="">·</span><span class="">MICHAEL TURNER</span></div>
<div class="w-full max-w-[680px] bg-surface-container border border-outline-variant rounded-xl p-space-md text-on-surface space-y-space-sm">
<p class="font-body-prose text-body-prose text-on-surface leading-relaxed">
What is the current status of WELL-0001, and why is it not producing?
</p>
<div class="flex flex-wrap items-center gap-space-xs pt-space-xs border-t border-outline-variant/60"><span class="font-label-mono-tag text-[11px] px-2 py-0.5 rounded bg-primary/10 border border-primary/25 text-primary">#WELL-0001</span><span class="font-label-mono-tag text-[11px] px-2 py-0.5 rounded bg-surface-container-high border border-outline-variant text-outline hover:text-on-surface cursor-pointer">#THERMAL-STATUS</span><span class="font-label-mono-tag text-[11px] px-2 py-0.5 rounded bg-surface-container-high border border-outline-variant text-outline hover:text-on-surface cursor-pointer">#INSPECTION-LOGS</span><span class="font-label-mono-tag text-[11px] px-2 py-0.5 rounded bg-surface-container-high border border-outline-variant text-outline hover:text-on-surface cursor-pointer">#ESV-VALVE-TRIP</span></div>
</div>
</div>
<!-- 2. Assistant Message Report Block (Loading State) -->
<article aria-busy="true" aria-live="polite" class="relative w-full bg-surface-container-low border border-outline-variant rounded-xl p-space-lg overflow-hidden space-y-space-lg">
<!-- Pulsing Signal Cyan Rail (Strict 2px Left Accent) -->
<div class="absolute left-0 top-0 bottom-0 w-[2px] bg-primary-container animate-pulse shadow-[0_0_12px_rgba(56,189,248,0.7)]"></div>
<!-- 3. Assistant Header with Equalizer & Execution Meta -->
<header class="flex items-start justify-between gap-space-md border-b border-outline-variant/70 pb-space-md">
<div class="flex items-center gap-space-sm">
<div class="w-8 h-8 rounded-lg bg-primary/10 border border-primary-container/40 flex items-center justify-center text-primary-container">
<span class="material-symbols-outlined text-[19px]">precision_manufacturing</span>
</div>
<div class="flex flex-col">
<div class="flex items-center gap-space-sm">
<span class="font-headline-panel text-body-prose-medium text-on-surface tracking-tight">Working on it</span>
<!-- Custom 3-bar vertical equalizer (Strictly NO spinners, NO sparkles) -->
<div aria-hidden="true" class="flex items-end gap-[3px] h-4 pb-0.5">
<span class="w-[3px] bg-primary-container rounded-full animate-[equalize1_0.85s_ease-in-out_infinite]"></span>
<span class="w-[3px] bg-primary-container rounded-full animate-[equalize2_0.75s_ease-in-out_infinite_0.15s]"></span>
<span class="w-[3px] bg-primary-container rounded-full animate-[equalize3_0.95s_ease-in-out_infinite_0.3s]"></span>
</div>
</div>
<span class="font-label-mono-tag text-[11px] text-outline uppercase tracking-wider">ASSET INTELLIGENCE ENGINE · PIPELINE V2.4</span>
</div>
</div>
<!-- Execution Metrics -->
<div class="flex items-center gap-space-sm select-none"><div class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-primary/10 border border-primary-container/30 font-label-mono-tag text-label-mono-tag text-primary-container"><span class="">gemma-4-26b-a4b-it</span></div></div>
</header>
<!-- 4. Tool Calls Step List (meta.tool_calls live execution trace) -->
<section aria-label="Tool execution sequence" class="bg-surface-container-lowest/90 border border-outline-variant/80 rounded-lg p-space-md space-y-space-sm">
<div class="flex items-center justify-between pb-space-xs border-b border-outline-variant/40"><span class="font-label-mono-tag text-[11px] uppercase tracking-wider text-outline flex items-center gap-1"><span class="material-symbols-outlined text-[13px] text-primary">account_tree</span>EXECUTION TRACE</span></div>
<ol class="space-y-space-sm font-body-spec-mono text-[13px]">
<!-- Step 1: DONE -->
<li class="flex items-center justify-between gap-space-sm py-1 border-b border-outline-variant/20"><div class="flex items-center gap-space-sm min-w-0"><span class="material-symbols-outlined text-secondary text-[16px] shrink-0" style="font-variation-settings: 'FILL' 1;">check_circle</span><span class="px-1.5 py-0.5 rounded bg-secondary/15 text-secondary border border-secondary/30 font-label-mono-tag text-xs font-semibold shrink-0">well_status</span><span class="text-on-surface truncate">Looked up WELL-0001</span></div></li>
<!-- Step 2: DONE -->
<li class="flex items-center justify-between gap-space-sm py-1 border-b border-outline-variant/20"><div class="flex items-center gap-space-sm min-w-0"><span class="material-symbols-outlined text-secondary text-[16px] shrink-0" style="font-variation-settings: 'FILL' 1;">check_circle</span><span class="px-1.5 py-0.5 rounded bg-secondary/15 text-secondary border border-secondary/30 font-label-mono-tag text-xs font-semibold shrink-0">latest_inspection</span><span class="text-on-surface truncate">Read inspection log <span class="text-primary-container underline decoration-dotted underline-offset-2">INS-0001-0203</span></span></div></li>
<!-- Step 3: ACTIVE -->
<li class="flex items-center justify-between gap-space-sm py-1 border-b border-outline-variant/20 bg-primary/5 px-2 -mx-2 rounded"><div class="flex items-center gap-space-sm min-w-0"><div class="relative w-4 h-4 flex items-center justify-center shrink-0"><span class="absolute w-2 h-2 rounded-full bg-primary-container animate-ping"></span><span class="w-2 h-2 rounded-full bg-primary-container"></span></div><span class="px-1.5 py-0.5 rounded bg-primary-container/20 text-primary-container border border-primary-container/50 font-label-mono-tag text-xs font-semibold shrink-0">search_documents</span><span class="text-on-surface font-medium truncate">Checking the T200 manual threshold<span class="inline-block w-4 text-left animate-pulse">...</span></span></div><span class="font-label-mono-tag text-xs text-primary-container border border-primary-container/30 bg-primary/10 px-1.5 py-0.2 rounded shrink-0">in progress</span></li>
<!-- Step 4: PENDING -->
<li class="flex items-center justify-between gap-space-sm py-1 opacity-60">
<div class="flex items-center gap-space-sm min-w-0">
<span class="material-symbols-outlined text-outline text-[16px] shrink-0">radio_button_unchecked</span>
<span class="px-1.5 py-0.5 rounded bg-surface-container-high text-outline border border-outline-variant font-label-mono-tag text-xs font-medium shrink-0">context_notes</span>
<span class="text-outline truncate">Checking field notes and maintenance corrections</span>
</div>
<span class="font-label-mono-tag text-xs text-outline shrink-0">queued</span>
</li>
<!-- Step 5: PENDING -->
<li class="flex items-center justify-between gap-space-sm py-1 opacity-60"><div class="flex items-center gap-space-sm min-w-0"><span class="material-symbols-outlined text-outline text-[16px] shrink-0">radio_button_unchecked</span><span class="px-1.5 py-0.5 rounded bg-surface-container-high text-outline border border-outline-variant font-label-mono-tag text-xs font-medium shrink-0">build_visual</span><span class="text-outline truncate">Preparing status card &amp; diagnostic graph</span></div><span class="font-label-mono-tag text-xs text-outline shrink-0">queued</span></li>
</ol>
</section>
<!-- 5. Shimmer Skeleton of Upcoming Answer -->
<section aria-label="Streaming content placeholder" class="space-y-space-md">
<!-- Text Paragraph Skeletons -->
<div class="space-y-space-sm">
<div class="h-3.5 w-[92%] rounded bg-gradient-to-r from-surface-container via-surface-container-highest to-surface-container bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-3.5 w-[78%] rounded bg-gradient-to-r from-surface-container via-surface-container-highest to-surface-container bg-[length:400%_100%] animate-[shimmer_2s_infinite_0.2s]"></div>
<div class="h-3.5 w-[45%] rounded bg-gradient-to-r from-surface-container via-surface-container-highest to-surface-container bg-[length:400%_100%] animate-[shimmer_2s_infinite_0.4s]"></div>
</div>
<!-- Skeleton Status Card (Raised Surface Tier) -->
<div class="bg-surface-container border border-outline-variant rounded-lg p-space-md space-y-space-md">
<!-- Header Row Skeleton -->
<div class="flex items-center justify-between">
<div class="flex items-center gap-space-sm">
<div class="w-8 h-8 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-4 w-36 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
<div class="h-5 w-24 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
<!-- Two Metric Tiles Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-space-md">
<!-- Tile 1 Skeleton -->
<div class="bg-surface-container-low border border-outline-variant/60 rounded p-space-md space-y-space-sm">
<div class="flex items-center justify-between">
<div class="h-3 w-20 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-3 w-10 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
<div class="h-7 w-28 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-2 w-full rounded bg-surface-container-high/60 overflow-hidden">
<div class="h-full w-2/3 bg-gradient-to-r from-surface-container-highest via-surface-bright to-surface-container-highest bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
</div>
<!-- Tile 2 Skeleton -->
<div class="bg-surface-container-low border border-outline-variant/60 rounded p-space-md space-y-space-sm">
<div class="flex items-center justify-between">
<div class="h-3 w-24 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-3 w-12 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
<div class="h-7 w-32 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-2 w-full rounded bg-surface-container-high/60 overflow-hidden">
<div class="h-full w-1/2 bg-gradient-to-r from-surface-container-highest via-surface-bright to-surface-container-highest bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
</div>
</div>
<!-- Citation Chips Skeleton -->
<div class="flex flex-wrap items-center gap-space-sm pt-space-xs border-t border-outline-variant/40">
<div class="h-5 w-24 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-5 w-32 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
<div class="h-5 w-20 rounded bg-gradient-to-r from-surface-container-high via-surface-bright to-surface-container-high bg-[length:400%_100%] animate-[shimmer_2s_infinite]"></div>
</div>
</div>
</section>
<!-- 6. Action Bar Below Skeleton -->
<footer class="flex flex-wrap items-center justify-between gap-space-sm pt-space-xs border-t border-outline-variant/50"><div class="flex items-center gap-space-md flex-wrap"><div class="flex items-center gap-space-xs font-label-mono-tag text-xs text-outline"><span class="w-1.5 h-1.5 rounded-full bg-primary-container animate-pulse"></span><span class="truncate">Synthesizing inspection records...</span></div><div class="font-label-mono-tag text-xs text-outline">gemma-4-26b-a4b-it · 1.4 s · tools: well_status</div></div><button class="px-space-sm py-1 rounded bg-surface-container hover:bg-error-container/20 border border-outline-variant hover:border-error/50 text-outline hover:text-error transition-all font-body-spec-mono text-xs flex items-center gap-space-xs" id="abort-btn" title="Cancel current engine execution" type="button"><span class="w-2.5 h-2.5 bg-error/80 rounded-[1px]"></span><span class="">Stop generation (Esc)</span></button></footer>
</article>
<!-- Context Footnote / Grounding Indicator -->

</div>
<!-- 7. Persistent Bottom Composer Bar (Console Prompt Input) -->
<div class="w-full bg-surface-container-low border-t border-outline-variant px-space-md py-space-sm z-20"><div class="max-w-[880px] mx-auto space-y-space-xs"><form class="flex items-center gap-space-sm bg-surface-container border border-outline-variant rounded-xl p-1.5 pl-space-md transition-colors focus-within:border-primary-container" onsubmit="event.preventDefault();"><div class="flex items-center gap-2 text-outline shrink-0"><span class="material-symbols-outlined text-[18px] text-primary">chat</span></div><input aria-disabled="true" class="flex-1 bg-transparent border-0 font-body-spec text-body-spec text-outline cursor-not-allowed focus:outline-none placeholder:text-outline" disabled="" type="text" value="Generating response for WELL-0001..."><div class="flex items-center gap-space-xs shrink-0 pr-1"><button aria-disabled="true" class="w-8 h-8 rounded-lg bg-primary-container text-on-primary-container opacity-50 cursor-not-allowed flex items-center justify-center transition-colors" disabled="" type="button"><span class="material-symbols-outlined text-[18px]">arrow_upward</span></button></div></form><div class="flex items-center justify-between px-space-xs text-outline font-label-mono-tag text-[11px]"><div class="flex items-center gap-space-sm"><span class="text-on-surface-variant font-medium">ESC</span><span class="">Abort</span></div><div class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-primary-container"></span><span class="">Busy (WELL-0001)</span></div></div></div></div>
</div>
<style>
@keyframes equalize1 {
0%, 100% { height: 4px; }
50% { height: 14px; }
}
@keyframes equalize2 {
0%, 100% { height: 8px; }
50% { height: 18px; }
}
@keyframes equalize3 {
0%, 100% { height: 6px; }
50% { height: 12px; }
}
@keyframes shimmer {
0% { background-position: -200% 0; }
100% { background-position: 200% 0; }
}
</style>
<script>
// Live elapsed timer increment simulation
(function() {
const timerEl = document.getElementById('execution-timer');
const abortBtn = document.getElementById('abort-btn');
let seconds = 3.2;

const interval = setInterval(() => {
seconds += 0.1;
if (timerEl) {
timerEl.textContent = seconds.toFixed(1) + ' s';
}
}, 100);

const handleAbort = () => {
clearInterval(interval);
if (timerEl) {
timerEl.textContent = 'ABORTED (' + seconds.toFixed(1) + ' s)';
timerEl.classList.remove('text-primary');
timerEl.classList.add('text-error');
}
if (abortBtn) {
abortBtn.disabled = true;
abortBtn.classList.add('opacity-40', 'cursor-not-allowed');
abortBtn.innerHTML = '<span class="material-symbols-outlined text-[13px] text-error">close</span><span>Generation halted</span>';
}
};

if (abortBtn) {
abortBtn.addEventListener('click', handleAbort);
}

window.addEventListener('keydown', (e) => {
if (e.key === 'Escape') {
handleAbort();
}
});
})();
</script>
</div></main></div>

</body></html>
```

6. copilot_error_states_asset_intelligence
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"outline-variant":"#3e484f","primary":"#8ed5ff","on-secondary-fixed-variant":"#005137","primary-container":"#38bdf8","surface-container":"#1a2028","surface-bright":"#343a42","on-error-container":"#ffdad6","surface":"#0e141c","on-secondary":"#003825","inverse-primary":"#00668a","error-container":"#93000a","tertiary":"#ffbcbf","primary-fixed":"#c4e7ff","secondary-fixed":"#68fcbf","on-error":"#690005","outline":"#87929a","on-secondary-fixed":"#002114","on-tertiary-container":"#8c0028","secondary-fixed-dim":"#45dfa4","on-tertiary-fixed-variant":"#92002a","surface-variant":"#2f353e","surface-tint":"#7bd0ff","on-primary-fixed":"#001e2c","on-tertiary":"#67001b","surface-container-highest":"#2f353e","surface-container-high":"#242a33","surface-container-low":"#161c24","on-surface":"#dde3ee","tertiary-fixed":"#ffdadb","background":"#0e141c","inverse-surface":"#dde3ee","on-primary-fixed-variant":"#004c69","on-primary-container":"#004965","on-surface-variant":"#bdc8d1","primary-fixed-dim":"#7bd0ff","on-secondary-container":"#00452e","surface-dim":"#0e141c","on-background":"#dde3ee","tertiary-fixed-dim":"#ffb2b7","error":"#ffb4ab","on-primary":"#00354a","inverse-on-surface":"#2b3139","tertiary-container":"#ff929a","surface-container-lowest":"#090f16","on-tertiary-fixed":"#40000d","secondary-container":"#00bd85","secondary":"#45dfa4"},borderRadius:{DEFAULT:"0.125rem",lg:"0.25rem",xl:"0.5rem",full:"0.75rem"},spacing:{"space-lg":"1.25rem","space-xl":"1.5rem","space-xs":"0.25rem","space-md":"1rem",margin:"1.5rem",gutter:"1.5rem","space-sm":"0.5rem"},fontFamily:{"body-spec":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"body-prose-medium":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel-mobile":["IBM Plex Sans"],"display-telemetry":["IBM Plex Mono"],"headline-panel":["IBM Plex Sans"]},fontSize:{"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}}</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low border-r border-outline-variant z-40 flex flex-col justify-between select-none"><div class="flex flex-col flex-1 min-h-0"><div class="p-space-md border-b border-outline-variant"><div class="flex items-center gap-space-sm mb-space-xs"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="font-headline-panel text-headline-panel tracking-tight text-on-surface">Asset Intelligence</span></div><div class="font-label-mono-tag text-label-mono-tag uppercase tracking-wider text-outline">Recent chats</div></div><div class="p-space-md border-b border-outline-variant bg-surface-container-low"><div class="flex items-center justify-between"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono text-primary font-bold">MT</div><div class="flex flex-col min-w-0"><div class="font-body-spec-mono text-body-spec-mono text-on-surface truncate leading-tight">Michael Turner</div><div class="font-label-mono-tag text-label-mono-tag text-outline truncate">Production Supervisor</div></div></div><span class="material-symbols-outlined text-outline-variant text-[18px]">expand_more</span></div><div class="mt-space-sm pt-space-xs border-t border-outline-variant flex items-center justify-between text-outline"><span class="font-label-mono-tag text-label-mono-tag truncate">Northeast Production</span><div class="flex items-center gap-space-xs text-outline"><span class="material-symbols-outlined text-[14px]">lock</span><span class="font-label-mono-tag text-label-mono-tag text-[10px]">Private</span></div></div></div><div class="p-space-md"><a class="w-full flex items-center justify-center gap-space-sm py-space-sm px-space-md rounded-lg border border-primary-container text-primary-container hover:bg-surface-container hover:text-primary transition-colors font-body-spec-mono text-body-spec-mono" data-path="copilot-workspace" href="#"><span class="material-symbols-outlined text-[18px]">add</span><span class="">+ New chat</span></a></div><div class="px-space-md pt-space-xs pb-space-xs"><div class="font-label-mono-tag text-label-mono-tag uppercase text-outline tracking-wider">Recent chats</div></div><nav class="flex-1 overflow-y-auto px-space-xs py-space-xs space-y-space-xs" data-active-classes="bg-surface-container text-primary border-l-2 border-primary-container"><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-body-spec truncate text-on-surface">WELL-0001 status and last inspection</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-body-spec truncate text-on-surface">Northeast Block 8 not producing</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-body-spec truncate text-on-surface">Block 7 downtime, top 3</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-body-spec truncate text-on-surface">WELL-0001 spills, last 4 years</span></a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" href="#"><span class="font-body-spec text-body-spec truncate text-on-surface">Pump jack root-cause wells</span></a></nav></div><div class="p-space-md border-t border-outline-variant bg-surface-container-lowest"><div class="flex items-center justify-between font-label-mono-tag text-label-mono-tag text-outline"><span class="">System connected</span></div></div></aside><div class="pl-[296px] min-h-screen flex flex-col"><header class="fixed top-0 left-[296px] right-0 h-14 bg-surface-container-low border-b border-outline-variant z-30 flex items-center justify-between px-space-lg"><div class="flex items-center gap-space-sm font-headline-panel text-[16px] text-on-surface font-semibold"><span class="material-symbols-outlined text-primary-container text-[20px]">chat</span><span class="">Field Copilot</span></div><div class="flex items-center gap-space-md"><div class="px-space-sm py-space-xs rounded-lg bg-surface-container border border-outline-variant font-label-mono-tag text-label-mono-tag text-outline">Today: 17 Oct 2026</div><div class="flex items-center gap-space-sm px-space-sm py-space-xs rounded-lg bg-surface-container border border-outline-variant"><div class="w-6 h-6 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[14px]">person</span></div><span class="font-body-spec-mono text-body-spec-mono text-on-surface font-medium">Michael Turner</span></div></div></header><main class="relative pt-14 w-full flex-1 bg-surface-container-lowest"><div class="flex flex-col w-full">
<div class="w-full max-w-[880px] mx-auto px-space-md py-space-lg flex flex-col gap-space-lg">
<!-- 1. SLIM TOP-OF-THREAD TOAST BANNER (neutral dark) -->
<div class="w-full flex items-center justify-between px-space-md py-space-xs rounded-lg bg-surface-container-low shadow-sm" id="reconnect-banner"><div class="flex items-center gap-space-sm min-w-0"><span class="relative flex h-2 w-2 shrink-0"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-outline opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-outline"></span></span><span class="font-label-mono-tag text-label-mono-tag text-outline">Reconnecting...</span></div><button aria-label="Dismiss banner" class="p-space-xs text-outline hover:text-on-surface transition-colors flex items-center justify-center shrink-0" onclick="document.getElementById('reconnect-banner').style.display='none'" type="button"><span class="material-symbols-outlined text-[16px]">close</span></button></div>
<!-- OPERATOR QUERY CONTEXT 1 -->
<div class="flex justify-end w-full">
<div class="max-w-[75%] bg-surface-container p-space-md rounded-xl shadow-sm flex flex-col gap-space-xs">
<div class="flex items-center justify-between gap-space-md text-outline font-label-mono-tag text-label-mono-tag">
<span class="">OPERATOR // CREW-A (FIELD_CONSOLE_04)</span>
<span class="">14:34:49 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">Execute correlation on <span class="font-body-spec-mono text-primary font-medium">WELL-0402</span> choke orifice delta versus line pressure decay.</p>
</div>
</div>
<!-- 2. ERROR STATE 1: System 500 Fault (Coral Red Left Rail) -->
<div class="relative w-full rounded-xl bg-surface-container-low p-space-lg shadow-sm flex flex-col gap-space-md overflow-hidden">
<!-- 3px Solid Red left rail -->
<div class="absolute left-0 top-0 bottom-0 w-[3px] bg-error"></div>
<!-- Sub-header metadata rail -->
<div class="flex items-center justify-between pl-space-xs"><div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-outline"><span class="material-symbols-outlined text-[16px] text-error">memory</span><span class="">ASSET INTELLIGENCE ENGINE // EXEC_ROUTER</span></div></div>
<!-- Tinted Red Header Box -->
<div class="rounded-lg bg-error-container/20 p-space-md flex flex-col sm:flex-row sm:items-center justify-between gap-space-sm">
<div class="flex items-center gap-space-sm">
<div class="w-8 h-8 rounded-lg bg-error-container/40 flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-error text-[20px]" style="font-variation-settings: 'FILL' 1;">warning</span>
</div>
<div class="flex flex-col">
<h2 class="font-headline-panel text-headline-panel text-on-error-container leading-tight">The copilot could not answer</h2>
<span class="font-body-spec text-body-spec text-error opacity-90">The backend returned an error (HTTP 500). Your question was not lost.</span>
</div>
</div>
<div class="self-start sm:self-center">
<span class="inline-flex items-center gap-space-xs px-space-sm py-space-xs rounded bg-error-container/50 font-label-mono-tag text-label-mono-tag text-error font-semibold">
<span class="material-symbols-outlined text-[14px]">error</span>
HTTP 500 · INTERNAL SERVER ERROR
</span>
</div>
</div>
<!-- Collapsible Diagnostic Disclosure Box -->
<div class="rounded-lg bg-surface-container-lowest p-space-md flex flex-col gap-space-sm">
<div class="flex items-center justify-between">
<div class="flex items-center gap-space-xs font-label-mono-tag text-label-mono-tag text-outline">
<span class="material-symbols-outlined text-[16px] text-outline">terminal</span>
<span class="">DIAGNOSTIC TRACE BUFFER</span>
</div>
<button class="font-label-mono-tag text-label-mono-tag text-primary hover:text-primary-container transition-colors flex items-center gap-space-xs" id="toggle-trace-btn" onclick="const code = document.getElementById('trace-code-block'); const txt = document.getElementById('toggle-trace-txt'); const isHidden = code.classList.toggle('hidden'); txt.textContent = isHidden ? 'Show details' : 'Hide details';" type="button">
<span id="toggle-trace-txt" class="">Hide details</span>
<span class="material-symbols-outlined text-[14px]">unfold_more</span>
</button>
</div>
<div class="pt-space-xs" id="trace-code-block"><div class="p-space-md rounded bg-surface-container font-label-mono-tag text-label-mono-tag text-on-surface-variant flex flex-col gap-space-xs overflow-x-auto"><div class="flex gap-space-md"><span class="text-outline w-24 shrink-0 select-none">status:</span><span class="text-error font-medium">500 Internal Server Error</span></div><div class="flex gap-space-md"><span class="text-outline w-24 shrink-0 select-none">message:</span><span class="text-on-surface-variant break-all">Inspection database gateway timeout</span></div><div class="flex gap-space-md"><span class="text-outline w-24 shrink-0 select-none">node:</span><span class="text-outline">ingest-edge-03a.internal</span></div></div></div>
</div>
<!-- Actions cluster -->
<div class="flex items-center justify-between pt-space-xs flex-wrap gap-space-sm"><div class="flex items-center gap-space-sm"><button class="px-space-md py-space-sm rounded-lg bg-error hover:opacity-90 text-on-error font-body-spec-mono text-body-spec-mono font-semibold flex items-center gap-space-xs transition-opacity shadow-sm" type="button"><span class="material-symbols-outlined text-[18px]">refresh</span><span class="">Retry Query</span></button><button class="px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface font-body-spec-mono text-body-spec-mono flex items-center gap-space-xs transition-colors" id="copy-btn-1" onclick="const b = this; b.classList.add('bg-surface-variant'); setTimeout(() =&gt; b.classList.remove('bg-surface-variant'), 1000);" type="button"><span class="material-symbols-outlined text-[18px] text-outline">content_copy</span><span class="">Copy details</span></button></div><div class="font-label-mono-tag text-label-mono-tag text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</div></div>
</div>
<!-- OPERATOR QUERY CONTEXT 2 -->
<div class="flex justify-end w-full">
<div class="max-w-[75%] bg-surface-container p-space-md rounded-xl shadow-sm flex flex-col gap-space-xs">
<div class="flex items-center justify-between gap-space-md text-outline font-label-mono-tag text-label-mono-tag">
<span class="">OPERATOR // CREW-A (FIELD_CONSOLE_04)</span>
<span class="">14:35:01 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">Sync production report for current active shifts across Block 1 and 2.</p>
</div>
</div>
<!-- 3. ERROR STATE 2: Network Disconnected (Coral Red Left Rail) -->
<div class="relative w-full rounded-xl bg-surface-container-low p-space-lg shadow-sm flex flex-col gap-space-md overflow-hidden">
<!-- 3px Solid Red left rail -->
<div class="absolute left-0 top-0 bottom-0 w-[3px] bg-error"></div>
<!-- Sub-header metadata rail -->
<div class="flex items-center justify-between pl-space-xs">
<div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-outline">
<span class="material-symbols-outlined text-[16px] text-error">cloud_off</span>
<span class="">NETWORK TRANSMISSION LAYER // SOCKET_BUS</span>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline">DIAG: NO_CARRIER</span>
</div>
<!-- Tinted Red Header Box -->
<div class="rounded-lg bg-error-container/20 p-space-md flex flex-col sm:flex-row sm:items-center justify-between gap-space-sm">
<div class="flex items-center gap-space-sm">
<div class="w-8 h-8 rounded-lg bg-error-container/40 flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-error text-[20px]" style="font-variation-settings: 'FILL' 1;">wifi_off</span>
</div>
<div class="flex flex-col">
<h2 class="font-headline-panel text-headline-panel text-on-error-container leading-tight">Cannot reach the server</h2>
<span class="font-body-spec text-body-spec text-error opacity-90">Check that the API is running and try again.</span>
</div>
</div>
<div class="self-start sm:self-center">
<span class="inline-flex items-center gap-space-xs px-space-sm py-space-xs rounded bg-error-container/50 font-label-mono-tag text-label-mono-tag text-error font-semibold">
<span class="material-symbols-outlined text-[14px]">link_off</span>
NETWORK_DISCONNECTED
</span>
</div>
</div>
<!-- Mono status hairline readout -->
<div class="rounded-lg bg-surface-container-lowest px-space-md py-space-sm flex items-center justify-between">
<div class="flex items-center gap-space-sm min-w-0">
<span class="w-1.5 h-1.5 rounded-full bg-error shrink-0"></span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant truncate">
GET /api/chats - failed (<span class="text-error font-medium">ERR_CONNECTION_REFUSED</span> at 14:35:02 UTC)
</span>
</div>
<span class="hidden md:inline font-label-mono-tag text-label-mono-tag text-outline shrink-0 ml-space-sm">PORT: 8443</span>
</div>
<!-- Actions cluster -->
<div class="flex items-center justify-between pt-space-xs flex-wrap gap-space-sm"><div class="flex items-center gap-space-sm"><button class="px-space-md py-space-sm rounded-lg bg-error hover:opacity-90 text-on-error font-body-spec-mono text-body-spec-mono font-semibold flex items-center gap-space-xs transition-opacity shadow-sm" type="button"><span class="material-symbols-outlined text-[18px]">refresh</span><span class="">Retry Connection</span></button><button class="px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface font-body-spec-mono text-body-spec-mono flex items-center gap-space-xs transition-colors" type="button"><span class="material-symbols-outlined text-[18px] text-outline">tune</span><span class="">Gateway Config</span></button></div><div class="font-label-mono-tag text-label-mono-tag text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</div></div>
</div>
<!-- OPERATOR QUERY CONTEXT 3 -->
<div class="flex justify-end w-full">
<div class="max-w-[75%] bg-surface-container p-space-md rounded-xl shadow-sm flex flex-col gap-space-xs">
<div class="flex items-center justify-between gap-space-md text-outline font-label-mono-tag text-label-mono-tag">
<span class="">OPERATOR // CREW-A (FIELD_CONSOLE_04)</span>
<span class="">14:36:18 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">Execute correlation on <span class="font-body-spec-mono text-primary font-medium">WELL-0402</span> choke orifice delta versus line pressure decay.</p>
</div>
</div>
<!-- 4. ERROR STATE 3: Query Unresolved / Not Found (Amber Left Rail) -->
<div class="relative w-full rounded-xl bg-surface-container-low p-space-lg shadow-sm flex flex-col gap-space-md overflow-hidden">
<!-- 3px Solid Amber left rail -->
<div class="absolute left-0 top-0 bottom-0 w-[3px] bg-tertiary-container"></div>
<!-- Sub-header metadata rail -->
<div class="flex items-center justify-between pl-space-xs">
<div class="flex items-center gap-space-sm font-label-mono-tag text-label-mono-tag text-outline">
<span class="material-symbols-outlined text-[16px] text-tertiary-container">manage_search</span>
<span class="">ASSET INDEX SERVICE // ENTITY_LOOKUP</span>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline">RECORDS SCAN: 200/200</span>
</div>
<!-- Tinted Amber Header Box -->
<div class="rounded-lg bg-tertiary-container/15 p-space-md flex flex-col sm:flex-row sm:items-center justify-between gap-space-sm">
<div class="flex items-center gap-space-sm">
<div class="w-8 h-8 rounded-lg bg-tertiary-container/30 flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-tertiary-container text-[20px]" style="font-variation-settings: 'FILL' 1;">search_off</span>
</div>
<div class="flex flex-col">
<h2 class="font-headline-panel text-headline-panel text-tertiary-fixed-dim leading-tight">No matching well</h2>
<span class="font-body-spec text-body-spec text-tertiary-container opacity-95">No well matches WELL-0999. Try an id from WELL-0001 to WELL-0200 or a block name.</span>
</div>
</div>
<div class="self-start sm:self-center">
<span class="inline-flex items-center gap-space-xs px-space-sm py-space-xs rounded bg-tertiary-container/30 font-label-mono-tag text-label-mono-tag text-tertiary-container font-semibold">
<span class="material-symbols-outlined text-[14px]">help</span>
QUERY_UNRESOLVED
</span>
</div>
</div>
<!-- Interactive Suggestion Chips Section -->
<div class="rounded-lg bg-surface-container-lowest p-space-md flex flex-col gap-space-sm">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric text-outline uppercase">Suggested queries &amp; active entities:</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">Click any chip to run immediately</span>
</div>
<div class="flex flex-wrap items-center gap-space-sm pt-space-xs"><button class="group px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high transition-colors flex items-center gap-space-sm shadow-sm" onclick="handleChipClick(this, 'WELL-0001')" type="button"><span class="material-symbols-outlined text-[16px] text-primary-container">oil_barrel</span><span class="font-body-spec-mono text-body-spec-mono text-primary font-semibold">WELL-0001</span><span class="material-symbols-outlined text-[14px] text-outline group-hover:text-primary transition-colors">arrow_outward</span></button><button class="group px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high transition-colors flex items-center gap-space-sm shadow-sm" onclick="handleChipClick(this, 'Northeast Block 8')" type="button"><span class="material-symbols-outlined text-[16px] text-secondary">location_on</span><span class="font-body-spec text-body-spec text-on-surface font-medium">Northeast Block 8</span><span class="material-symbols-outlined text-[14px] text-outline group-hover:text-secondary transition-colors">arrow_outward</span></button><button class="group px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high transition-colors flex items-center gap-space-sm shadow-sm" onclick="handleChipClick(this, 'Southwest Block 24')" type="button"><span class="material-symbols-outlined text-[16px] text-secondary">location_on</span><span class="font-body-spec text-body-spec text-on-surface font-medium">Southwest Block 24</span><span class="material-symbols-outlined text-[14px] text-outline group-hover:text-secondary transition-colors">arrow_outward</span></button></div>
</div>
<!-- Footer info bar -->
<div class="flex items-center justify-between text-outline font-label-mono-tag text-label-mono-tag pt-space-xs"><div class="flex items-center gap-space-xs"><span class="material-symbols-outlined text-[14px] text-primary">info</span><span class="">Weekly inspection database synchronized</span></div><div class="font-label-mono-tag text-label-mono-tag text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</div></div>
</div>
<!-- DOCKED QUERY INPUT BAR -->
<div class="sticky bottom-4 w-full rounded-xl bg-surface-container p-space-md shadow-xl flex flex-col gap-space-sm mt-space-md"><div class="flex items-center justify-between"><div class="flex items-center gap-space-xs font-label-mono-tag text-label-mono-tag text-outline"><span class="material-symbols-outlined text-[16px] text-primary-container">psychology</span><span class="">QUERY CONSOLE</span></div></div><div class="flex items-center gap-space-sm"><div class="relative flex-1"><input class="w-full h-11 px-space-md rounded-lg bg-surface-container-low text-on-surface placeholder:text-outline font-body-spec text-body-spec focus:outline-none focus:bg-surface-container-high transition-colors" id="prompt-input" placeholder="Ask about wellhead status, valve clearances, or trip records..." type="text"></div><button aria-label="Send" class="h-11 w-11 rounded-lg bg-primary-container text-on-primary-container flex items-center justify-center hover:opacity-90 transition-opacity shrink-0" type="button"><span class="material-symbols-outlined text-[20px]">arrow_forward</span></button></div></div>
</div>
</div>
<script>
function handleChipClick(element, queryText) {
const input = document.getElementById('prompt-input');
if (input) {
input.value = 'Show status and telemetry for ' + queryText;
input.focus();
}
}
</script></main></div>

</body></html>
```

7. evidence_inspection_slide_over_drawer_asset_intelligence
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"outline-variant":"#3e484f","primary":"#8ed5ff","on-secondary-fixed-variant":"#005137","primary-container":"#38bdf8","surface-container":"#1a2028","surface-bright":"#343a42","on-error-container":"#ffdad6","surface":"#0e141c","on-secondary":"#003825","inverse-primary":"#00668a","error-container":"#93000a","tertiary":"#ffbcbf","primary-fixed":"#c4e7ff","secondary-fixed":"#68fcbf","on-error":"#690005","outline":"#87929a","on-secondary-fixed":"#002114","on-tertiary-container":"#8c0028","secondary-fixed-dim":"#45dfa4","on-tertiary-fixed-variant":"#92002a","surface-variant":"#2f353e","surface-tint":"#7bd0ff","on-primary-fixed":"#001e2c","on-tertiary":"#67001b","surface-container-highest":"#2f353e","surface-container-high":"#242a33","surface-container-low":"#161c24","on-surface":"#dde3ee","tertiary-fixed":"#ffdadb","background":"#0e141c","inverse-surface":"#dde3ee","on-primary-fixed-variant":"#004c69","on-primary-container":"#004965","on-surface-variant":"#bdc8d1","primary-fixed-dim":"#7bd0ff","on-secondary-container":"#00452e","surface-dim":"#0e141c","on-background":"#dde3ee","tertiary-fixed-dim":"#ffb2b7","error":"#ffb4ab","on-primary":"#00354a","inverse-on-surface":"#2b3139","tertiary-container":"#ff929a","surface-container-lowest":"#090f16","on-tertiary-fixed":"#40000d","secondary-container":"#00bd85","secondary":"#45dfa4"},borderRadius:{DEFAULT:"0.125rem",lg:"0.25rem",xl:"0.5rem",full:"0.75rem"},spacing:{"space-lg":"1.25rem","space-xl":"1.5rem","space-xs":"0.25rem","space-md":"1rem",margin:"1.5rem",gutter:"1.5rem","space-sm":"0.5rem"},fontFamily:{"body-spec":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"body-prose-medium":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel-mobile":["IBM Plex Sans"],"display-telemetry":["IBM Plex Mono"],"headline-panel":["IBM Plex Sans"]},fontSize:{"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}}</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low border-r border-outline-variant z-40 flex flex-col justify-between select-none"><div class="flex flex-col flex-1 min-h-0"><div class="p-space-md border-b border-outline-variant"><div class="flex items-center gap-space-sm mb-space-xs"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="font-headline-panel text-headline-panel tracking-tight text-on-surface">Asset Intelligence</span></div></div><div class="p-space-md border-b border-outline-variant bg-surface-container-low"><div class="flex items-center justify-between"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono text-primary font-bold">MT</div><div class="flex flex-col min-w-0"><div class="font-body-spec-mono text-body-spec-mono text-on-surface truncate leading-tight">Michael Turner</div><div class="font-label-mono-tag text-label-mono-tag text-outline truncate">Production Supervisor</div></div></div><span class="material-symbols-outlined text-outline-variant text-[18px]">expand_more</span></div><div class="mt-space-sm pt-space-xs border-t border-outline-variant flex items-center justify-between text-outline"><span class="font-label-mono-tag text-label-mono-tag truncate">Northeast Production</span><div class="flex items-center gap-space-xs text-outline"><span class="material-symbols-outlined text-[14px]">lock</span><span class="font-label-mono-tag text-label-mono-tag text-[10px]">Private</span></div></div></div><div class="p-space-md"><a class="w-full flex items-center justify-center gap-space-sm py-space-sm px-space-md rounded-lg border border-primary-container text-primary-container hover:bg-surface-container hover:text-primary transition-colors font-body-spec-mono text-body-spec-mono" data-path="copilot-workspace" href="#"><span class="material-symbols-outlined text-[18px]">add</span><span class="">New chat</span></a></div><div class="px-space-md pt-space-xs pb-space-xs"><div class="font-label-mono-tag text-label-mono-tag uppercase text-outline tracking-wider">Recent chats</div></div><nav class="flex-1 overflow-y-auto px-space-xs py-space-xs space-y-space-xs" data-active-classes="bg-surface-container text-primary border-l-2 border-primary-container"><a class="flex flex-col px-space-md py-space-sm rounded-lg text-primary bg-surface-container border-l-2 border-primary-container font-body-spec text-sm truncate hover:bg-surface-container-high transition-colors" href="#">WELL-0001 status and last inspection</a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-sm truncate" href="#">Northeast Block 8 not producing</a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-sm truncate" href="#">Block 7 downtime, top 3</a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-sm truncate" href="#">WELL-0001 spills, last 4 years</a><a class="flex flex-col px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-sm truncate" href="#">Pump jack root-cause wells</a></nav></div><div class="p-space-md border-t border-outline-variant bg-surface-container-lowest"><div class="flex items-center justify-between text-outline font-label-mono-tag text-[11px]"><span class="">Asset Intelligence</span><span class="">v4.19</span></div></div></aside><div class="pl-[296px] min-h-screen flex flex-col"><header class="fixed top-0 left-[296px] right-0 h-14 bg-surface-container-low border-b border-outline-variant z-30 flex items-center justify-between px-space-lg"><div class="flex items-center gap-space-sm font-headline-panel text-body-prose font-semibold text-on-surface"><span class="material-symbols-outlined text-primary-container text-[20px]">chat</span><span class="">Operational Chat</span></div><div class="flex items-center gap-space-md"><div class="px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-xs text-outline">Today: 17 Oct 2026</div><div class="flex items-center gap-space-xs px-2.5 py-1 rounded-full bg-surface-container border border-outline-variant"><div class="w-6 h-6 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[15px]">person</span></div><span class="font-body-spec-mono text-xs text-on-surface">Michael Turner</span></div></div></header><main class="relative pt-14 w-full flex-1 bg-surface-container-lowest"><div class="flex flex-col w-full relative min-h-[calc(100vh-3.5rem)] overflow-hidden font-body-spec text-on-surface">
<!-- BACKGROUND: MAIN OPERATIONAL CONSOLE & ASSISTANT WORKSPACE -->
<div class="w-full p-space-lg flex flex-col gap-space-lg select-text transition-all duration-300 pointer-events-none filter blur-[1px]">
<!-- Top Telemetry Summary Strip -->
<div class="grid grid-cols-1 md:grid-cols-4 gap-space-md">
<div class="p-space-md rounded-lg bg-surface-container border border-outline-variant flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Target Production</span>
<span class="flex items-center gap-1 font-label-mono-tag text-[11px] text-secondary">
<span class="material-symbols-outlined text-[14px]">check_circle</span> 94.2% NOMINAL
</span>
</div>
<div class="mt-space-sm flex items-baseline gap-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">3,420</span>
<span class="font-label-mono-tag text-outline">BPD</span>
</div>
<div class="mt-space-xs w-full bg-surface-container-high h-1 rounded-full overflow-hidden">
<div class="bg-secondary h-full w-[94.2%]"></div>
</div>
</div>
<div class="p-space-md rounded-lg bg-surface-container border border-outline-variant flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Active Wellhead Lift</span>
<span class="flex items-center gap-1 font-label-mono-tag text-[11px] text-primary">
<span class="material-symbols-outlined text-[14px]">sync</span> DUAL ESP
</span>
</div>
<div class="mt-space-sm flex items-baseline gap-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">198</span>
<span class="font-label-mono-tag text-outline">/ 200 PRODUCING</span>
</div>
<div class="mt-space-xs w-full bg-surface-container-high h-1 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[99%]"></div>
</div>
</div>
<div class="p-space-md rounded-lg bg-surface-container border border-outline-variant flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Surface ΔT Baseline</span>
<span class="flex items-center gap-1 font-label-mono-tag text-[11px] text-error">
<span class="material-symbols-outlined text-[14px]">warning</span> EXCEEDANCE
</span>
</div>
<div class="mt-space-sm flex items-baseline gap-space-xs">
<span class="font-display-telemetry text-display-telemetry text-error">+3.2</span>
<span class="font-label-mono-tag text-outline">°C SHUT-IN CONFIRM</span>
</div>
<div class="mt-space-xs w-full bg-surface-container-high h-1 rounded-full overflow-hidden">
<div class="bg-error h-full w-[38%]"></div>
</div>
</div>
<div class="p-space-md rounded-lg bg-surface-container border border-outline-variant flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Flowline Manifold PSI</span>
<span class="flex items-center gap-1 font-label-mono-tag text-[11px] text-secondary">
<span class="material-symbols-outlined text-[14px]">check_circle</span> STABLE
</span>
</div>
<div class="mt-space-sm flex items-baseline gap-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">1,248</span>
<span class="font-label-mono-tag text-outline">PSIG</span>
</div>
<div class="mt-space-xs w-full bg-surface-container-high h-1 rounded-full overflow-hidden">
<div class="bg-secondary h-full w-[82%]"></div>
</div>
</div>
</div>
<!-- Active Assistant Interaction Canvas -->
<div class="w-full flex flex-col gap-space-lg max-w-[1100px]">
<!-- Operator Query Plate -->
<div class="self-end max-w-[70%] bg-surface-container border border-outline-variant rounded-xl p-space-md flex flex-col gap-space-xs">
<div class="flex items-center justify-between text-outline gap-space-md">
<span class="font-label-mono-tag text-label-mono-tag uppercase">OPERATOR // CREW-A (M. TURNER)</span>
<span class="font-label-mono-tag text-[11px]">14:24:08 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">
Analyze thermal delta signature for WELL-0001 against latest IR inspection run and confirm if production status matches SCADA telemetry.
</p>
</div>
<!-- Assistant Report Structural Block -->
<div class="w-full bg-surface-container-low border border-outline-variant rounded-lg p-space-lg relative flex flex-col gap-space-md">
<!-- Signal Cyan Left Border Rail -->
<div class="absolute left-0 top-0 bottom-0 w-1 bg-primary-container rounded-l-lg"></div>
<!-- Assistant Header -->
<div class="flex items-center justify-between border-b border-outline-variant pb-space-sm"><div class="flex items-center gap-space-sm"><span class="material-symbols-outlined text-primary text-[20px]">smart_toy</span><span class="font-body-spec-mono text-body-spec-mono font-semibold tracking-wide text-on-surface">ASSET INTELLIGENCE ENGINE</span></div><div class="font-label-mono-tag text-xs text-outline">Weekly Inspection Ingest</div></div>
<!-- Report Content -->
<div class="font-body-prose text-body-prose text-on-surface space-y-space-sm">
<p class="">
Thermal inspection telemetry for <span class="font-body-spec-mono text-primary bg-primary/10 px-1 py-0.5 rounded">WELL-0001</span> demonstrates an anomalous wellhead thermal delta of only <strong class="text-on-surface font-semibold">+3.2 °C</strong> above air. This firmly places the well under the static non-flow threshold defined in the operating manual.
</p>
<!-- Highlighted Citation Trigger: Active glowing state -->
<div class="p-space-sm rounded-lg bg-surface-container border border-primary-container/60 inline-flex items-center gap-space-sm shadow-[0_0_15px_rgba(56,189,248,0.25)]"><span class="font-body-spec text-on-surface text-sm">Citations:</span><button class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-primary-container/20 border border-primary-container text-primary font-label-mono-tag text-label-mono-tag tracking-wider cursor-pointer"><span class="material-symbols-outlined text-[15px]">fact_check</span><span class="">INS-0001-0203</span></button><span class="inline-flex items-center gap-1 px-2 py-1 rounded bg-surface-container-high border border-outline-variant text-on-surface-variant font-label-mono-tag text-label-mono-tag"><span class="material-symbols-outlined text-[14px]">history_edu</span><span class="">CTX-0001-003</span></span></div>
<!-- Inline Telemetry Diagnostic Chart Rendering -->
<div class="mt-space-md p-space-md rounded-lg bg-surface-container border border-outline-variant space-y-space-sm">
<div class="flex items-center justify-between text-outline">
<span class="font-label-metric text-label-metric uppercase">THERMAL DISPERSION vs RUN TIME (LAST 72 HRS)</span>
<span class="font-label-mono-tag text-xs text-outline font-mono">SENSOR: IR-FLIR-RB04</span>
</div>
<!-- SVG Sparkline & Baseline Curve -->
<div class="w-full h-32 relative">
<svg class="w-full h-full overflow-visible" preserveAspectRatio="none" viewBox="0 0 600 120">
<line stroke="#263140" stroke-dasharray="3 3" stroke-width="1" x1="0" x2="600" y1="40" y2="40"></line>
<line stroke="#263140" stroke-dasharray="3 3" stroke-width="1" x1="0" x2="600" y1="80" y2="80"></line>
<text class="font-label-mono-tag text-[9px] fill-outline" x="5" y="36">PRODUCING THRESHOLD (+12.0 °C)</text>
<text class="font-label-mono-tag text-[9px] fill-error" x="5" y="76">SHUT-IN CEILING (+3.5 °C)</text>
<!-- Telemetry trace -->
<path d="M 0,38 Q 80,42 160,50 T 300,78 T 420,88 T 600,92" fill="none" stroke="#38bdf8" stroke-width="2.5"></path>
<!-- Target Inspection Point -->
<circle cx="420" cy="88" fill="#38bdf8" r="4" stroke="#0e141c" stroke-width="2"></circle>
</svg>
</div>
<div class="flex items-center justify-between font-label-mono-tag text-[11px] text-outline pt-space-xs border-t border-outline-variant/50">
<span class="">OCT 13 00:00 UTC</span>
<span class="text-primary font-bold">▲ DRONE RUN: OCT 15 14:12 UTC (+3.2 °C)</span>
<span class="">OCT 16 00:00 UTC</span>
</div>
</div>
</div>
<div class="pt-2 border-t border-outline-variant/40 flex items-center justify-between font-label-mono-tag text-[11px] text-outline"><span class="">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div></div>
</div>
<!-- Persistent Bottom Prompt Dock (Dimmed Base) -->
<div class="max-w-[1100px] mt-space-md p-space-sm bg-surface-container border border-outline-variant rounded-xl flex items-center justify-between gap-space-md">
<div class="flex items-center gap-space-sm flex-1 text-outline">
<span class="material-symbols-outlined text-[20px]">terminal</span>
<span class="font-body-spec text-sm">Query telemetry, logs, or correlate wellhead anomalies...</span>
</div>
<button class="px-space-md py-1.5 rounded-lg bg-primary-container text-on-primary-container font-body-spec-mono text-body-spec-mono font-semibold flex items-center gap-1.5">
<span class="">Execute</span>
<span class="material-symbols-outlined text-[16px]">arrow_forward</span>
</button>
</div>
</div>
<!-- DIMMING OVERLAY OVER CONSOLE (40% Dim + blur) -->
<div class="fixed inset-0 bg-black/40 backdrop-blur-[2px] z-40 transition-opacity duration-300"></div>
<!-- 420PX RIGHT-SIDE SLIDE-OVER DRAWER -->
<aside class="fixed top-0 right-0 h-full w-[420px] bg-[#121820] border-l border-[#263140] shadow-2xl shadow-black/80 z-50 flex flex-col transition-transform duration-300 ease-out select-none">
<!-- DRAWER TOP BAR -->
<div class="p-space-lg border-b border-[#263140] bg-[#121820] flex flex-col gap-space-xs">
<!-- Top Action Row & Tags -->
<div class="flex items-center justify-between">
<div class="flex items-center gap-space-xs">
<!-- Kind Pill: INSPECTION -->
<div class="flex items-center gap-1 px-2 py-0.5 rounded bg-[#1E2733] border border-[#263140] text-[#94A3B8] font-label-mono-tag text-[11px] font-semibold">
<span class="material-symbols-outlined text-[14px] text-primary">fact_check</span>
<span class="">INSPECTION</span>
</div>
<!-- ID Chip -->
<span class="px-2 py-0.5 rounded bg-[#1A222D] border border-primary-container/30 text-primary-container font-label-mono-tag text-[12px] font-semibold tracking-wide">
INS-0001-0203
</span>
</div>
<!-- Close Action & ESC Pill Hint -->
<div class="flex items-center gap-space-xs">
<span class="px-1.5 py-0.5 rounded bg-[#1A222D] border border-[#263140] font-label-mono-tag text-[10px] text-outline">ESC</span>
<button class="p-1 rounded hover:bg-[#1A222D] text-outline hover:text-on-surface transition-colors flex items-center justify-center">
<span class="material-symbols-outlined text-[20px]">close</span>
</button>
</div>
</div>
<!-- Drawer Main Title & Well Reference -->
<div class="mt-space-xs">
<h2 class="font-headline-panel text-[20px] leading-tight font-semibold text-white tracking-tight">
Inspection INS-0001-0203
</h2>
<div class="mt-1 flex items-center gap-1.5 font-label-mono-tag text-xs text-outline"><a class="text-primary hover:underline font-semibold" href="#">WELL-0001</a><span class="">·</span><span class="">Southwest Block 23</span></div>
</div>
</div>
<!-- DRAWER SCROLLABLE BODY -->
<div class="p-space-lg flex-1 overflow-y-auto space-y-5 text-on-surface">
<!-- 1. SUMMARY SECTION -->
<section class="flex flex-col gap-1.5">
<div class="rounded-lg bg-[#1A222D] border border-[#263140] p-4 flex flex-col">
<span class="font-label-mono-tag text-[11px] uppercase tracking-wider text-outline mb-1.5 font-semibold">INSPECTION SUMMARY</span>
<p class="font-body-spec text-[14px] text-slate-200 leading-relaxed">
15 Oct 2026, drone, Ryan Brooks. Wellhead 3.2 °C above air, so the well is not producing oil.
</p>
</div>
</section>
<!-- 2. RECORD FIELDS SECTION -->
<section class="flex flex-col">
<div class="flex items-center justify-between mb-2">
<span class="font-label-metric text-[12px] uppercase tracking-wider text-outline font-semibold">
RECORD METRICS &amp; METADATA
</span>
<span class="font-label-mono-tag text-[11px] text-outline">7 ATTRS</span>
</div>
<div class="bg-surface-container-low border border-[#263140] rounded-lg p-3 space-y-2.5"><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2"><span class="font-label-mono-tag text-xs text-outline">Date &amp; Time</span><span class="font-body-spec-mono text-xs text-on-surface">15 Oct 2026, 14:12 UTC</span></div><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2"><span class="font-label-mono-tag text-xs text-outline">Inspector / Crew</span><span class="font-body-spec text-xs text-on-surface">Ryan Brooks (Field Crew A)</span></div><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2"><span class="font-label-mono-tag text-xs text-outline">Inspection Method</span><span class="font-body-spec text-xs text-on-surface">Autonomous Drone IR Survey</span></div><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2 bg-primary/5 -mx-3 px-3 py-1.5"><span class="font-label-mono-tag text-xs text-primary font-medium">Surface ΔT Baseline</span><span class="font-body-spec-mono text-xs text-primary font-bold">+3.2 °C above ambient</span></div><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2"><span class="font-label-mono-tag text-xs text-outline">Flow Condition</span><span class="font-body-spec-mono text-xs text-error font-medium">Non-Flow / Shut-in</span></div><div class="flex items-center justify-between border-b border-[#263140]/60 pb-2"><span class="font-label-mono-tag text-xs text-outline">Equipment Tag</span><span class="font-body-spec-mono text-xs text-on-surface">WELL-0001 (WH-01)</span></div><div class="flex items-center justify-between pt-0.5"><span class="font-label-mono-tag text-xs text-outline">Sensor Calib</span><span class="font-body-spec-mono text-xs text-on-surface">Pass (FLIR-RB04)</span></div></div>
</section>
<!-- 3. FLAGS THAT USE THIS RECORD -->
<section class="flex flex-col">
<span class="font-label-metric text-[12px] uppercase tracking-wider text-outline font-semibold mb-2">
FLAGS &amp; CONFLICTS
</span>
<div class="bg-[#FBBF24]/10 border border-[#FBBF24]/40 text-[#FDE68A] p-3 rounded-lg flex items-start gap-2.5"><span class="material-symbols-outlined text-[#FBBF24] text-[20px] shrink-0 mt-0.5">warning</span><div class="flex flex-col min-w-0"><span class="font-body-prose-medium text-xs font-semibold text-[#FDE68A] leading-tight">Recorded status still says active (out of date)</span><span class="font-body-spec text-[12px] text-slate-300 mt-1 leading-normal">Weekly inspection indicates shut-in condition since 8 Oct 2026.</span></div></div>
</section>
<!-- 4. RELATED RECORDS SECTION -->
<section class="flex flex-col">
<div class="flex items-center justify-between mb-2">
<span class="font-label-metric text-[12px] uppercase tracking-wider text-outline font-semibold">
RELATED RECORDS
</span>
<span class="font-label-mono-tag text-[10px] text-outline">2 LINKED ITEMS</span>
</div>
<div class="space-y-2">
<!-- Row 1: Note -->
<div class="bg-surface-container-low hover:bg-surface-container border border-[#263140] hover:border-outline rounded-lg p-3 transition flex items-start justify-between gap-2.5 cursor-pointer">
<div class="flex items-start gap-2.5 min-w-0">
<span class="material-symbols-outlined text-[#A78BFA] text-[18px] shrink-0 mt-0.5">chat_bubble</span>
<div class="flex flex-col min-w-0">
<div class="flex items-center gap-2 mb-1">
<span class="px-1.5 py-0.5 rounded bg-[#A78BFA]/10 border border-[#A78BFA]/30 text-[#A78BFA] font-label-mono-tag text-[10px] font-semibold">
CTX-0001-003
</span>
<span class="font-label-mono-tag text-[10px] text-outline">FIELD NOTE</span>
</div>
<p class="font-body-spec text-xs text-slate-300 line-clamp-2">
Planned shut-in from 7 Oct, rod string replacement, back around 20 Oct – Jake Morales
</p>
</div>
</div>
<span class="material-symbols-outlined text-outline text-[16px] shrink-0 mt-1">chevron_right</span>
</div>
<!-- Row 2: Document -->
<div class="bg-surface-container-low hover:bg-surface-container border border-[#263140] hover:border-outline rounded-lg p-3 transition flex items-start justify-between gap-2.5 cursor-pointer">
<div class="flex items-start gap-2.5 min-w-0">
<span class="material-symbols-outlined text-primary-container text-[18px] shrink-0 mt-0.5">description</span>
<div class="flex flex-col min-w-0">
<div class="flex items-center gap-2 mb-1">
<span class="px-1.5 py-0.5 rounded bg-primary-container/10 border border-primary-container/30 text-primary font-label-mono-tag text-[10px] font-semibold">
DOC-T200
</span>
<span class="font-label-mono-tag text-[10px] text-outline">OPERATIONS MANUAL</span>
</div>
<p class="font-body-spec text-xs text-slate-300">
T200 manual: producing-oil threshold
</p>
</div>
</div>
<span class="material-symbols-outlined text-outline text-[16px] shrink-0 mt-1">chevron_right</span>
</div>
</div>
</section>
<!-- SPECIFICATION & KIND VARIANTS BENCHMARK CARD -->
<section class="pt-2 border-t border-[#263140]">
<span class="font-label-metric text-[11px] uppercase tracking-wider text-outline font-semibold block mb-2">
RECORD KIND IDENTIFICATION MATRIX
</span>
<div class="grid grid-cols-2 gap-2">
<!-- Variant 1: Maintenance -->
<div class="p-2 rounded bg-surface-container-low border border-[#263140] flex flex-col gap-1">
<div class="flex items-center justify-between">
<span class="material-symbols-outlined text-[#FB923C] text-[16px]">build</span>
<span class="px-1.5 py-0.2 rounded bg-[#FB923C]/10 border border-[#FB923C]/30 text-[#FB923C] font-label-mono-tag text-[9px] font-bold">
MAINTENANCE
</span>
</div>
<span class="font-label-mono-tag text-[11px] text-slate-300">MNT-0001-032</span>
</div>
<!-- Variant 2: Regulatory -->
<div class="p-2 rounded bg-surface-container-low border border-[#263140] flex flex-col gap-1">
<div class="flex items-center justify-between">
<span class="material-symbols-outlined text-[#F43F5E] text-[16px]">account_balance</span>
<span class="px-1.5 py-0.2 rounded bg-[#F43F5E]/10 border border-[#F43F5E]/30 text-[#F43F5E] font-label-mono-tag text-[9px] font-bold">
REGULATORY
</span>
</div>
<span class="font-label-mono-tag text-[11px] text-slate-300">REG-0001-002</span>
</div>
<!-- Variant 3: Note -->
<div class="p-2 rounded bg-surface-container-low border border-[#263140] flex flex-col gap-1">
<div class="flex items-center justify-between">
<span class="material-symbols-outlined text-[#A78BFA] text-[16px]">chat</span>
<span class="px-1.5 py-0.2 rounded bg-[#A78BFA]/10 border border-[#A78BFA]/30 text-[#A78BFA] font-label-mono-tag text-[9px] font-bold">
NOTE
</span>
</div>
<span class="font-label-mono-tag text-[11px] text-slate-300">CTX-0001-003</span>
</div>
<!-- Variant 4: Document -->
<div class="p-2 rounded bg-surface-container-low border border-[#263140] flex flex-col gap-1">
<div class="flex items-center justify-between">
<span class="material-symbols-outlined text-[#38BDF8] text-[16px]">draft</span>
<span class="px-1.5 py-0.2 rounded bg-[#38BDF8]/10 border border-[#38BDF8]/30 text-[#38BDF8] font-label-mono-tag text-[9px] font-bold">
DOCUMENT
</span>
</div>
<span class="font-label-mono-tag text-[11px] text-slate-300">DOC-SR-SOP</span>
</div>
</div>
</section>
</div>
<!-- DRAWER FOOTER (Fixed Bottom Action Dock) -->
<div class="p-4 bg-[#0e141c] border-t border-[#263140] flex items-center justify-between gap-3">
<!-- Copy ID Button -->
<button class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-md border border-[#263140] hover:bg-[#1A222D] text-slate-300 hover:text-white font-label-mono-tag text-xs font-mono transition-colors">
<span class="material-symbols-outlined text-[15px]">content_copy</span>
<span class="">Copy ID</span>
</button>
<!-- Correction Button -->
<button class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-md bg-primary-container/20 hover:bg-primary-container/30 text-primary border border-primary-container/40 font-body-spec text-xs font-medium transition-colors"><span class="material-symbols-outlined text-[15px]">assignment_turned_in</span><span class="">Suggest field check</span></button>
</div>
</aside>
</div></main></div>

</body></html>
```

8. new_chat_asset_intelligence_copilot
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"outline-variant":"#3e484f","primary":"#8ed5ff","on-secondary-fixed-variant":"#005137","primary-container":"#38bdf8","surface-container":"#1a2028","surface-bright":"#343a42","on-error-container":"#ffdad6","surface":"#0e141c","on-secondary":"#003825","inverse-primary":"#00668a","error-container":"#93000a","tertiary":"#ffbcbf","primary-fixed":"#c4e7ff","secondary-fixed":"#68fcbf","on-error":"#690005","outline":"#87929a","on-secondary-fixed":"#002114","on-tertiary-container":"#8c0028","secondary-fixed-dim":"#45dfa4","on-tertiary-fixed-variant":"#92002a","surface-variant":"#2f353e","surface-tint":"#7bd0ff","on-primary-fixed":"#001e2c","on-tertiary":"#67001b","surface-container-highest":"#2f353e","surface-container-high":"#242a33","surface-container-low":"#161c24","on-surface":"#dde3ee","tertiary-fixed":"#ffdadb","background":"#0e141c","inverse-surface":"#dde3ee","on-primary-fixed-variant":"#004c69","on-primary-container":"#004965","on-surface-variant":"#bdc8d1","primary-fixed-dim":"#7bd0ff","on-secondary-container":"#00452e","surface-dim":"#0e141c","on-background":"#dde3ee","tertiary-fixed-dim":"#ffb2b7","error":"#ffb4ab","on-primary":"#00354a","inverse-on-surface":"#2b3139","tertiary-container":"#ff929a","surface-container-lowest":"#090f16","on-tertiary-fixed":"#40000d","secondary-container":"#00bd85","secondary":"#45dfa4"},borderRadius:{DEFAULT:"0.125rem",lg:"0.25rem",xl:"0.5rem",full:"0.75rem"},spacing:{"space-lg":"1.25rem","space-xl":"1.5rem","space-xs":"0.25rem","space-md":"1rem",margin:"1.5rem",gutter:"1.5rem","space-sm":"0.5rem"},fontFamily:{"body-spec":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"body-prose-medium":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel-mobile":["IBM Plex Sans"],"display-telemetry":["IBM Plex Mono"],"headline-panel":["IBM Plex Sans"]},fontSize:{"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}}</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low border-r border-outline-variant z-40 flex flex-col justify-between select-none"><div class="flex flex-col flex-1 min-h-0"><div class="p-space-md border-b border-outline-variant"><div class="flex items-center gap-space-sm mb-space-xs"><span class="material-symbols-outlined text-primary-container text-[22px]">precision_manufacturing</span><span class="font-headline-panel text-headline-panel tracking-tight text-on-surface">Asset Intelligence</span></div><div class="font-label-mono-tag text-label-mono-tag uppercase tracking-wider text-outline">WEEKLY INSPECTION INTELLIGENCE</div></div><div class="p-space-md border-b border-outline-variant bg-surface-container-low"><div class="flex items-center justify-between"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono text-primary font-bold">MT</div><div class="flex flex-col min-w-0"><div class="font-body-spec-mono text-body-spec-mono text-on-surface truncate leading-tight">Michael Turner</div><div class="font-label-mono-tag text-label-mono-tag text-outline truncate">Production Supervisor</div></div></div><span class="material-symbols-outlined text-outline-variant text-[18px]">expand_more</span></div><div class="mt-space-sm pt-space-xs border-t border-outline-variant flex items-center justify-between text-outline"><span class="font-label-mono-tag text-label-mono-tag truncate">Northeast Production</span><div class="flex items-center gap-space-xs text-outline"><span class="material-symbols-outlined text-[14px]">lock</span><span class="font-label-mono-tag text-label-mono-tag text-[10px]">Private</span></div></div></div><div class="p-space-md"><a class="w-full flex items-center justify-center gap-space-sm py-space-sm px-space-md rounded-lg border border-primary-container text-primary-container hover:bg-surface-container hover:text-primary transition-colors font-body-spec-mono text-body-spec-mono" data-path="copilot-workspace" href="#"><span class="material-symbols-outlined text-[18px]">add</span><span class="">New chat</span></a></div><div class="px-space-md pt-space-xs pb-space-xs"><div class="font-label-mono-tag text-label-mono-tag uppercase text-outline tracking-wider">RECENT CHATS</div></div><nav class="flex-1 overflow-y-auto px-space-xs py-space-xs space-y-space-xs" data-active-classes="bg-surface-container text-primary border-l-2 border-primary-container"><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec-mono text-body-spec-mono truncate" href="#"><span class="truncate">WELL-0001 status and last inspection</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec-mono text-body-spec-mono truncate" href="#"><span class="truncate">Northeast Block 8 not producing</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec-mono text-body-spec-mono truncate" href="#"><span class="truncate">Block 7 downtime, top 3</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec-mono text-body-spec-mono truncate" href="#"><span class="truncate">WELL-0001 spills, last 4 years</span></a><a class="flex items-center px-space-md py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec-mono text-body-spec-mono truncate" href="#"><span class="truncate">Pump jack root-cause wells</span></a></nav></div><div class="p-space-md border-t border-outline-variant bg-surface-container-lowest"><div class="flex items-center justify-between text-outline font-label-mono-tag text-[11px]"><span class="">INSPECTIONS WORKSPACE</span><span class="">OCT 2026</span></div></div></aside><div class="pl-[296px] min-h-screen flex flex-col"><header class="fixed top-0 left-[296px] right-0 h-14 bg-surface-container-low border-b border-outline-variant z-30 flex items-center justify-between px-space-lg"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] font-semibold text-on-surface">Asset Intelligence Copilot</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-[12px] text-on-surface-variant"><span class="material-symbols-outlined text-[15px] text-outline">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-space-xs px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-body-spec-mono text-[13px] text-on-surface"><div class="w-5 h-5 rounded-full bg-primary flex items-center justify-center font-bold text-[10px] text-on-primary">MT</div><span class="">Michael Turner</span></div></div></header><main class="relative pt-14 w-full flex-1 bg-surface-container-lowest"><div class="flex flex-col w-full">
<div class="w-full flex justify-center px-space-md lg:px-space-xl py-space-lg">
<div class="w-full max-w-[880px] flex flex-col justify-between min-h-[calc(100vh-5.5rem)]">
<!-- Upper Section: Greeting & Exploration Surface -->
<div class="flex flex-col space-y-space-xl pt-space-xs">
<!-- Header Group -->
<div class="flex flex-col space-y-space-xs">
<div class="flex items-center gap-space-sm mb-space-xs"><span class="inline-flex items-center gap-1.5 px-space-sm py-0.5 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-[11px] tracking-wider uppercase text-primary-container"><span class="material-symbols-outlined text-[14px]">assignment</span>Weekly Inspections</span></div>
<h1 class="font-headline-panel text-[28px] leading-[34px] font-semibold tracking-tight text-on-surface">
Good afternoon, Michael
</h1>
<p class="font-body-prose text-on-surface-variant text-[15px] leading-relaxed">
Ask about any of the 200 wells. Answers come with the records behind them.
</p>
</div>
<!-- 3x2 Example Query Matrix -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-space-md">
<!-- Card 1: Status Card -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('Is WELL-0001 producing oil right now?')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#38BDF8]/10 text-primary-container font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">play_circle</span>
STATUS CARD
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 01</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
Is WELL-0001 producing oil right now?
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
<!-- Card 2: Table -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('Which wells in Northeast Block 8 are not producing oil, and why?')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#A78BFA]/10 text-[#C4B5FD] font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">table_chart</span>
TABLE
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 02</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
Which wells in Northeast Block 8 are not producing oil, and why?
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
<!-- Card 3: Line Chart -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('WELL-0001 wellhead vs air temperature, last 13 weeks')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#38BDF8]/10 text-primary font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">show_chart</span>
LINE CHART
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 03</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
WELL-0001 wellhead vs air temperature, last 13 weeks
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
<!-- Card 4: Bar Chart -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('Top 3 downtime wells in Northeast Block 7, last 4 months')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#FB923C]/10 text-[#FDBA74] font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">bar_chart</span>
BAR CHART
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 04</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
Top 3 downtime wells in Northeast Block 7, last 4 months
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
<!-- Card 5: Map -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('Real spills in Northeast Block 8, last 90 days')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#F43F5E]/10 text-tertiary-fixed font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">pin_drop</span>
MAP
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 05</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
Real spills in Northeast Block 8, last 90 days
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
<!-- Card 6: Heatmap -->
<button class="group text-left p-[18px] bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container rounded-lg transition-all duration-150 flex flex-col justify-between h-[152px] select-none shadow-none" onclick="setQuery('2026 spills by area and month')" type="button">
<div class="flex items-center justify-between w-full">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-[#FBBF24]/10 text-[#FDE68A] font-label-mono-tag text-[11px] tracking-wider uppercase">
<span class="material-symbols-outlined text-[15px]">calendar_view_month</span>
HEATMAP
</span>
<span class="font-label-mono-tag text-[11px] text-outline group-hover:text-primary-container transition-colors">QUERY 06</span>
</div>
<div class="font-body-prose-medium text-[15px] text-on-surface group-hover:text-white leading-snug line-clamp-2">
2026 spills by area and month
</div>
<div class="flex items-center justify-end w-full text-outline group-hover:text-primary-container transition-colors">
<span class="font-label-mono-tag text-[11px] mr-1 opacity-0 group-hover:opacity-100 transition-opacity">Run query</span>
<span class="material-symbols-outlined text-[16px] transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform">north_east</span>
</div>
</button>
</div>
<!-- Callout / Feedback Calibration Tip Box -->
<div class="p-space-md rounded-lg bg-surface-container-low border border-outline-variant flex flex-col space-y-space-sm">
<div class="flex items-start gap-space-sm">
<span class="material-symbols-outlined text-[18px] text-primary-container shrink-0 mt-0.5">tips_and_updates</span>
<div class="flex flex-col space-y-1">
<p class="font-body-spec text-[14px] leading-relaxed text-on-surface">
<strong class="font-semibold text-on-surface">You can also teach me.</strong> Try:
<button class="font-body-spec-mono text-[13px] text-primary hover:underline bg-surface-container px-1.5 py-0.5 rounded inline-block text-left border border-outline-variant" onclick="setQuery('The 15 Oct reading for WELL-0164 is wrong, the crew re-measured 41.0 C.')" type="button">
“The 15 Oct reading for WELL-0164 is wrong, the crew re-measured 41.0 C.”
</button>
</p>
</div>
</div>
<div class="pt-space-xs border-t border-outline-variant/60 flex items-center gap-space-xs text-outline font-label-mono-tag text-[11px]">
<span class="material-symbols-outlined text-[14px]">verified_user</span>
<span class="">Your chats stay private. Corrections you give are cataloged with audit IDs and shared across shifts.</span>
</div>
</div>
</div>
<!-- Docked Bottom Terminal Composer -->
<div class="sticky bottom-0 pt-space-lg pb-space-sm bg-surface-container-lowest">
<div class="relative bg-surface-container-low border border-outline-variant focus-within:border-primary-container rounded-xl transition-colors duration-150 p-space-md">

<form class="flex flex-col gap-space-sm" id="consoleForm" onsubmit="handleSend(event)"><div class="flex items-center justify-between pb-space-xs mb-space-xs border-b border-outline-variant/40"><div class="flex items-center gap-space-xs text-outline font-label-mono-tag text-[11px]"><span class="material-symbols-outlined text-[14px] text-primary-container">terminal</span><span class="">INPUT CANONICAL CHANNEL</span></div></div><textarea class="w-full bg-transparent resize-none text-[15px] font-body-spec text-on-surface placeholder:text-outline focus:outline-none leading-relaxed" id="queryInput" onkeydown="handleKeyDown(event)" placeholder="Ask about wellhead inspections, valve clearances, or downtime records..." rows="2"></textarea><div class="flex items-center justify-between pt-space-xs"><div class="flex items-center gap-space-xs"><button class="p-1.5 rounded text-outline hover:text-on-surface hover:bg-surface-container transition-colors" title="Attach Log" type="button"><span class="material-symbols-outlined text-[18px]">attachment</span></button><button class="p-1.5 rounded text-outline hover:text-on-surface hover:bg-surface-container transition-colors" title="Filter Wells" type="button"><span class="material-symbols-outlined text-[18px]">filter_alt</span></button><span class="h-3.5 w-px bg-outline-variant mx-1"></span><span class="font-label-mono-tag text-[11px] text-outline">READY</span></div><div class="flex items-center gap-space-sm"><button aria-label="Send" class="flex items-center justify-center w-8 h-8 rounded-lg bg-primary-container text-surface-container-lowest font-body-spec-mono font-semibold hover:bg-primary transition-colors cursor-pointer select-none" type="submit"><span class="material-symbols-outlined text-[18px]">arrow_forward</span></button></div></div></form>
</div>
<!-- Hotkeys Footer Hint -->
<div class="flex items-center justify-between px-space-xs pt-space-xs font-label-mono-tag text-[11px] text-outline"><div class="flex items-center gap-space-sm"><span class=""><strong class="text-on-surface-variant font-medium">Enter</strong> to send</span><span class="">·</span><span class=""><strong class="text-on-surface-variant font-medium">Shift + Enter</strong> for line break</span><span class="">·</span><span class=""><strong class="text-on-surface-variant font-medium">/</strong> for well quick-search</span></div></div>
</div>
</div>
</div>
</div>
<script>
function setQuery(text) {
const input = document.getElementById('queryInput');
if (input) {
input.value = text;
input.focus();
// Auto adjust height if needed
input.setSelectionRange(text.length, text.length);
}
}

function handleKeyDown(e) {
if (e.key === 'Enter' && !e.shiftKey) {
e.preventDefault();
handleSend(e);
}
}

function handleSend(e) {
e.preventDefault();
const input = document.getElementById('queryInput');
if (!input || !input.value.trim()) return;

// UI response feedback
const btn = document.querySelector('button[type="submit"]');
if (btn) {
const origText = btn.innerHTML;
btn.innerHTML = `<span class="material-symbols-outlined text-[15px] animate-spin">refresh</span><span>Processing</span>`;
btn.disabled = true;
setTimeout(() => {
btn.innerHTML = origText;
btn.disabled = false;
input.value = '';
}, 700);
}
}
</script></main></div>

</body></html>
```

9. 
```
<!DOCTYPE html><html class="dark" lang="en" style=""><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config = { darkMode: "class", theme: { extend: { "colors": { "on-primary-fixed": "#001e2c", "surface-variant": "#2f353e", "on-primary": "#00354a", "primary-fixed-dim": "#7bd0ff", "surface-bright": "#343a42", "primary": "#8ed5ff", "tertiary-fixed-dim": "#ffb2b7", "surface-container-low": "#161c24", "outline-variant": "#3e484f", "surface-dim": "#0e141c", "on-error-container": "#ffdad6", "secondary-container": "#00bd85", "on-error": "#690005", "surface-container": "#1a2028", "on-tertiary-fixed-variant": "#92002a", "secondary-fixed-dim": "#45dfa4", "outline": "#87929a", "secondary-fixed": "#68fcbf", "surface": "#0e141c", "tertiary-fixed": "#ffdadb", "on-secondary": "#003825", "error": "#ffb4ab", "surface-container-highest": "#2f353e", "background": "#0e141c", "on-tertiary-fixed": "#40000d", "inverse-on-surface": "#2b3139", "on-primary-fixed-variant": "#004c69", "on-secondary-fixed-variant": "#005137", "on-secondary-fixed": "#002114", "inverse-primary": "#00668a", "error-container": "#93000a", "surface-container-high": "#242a33", "on-secondary-container": "#00452e", "on-background": "#dde3ee", "tertiary": "#ffbcbf", "on-surface": "#dde3ee", "secondary": "#45dfa4", "on-tertiary": "#67001b", "tertiary-container": "#ff929a", "on-tertiary-container": "#8c0028", "primary-fixed": "#c4e7ff", "primary-container": "#38bdf8", "surface-tint": "#7bd0ff", "inverse-surface": "#dde3ee", "surface-container-lowest": "#090f16", "on-primary-container": "#004965", "on-surface-variant": "#bdc8d1" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-lg": "1.25rem", "space-md": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "gutter": "1.5rem", "space-sm": "0.5rem", "margin": "1.5rem" }, "fontFamily": { "body-spec": [ "IBM Plex Sans" ], "label-mono-tag": [ "IBM Plex Mono" ], "body-prose-medium": [ "IBM Plex Sans" ], "label-metric": [ "IBM Plex Sans" ], "body-spec-mono": [ "IBM Plex Mono" ], "headline-panel": [ "IBM Plex Sans" ], "headline-panel-mobile": [ "IBM Plex Sans" ], "body-prose": [ "IBM Plex Sans" ], "display-telemetry": [ "IBM Plex Mono" ] }, "fontSize": { "body-spec": [ "14px", { "lineHeight": "20px", "fontWeight": "400" } ], "label-mono-tag": [ "12px", { "lineHeight": "16px", "fontWeight": "500" } ], "body-prose-medium": [ "16px", { "lineHeight": "24px", "fontWeight": "500" } ], "label-metric": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "body-spec-mono": [ "14px", { "lineHeight": "20px", "fontWeight": "500" } ], "headline-panel": [ "20px", { "lineHeight": "28px", "letterSpacing": "-0.01em", "fontWeight": "600" } ], "headline-panel-mobile": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ], "body-prose": [ "16px", { "lineHeight": "24px", "fontWeight": "400" } ], "display-telemetry": [ "28px", { "lineHeight": "34px", "letterSpacing": "-0.01em", "fontWeight": "600" } ] } } } };</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface antialiased"><aside class="fixed left-0 top-0 h-full w-16 bg-surface-container-low flex flex-col items-center justify-between py-space-md z-50 border-r border-surface-container-high"><div class="flex flex-col h-full w-full justify-between items-center py-space-md"><div class="flex flex-col items-center gap-space-md w-full px-2"><div class="w-10 h-10 rounded bg-surface-container flex items-center justify-center border border-outline-variant text-primary"><span class="material-symbols-outlined text-[20px]">terminal</span></div><button type="button" class="w-10 h-10 rounded bg-primary-container text-on-primary-container flex items-center justify-center hover:opacity-90 transition-opacity" title="+ New chat"><span class="material-symbols-outlined text-[20px]">add</span></button><div class="w-8 h-[1px] bg-outline-variant my-1"></div><div class="flex flex-col items-center gap-2 w-full" title="Recent chats"><button type="button" class="w-10 h-10 rounded bg-surface-container text-primary flex items-center justify-center border border-primary/40" title="Block 7 downtime, top 3"><span class="material-symbols-outlined text-[18px]">chat</span></button><button type="button" class="w-10 h-10 rounded text-on-surface-variant hover:bg-surface-container flex items-center justify-center transition-colors" title="WELL-0001 status and last inspection"><span class="material-symbols-outlined text-[18px]">history</span></button><button type="button" class="w-10 h-10 rounded text-on-surface-variant hover:bg-surface-container flex items-center justify-center transition-colors" title="Northeast Block 8 not producing"><span class="material-symbols-outlined text-[18px]">history</span></button><button type="button" class="w-10 h-10 rounded text-on-surface-variant hover:bg-surface-container flex items-center justify-center transition-colors" title="WELL-0001 spills, last 4 years"><span class="material-symbols-outlined text-[18px]">history</span></button><button type="button" class="w-10 h-10 rounded text-on-surface-variant hover:bg-surface-container flex items-center justify-center transition-colors" title="Pump jack root-cause wells"><span class="material-symbols-outlined text-[18px]">history</span></button></div></div><div class="flex flex-col items-center gap-space-sm"><div class="w-8 h-8 rounded bg-primary flex items-center justify-center text-on-primary font-bold text-xs">MT</div></div></div></aside><div class="pl-16 min-h-screen flex flex-col"><header class="fixed top-0 left-16 right-0 h-14 bg-surface-container-lowest/95 backdrop-blur-md z-40 border-b border-surface-container-high"><div class="w-full h-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] text-on-surface font-semibold">Northeast Block 7 Downtime</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-label-mono-tag text-xs text-on-surface-variant"><span class="material-symbols-outlined text-[15px] text-primary">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-space-xs px-space-sm py-1 rounded bg-surface-container border border-outline-variant font-body-spec text-xs text-on-surface"><div class="w-5 h-5 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold text-[10px]">MT</div><span class="">Michael Turner</span></div></div></div></header><main class="w-full pt-14 bg-surface-container-lowest flex-1"><div class="flex flex-col w-full">
<div class="w-full max-w-[880px] mx-auto px-space-md py-space-xl flex flex-col gap-space-xl font-body-spec">
<!-- 1. Operator Query Plate (Right-Aligned) -->
<div class="flex flex-col items-end w-full">
<div class="max-w-[75%] bg-surface-container border border-outline-variant rounded-xl p-space-md flex flex-col gap-space-xs">
<div class="flex items-center justify-between gap-space-md w-full border-b border-surface-container-high pb-space-xs">
<div class="flex items-center gap-space-xs">
<span class="w-1.5 h-1.5 rounded-full bg-primary"></span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase tracking-wider">OPERATOR QUERY // CREW-A (CONSOLE-04)</span>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline">14:32:15 UTC</span>
</div>
<p class="font-body-prose-medium text-body-prose-medium text-on-surface pt-space-xs">
Which 3 wells in Northeast Block 7 had the most downtime in the last 4 months?
<span class="inline-flex items-center px-1.5 py-0.5 rounded bg-primary/10 border border-primary/30 font-body-spec-mono text-primary text-xs ml-1">#NE-BLOCK-7</span>
</p>
</div>
</div>
<!-- 2. Assistant Report Block -->
<div class="w-full bg-surface-container-low border border-outline-variant border-l-[3px] border-l-primary-container rounded-xl p-space-lg flex flex-col gap-space-lg">
<!-- Report Header Metadata -->
<div class="flex flex-wrap items-center justify-between gap-space-md border-b border-outline-variant/60 pb-space-md">
<div class="flex items-center gap-space-md">
<div class="w-8 h-8 rounded bg-surface-container border border-outline-variant flex items-center justify-center text-primary-container">
<span class="material-symbols-outlined text-[18px]">smart_toy</span>
</div>
<div class="flex flex-col">
<div class="flex items-center gap-space-sm">
<span class="font-headline-panel text-headline-panel text-on-surface">Asset Intelligence Copilot</span>

</div>

</div>
</div>
<div class="flex items-center gap-space-md font-label-mono-tag text-label-mono-tag text-on-surface-variant">
<div class="flex items-center gap-1">
<span class="material-symbols-outlined text-[15px] text-secondary">timer</span>
<span class="">1.3s</span>
</div>
<span class="text-outline-variant">|</span>
<div class="flex items-center gap-1">
<span class="material-symbols-outlined text-[15px] text-primary">schedule</span>
<span class="">14:32:17 UTC</span>
</div>
</div>
</div>
<!-- Executive Synthesis Prose -->
<div class="font-body-prose text-body-prose text-on-surface leading-relaxed">
3 wells in Northeast Block 7 accounted for <span class="font-body-spec-mono font-semibold text-on-surface">133 aggregate days</span> of non-production between 16 Jun and 16 Oct 2026.
<span class="text-error font-semibold font-body-spec-mono">WELL-0121 recorded the maximum downtime at 49 days</span>
(7 shut-in inspection intervals), followed by
<span class="text-primary-container font-semibold font-body-spec-mono">WELL-0138</span> and
<span class="text-primary-container font-semibold font-body-spec-mono">WELL-0107</span> at 42 days each.
</div>
<!-- 3. Specialized Horizontal Bar Chart Card -->
<div class="w-full bg-surface-container rounded-lg border border-outline-variant overflow-hidden flex flex-col">
<!-- Chart Header -->
<div class="flex items-center justify-between px-space-md py-space-sm bg-surface-container-high border-b border-outline-variant">
<div class="flex items-center gap-space-sm">
<span class="material-symbols-outlined text-[18px] text-primary">bar_chart</span>
<span class="font-label-metric text-label-metric text-on-surface uppercase">Northeast Block 7: downtime, 16 Jun to 16 Oct 2026</span>
</div>
<span class="font-label-mono-tag text-[10px] tracking-wider uppercase px-2 py-0.5 rounded bg-surface-container border border-outline-variant text-on-surface-variant">
BAR CHART
</span>
</div>
<!-- Chart Grid Stage -->
<div class="p-space-lg bg-surface-dim relative flex flex-col gap-space-lg">
<!-- Reference Indicator Flag -->
<div class="relative w-full h-5">
<div class="absolute left-[50%] -translate-x-1/2 flex items-center gap-1 px-2 py-0.5 rounded bg-surface-container border border-outline-variant z-10">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary-container"></span>
<span class="font-label-mono-tag text-[11px] text-on-surface-variant whitespace-nowrap">Next best: WELL-0119, 28 d</span>
</div>
</div>
<!-- Chart Area: Rows with absolute reference line behind -->
<div class="relative w-full flex flex-col gap-space-md">
<!-- Gridlines Background -->
<div class="absolute inset-0 flex justify-between pointer-events-none pl-[110px] pr-4">
<!-- 8 vertical grid segments (0 to 56 days) -->
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<!-- 28d reference line (middle) -->
<div class="h-full border-r-2 border-dashed border-tertiary-container/60 relative"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full border-r border-surface-variant/40"></div>
<div class="h-full"></div>
</div>
<!-- ROW 1: WELL-0121 (49d / 56d = 87.5%) -->
<div class="relative flex items-center h-11 z-10">
<div class="w-[110px] shrink-0 flex flex-col justify-center pr-space-sm">
<button class="inline-flex items-center justify-between w-full px-2 py-1 rounded bg-surface-container border border-outline-variant hover:border-primary-container text-primary text-xs font-label-mono-tag transition-colors" title="Inspect WELL-0121" type="button">
<span class="">WELL-0121</span>
<span class="material-symbols-outlined text-[14px]">open_in_new</span>
</button>
<span class="font-label-mono-tag text-[10px] text-outline mt-0.5 pl-1">PUMP // T200</span>
</div>
<div class="flex-1 flex items-center pr-4">
<div class="h-7 rounded-r bg-error border-y border-r border-error/50 flex items-center transition-all duration-500 relative" style="width: 87.5%;">
<div class="absolute right-2 flex items-center gap-2 whitespace-nowrap">
<span class="font-display-telemetry text-sm font-bold text-[#0e141c] tracking-tight">49 d</span>
</div>
</div>
<span class="ml-3 font-label-mono-tag text-[11px] text-error whitespace-nowrap hidden sm:inline-block">7 weekly inspections</span>
</div>
</div>
<!-- ROW 2: WELL-0138 (42d / 56d = 75.0%) -->
<div class="relative flex items-center h-11 z-10">
<div class="w-[110px] shrink-0 flex flex-col justify-center pr-space-sm">
<button class="inline-flex items-center justify-between w-full px-2 py-1 rounded bg-surface-container border border-outline-variant hover:border-primary-container text-primary text-xs font-label-mono-tag transition-colors" title="Inspect WELL-0138" type="button">
<span class="">WELL-0138</span>
<span class="material-symbols-outlined text-[14px]">open_in_new</span>
</button>
<span class="font-label-mono-tag text-[10px] text-outline mt-0.5 pl-1">PUMP // T350</span>
</div>
<div class="flex-1 flex items-center pr-4">
<div class="h-7 rounded-r bg-primary-container border-y border-r border-primary-container/50 flex items-center transition-all duration-500 relative" style="width: 75%;">
<div class="absolute right-2 flex items-center gap-2 whitespace-nowrap">
<span class="font-display-telemetry text-sm font-bold text-on-primary-container tracking-tight">42 d</span>
</div>
</div>
<span class="ml-3 font-label-mono-tag text-[11px] text-primary whitespace-nowrap hidden sm:inline-block">6 weekly inspections</span>
</div>
</div>
<!-- ROW 3: WELL-0107 (42d / 56d = 75.0%) -->
<div class="relative flex items-center h-11 z-10">
<div class="w-[110px] shrink-0 flex flex-col justify-center pr-space-sm">
<button class="inline-flex items-center justify-between w-full px-2 py-1 rounded bg-surface-container border border-outline-variant hover:border-primary-container text-primary text-xs font-label-mono-tag transition-colors" title="Inspect WELL-0107" type="button">
<span class="">WELL-0107</span>
<span class="material-symbols-outlined text-[14px]">open_in_new</span>
</button>
<span class="font-label-mono-tag text-[10px] text-outline mt-0.5 pl-1">PUMP // T350</span>
</div>
<div class="flex-1 flex items-center pr-4">
<div class="h-7 rounded-r bg-primary-container border-y border-r border-primary-container/50 flex items-center transition-all duration-500 relative" style="width: 75%;">
<div class="absolute right-2 flex items-center gap-2 whitespace-nowrap">
<span class="font-display-telemetry text-sm font-bold text-on-primary-container tracking-tight">42 d</span>
</div>
</div>
<span class="ml-3 font-label-mono-tag text-[11px] text-primary whitespace-nowrap hidden sm:inline-block">6 weekly inspections</span>
</div>
</div>
</div>
<!-- X-Axis Scale & Labels -->
<div class="pt-space-xs border-t border-outline-variant/80 pl-[110px] pr-4">
<div class="flex justify-between text-on-surface-variant font-label-mono-tag text-[11px]">
<span class="">0 d</span>
<span class="">7 d</span>
<span class="">14 d</span>
<span class="">21 d</span>
<span class="text-tertiary-container font-semibold">28 d</span>
<span class="">35 d</span>
<span class="">42 d</span>
<span class="text-error font-semibold">49 d</span>
<span class="">56 d</span>
</div>
<div class="text-center font-label-metric text-[11px] text-outline uppercase tracking-wider mt-space-xs">Downtime, days (16 Jun to 16 Oct 2026)</div>
</div>
</div>
<!-- Chart Caption / Context Note -->
<div class="px-space-md py-space-sm bg-surface-container-high/60 border-t border-outline-variant flex items-center gap-space-sm text-on-surface-variant font-body-spec text-xs">
<span class="material-symbols-outlined text-[16px] text-primary shrink-0">info</span>
<span class="">Each inspection that found the well not producing counts as 7 days.</span>
</div>
</div>
<!-- 4. Evidentiary Citations Strip -->
<div class="flex flex-col gap-space-xs pt-space-xs">
<span class="font-label-metric text-[11px] uppercase tracking-wider text-outline">EVIDENTIARY RECORD SOURCES:</span>
<div class="flex flex-wrap gap-2"><span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container border border-outline-variant font-body-spec-mono text-xs text-primary"><span class="material-symbols-outlined text-[14px]">description</span><span class="">INS-0121-001</span></span><span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container border border-outline-variant font-body-spec-mono text-xs text-primary"><span class="material-symbols-outlined text-[14px]">description</span><span class="">INS-0138-001</span></span><span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container border border-outline-variant font-body-spec-mono text-xs text-primary"><span class="material-symbols-outlined text-[14px]">description</span><span class="">INS-0107-001</span></span><span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container border border-outline-variant font-body-spec-mono text-xs text-secondary"><span class="material-symbols-outlined text-[14px]">build</span><span class="">MNT-0107-002</span></span></div>
</div>
<!-- 5. Footer Metadata Line & Audit Actions -->
<div class="flex flex-wrap items-center justify-between gap-space-md pt-space-sm border-t border-outline-variant/60"><span class="font-label-mono-tag text-[11px] text-outline">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div>
<!-- 6. Recommended Next Actions -->

</div>
<div class="w-full bg-surface-container border border-outline-variant rounded-xl p-space-sm flex items-center gap-space-sm"><input type="text" placeholder="Ask about Block 7 (50 wells) or inspection history..." class="flex-1 bg-transparent px-space-sm py-1.5 text-on-surface font-body-spec text-sm focus:outline-none placeholder:text-outline"><button type="button" class="w-9 h-9 rounded bg-primary-container text-on-primary-container flex items-center justify-center hover:opacity-90 transition-opacity shrink-0" title="Send"><span class="material-symbols-outlined text-[18px]">arrow_upward</span></button></div></div>
</div></main></div>

</body></html>
```

10. northeast_block_8_90_day_spills_gis_map
```
<!DOCTYPE html><html class="dark" lang="en" style=""><svg class="inline-defs-container" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden"></svg><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config = { darkMode: "class", theme: { extend: { "colors": { "on-primary-fixed": "#001e2c", "surface-variant": "#2f353e", "on-primary": "#00354a", "primary-fixed-dim": "#7bd0ff", "surface-bright": "#343a42", "primary": "#8ed5ff", "tertiary-fixed-dim": "#ffb2b7", "surface-container-low": "#161c24", "outline-variant": "#3e484f", "surface-dim": "#0e141c", "on-error-container": "#ffdad6", "secondary-container": "#00bd85", "on-error": "#690005", "surface-container": "#1a2028", "on-tertiary-fixed-variant": "#92002a", "secondary-fixed-dim": "#45dfa4", "outline": "#87929a", "secondary-fixed": "#68fcbf", "surface": "#0e141c", "tertiary-fixed": "#ffdadb", "on-secondary": "#003825", "error": "#ffb4ab", "surface-container-highest": "#2f353e", "background": "#0e141c", "on-tertiary-fixed": "#40000d", "inverse-on-surface": "#2b3139", "on-primary-fixed-variant": "#004c69", "on-secondary-fixed-variant": "#005137", "on-secondary-fixed": "#002114", "inverse-primary": "#00668a", "error-container": "#93000a", "surface-container-high": "#242a33", "on-secondary-container": "#00452e", "on-background": "#dde3ee", "tertiary": "#ffbcbf", "on-surface": "#dde3ee", "secondary": "#45dfa4", "on-tertiary": "#67001b", "tertiary-container": "#ff929a", "on-tertiary-container": "#8c0028", "primary-fixed": "#c4e7ff", "primary-container": "#38bdf8", "surface-tint": "#7bd0ff", "inverse-surface": "#dde3ee", "surface-container-lowest": "#090f16", "on-primary-container": "#004965", "on-surface-variant": "#bdc8d1" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-lg": "1.25rem", "space-md": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "gutter": "1.5rem", "space-sm": "0.5rem", "margin": "1.5rem" }, "fontFamily": { "body-spec": [ "IBM Plex Sans" ], "label-mono-tag": [ "IBM Plex Mono" ], "body-prose-medium": [ "IBM Plex Sans" ], "label-metric": [ "IBM Plex Sans" ], "body-spec-mono": [ "IBM Plex Mono" ], "headline-panel": [ "IBM Plex Sans" ], "headline-panel-mobile": [ "IBM Plex Sans" ], "body-prose": [ "IBM Plex Sans" ], "display-telemetry": [ "IBM Plex Mono" ] }, "fontSize": { "body-spec": [ "14px", { "lineHeight": "20px", "fontWeight": "400" } ], "label-mono-tag": [ "12px", { "lineHeight": "16px", "fontWeight": "500" } ], "body-prose-medium": [ "16px", { "lineHeight": "24px", "fontWeight": "500" } ], "label-metric": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "body-spec-mono": [ "14px", { "lineHeight": "20px", "fontWeight": "500" } ], "headline-panel": [ "20px", { "lineHeight": "28px", "letterSpacing": "-0.01em", "fontWeight": "600" } ], "headline-panel-mobile": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ], "body-prose": [ "16px", { "lineHeight": "24px", "fontWeight": "400" } ], "display-telemetry": [ "28px", { "lineHeight": "34px", "letterSpacing": "-0.01em", "fontWeight": "600" } ] } } } };</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface antialiased"><aside class="fixed left-0 top-0 h-full w-64 bg-surface-container-low flex flex-col justify-between py-space-md px-3 z-50 border-r border-surface-container-high"><div class="flex flex-col gap-4"><button class="w-full py-2 px-3 rounded-sm bg-surface-container hover:bg-surface-container-high text-primary border border-outline-variant font-body-spec text-[13px] font-semibold flex items-center justify-center gap-2 transition-colors"><span class="material-symbols-outlined text-[18px]">add</span><span class="">+ New chat</span></button><div class="flex flex-col gap-1"><span class="font-label-metric text-[11px] text-outline uppercase tracking-wider px-2 py-1">Recent chats</span><div class="flex flex-col gap-1"><a href="#" class="px-2.5 py-2 rounded-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-body-spec text-[12px] truncate transition-colors">WELL-0001 status and last inspection</a><a href="#" class="px-2.5 py-2 rounded-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-body-spec text-[12px] truncate transition-colors">Northeast Block 8 not producing</a><a href="#" class="px-2.5 py-2 rounded-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-body-spec text-[12px] truncate transition-colors">Block 7 downtime, top 3</a><a href="#" class="px-2.5 py-2 rounded-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-body-spec text-[12px] truncate transition-colors">WELL-0001 spills, last 4 years</a><a href="#" class="px-2.5 py-2 rounded-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-body-spec text-[12px] truncate transition-colors">Pump jack root-cause wells</a></div></div></div><div class="flex items-center gap-2 px-2 py-2 border-t border-surface-container"><div class="w-7 h-7 rounded bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[16px]">person</span></div><span class="font-body-spec text-[12px] text-on-surface font-medium truncate">Michael Turner</span></div></aside><div class="pl-64 min-h-screen flex flex-col"><header class="fixed top-0 left-64 right-0 h-14 bg-surface-container-lowest/95 backdrop-blur-md z-40 border-b border-surface-container-high"><div class="w-full h-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] text-on-surface font-semibold">Northeast Block 8 - 90-Day Spills</span></div><div class="flex items-center gap-3"><div class="px-2.5 py-1 rounded-sm bg-surface-container border border-outline-variant font-label-mono-tag text-[11px] text-on-surface-variant">Today: 17 Oct 2026</div><div class="flex items-center gap-2 px-2.5 py-1 rounded-sm bg-surface-container border border-outline-variant"><span class="w-2 h-2 rounded-full bg-primary"></span><span class="font-body-spec text-[13px] text-on-surface font-medium">Michael Turner</span></div></div></div></header><main class="w-full pt-14 bg-surface-container-lowest flex-1"><div class="flex flex-col w-full"><div class="w-full max-w-[1440px] mx-auto px-6 py-6 flex flex-col gap-6"><!-- Main Chat Workspace Stream (Dual Alignment Layout) --><div class="w-full flex flex-col items-center"><div class="w-full max-w-[880px] flex flex-col gap-5"><!-- 1. Operator Query Plate (Aligned Right) --><div class="w-full flex justify-end"><div class="w-full max-w-[660px] bg-surface-container p-4 rounded-xl flex flex-col gap-2.5"><div class="flex items-center justify-between font-label-mono-tag text-label-mono-tag text-on-surface-variant"><div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">person</span><span class="text-primary font-medium tracking-wide">OPERATOR QUERY // CREW-A</span><span class="">CONSOLE-04</span></div><span class="text-outline">14:33:10 UTC</span></div><p class="font-body-spec text-body-spec text-on-surface text-[15px] leading-relaxed">Show on a map every well in Northeast Block 8 with a real spill in the last 90 days.</p><div class="flex items-center gap-2 pt-1"><span class="px-2 py-0.5 rounded-sm bg-primary/10 text-primary font-label-mono-tag text-[11px] tracking-wide">#NE-BLOCK-8</span><span class="px-2 py-0.5 rounded-sm bg-primary/10 text-primary font-label-mono-tag text-[11px] tracking-wide">#SPILL-MONITOR</span></div></div></div><!-- 2. Assistant Message Container --><div class="w-full bg-surface-container-low rounded-sm relative pl-0.5"><div class="absolute left-0 top-0 bottom-0 w-0.5 bg-primary-container"></div><div class="p-5 flex flex-col gap-4"><!-- Assistant Header --><div class="flex items-start justify-between pb-3"><div class="flex items-center gap-3"><div class="w-8 h-8 rounded-sm bg-surface-container-high flex items-center justify-center text-primary"><span class="material-symbols-outlined text-[18px]">smart_toy</span></div><div class="flex flex-col"><div class="flex items-center gap-2"><span class="font-headline-panel text-headline-panel text-[16px] text-on-surface">Asset Intelligence Copilot</span><span class="px-2 py-0.5 rounded-sm bg-surface-container-highest text-primary font-label-mono-tag text-[10px] tracking-wider uppercase">INCIDENT GEOSPATIAL // SPILL EVENT MAPPING</span></div><span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant text-[11px]">WEEKLY INSPECTIONS · SECTOR 08 NORTH</span></div></div><div class="flex items-center gap-3 font-label-mono-tag text-label-mono-tag text-outline text-[11px]"><span class="flex items-center gap-1"><span class="material-symbols-outlined text-[14px] text-secondary">speed</span><span class="">1.4s</span></span><span class="">•</span><span class="">14:33:12 UTC</span></div></div><!-- Lead Diagnostic Text --><div class="font-body-prose text-body-prose text-on-surface text-[15px] leading-[1.58] max-w-prose"><p class="">4 verified containment breaches were logged across Northeast Block 8 within the 90-day inspection window (18 Jul to 16 Oct 2026), totaling <strong class="text-on-surface font-semibold underline decoration-primary/40 decoration-1 underline-offset-2">10.2 bbl</strong> of liquid hydrocarbons. <strong class="text-error font-semibold">WELL-0151 accounted for the single critical discharge of 4.5 bbl</strong> on 24 Sep 2026.</p></div><!-- Summary Telemetry Readouts Bar (Without remediation card, 3 columns) --><div class="grid grid-cols-3 gap-3 py-1"><div class="bg-surface-container p-2.5 rounded-sm flex flex-col"><span class="font-label-metric text-[11px] text-on-surface-variant uppercase tracking-wider">TOTAL INCIDENTS</span><span class="font-display-telemetry text-display-telemetry text-[22px] text-on-surface mt-0.5">04</span><span class="font-label-mono-tag text-[10px] text-outline mt-0.5">100% CADASTRE MATCH</span></div><div class="bg-surface-container p-2.5 rounded-sm flex flex-col"><span class="font-label-metric text-[11px] text-on-surface-variant uppercase tracking-wider">DISCHARGED HYDROCARBONS</span><div class="flex items-baseline gap-1 mt-0.5"><span class="font-display-telemetry text-display-telemetry text-[22px] text-on-surface">10.2</span><span class="font-body-spec-mono text-body-spec-mono text-[12px] text-outline">bbl</span></div><span class="font-label-mono-tag text-[10px] text-error mt-0.5">TOTAL LOGGED</span></div><div class="bg-surface-container p-2.5 rounded-sm flex flex-col"><span class="font-label-metric text-[11px] text-on-surface-variant uppercase tracking-wider">CRITICAL EXCEEDANCES</span><span class="font-display-telemetry text-display-telemetry text-[22px] text-error mt-0.5">01</span><span class="font-label-mono-tag text-[10px] text-error mt-0.5">WELL-0151 (ACTIVE)</span></div></div><!-- Interactive Map Card Container --><div class="w-full bg-surface-container-lowest rounded-sm overflow-hidden flex flex-col"><div class="px-3.5 py-2.5 bg-surface-container flex items-center justify-between"><div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-error">warning</span><span class="font-body-prose-medium text-[13px] text-on-surface tracking-wide">Northeast Block 8: spills, last 90 days, to 17 Oct 2026</span></div><div class="flex items-center gap-2"><span class="px-2 py-0.5 bg-surface-container-high rounded-sm font-label-mono-tag text-[11px] text-primary">MAP — 4 pins</span></div></div><div class="relative w-full h-[380px] bg-[#0b0f14] overflow-hidden select-none" id="tactical-spill-map"><svg class="absolute inset-0 w-full h-full pointer-events-none opacity-90" xmlns="http://www.w3.org/2000/svg"><defs><pattern height="80" id="cadastral-grid" patternUnits="userSpaceOnUse" width="80"><path d="M 80 0 L 0 0 0 80" fill="none" stroke="#161f2b" stroke-dasharray="2 3" stroke-width="0.75"></path><circle cx="80" cy="0" fill="#263140" r="1.5"></circle></pattern><pattern height="240" id="block-subdivision" patternUnits="userSpaceOnUse" width="240"><rect fill="none" height="240" stroke="#1e2a3a" stroke-width="1.25" width="240"></rect></pattern></defs><rect fill="#0b0f14" height="100%" width="100%"></rect><rect fill="url(#cadastral-grid)" height="100%" width="100%"></rect><rect fill="url(#block-subdivision)" height="100%" width="100%"></rect><path d="M-20,120 Q180,140 320,110 T640,160 T920,130" fill="none" stroke="#17222f" stroke-linecap="round" stroke-width="2.5"></path><path d="M320,0 L340,380" fill="none" stroke="#17222f" stroke-dasharray="6 4" stroke-width="1.5"></path><path d="M680,0 L660,380" fill="none" stroke="#17222f" stroke-width="1.5"></path><path d="M110,380 L180,0" fill="none" stroke="#141c26" stroke-width="1.25"></path><path d="M0,280 L880,310" fill="none" stroke="#162230" stroke-width="1.5"></path><polygon fill="#38bdf8" fill-opacity="0.015" points="120,40 820,35 840,350 140,355" stroke="#38bdf8" stroke-dasharray="4 4" stroke-opacity="0.25" stroke-width="1"></polygon><text fill="#38bdf8" fill-opacity="0.45" font-family="IBM Plex Mono" font-size="10px" font-weight="600" letter-spacing="1" x="145" y="60">CADASTRAL ZONE // BLOCK 8</text><path d="M190,40 Q220,160 210,240 T270,360" fill="none" stroke="#004965" stroke-dasharray="3 3" stroke-width="1.25"></path><text fill="#004965" font-family="IBM Plex Mono" font-size="9px" x="215" y="340">TRIBUTARY RUNOFF CORRIDOR</text></svg><div class="absolute top-1 left-28 font-label-mono-tag text-[9px] text-outline font-medium">32.18° N</div><div class="absolute top-1 left-1/2 -translate-x-1/2 font-label-mono-tag text-[9px] text-outline font-medium">32.15° N</div><div class="absolute top-1 right-28 font-label-mono-tag text-[9px] text-outline font-medium">32.12° N</div><div class="absolute bottom-1.5 left-28 font-label-mono-tag text-[9px] text-outline font-medium">-102.18° W</div><div class="absolute bottom-1.5 left-1/2 -translate-x-1/2 font-label-mono-tag text-[9px] text-outline font-medium">-102.1638° W (CTR)</div><div class="absolute bottom-1.5 right-28 font-label-mono-tag text-[9px] text-outline font-medium">-102.15° W</div><div class="absolute left-1 top-24 font-label-mono-tag text-[9px] text-outline">32.17° N</div><div class="absolute left-1 top-64 font-label-mono-tag text-[9px] text-outline">32.13° N</div><div class="absolute top-3 left-3 flex items-center gap-2 z-20"><div class="bg-surface-container-high/90 backdrop-blur px-2.5 py-1 rounded-sm flex items-center gap-1.5 font-label-mono-tag text-[10px] text-on-surface"><span class="w-1.5 h-1.5 rounded-full bg-primary animate-pulse"></span><span class="">BASE: DARK VECTOR</span><span class="text-surface-variant">|</span><span class="text-on-surface-variant">GRID: O&amp;G BLK 8</span></div></div><div class="absolute top-3 right-3 flex items-center gap-2 z-20"><div class="w-7 h-7 rounded-sm bg-surface-container-high/90 backdrop-blur flex items-center justify-center font-label-mono-tag text-on-surface text-[11px] font-bold" title="True North"><span class="text-error text-[10px]">▲</span><span class="text-[9px] -ml-0.5">N</span></div><div class="flex flex-col bg-surface-container-high/90 backdrop-blur rounded-sm overflow-hidden"><button class="w-7 h-7 flex items-center justify-center text-on-surface hover:bg-surface-container-highest transition-colors active:text-primary" title="Zoom in"><span class="material-symbols-outlined text-[15px]">add</span></button><div class="w-full h-px bg-surface-container"></div><button class="w-7 h-7 flex items-center justify-center text-on-surface hover:bg-surface-container-highest transition-colors active:text-primary" title="Zoom out"><span class="material-symbols-outlined text-[15px]">remove</span></button><div class="w-full h-px bg-surface-container"></div><button class="w-7 h-7 flex items-center justify-center text-on-surface-variant hover:bg-surface-container-highest transition-colors" title="Reset extent"><span class="material-symbols-outlined text-[14px]">filter_center_focus</span></button></div></div><div class="absolute bottom-3 right-3 z-20 bg-surface-container-lowest/80 backdrop-blur px-2 py-1 rounded-sm flex flex-col items-end gap-0.5"><span class="font-label-mono-tag text-[9px] text-on-surface-variant">1 km / 0.62 mi</span><div class="flex items-center"><div class="w-1 h-1.5 bg-outline"></div><div class="w-16 h-0.5 bg-outline"></div><div class="w-1 h-1.5 bg-outline"></div></div></div><div class="absolute left-[215px] top-[105px] z-10 group cursor-pointer" title="WELL-0186 (0.6 bbl)"><div class="relative flex items-center justify-center"><span class="absolute w-6 h-6 rounded-full bg-slate-400/20 animate-ping opacity-30"></span><div class="w-5 h-5 rounded-full bg-[#94A3B8] p-0.5 shadow-none flex items-center justify-center"><div class="w-2.5 h-2.5 rounded-full bg-surface-container-lowest"></div></div></div><div class="absolute left-6 -top-1 bg-surface-container-lowest/90 px-1.5 py-0.5 rounded-sm font-label-mono-tag text-[9px] text-slate-300 pointer-events-none whitespace-nowrap">WELL-0186 <span class="text-outline">0.6 bbl</span></div></div><div class="absolute left-[620px] top-[80px] z-10 group cursor-pointer" title="WELL-0175 (3.9 bbl)"><div class="relative flex items-center justify-center"><span class="absolute w-8 h-8 rounded-full bg-amber-400/20 animate-pulse"></span><div class="w-7 h-7 rounded-full bg-[#FBBF24] p-0.5 shadow-none flex items-center justify-center"><div class="w-3.5 h-3.5 rounded-full bg-surface-container-lowest flex items-center justify-center"><span class="w-1.5 h-1.5 rounded-full bg-[#FBBF24]"></span></div></div></div><div class="absolute left-8 -top-1 bg-surface-container-lowest/90 px-1.5 py-0.5 rounded-sm font-label-mono-tag text-[9px] text-[#FBBF24] pointer-events-none whitespace-nowrap">WELL-0175 <span class="text-on-surface">3.9 bbl</span></div></div><div class="absolute left-[670px] top-[190px] z-10 group cursor-pointer" title="WELL-0165 (1.2 bbl)"><div class="relative flex items-center justify-center"><div class="w-6 h-6 rounded-full bg-[#FBBF24] p-0.5 shadow-none flex items-center justify-center"><div class="w-3 h-3 rounded-full bg-surface-container-lowest flex items-center justify-center"><span class="w-1 h-1 rounded-full bg-[#FBBF24]"></span></div></div></div><div class="absolute left-7 -top-1 bg-surface-container-lowest/90 px-1.5 py-0.5 rounded-sm font-label-mono-tag text-[9px] text-[#FBBF24] pointer-events-none whitespace-nowrap">WELL-0165 <span class="text-on-surface">1.2 bbl</span></div></div><div class="absolute left-[230px] top-[250px] z-30"><div class="relative flex items-center justify-center"><span class="absolute w-12 h-12 rounded-full bg-error/25 animate-ping opacity-40"></span><span class="absolute w-9 h-9 rounded-full bg-error/30 animate-pulse"></span><div class="w-8 h-8 rounded-full bg-error p-0.5 flex items-center justify-center cursor-pointer"><div class="w-4 h-4 rounded-full bg-surface-container-lowest flex items-center justify-center"><span class="w-2 h-2 rounded-full bg-error"></span></div></div></div><div class="absolute bottom-10 left-1/2 -translate-x-1/2 w-72 bg-[#161e27] rounded-sm p-3 z-40"><div class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-[#161e27] rotate-45"></div><div class="flex flex-col gap-2 relative z-10"><div class="flex items-center justify-between"><div class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-error"></span><span class="font-label-mono-tag text-label-mono-tag font-semibold text-primary">WELL-0151</span></div><span class="px-1.5 py-0.5 rounded-sm bg-error-container/40 text-error font-label-mono-tag text-[9px] tracking-wider font-semibold">DISCHARGE ACTIVE</span></div><div class="flex items-baseline justify-between pt-0.5"><div class="flex items-baseline gap-1"><span class="font-display-telemetry text-display-telemetry text-[20px] text-on-surface">4.5</span><span class="font-label-mono-tag text-[12px] text-error font-semibold">bbl</span></div><span class="font-label-mono-tag text-[11px] text-on-surface-variant">24 Sep 2026</span></div><div class="font-body-spec text-[12px] text-on-surface-variant leading-tight">Inspection record logged.</div><div class="pt-1.5 flex items-center justify-between"><span class="font-label-mono-tag text-[10px] text-outline">REF: INS-0151-0924</span><a class="inline-flex items-center gap-1 font-label-mono-tag text-[11px] text-primary hover:text-primary-fixed transition-colors font-medium" href="#"><span class="">Open well</span><span class="material-symbols-outlined text-[14px]">arrow_forward</span></a></div></div></div></div><div class="absolute bottom-3 left-3 z-20 bg-surface-container-lowest/90 backdrop-blur p-2.5 rounded-sm"><div class="font-label-mono-tag text-[11px] text-on-surface-variant uppercase tracking-wider">pin color = spill size</div></div></div></div><!-- Evidentiary Sources Strip (Record IDs only, mono, with kind icon) --><div class="flex flex-col gap-2 pt-1"><div class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-primary">description</span><span class="font-label-metric text-label-metric text-[11px] text-on-surface-variant tracking-wider uppercase">SOURCES</span></div><div class="flex flex-wrap items-center gap-2"><a class="px-2.5 py-1 rounded-sm bg-primary/10 hover:bg-primary/20 text-primary font-body-spec-mono text-[11px] flex items-center gap-1.5 transition-colors" href="#"><span class="material-symbols-outlined text-[14px] text-error">assignment</span><span class="">INS-0151-0924</span></a><a class="px-2.5 py-1 rounded-sm bg-primary/10 hover:bg-primary/20 text-primary font-body-spec-mono text-[11px] flex items-center gap-1.5 transition-colors" href="#"><span class="material-symbols-outlined text-[14px] text-amber-400">assignment</span><span class="">INS-0175-0730</span></a><a class="px-2.5 py-1 rounded-sm bg-primary/10 hover:bg-primary/20 text-primary font-body-spec-mono text-[11px] flex items-center gap-1.5 transition-colors" href="#"><span class="material-symbols-outlined text-[14px] text-amber-400">assignment</span><span class="">INS-0165-0730</span></a><a class="px-2.5 py-1 rounded-sm bg-primary/10 hover:bg-primary/20 text-primary font-body-spec-mono text-[11px] flex items-center gap-1.5 transition-colors" href="#"><span class="material-symbols-outlined text-[14px] text-slate-400">assignment</span><span class="">INS-0186-0723</span></a></div></div><!-- Assistant Footer Telemetry: EXACTLY 'gemma-4-26b-a4b-it - 1.4 s - tools: well_status' --><div class="pt-3 flex items-center justify-between font-label-mono-tag text-label-mono-tag text-[11px] text-outline"><div class="flex items-center gap-2"><span class="">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div><div class="flex items-center gap-1 text-on-surface-variant"><button class="p-1 rounded-sm hover:bg-surface-container hover:text-on-surface transition-colors" title="Copy response markdown"><span class="material-symbols-outlined text-[16px]">content_copy</span></button><button class="p-1 rounded-sm hover:bg-surface-container hover:text-secondary transition-colors" title="Accurate data"><span class="material-symbols-outlined text-[16px]">thumb_up</span></button><button class="p-1 rounded-sm hover:bg-surface-container hover:text-error transition-colors" title="Inaccurate telemetry"><span class="material-symbols-outlined text-[16px]">thumb_down</span></button></div></div></div></div><!-- 3. Interactive Command / Prompt Input Terminal Bar (Send button cyan arrow icon only; removed CONSOLE READY / SQL SYNTHESIS) --><div class="w-full bg-surface-container-low p-3 rounded-sm flex flex-col gap-2 mt-2"><div class="flex items-center gap-2"><div class="flex-1 bg-surface-container h-11 rounded-sm px-3 flex items-center gap-2.5 focus-within:ring-1 focus-within:ring-primary transition-all"><span class="material-symbols-outlined text-[18px] text-primary">terminal</span><input class="w-full bg-transparent border-none text-on-surface font-body-spec text-[13px] placeholder:text-outline focus:outline-none" placeholder="Inquire about wells, inspection records, or past incidents..." type="text"><button class="text-outline hover:text-on-surface transition-colors" title="Attach"><span class="material-symbols-outlined text-[18px]">attachment</span></button></div><button class="h-11 px-3 bg-primary-container text-on-primary-container rounded-sm flex items-center justify-center hover:bg-primary transition-colors active:scale-[0.99]" title="Send"><span class="material-symbols-outlined text-[20px]">arrow_upward</span></button></div></div></div></div></div></div></main></div>

</body></html>
```

11. northeast_block_8_non_producing_wells_table
```
<!DOCTYPE html><html class="dark" lang="en"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config = { darkMode: "class", theme: { extend: { "colors": { "on-primary-fixed": "#001e2c", "surface-variant": "#2f353e", "on-primary": "#00354a", "primary-fixed-dim": "#7bd0ff", "surface-bright": "#343a42", "primary": "#8ed5ff", "tertiary-fixed-dim": "#ffb2b7", "surface-container-low": "#161c24", "outline-variant": "#3e484f", "surface-dim": "#0e141c", "on-error-container": "#ffdad6", "secondary-container": "#00bd85", "on-error": "#690005", "surface-container": "#1a2028", "on-tertiary-fixed-variant": "#92002a", "secondary-fixed-dim": "#45dfa4", "outline": "#87929a", "secondary-fixed": "#68fcbf", "surface": "#0e141c", "tertiary-fixed": "#ffdadb", "on-secondary": "#003825", "error": "#ffb4ab", "surface-container-highest": "#2f353e", "background": "#0e141c", "on-tertiary-fixed": "#40000d", "inverse-on-surface": "#2b3139", "on-primary-fixed-variant": "#004c69", "on-secondary-fixed-variant": "#005137", "on-secondary-fixed": "#002114", "inverse-primary": "#00668a", "error-container": "#93000a", "surface-container-high": "#242a33", "on-secondary-container": "#00452e", "on-background": "#dde3ee", "tertiary": "#ffbcbf", "on-surface": "#dde3ee", "secondary": "#45dfa4", "on-tertiary": "#67001b", "tertiary-container": "#ff929a", "on-tertiary-container": "#8c0028", "primary-fixed": "#c4e7ff", "primary-container": "#38bdf8", "surface-tint": "#7bd0ff", "inverse-surface": "#dde3ee", "surface-container-lowest": "#090f16", "on-primary-container": "#004965", "on-surface-variant": "#bdc8d1" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-lg": "1.25rem", "space-md": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "gutter": "1.5rem", "space-sm": "0.5rem", "margin": "1.5rem" }, "fontFamily": { "body-spec": [ "IBM Plex Sans" ], "label-mono-tag": [ "IBM Plex Mono" ], "body-prose-medium": [ "IBM Plex Sans" ], "label-metric": [ "IBM Plex Sans" ], "body-spec-mono": [ "IBM Plex Mono" ], "headline-panel": [ "IBM Plex Sans" ], "headline-panel-mobile": [ "IBM Plex Sans" ], "body-prose": [ "IBM Plex Sans" ], "display-telemetry": [ "IBM Plex Mono" ] }, "fontSize": { "body-spec": [ "14px", { "lineHeight": "20px", "fontWeight": "400" } ], "label-mono-tag": [ "12px", { "lineHeight": "16px", "fontWeight": "500" } ], "body-prose-medium": [ "16px", { "lineHeight": "24px", "fontWeight": "500" } ], "label-metric": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "body-spec-mono": [ "14px", { "lineHeight": "20px", "fontWeight": "500" } ], "headline-panel": [ "20px", { "lineHeight": "28px", "letterSpacing": "-0.01em", "fontWeight": "600" } ], "headline-panel-mobile": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ], "body-prose": [ "16px", { "lineHeight": "24px", "fontWeight": "400" } ], "display-telemetry": [ "28px", { "lineHeight": "34px", "letterSpacing": "-0.01em", "fontWeight": "600" } ] } } } };</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface antialiased"><aside class="fixed left-0 top-0 h-full bg-surface-container-low flex flex-col items-center justify-between py-space-md z-50 border-r border-surface-container-high" style="width: 260px;"><div class="flex flex-col w-full px-3 gap-space-md flex-1 overflow-hidden"><div class="flex items-center gap-2 py-1"><div class="w-8 h-8 rounded bg-surface-container flex items-center justify-center border border-outline-variant text-primary flex-shrink-0"><span class="material-symbols-outlined text-[18px]">terminal</span></div><span class="font-label-mono-tag text-xs font-semibold text-primary uppercase tracking-wider">ASSET INTEL</span></div><button class="w-full py-2 px-3 rounded bg-primary text-on-primary font-body-spec text-xs font-semibold flex items-center justify-center gap-1.5 hover:bg-primary-container transition-colors" type="button"><span class="material-symbols-outlined text-[16px]">add</span><span class="">+ New chat</span></button><div class="flex flex-col gap-1 w-full mt-2 overflow-hidden flex-1"><div class="font-label-mono-tag text-[11px] text-outline uppercase tracking-wider px-1 pb-1 font-semibold">Recent chats</div><div class="flex flex-col gap-0.5 overflow-y-auto w-full"><a class="px-2 py-1.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-spec text-[12px] truncate transition-colors" href="#" title="WELL-0001 status and last inspection">WELL-0001 status and last inspection</a><a class="px-2 py-1.5 rounded bg-surface-container text-primary font-body-spec text-[12px] font-medium truncate transition-colors border-l-2 border-primary" href="#" title="Northeast Block 8 not producing">Northeast Block 8 not producing</a><a class="px-2 py-1.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-spec text-[12px] truncate transition-colors" href="#" title="Block 7 downtime, top 3">Block 7 downtime, top 3</a><a class="px-2 py-1.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-spec text-[12px] truncate transition-colors" href="#" title="WELL-0001 spills, last 4 years">WELL-0001 spills, last 4 years</a><a class="px-2 py-1.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-spec text-[12px] truncate transition-colors" href="#" title="Pump jack root-cause wells">Pump jack root-cause wells</a></div></div></div><div class="flex items-center justify-between px-3 pt-2 border-t border-surface-container-high w-full"><div class="flex items-center gap-2"><div class="w-7 h-7 rounded-full bg-primary flex items-center justify-center text-on-primary text-xs font-semibold"><span class="material-symbols-outlined text-[15px]">person</span></div><span class="font-body-spec text-xs text-on-surface truncate">Michael Turner</span></div><div class="text-on-surface-variant hover:text-on-surface cursor-pointer"><span class="material-symbols-outlined text-[18px]">help_center</span></div></div></aside><div class="pl-16 min-h-screen flex flex-col" style="padding-left: 260px;"><header class="fixed top-0 left-16 right-0 h-14 bg-surface-container-lowest/95 backdrop-blur-md z-40 border-b border-surface-container-high" style="left: 260px;"><div class="w-full h-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] font-semibold text-on-surface">Northeast Block 8 - Non-Producing Wells</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-space-sm py-1 rounded bg-surface-container border border-outline-variant/60 font-label-mono-tag text-xs text-on-surface-variant"><span class="material-symbols-outlined text-[15px] text-primary">calendar_today</span><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-1.5 px-space-sm py-1 rounded bg-surface-container border border-outline-variant/60 font-body-spec text-xs text-on-surface"><div class="w-5 h-5 rounded-full bg-primary flex items-center justify-center text-on-primary text-[11px] font-semibold"><span class="material-symbols-outlined text-[13px]">person</span></div><span class="font-medium">Michael Turner</span></div></div></div></header><main class="w-full pt-14 bg-surface-container-lowest flex-1"><div class="max-w-[880px] mx-auto px-space-md py-space-xl"><div class="flex flex-col w-full max-w-[880px] mx-auto space-y-space-lg text-on-surface">
<!-- TOP BREADCRUMB / SPECIFICATION BANNER -->

<!-- OPERATOR QUERY PLATE (USER PROMPT) -->
<div class="flex justify-end w-full">
<div class="w-full max-w-[620px] bg-surface-container rounded-lg border border-outline-variant/60 p-space-md flex flex-col gap-space-xs">
<div class="flex items-center justify-between border-b border-surface-container-high pb-1.5 mb-1">
<div class="flex items-center gap-1.5 text-primary">
<span class="material-symbols-outlined text-[16px]">account_circle</span>
<span class="font-label-mono-tag text-label-mono-tag tracking-wider uppercase font-semibold text-primary">OPERATOR QUERY // CREW-A</span>
</div>
<span class="font-label-mono-tag text-[11px] text-on-surface-variant tracking-wider">14:29:40 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface font-medium leading-relaxed">
Which wells in Northeast Block 8 are not producing oil right now, and why?
</p>
</div>
</div>
<!-- ASSISTANT MESSAGE REPORT BLOCK (AI RESPONSE) -->
<article class="w-full bg-surface-container-low rounded-lg border border-outline-variant/60 border-l-2 border-l-primary-container p-space-lg flex flex-col gap-space-lg relative">
<!-- ASSISTANT HEADER METADATA -->
<header class="flex flex-wrap items-center justify-between gap-y-2 border-b border-surface-container-high pb-space-sm"><div class="flex items-center gap-space-sm"><div class="w-6 h-6 rounded bg-primary-container/10 border border-primary-container/40 flex items-center justify-center text-primary-container"><span class="material-symbols-outlined text-[16px]">neurology</span></div><div class="flex items-center gap-2"><span class="font-headline-panel text-[15px] font-semibold tracking-tight text-on-surface">Asset Intelligence Copilot</span><span class="font-label-mono-tag text-[11px] text-primary tracking-widest uppercase bg-surface-container px-1.5 py-0.5 rounded border border-outline-variant/40">INSPECTION SYNTHESIS</span></div></div><div class="flex items-center gap-space-md font-label-mono-tag text-[11px] text-on-surface-variant"><span class="flex items-center gap-1"><span class="material-symbols-outlined text-[13px] text-primary">timer</span>LATENCY: 1.4s</span><span class="text-outline-variant">|</span><span class="">14:29:42 UTC</span></div></header>
<!-- EXECUTIVE SUMMARY SYNTHESIS -->
<div class="flex flex-col gap-space-xs text-on-surface"><p class="font-body-prose text-body-prose leading-relaxed"><strong class="font-semibold text-error">4 of 50 wells in Northeast Block 8</strong> are currently shut in or failing to produce oil. Wellhead temperatures are significantly depressed below baseline operational thresholds (<span class="font-label-mono-tag text-primary-container font-semibold">0.4 °C – 5.7 °C</span> above ambient air). <span class="text-tertiary font-medium">3 wells</span> carry unconfirmed active statuses conflicting with weekly inspection logs, and <span class="text-on-surface-variant">2 wells lack recorded maintenance work orders</span>.</p></div>
<!-- DATA TABLE EMBEDDED CARD -->
<section class="w-full bg-surface-container-lowest rounded-md border border-outline-variant/50 overflow-hidden flex flex-col">
<!-- CARD SUB-HEADER -->
<div class="bg-surface-container px-space-md py-space-sm border-b border-surface-container-high flex items-center justify-between">
<div class="flex items-center gap-space-sm">
<span class="material-symbols-outlined text-[18px] text-tertiary">error</span>
<h2 class="font-body-spec-mono text-body-spec-mono font-semibold text-on-surface">
Northeast Block 8: not producing oil, 15 Oct 2026
</h2>
</div>
<div class="font-label-mono-tag text-label-mono-tag text-on-surface-variant uppercase tracking-wider bg-surface-container-low px-2 py-0.5 rounded border border-outline-variant/50">
TABLE — 4 ROWS
</div>
</div>
<!-- INTERACTIVE DATA TABLE -->
<div class="w-full overflow-x-auto">
<table class="w-full text-left border-collapse" id="telemetry-table">
<thead>
<tr class="bg-surface-container border-b border-surface-container-high font-label-mono-tag text-label-mono-tag text-on-surface-variant select-none">
<th class="py-2.5 px-4 font-semibold tracking-wider text-left cursor-pointer hover:text-on-surface transition-colors" onclick="sortTable(0)" scope="col">
<div class="flex items-center gap-1.5">
<span class="">WELL</span>
<span class="material-symbols-outlined text-[14px] text-outline">unfold_more</span>
</div>
</th>
<th class="py-2.5 px-4 font-semibold tracking-wider text-right cursor-pointer hover:text-on-surface transition-colors" onclick="sortTable(1, true)" scope="col">
<div class="flex items-center justify-end gap-1.5">
<span class="">WELLHEAD ABOVE AIR</span>
<span class="material-symbols-outlined text-[14px] text-outline">unfold_more</span>
</div>
</th>
<th class="py-2.5 px-4 font-semibold tracking-wider text-left cursor-pointer hover:text-on-surface transition-colors" onclick="sortTable(2)" scope="col">
<div class="flex items-center gap-1.5">
<span class="">RECORDED STATUS</span>
<span class="material-symbols-outlined text-[14px] text-outline">unfold_more</span>
</div>
</th>
<th class="py-2.5 px-4 font-semibold tracking-wider text-left" scope="col">
<span class="">REASON / EVIDENCE NOTES</span>
</th>
</tr>
</thead>
<tbody class="font-body-spec text-body-spec text-on-surface divide-y divide-surface-container-high/80">
<!-- ROW 1 -->
<tr class="hover:bg-surface-container/50 transition-colors group">
<td class="py-3 px-4 whitespace-nowrap align-middle">
<a class="font-label-mono-tag text-xs font-semibold px-2 py-1 rounded bg-surface-container border border-primary/40 text-primary hover:border-primary transition-colors inline-flex items-center gap-1" href="#well-0164">
<span class="material-symbols-outlined text-[12px]">precision_manufacturing</span>
WELL-0164
</a>
</td>
<td class="py-3 px-4 text-right align-middle whitespace-nowrap">
<div class="inline-flex items-center gap-1 font-label-mono-tag text-xs font-semibold text-tertiary">
<span class="material-symbols-outlined text-[13px] text-tertiary">arrow_downward</span>
<span class="tabular-nums">4.1 °C</span>
</div>
</td>
<td class="py-3 px-4 whitespace-nowrap align-middle">
<span class="font-label-mono-tag text-[11px] font-medium tracking-wide text-primary-container px-2 py-0.5 rounded border border-dashed border-primary-container/80 bg-primary-container/10 inline-flex items-center gap-1">
<span class="material-symbols-outlined text-[13px]">help</span>
active (out of date)
</span>
</td>
<td class="py-3 px-4 align-middle font-body-spec text-[13px] text-on-surface-variant leading-snug">
<span class="italic inline-flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[14px] text-primary-container">help_outline</span>
No recorded reason.
</span>
<span class="ml-1">Inspector noted <span class="font-label-mono-tag text-on-surface font-medium not-italic px-1 py-0.5 rounded bg-surface-container border border-outline-variant/40">‘Pump jack not moving.’</span></span>
<a class="ml-2 inline-flex items-center gap-0.5 text-primary hover:underline font-label-mono-tag text-xs whitespace-nowrap" href="#dispatch-0164">
<span class="">Suggest field check</span>
<span class="material-symbols-outlined text-[13px]">arrow_right_alt</span>
</a>
</td>
</tr>
<!-- ROW 2 -->
<tr class="hover:bg-surface-container/50 transition-colors group">
<td class="py-3 px-4 whitespace-nowrap align-middle">
<a class="font-label-mono-tag text-xs font-semibold px-2 py-1 rounded bg-surface-container border border-primary/40 text-primary hover:border-primary transition-colors inline-flex items-center gap-1" href="#well-0170">
<span class="material-symbols-outlined text-[12px]">precision_manufacturing</span>
WELL-0170
</a>
</td>
<td class="py-3 px-4 text-right align-middle whitespace-nowrap">
<div class="inline-flex items-center gap-1 font-label-mono-tag text-xs font-semibold text-error">
<span class="material-symbols-outlined text-[13px] text-error">arrow_downward</span>
<span class="tabular-nums">2.9 °C</span>
</div>
</td>
<td class="py-3 px-4 whitespace-nowrap align-middle">
<span class="font-label-mono-tag text-[11px] font-medium tracking-wide text-error px-2 py-0.5 rounded border border-error bg-error/10 inline-flex items-center gap-1">
<span class="material-symbols-outlined text-[13px]">pause_circle</span>
down
</span>
</td>
<td class="py-3 px-4 align-middle font-body-spec text-[13px] text-on-surface leading-snug">
<span class="">Repair</span>
<a class="font-label-mono-tag text-xs text-primary px-1.5 py-0.5 rounded bg-surface-container border border-primary/30 mx-1 inline-flex items-center gap-0.5 hover:border-primary transition-colors" href="#ticket-mnt-0170-031">
MNT-0170-031
</a>,
<span class="text-on-surface-variant">pump jack walking beam bearing wear, started</span>
<span class="font-label-mono-tag text-xs text-on-surface font-semibold ml-1">19 Sep</span>,
<span class="text-tertiary font-semibold ml-1 inline-flex items-center gap-0.5">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary"></span>
still open
</span>.
</td>
</tr>
<!-- ROW 3 -->
<tr class="hover:bg-surface-container/50 transition-colors group">
<td class="py-3 px-4 whitespace-nowrap align-middle">
<a class="font-label-mono-tag text-xs font-semibold px-2 py-1 rounded bg-surface-container border border-primary/40 text-primary hover:border-primary transition-colors inline-flex items-center gap-1" href="#well-0172">
<span class="material-symbols-outlined text-[12px]">precision_manufacturing</span>
WELL-0172
</a>
</td>
<td class="py-3 px-4 text-right align-middle whitespace-nowrap">
<div class="inline-flex items-center gap-1 font-label-mono-tag text-xs font-semibold text-tertiary">
<span class="material-symbols-outlined text-[13px] text-tertiary">arrow_downward</span>
<span class="tabular-nums">5.7 °C</span>
</div>
</td>
<td class="py-3 px-4 whitespace-nowrap align-middle">
<span class="font-label-mono-tag text-[11px] font-medium tracking-wide text-primary-container px-2 py-0.5 rounded border border-dashed border-primary-container/80 bg-primary-container/10 inline-flex items-center gap-1">
<span class="material-symbols-outlined text-[13px]">help</span>
active (out of date)
</span>
</td>
<td class="py-3 px-4 align-middle font-body-spec text-[13px] text-on-surface leading-snug">
<span class="">Repair</span>
<a class="font-label-mono-tag text-xs text-primary px-1.5 py-0.5 rounded bg-surface-container border border-primary/30 mx-1 inline-flex items-center gap-0.5 hover:border-primary transition-colors" href="#ticket-mnt-0172-028">
MNT-0172-028
</a>,
<span class="text-on-surface-variant">flowline pinhole leak, started</span>
<span class="font-label-mono-tag text-xs text-on-surface font-semibold ml-1">3 Oct</span>,
<span class="text-tertiary font-semibold ml-1 inline-flex items-center gap-0.5">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary"></span>
still open
</span>.
</td>
</tr>
<!-- ROW 4 -->
<tr class="hover:bg-surface-container/50 transition-colors group">
<td class="py-3 px-4 whitespace-nowrap align-middle">
<a class="font-label-mono-tag text-xs font-semibold px-2 py-1 rounded bg-surface-container border border-primary/40 text-primary hover:border-primary transition-colors inline-flex items-center gap-1" href="#well-0175">
<span class="material-symbols-outlined text-[12px]">precision_manufacturing</span>
WELL-0175
</a>
</td>
<td class="py-3 px-4 text-right align-middle whitespace-nowrap">
<div class="inline-flex items-center gap-1 font-label-mono-tag text-xs font-semibold text-error">
<span class="material-symbols-outlined text-[13px] text-error">arrow_downward</span>
<span class="tabular-nums">0.4 °C</span>
</div>
</td>
<td class="py-3 px-4 whitespace-nowrap align-middle">
<span class="font-label-mono-tag text-[11px] font-medium tracking-wide text-primary-container px-2 py-0.5 rounded border border-dashed border-primary-container/80 bg-primary-container/10 inline-flex items-center gap-1">
<span class="material-symbols-outlined text-[13px]">help</span>
active (out of date)
</span>
</td>
<td class="py-3 px-4 align-middle font-body-spec text-[13px] text-on-surface-variant leading-snug">
<span class="italic inline-flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[14px] text-primary-container">help_outline</span>
No recorded reason
</span>
<a class="ml-2 inline-flex items-center gap-0.5 text-primary hover:underline font-label-mono-tag text-xs whitespace-nowrap" href="#dispatch-0175">
<span class="">Suggest field check</span>
<span class="material-symbols-outlined text-[13px]">arrow_right_alt</span>
</a>
</td>
</tr>
</tbody>
</table>
</div>
<!-- TABLE FOOTER CONTROLS -->
<footer class="bg-surface-container px-space-md py-2 border-t border-surface-container-high flex items-center justify-between font-label-mono-tag text-[12px]"><div class="text-on-surface-variant">Showing <span class="font-semibold text-on-surface">4 of 4</span> wells flagged</div><div class="flex items-center gap-space-md"><button class="inline-flex items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" onclick="filterAnomaly()" type="button"><span class="material-symbols-outlined text-[15px]">filter_list</span><span class="">Filter by anomaly</span></button></div></footer>
</section>
<!-- DATA SOURCES / CITATION CHIPS -->
<div class="flex flex-col gap-space-xs pt-1">
<div class="flex items-center gap-1.5 font-label-mono-tag text-[11px] text-on-surface-variant font-semibold tracking-wider uppercase"><span class="material-symbols-outlined text-[14px] text-primary">link</span>SOURCES (5 LOGS)</div>
<div class="flex flex-wrap items-center gap-2"><button class="font-label-mono-tag text-[12px] px-2 py-1 rounded bg-surface-container border border-outline-variant/60 text-primary hover:border-primary transition-colors inline-flex items-center gap-1.5" type="button"><span class="material-symbols-outlined text-[13px] text-on-surface-variant">assignment</span><span class="">INS-0164-0205</span></button><button class="font-label-mono-tag text-[12px] px-2 py-1 rounded bg-surface-container border border-outline-variant/60 text-primary hover:border-primary transition-colors inline-flex items-center gap-1.5" type="button"><span class="material-symbols-outlined text-[13px] text-on-surface-variant">build</span><span class="">MNT-0170-031</span></button><button class="font-label-mono-tag text-[12px] px-2 py-1 rounded bg-surface-container border border-outline-variant/60 text-primary hover:border-primary transition-colors inline-flex items-center gap-1.5" type="button"><span class="material-symbols-outlined text-[13px] text-on-surface-variant">build</span><span class="">MNT-0172-028</span></button><button class="font-label-mono-tag text-[12px] px-2 py-1 rounded bg-surface-container border border-outline-variant/60 text-primary hover:border-primary transition-colors inline-flex items-center gap-1.5" type="button"><span class="material-symbols-outlined text-[13px] text-on-surface-variant">assignment</span><span class="">INS-0175-0205</span></button><button class="font-label-mono-tag text-[12px] px-2 py-1 rounded bg-surface-container border border-outline-variant/60 text-primary hover:border-primary transition-colors inline-flex items-center gap-1.5" type="button"><span class="material-symbols-outlined text-[13px] text-on-surface-variant">assignment</span><span class="">INS-0008-0100</span></button></div>
</div>
<!-- MESSAGE FOOTER META & ACTIONS -->
<div class="flex flex-wrap items-center justify-between gap-y-3 pt-space-sm border-t border-surface-container-high text-on-surface-variant">
<div class="font-label-mono-tag text-[11px] tracking-wide text-on-surface-variant"><span class="">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div>
<div class="flex items-center gap-1">
<button class="p-1.5 rounded hover:bg-surface-container hover:text-on-surface text-on-surface-variant transition-colors" title="Copy response markdown" type="button">
<span class="material-symbols-outlined text-[16px]">content_copy</span>
</button>
<button class="p-1.5 rounded hover:bg-surface-container hover:text-secondary text-on-surface-variant transition-colors" title="Mark response accurate" type="button">
<span class="material-symbols-outlined text-[16px]">thumb_up</span>
</button>
<button class="p-1.5 rounded hover:bg-surface-container hover:text-error text-on-surface-variant transition-colors" title="Flag inaccurate response" type="button">
<span class="material-symbols-outlined text-[16px]">thumb_down</span>
</button>
<span class="w-[1px] h-3.5 bg-outline-variant mx-1"></span>
<button class="inline-flex items-center gap-1 px-2 py-1 rounded bg-surface-container border border-outline-variant/50 text-[12px] font-label-mono-tag text-on-surface hover:border-primary transition-colors" type="button">
<span class="material-symbols-outlined text-[14px] text-primary">edit_note</span>
<span class="">Correct this</span>
</button>
</div>
</div>
</article>
<!-- QUICK OPERATOR PROMPT SUGGESTIONS (INSPECTION ACTIONS) -->

</div>
<script>
let sortDirections = {};

function sortTable(columnIndex, isNumeric = false) {
const table = document.getElementById("telemetry-table");
const tbody = table.querySelector("tbody");
const rows = Array.from(tbody.querySelectorAll("tr"));

// Toggle sort order
sortDirections[columnIndex] = !sortDirections[columnIndex];
const ascending = sortDirections[columnIndex];

rows.sort((a, b) => {
let cellA = a.children[columnIndex].innerText.trim();
let cellB = b.children[columnIndex].innerText.trim();

if (isNumeric) {
// Extract float value from string like "4.1 °C"
const numA = parseFloat(cellA.replace(/[^\d.-]/g, '')) || 0;
const numB = parseFloat(cellB.replace(/[^\d.-]/g, '')) || 0;
return ascending ? numA - numB : numB - numA;
} else {
return ascending
? cellA.localeCompare(cellB, undefined, { sensitivity: 'base' })
: cellB.localeCompare(cellA, undefined, { sensitivity: 'base' });
}
});

// Re-attach sorted rows
rows.forEach(row => tbody.appendChild(row));
}

function exportCSV() {
const table = document.getElementById("telemetry-table");
let csv = [];
const rows = table.querySelectorAll("tr");

for (let i = 0; i < rows.length; i++) {
let row = [], cols = rows[i].querySelectorAll("td, th");
for (let j = 0; j < cols.length; j++) {
let cleanText = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, " ").replace(/\s+/g, " ").trim();
row.push('"' + cleanText.replace(/"/g, '""') + '"');
}
csv.push(row.join(","));
}

const csvContent = "data:text/csv;charset=utf-8," + csv.join("\n");
const encodedUri = encodeURI(csvContent);
const link = document.createElement("a");
link.setAttribute("href", encodedUri);
link.setAttribute("download", "northeast_block8_non_producing_wells.csv");
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
}

function filterAnomaly() {
const table = document.getElementById("telemetry-table");
const rows = table.querySelectorAll("tbody tr");
rows.forEach(row => {
// Toggle highlight on anomalous status rows
const statusText = row.children[2].innerText;
if (statusText.includes("out of date")) {
row.classList.toggle("bg-primary-container/5");
}
});
}
</script></div></main></div>

</body></html>
```



12. record_correction_flow_conflict_alert_asset_intelligence

```
<!DOCTYPE html>

<html class="dark" lang="en"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="web_dashboard" name="shell-type"/><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"surface":"#0e141c","primary-container":"#38bdf8","on-tertiary-container":"#8c0028","surface-container":"#1a2028","surface-bright":"#343a42","on-tertiary":"#67001b","inverse-primary":"#00668a","surface-container-high":"#242a33","secondary-fixed-dim":"#45dfa4","primary":"#8ed5ff","error-container":"#93000a","on-error-container":"#ffdad6","surface-container-lowest":"#090f16","outline-variant":"#3e484f","on-secondary":"#003825","outline":"#87929a","surface-variant":"#2f353e","on-secondary-container":"#00452e","surface-dim":"#0e141c","primary-fixed":"#c4e7ff","surface-tint":"#7bd0ff","on-secondary-fixed":"#002114","on-tertiary-fixed-variant":"#92002a","secondary-fixed":"#68fcbf","on-primary-fixed-variant":"#004c69","secondary-container":"#00bd85","on-surface-variant":"#bdc8d1","secondary":"#45dfa4","error":"#ffb4ab","on-surface":"#dde3ee","surface-container-highest":"#2f353e","inverse-surface":"#dde3ee","background":"#0e141c","on-background":"#dde3ee","on-primary-fixed":"#001e2c","primary-fixed-dim":"#7bd0ff","tertiary-fixed":"#ffdadb","on-error":"#690005","on-primary-container":"#004965","tertiary-container":"#ff929a","tertiary":"#ffbcbf","inverse-on-surface":"#2b3139","surface-container-low":"#161c24","on-secondary-fixed-variant":"#005137","on-tertiary-fixed":"#40000d","on-primary":"#00354a","tertiary-fixed-dim":"#ffb2b7"},borderRadius:{"DEFAULT":"0.125rem","lg":"0.25rem","xl":"0.5rem","full":"0.75rem"},spacing:{"space-xs":"0.25rem","space-xl":"1.5rem","space-md":"1rem","space-sm":"0.5rem","gutter":"1.5rem","margin":"1.5rem","space-lg":"1.25rem"},fontFamily:{"headline-panel-mobile":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"display-telemetry":["IBM Plex Mono"],"body-spec":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose-medium":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel":["IBM Plex Sans"]},fontSize:{"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}};</script></head><body class="bg-surface font-body-spec text-on-surface antialiased min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low z-50 flex flex-col justify-between shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="flex flex-col p-space-md gap-space-md"><div class="flex items-center gap-space-sm px-space-xs py-space-xs"><span class="material-symbols-outlined text-primary text-[20px]">neurology</span><span class="font-headline-panel text-headline-panel text-on-surface tracking-tight">Asset Copilot</span></div><button class="w-full flex items-center justify-center gap-space-sm bg-surface-container hover:bg-surface-container-high text-on-surface hover:text-on-surface py-space-sm px-space-md rounded-xl transition-colors" type="button"><span class="material-symbols-outlined text-[18px] text-primary">add</span><span class="font-body-spec-mono text-body-spec-mono">+ New chat</span></button><div class="flex flex-col gap-space-xs mt-space-sm"><span class="font-label-metric text-label-metric uppercase text-outline px-space-xs tracking-wider">Recent chats</span><nav class="flex flex-col gap-space-xs" data-active-classes="bg-surface-container-high text-primary font-body-spec-mono rounded-lg"><a aria-current="page" class="flex items-center gap-space-sm px-space-sm py-space-sm transition-colors truncate bg-surface-container-high text-primary font-body-spec-mono rounded-lg" data-path="well-0001-status-and-last-inspection" href="#"><span class="font-label-mono-tag text-label-mono-tag text-primary truncate">WELL-0001 status and last inspection</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="northeast-block-8-not-producing" href="#"><span>Northeast Block 8 not producing</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="block-7-downtime-top-3" href="#"><span>Block 7 downtime, top 3</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="well-0001-spills-last-4-years" href="#"><span class="font-label-mono-tag text-label-mono-tag text-primary truncate">WELL-0001 spills, last 4 years</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="pump-jack-root-cause-wells" href="#"><span>Pump jack root-cause wells</span></a></nav></div></div><div class="p-space-md bg-surface-container-lowest"><div class="flex items-center justify-between p-space-sm rounded-xl bg-surface-container-low"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div><div class="flex flex-col"><span class="font-body-spec-mono text-body-spec-mono text-on-surface">Michael Turner</span><span class="font-label-mono-tag text-label-mono-tag text-outline">Lead Field Engineer</span></div></div><span class="material-symbols-outlined text-outline text-[18px]">more_vert</span></div></div></aside><div class="pl-[296px] flex flex-col min-h-screen"><header class="fixed top-0 left-[296px] right-0 z-40 bg-surface/80 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="h-14 w-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-headline-panel text-on-surface tracking-tight">Asset Intelligence Copilot</span><span class="h-4 w-[1px] bg-outline-variant"></span><span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant">Investigation Workspace</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-space-sm py-space-xs rounded-lg bg-surface-container"><span class="material-symbols-outlined text-[16px] text-outline">calendar_today</span><span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant">Today: 17 Oct 2026</span></div><div class="flex items-center gap-space-xs px-space-sm py-space-xs rounded-lg bg-surface-container"><span class="w-2 h-2 rounded-full bg-secondary"></span><span class="font-label-mono-tag text-label-mono-tag text-on-surface">Michael Turner</span></div><div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div></div></div></header><main class="relative pt-14 pb-28 flex-1 bg-surface flex flex-col items-center"><div class="w-full max-w-[880px] px-space-md flex-1 flex flex-col"><div class="flex flex-col w-full gap-space-xl py-space-md relative">
<!-- Prior Context User Query Plate -->
<div class="flex justify-end w-full">
<div class="max-w-[75%] bg-surface-container rounded-xl p-space-md flex flex-col gap-space-xs shadow-md">
<div class="flex items-center justify-between gap-space-md">
<span class="font-label-mono-tag text-label-mono-tag text-outline uppercase tracking-wider">OPERATOR // CREW-ALPHA</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline-variant">08:41:12 UTC</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">
Inspect bearing temp anomaly on <span class="font-label-mono-tag text-label-mono-tag text-primary-container bg-surface-container-high px-space-xs py-0.5 rounded">WELL-0164</span> from yesterday's field pass. Value seems physically inconsistent with line current.
</p>
</div>
</div>
<!-- Primary System Response Canvas -->
<article class="w-full bg-surface-container-low rounded-xl p-space-lg flex flex-col gap-space-md shadow-lg relative overflow-hidden">
<!-- Visual Left Rail Indicator -->
<div class="absolute left-0 top-0 bottom-0 w-1 bg-primary-container"></div>
<!-- Header Meta Row -->
<div class="flex flex-wrap items-center justify-between gap-space-sm pl-space-xs">
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag uppercase text-primary font-semibold tracking-wider">ASSET INTELLIGENCE ENGINE</span>
<span class="w-1.5 h-1.5 rounded-full bg-outline-variant"></span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">RECORD DISCREPANCY AUDIT</span>
</div>
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag text-outline">17 OCT 2026 // 08:42:04 UTC</span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary bg-surface-container px-space-xs py-0.5 rounded">ID: EV-88102</span>
</div>
</div>
<!-- Assistant Message Prose -->
<div class="pl-space-xs flex flex-col gap-space-sm">
<p class="font-body-prose text-body-prose text-on-surface">
Analysis of field record <span class="font-label-mono-tag text-label-mono-tag text-primary-container bg-surface-container px-1.5 py-0.5 rounded">INS-0164-0205</span> shows thermal capture deviates by -19.4 C relative to shaft torque signature. Manual override initiated via engineering workstation.
</p>
</div>
<!-- SUCCESS CONFIRMATION BLOCK (Post-Correction State) -->
<div class="pl-space-xs flex flex-col gap-space-sm">
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-sm shadow-sm">
<div class="flex items-start justify-between gap-space-md">
<div class="flex items-center gap-space-sm">
<span class="material-symbols-outlined text-secondary text-[20px]" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="font-body-spec-mono text-body-spec-mono text-on-surface font-semibold">Correction recorded against record</span>
<span class="font-label-mono-tag text-label-mono-tag text-primary-container bg-surface-container-high px-space-sm py-0.5 rounded font-medium">INS-0164-0205</span>
</div>
<div class="flex items-center gap-space-xs">
<span class="font-label-mono-tag text-label-mono-tag text-outline bg-surface-container-lowest px-1.5 py-0.5 rounded">CTX-0164-001</span>
</div>
</div>
<div class="bg-surface-container-lowest rounded-md p-space-sm flex flex-col gap-space-xs">
<p class="font-body-spec text-body-spec text-on-surface-variant leading-relaxed">
Original <span class="font-body-spec-mono text-body-spec-mono text-outline">24.0 C</span> kept. Corrected to <span class="font-body-spec-mono text-body-spec-mono text-primary font-bold">41.0 C</span> by <span class="text-on-surface font-medium">Michael Turner</span>. Reason: <span class="italic text-on-surface">faulty thermal gun</span>.
</p>
<div class="flex items-center gap-space-md text-outline font-label-mono-tag text-label-mono-tag pt-space-xs">
<span>SCOPE: WELLHEAD ONLY</span>
<span>•</span>
<span>AUDIT TRAIL: COMMITTED</span>
<span>•</span>
<span>FLAG: USER_VERIFIED</span>
</div>
</div>
</div>
<!-- CONFLICT BANNER ATTACHED -->
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-md shadow-sm">
<div class="flex items-start gap-space-md">
<div class="w-8 h-8 rounded-md bg-tertiary-container/20 flex items-center justify-center flex-shrink-0 mt-0.5">
<span class="material-symbols-outlined text-tertiary text-[20px]" style="font-variation-settings: 'FILL' 1;">warning</span>
</div>
<div class="flex flex-col flex-1 gap-space-xs">
<div class="flex items-center gap-space-sm">
<span class="font-label-metric text-label-metric uppercase text-tertiary font-bold tracking-wider">CONFLICT</span>
<span class="w-1 h-1 rounded-full bg-outline-variant"></span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">INSPECTOR OBSERVATION MISMATCH</span>
</div>
<p class="font-body-spec text-body-spec text-on-surface">
Inspector note <span class="text-tertiary font-medium">"Pump jack not moving."</span> (Tyler Hughes) disagrees. Please confirm.
</p>
</div>
</div>
<!-- Conflict Actions -->
<div class="flex flex-wrap items-center gap-space-sm pl-11">
<button class="flex items-center gap-space-xs bg-surface-container-high hover:bg-surface-bright text-primary font-body-spec-mono text-body-spec-mono px-space-md py-space-xs rounded-lg transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">verified</span>
<span>Keep 41.0 C &amp; Flag Note</span>
</button>
<button class="flex items-center gap-space-xs bg-surface-container-lowest hover:bg-surface-container-high text-on-surface-variant font-body-spec-mono text-body-spec-mono px-space-md py-space-xs rounded-lg transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">history_edu</span>
<span>Review Tyler's Inspection</span>
</button>
</div>
</div>
</div>
<!-- Comparative Visual Telemetry Sparkline -->
<div class="pl-space-xs mt-space-xs">
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-sm">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Shaft Journal Temperature Trend (24h Window)</span>
<div class="flex items-center gap-space-md">
<div class="flex items-center gap-1.5">
<span class="w-2.5 h-0.5 bg-outline"></span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">Raw (24.0 C)</span>
</div>
<div class="flex items-center gap-1.5">
<span class="w-2.5 h-0.5 bg-primary-container"></span>
<span class="font-label-mono-tag text-label-mono-tag text-primary-container">Corrected (41.0 C)</span>
</div>
</div>
</div>
<div class="h-16 w-full flex items-end">
<svg class="w-full h-14 overflow-visible" preserveaspectratio="none" viewbox="0 0 600 60">
<!-- Gridlines -->
<line class="text-surface-container-high" stroke="currentColor" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="600" y1="15" y2="15"></line>
<line class="text-surface-container-high" stroke="currentColor" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="600" y1="35" y2="35"></line>
<line class="text-surface-container-high" stroke="currentColor" stroke-dasharray="2 2" stroke-width="1" x1="0" x2="600" y1="55" y2="55"></line>
<!-- Baseline curve -->
<path class="text-outline" d="M0,45 Q120,44 240,43 T400,42 T520,44 L600,45" fill="none" stroke="currentColor" stroke-dasharray="4 3" stroke-width="1.5"></path>
<!-- Corrected path -->
<path class="text-primary-container" d="M0,45 Q120,42 240,36 T400,24 T520,18 L600,16" fill="none" stroke="currentColor" stroke-width="2"></path>
<!-- Marker at correction point -->
<circle class="fill-primary-container text-surface" cx="520" cy="18" r="4" stroke="currentColor" stroke-width="2"></circle>
</svg>
</div>
</div>
</div>
<!-- Assistant Footer Metadata Strip -->
<div class="pt-space-sm pl-space-xs flex items-center justify-between text-outline font-label-mono-tag text-label-mono-tag">
<div class="flex items-center gap-space-xs">
<span class="material-symbols-outlined text-[14px]">tune</span>
<span>gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span>
</div>
<div class="flex items-center gap-space-sm">
<button class="hover:text-primary transition-colors flex items-center gap-1" type="button">
<span class="material-symbols-outlined text-[14px]">history</span>
<span>Diff View</span>
</button>
<span>•</span>
<button class="hover:text-primary transition-colors flex items-center gap-1" type="button">
<span class="material-symbols-outlined text-[14px]">share</span>
<span>Export Entry</span>
</button>
</div>
</div>
</article>
<!-- MODAL DIALOG OVERLAY: 'Correct this' Flow -->
<div class="fixed inset-0 z-50 flex items-center justify-center p-space-md bg-surface-container-lowest/80 backdrop-blur-sm" id="correction-modal-backdrop">
<div class="w-full max-w-[560px] bg-surface-container-low rounded-xl flex flex-col shadow-2xl overflow-hidden relative">
<!-- Top Accent Bar -->
<div class="h-1 w-full bg-primary-container"></div>
<!-- Modal Header -->
<div class="p-space-lg pb-space-md flex items-center justify-between bg-surface-container-low">
<div class="flex items-center gap-space-md">
<div class="w-9 h-9 rounded-lg bg-surface-container flex items-center justify-center">
<span class="material-symbols-outlined text-primary text-[20px]">edit_note</span>
</div>
<div class="flex flex-col">
<h2 class="font-headline-panel text-headline-panel text-on-surface">Submit Record Correction</h2>
<div class="flex items-center gap-space-xs mt-0.5">
<span class="font-label-metric text-label-metric uppercase text-outline">TARGET AUDIT OBJECT:</span>
<span class="font-label-mono-tag text-label-mono-tag text-primary-container bg-surface-container px-1.5 py-0.5 rounded flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">assignment</span>
INS-0164-0205
</span>
</div>
</div>
</div>
<button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-surface-container-high text-outline hover:text-on-surface flex items-center justify-center transition-colors" onclick="document.getElementById('correction-modal-backdrop').style.display='none'" type="button">
<span class="material-symbols-outlined text-[20px]">close</span>
</button>
</div>
<!-- Modal Body -->
<div class="p-space-lg flex flex-col gap-space-md bg-surface-container-low">
<!-- Field 1: Read-Only Locked Value -->
<div class="flex flex-col gap-space-xs">
<label class="font-label-metric text-label-metric uppercase text-outline flex items-center justify-between">
<span>Original Captured Metric</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline-variant flex items-center gap-1">
<span class="material-symbols-outlined text-[12px]">lock</span> LOCKED RECORD
</span>
</label>
<div class="w-full bg-surface-container-lowest rounded-lg p-space-md flex items-center justify-between">
<div class="flex items-baseline gap-space-xs">
<span class="font-display-telemetry text-display-telemetry text-outline line-through opacity-70">24.0</span>
<span class="font-body-spec-mono text-body-spec-mono text-outline">C</span>
</div>
<div class="flex items-center gap-space-xs bg-surface-container px-space-sm py-1 rounded">
<span class="material-symbols-outlined text-outline text-[14px]">archive</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">Original value 24.0 C (kept)</span>
</div>
</div>
</div>
<!-- Field 2: Corrected Input -->
<div class="flex flex-col gap-space-xs">
<label class="font-label-metric text-label-metric uppercase text-primary font-semibold flex items-center justify-between" for="corrected-val-input">
<span>Corrected Value</span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary">PHYSICAL DELTA +17.0 C</span>
</label>
<div class="relative flex items-center">
<input class="w-full bg-surface-container rounded-lg px-space-md py-space-sm font-display-telemetry text-display-telemetry text-on-surface focus:outline-none focus:bg-surface-container-high transition-colors" id="corrected-val-input" type="text" value="41.0 C"/>
<span class="absolute right-space-md font-body-spec-mono text-body-spec-mono text-primary bg-surface-container-lowest px-2 py-1 rounded">
THERMAL_POINT
</span>
</div>
</div>
<!-- Field 3: Reason Textarea -->
<div class="flex flex-col gap-space-xs">
<label class="font-label-metric text-label-metric uppercase text-outline" for="reason-input">
Reason For Revision
</label>
<textarea class="w-full bg-surface-container rounded-lg p-space-md font-body-spec text-body-spec text-on-surface focus:outline-none focus:bg-surface-container-high transition-colors resize-none" id="reason-input" rows="2">faulty thermal gun</textarea>
<span class="font-label-mono-tag text-label-mono-tag text-outline-variant">Requires supervisor review upon transmission.</span>
</div>
<!-- Scope Segmented Switch -->
<div class="flex flex-col gap-space-xs pt-space-xs">
<span class="font-label-metric text-label-metric uppercase text-outline">Application Scope</span>
<div class="grid grid-cols-2 bg-surface-container-lowest p-1 rounded-lg gap-1">
<button class="py-space-sm px-space-md rounded-md bg-surface-container-high text-primary font-body-spec-mono text-body-spec-mono flex items-center justify-center gap-space-xs shadow-sm" type="button">
<span class="material-symbols-outlined text-[16px]">filter_1</span>
<span>This well only</span>
</button>
<button class="py-space-sm px-space-md rounded-md hover:bg-surface-container text-outline hover:text-on-surface font-body-spec-mono text-body-spec-mono flex items-center justify-center gap-space-xs transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">grid_view</span>
<span>All wells of this type</span>
</button>
</div>
</div>
</div>
<!-- Modal Actions Footer -->
<div class="p-space-lg pt-space-md bg-surface-container-lowest flex items-center justify-end gap-space-md">
<button class="px-space-md py-space-sm rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface-variant font-body-spec-mono text-body-spec-mono transition-colors" onclick="document.getElementById('correction-modal-backdrop').style.display='none'" type="button">
Cancel
</button>
<button class="px-space-xl py-space-sm rounded-lg bg-primary-container hover:bg-primary text-on-primary-container font-body-spec-mono text-body-spec-mono font-semibold flex items-center gap-space-xs shadow-md transition-colors" onclick="document.getElementById('correction-modal-backdrop').style.display='none'" type="button">
<span class="material-symbols-outlined text-[18px]">save</span>
<span>Save correction</span>
</button>
</div>
</div>
</div>
</div></div></main><footer class="fixed bottom-0 left-[296px] right-0 z-40 bg-surface/90 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="max-w-[880px] mx-auto p-space-md"><div class="flex items-center bg-surface-container rounded-xl px-space-md py-space-sm"><input class="flex-1 bg-transparent text-on-surface font-body-spec text-body-spec placeholder:text-outline focus:outline-none" placeholder="Query asset records, maintenance history, or operational logs..." type="text"/><button class="w-9 h-9 flex items-center justify-center bg-primary-container text-on-primary-container hover:bg-primary transition-colors rounded-lg flex-shrink-0" type="button"><span class="material-symbols-outlined text-[20px]">arrow_upward</span></button></div></div></footer></div></body></html>
```


13. user_picker_dropdown_asset_intelligence
```
<!DOCTYPE html>

<html class="dark" lang="en"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="web_dashboard" name="shell-type"/><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{colors:{"surface":"#0e141c","primary-container":"#38bdf8","on-tertiary-container":"#8c0028","surface-container":"#1a2028","surface-bright":"#343a42","on-tertiary":"#67001b","inverse-primary":"#00668a","surface-container-high":"#242a33","secondary-fixed-dim":"#45dfa4","primary":"#8ed5ff","error-container":"#93000a","on-error-container":"#ffdad6","surface-container-lowest":"#090f16","outline-variant":"#3e484f","on-secondary":"#003825","outline":"#87929a","surface-variant":"#2f353e","on-secondary-container":"#00452e","surface-dim":"#0e141c","primary-fixed":"#c4e7ff","surface-tint":"#7bd0ff","on-secondary-fixed":"#002114","on-tertiary-fixed-variant":"#92002a","secondary-fixed":"#68fcbf","on-primary-fixed-variant":"#004c69","secondary-container":"#00bd85","on-surface-variant":"#bdc8d1","secondary":"#45dfa4","error":"#ffb4ab","on-surface":"#dde3ee","surface-container-highest":"#2f353e","inverse-surface":"#dde3ee","background":"#0e141c","on-background":"#dde3ee","on-primary-fixed":"#001e2c","primary-fixed-dim":"#7bd0ff","tertiary-fixed":"#ffdadb","on-error":"#690005","on-primary-container":"#004965","tertiary-container":"#ff929a","tertiary":"#ffbcbf","inverse-on-surface":"#2b3139","surface-container-low":"#161c24","on-secondary-fixed-variant":"#005137","on-tertiary-fixed":"#40000d","on-primary":"#00354a","tertiary-fixed-dim":"#ffb2b7"},borderRadius:{"DEFAULT":"0.125rem","lg":"0.25rem","xl":"0.5rem","full":"0.75rem"},spacing:{"space-xs":"0.25rem","space-xl":"1.5rem","space-md":"1rem","space-sm":"0.5rem","gutter":"1.5rem","margin":"1.5rem","space-lg":"1.25rem"},fontFamily:{"headline-panel-mobile":["IBM Plex Sans"],"label-mono-tag":["IBM Plex Mono"],"display-telemetry":["IBM Plex Mono"],"body-spec":["IBM Plex Sans"],"body-spec-mono":["IBM Plex Mono"],"label-metric":["IBM Plex Sans"],"body-prose-medium":["IBM Plex Sans"],"body-prose":["IBM Plex Sans"],"headline-panel":["IBM Plex Sans"]},fontSize:{"headline-panel-mobile":["18px",{lineHeight:"24px",fontWeight:"600"}],"label-mono-tag":["12px",{lineHeight:"16px",fontWeight:"500"}],"display-telemetry":["28px",{lineHeight:"34px",letterSpacing:"-0.01em",fontWeight:"600"}],"body-spec":["14px",{lineHeight:"20px",fontWeight:"400"}],"body-spec-mono":["14px",{lineHeight:"20px",fontWeight:"500"}],"label-metric":["12px",{lineHeight:"16px",letterSpacing:"0.04em",fontWeight:"600"}],"body-prose-medium":["16px",{lineHeight:"24px",fontWeight:"500"}],"body-prose":["16px",{lineHeight:"24px",fontWeight:"400"}],"headline-panel":["20px",{lineHeight:"28px",letterSpacing:"-0.01em",fontWeight:"600"}]}}}};</script></head><body class="bg-surface font-body-spec text-on-surface antialiased min-h-screen"><aside class="fixed left-0 top-0 h-full w-[296px] bg-surface-container-low z-50 flex flex-col justify-between shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="flex flex-col p-space-md gap-space-md"><div class="flex items-center gap-space-sm px-space-xs py-space-xs"><span class="material-symbols-outlined text-primary text-[20px]">neurology</span><span class="font-headline-panel text-headline-panel text-on-surface tracking-tight">Asset Copilot</span></div><button class="w-full flex items-center justify-center gap-space-sm bg-surface-container hover:bg-surface-container-high text-on-surface hover:text-on-surface py-space-sm px-space-md rounded-xl transition-colors" type="button"><span class="material-symbols-outlined text-[18px] text-primary">add</span><span class="font-body-spec-mono text-body-spec-mono">+ New chat</span></button><div class="flex flex-col gap-space-xs mt-space-sm"><span class="font-label-metric text-label-metric uppercase text-outline px-space-xs tracking-wider">Recent chats</span><nav class="flex flex-col gap-space-xs" data-active-classes="bg-surface-container-high text-primary font-body-spec-mono rounded-lg"><a aria-current="page" class="flex items-center gap-space-sm px-space-sm py-space-sm transition-colors truncate bg-surface-container-high text-primary font-body-spec-mono rounded-lg" data-path="well-0001-status-and-last-inspection" href="#"><span class="font-label-mono-tag text-label-mono-tag text-primary truncate">WELL-0001 status and last inspection</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="northeast-block-8-not-producing" href="#"><span>Northeast Block 8 not producing</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="block-7-downtime-top-3" href="#"><span>Block 7 downtime, top 3</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="well-0001-spills-last-4-years" href="#"><span class="font-label-mono-tag text-label-mono-tag text-primary truncate">WELL-0001 spills, last 4 years</span></a><a class="flex items-center gap-space-sm px-space-sm py-space-sm rounded-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors font-body-spec text-body-spec truncate" data-path="pump-jack-root-cause-wells" href="#"><span>Pump jack root-cause wells</span></a></nav></div></div><div class="p-space-md bg-surface-container-lowest"><div class="flex items-center justify-between p-space-sm rounded-xl bg-surface-container-low"><div class="flex items-center gap-space-sm"><div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div><div class="flex flex-col"><span class="font-body-spec-mono text-body-spec-mono text-on-surface">Michael Turner</span><span class="font-label-mono-tag text-label-mono-tag text-outline">Lead Field Engineer</span></div></div><span class="material-symbols-outlined text-outline text-[18px]">more_vert</span></div></div></aside><div class="pl-[296px] flex flex-col min-h-screen"><header class="fixed top-0 left-[296px] right-0 z-40 bg-surface/80 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="h-14 w-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-headline-panel text-on-surface tracking-tight">Asset Intelligence Copilot</span><span class="h-4 w-[1px] bg-outline-variant"></span><span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant">Investigation Workspace</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-space-sm py-space-xs rounded-lg bg-surface-container"><span class="material-symbols-outlined text-[16px] text-outline">calendar_today</span><span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant">Today: 17 Oct 2026</span></div><div class="flex items-center gap-space-xs px-space-sm py-space-xs rounded-lg bg-surface-container"><span class="w-2 h-2 rounded-full bg-secondary"></span><span class="font-label-mono-tag text-label-mono-tag text-on-surface">Michael Turner</span></div><div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div></div></div></header><main class="relative pt-14 pb-28 flex-1 bg-surface flex flex-col items-center"><div class="w-full max-w-[880px] px-space-md flex-1 flex flex-col"><div class="flex flex-col w-full relative">
<!-- Interactive Popover Anchored to the Sidebar User Section -->
<div class="fixed left-[16px] bottom-[76px] w-[320px] z-50 bg-surface-container-high rounded-xl shadow-2xl p-space-sm flex flex-col gap-space-xs backdrop-blur-xl">
<!-- Popover Header -->
<div class="flex items-center justify-between px-space-sm py-space-xs">
<span class="font-label-metric text-label-metric uppercase text-outline tracking-wider">Switch Profile</span>
<span class="font-label-mono-tag text-label-mono-tag text-primary bg-surface-container px-space-xs py-0.5 rounded">5 Verified</span>
</div>
<!-- User Rows Container -->
<div class="flex flex-col gap-1 mt-space-xs">
<!-- 1. Michael Turner (Active Row) -->
<button class="w-full flex items-center justify-between p-space-sm rounded-lg bg-surface-variant transition-colors text-left group" type="button">
<div class="flex items-center gap-space-sm min-w-0">
<div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center font-body-spec-mono text-body-spec-mono font-semibold flex-shrink-0">
MT
</div>
<div class="flex flex-col min-w-0">
<span class="font-body-spec-mono text-body-spec-mono text-on-surface font-semibold truncate">Michael Turner</span>
<span class="font-label-mono-tag text-label-mono-tag text-primary truncate">Production supervisor</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline truncate">Northeast Production</span>
</div>
</div>
<span class="material-symbols-outlined text-primary text-[20px] flex-shrink-0 ml-space-xs">check</span>
</button>
<!-- 2. Tyler Hughes -->
<button class="w-full flex items-center justify-between p-space-sm rounded-lg hover:bg-surface-container transition-colors text-left group" type="button">
<div class="flex items-center gap-space-sm min-w-0">
<div class="w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono font-semibold flex-shrink-0 group-hover:bg-surface-bright group-hover:text-on-surface">
TH
</div>
<div class="flex flex-col min-w-0">
<span class="font-body-spec text-body-spec text-on-surface truncate">Tyler Hughes</span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant truncate">Field operator</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline truncate">Northeast Production</span>
</div>
</div>
</button>
<!-- 3. Jessica Reed -->
<button class="w-full flex items-center justify-between p-space-sm rounded-lg hover:bg-surface-container transition-colors text-left group" type="button">
<div class="flex items-center gap-space-sm min-w-0">
<div class="w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono font-semibold flex-shrink-0 group-hover:bg-surface-bright group-hover:text-on-surface">
JR
</div>
<div class="flex flex-col min-w-0">
<span class="font-body-spec text-body-spec text-on-surface truncate">Jessica Reed</span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant truncate">Field inspector</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline truncate">Northeast Production</span>
</div>
</div>
</button>
<!-- 4. Jake Morales -->
<button class="w-full flex items-center justify-between p-space-sm rounded-lg hover:bg-surface-container transition-colors text-left group" type="button">
<div class="flex items-center gap-space-sm min-w-0">
<div class="w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono font-semibold flex-shrink-0 group-hover:bg-surface-bright group-hover:text-on-surface">
JM
</div>
<div class="flex flex-col min-w-0">
<span class="font-body-spec text-body-spec text-on-surface truncate">Jake Morales</span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant truncate">Field operator</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline truncate">Southwest Production</span>
</div>
</div>
</button>
<!-- 5. Laura Simmons -->
<button class="w-full flex items-center justify-between p-space-sm rounded-lg hover:bg-surface-container transition-colors text-left group" type="button">
<div class="flex items-center gap-space-sm min-w-0">
<div class="w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant flex items-center justify-center font-body-spec-mono text-body-spec-mono font-semibold flex-shrink-0 group-hover:bg-surface-bright group-hover:text-on-surface">
LS
</div>
<div class="flex flex-col min-w-0">
<span class="font-body-spec text-body-spec text-on-surface truncate">Laura Simmons</span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant truncate">HSE officer</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline truncate">Health, Safety &amp; Environment</span>
</div>
</div>
</button>
</div>
<!-- Footer Privacy Note -->
<div class="mt-space-xs pt-space-xs px-space-sm pb-space-xs bg-surface-container-lowest rounded-lg flex items-center gap-space-sm">
<span class="material-symbols-outlined text-outline text-[16px] flex-shrink-0">lock</span>
<span class="font-label-mono-tag text-label-mono-tag text-on-surface-variant">Your chats are private. Corrections are shared.</span>
</div>
</div>
<!-- Main Center Area: Active Investigation / Conversation Canvas -->
<div class="flex flex-col gap-space-lg w-full py-space-md">
<!-- Operator Query Plate -->
<div class="self-end max-w-[80%] flex flex-col items-end gap-space-xs">
<div class="flex items-center gap-space-xs px-space-xs">
<span class="font-label-mono-tag text-label-mono-tag text-outline uppercase tracking-wider">Michael Turner // Supervisor</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">10:14 AM</span>
</div>
<div class="bg-surface-container-high rounded-xl p-space-md text-on-surface shadow-md">
<p class="font-body-spec text-body-spec">
Status summary for WELL-0001, recent inspection flags, and primary pump-jack diagnostics over the last 30 operational days.
</p>
</div>
</div>
<!-- Assistant Structured Report Module -->
<div class="w-full bg-surface-container-low rounded-xl p-space-lg flex flex-col gap-space-md relative overflow-hidden shadow-lg">
<!-- Left Signal Accent Rail -->
<div class="absolute left-0 top-0 bottom-0 w-1 bg-primary"></div>
<!-- Report Metadata Header -->
<div class="flex flex-wrap items-center justify-between gap-space-sm pl-space-xs">
<div class="flex items-center gap-space-sm">
<span class="font-label-metric text-label-metric uppercase text-primary tracking-wider">Asset Intelligence Engine</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">REC-77419</span>
</div>
<div class="flex items-center gap-space-md">
<div class="flex items-center gap-space-xs">
<span class="material-symbols-outlined text-secondary text-[16px]">check_circle</span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary uppercase">Synchronized</span>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline">17 Oct 2026 10:14:22</span>
</div>
</div>
<!-- Executive Overview Text -->
<div class="pl-space-xs">
<p class="font-body-prose text-body-prose text-on-surface leading-relaxed">
Record retrieval complete for asset <span class="font-label-mono-tag text-label-mono-tag text-primary bg-surface-container px-1.5 py-0.5 rounded">WELL-0001</span> located in Northeast Sector. System shows steady operating parameters following the scheduled rod packing maintenance executed on 02 Oct 2026. Zero environmental containment breaches documented within the requested interval.
</p>
</div>
<!-- Telemetry Readout Metrics Grid -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-space-md mt-space-xs">
<!-- Metric Tile 1 -->
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-xs shadow-sm">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Tubing Pressure</span>
<div class="flex items-center gap-1">
<span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary">NORMAL</span>
</div>
</div>
<div class="flex items-baseline gap-space-xs mt-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">342.8</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">PSI</span>
</div>
<div class="w-full bg-surface-container-high h-1 rounded-full overflow-hidden mt-space-xs">
<div class="bg-secondary h-full w-[68%]"></div>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline mt-1">Variance: +4.2 PSI vs baseline</span>
</div>
<!-- Metric Tile 2 -->
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-xs shadow-sm">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Casing Pressure</span>
<div class="flex items-center gap-1">
<span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary">STABLE</span>
</div>
</div>
<div class="flex items-baseline gap-space-xs mt-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">118.5</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">PSI</span>
</div>
<div class="w-full bg-surface-container-high h-1 rounded-full overflow-hidden mt-space-xs">
<div class="bg-secondary h-full w-[42%]"></div>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline mt-1">Baseline nominal: 120.0 PSI</span>
</div>
<!-- Metric Tile 3 -->
<div class="bg-surface-container rounded-lg p-space-md flex flex-col gap-space-xs shadow-sm">
<div class="flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-outline">Stroke Rate</span>
<div class="flex items-center gap-1">
<span class="w-1.5 h-1.5 rounded-full bg-primary"></span>
<span class="font-label-mono-tag text-label-mono-tag text-primary">OPERATIONAL</span>
</div>
</div>
<div class="flex items-baseline gap-space-xs mt-space-xs">
<span class="font-display-telemetry text-display-telemetry text-on-surface">6.4</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">SPM</span>
</div>
<div class="w-full bg-surface-container-high h-1 rounded-full overflow-hidden mt-space-xs">
<div class="bg-primary h-full w-[80%]"></div>
</div>
<span class="font-label-mono-tag text-label-mono-tag text-outline mt-1">Target operational: 6.5 SPM</span>
</div>
</div>
<!-- Recent Records Table Plate -->
<div class="bg-surface-container rounded-lg overflow-hidden shadow-sm mt-space-xs">
<div class="bg-surface-container-high px-space-md py-space-sm flex items-center justify-between">
<span class="font-label-metric text-label-metric uppercase text-on-surface-variant tracking-wider">Field Log Verification</span>
<span class="font-label-mono-tag text-label-mono-tag text-outline">Archive: 2026-Q3/Q4</span>
</div>
<div class="divide-y divide-surface-container-low">
<!-- Row 1 -->
<div class="px-space-md py-space-sm flex flex-wrap items-center justify-between gap-space-sm hover:bg-surface-variant transition-colors">
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag text-primary">INS-0001-0203</span>
<span class="font-body-spec text-body-spec text-on-surface">Quarterly visual inspection and valve seal integrity check</span>
</div>
<div class="flex items-center gap-space-md">
<span class="font-label-mono-tag text-label-mono-tag text-outline">08 Oct 2026</span>
<div class="flex items-center gap-1 px-2 py-0.5 rounded bg-surface-container-lowest">
<span class="material-symbols-outlined text-secondary text-[14px]">check_circle</span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary">PASS</span>
</div>
</div>
</div>
<!-- Row 2 -->
<div class="px-space-md py-space-sm flex flex-wrap items-center justify-between gap-space-sm hover:bg-surface-variant transition-colors">
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag text-primary">MNT-0001-032</span>
<span class="font-body-spec text-body-spec text-on-surface">Rod packing replacement and stuffing box lubrication</span>
</div>
<div class="flex items-center gap-space-md">
<span class="font-label-mono-tag text-label-mono-tag text-outline">02 Oct 2026</span>
<div class="flex items-center gap-1 px-2 py-0.5 rounded bg-surface-container-lowest">
<span class="material-symbols-outlined text-primary text-[14px]">done_all</span>
<span class="font-label-mono-tag text-label-mono-tag text-primary">COMPLETED</span>
</div>
</div>
</div>
<!-- Row 3 -->
<div class="px-space-md py-space-sm flex flex-wrap items-center justify-between gap-space-sm hover:bg-surface-variant transition-colors">
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag text-primary">ENV-0001-008</span>
<span class="font-body-spec text-body-spec text-on-surface">Containment berm assessment and soil runoff test</span>
</div>
<div class="flex items-center gap-space-md">
<span class="font-label-mono-tag text-label-mono-tag text-outline">19 Sep 2026</span>
<div class="flex items-center gap-1 px-2 py-0.5 rounded bg-surface-container-lowest">
<span class="material-symbols-outlined text-secondary text-[14px]">check_circle</span>
<span class="font-label-mono-tag text-label-mono-tag text-secondary">CLEAR</span>
</div>
</div>
</div>
</div>
</div>
<!-- Evidentiary Verification Footnote -->
<div class="flex items-center justify-between pt-space-xs pl-space-xs text-outline">
<div class="flex items-center gap-space-xs">
<span class="material-symbols-outlined text-[16px]">verified</span>
<span class="font-label-mono-tag text-label-mono-tag">Corroborated with field work order database</span>
</div>
<div class="flex items-center gap-space-sm">
<span class="font-label-mono-tag text-label-mono-tag text-outline">ID: WRK-8812</span>
</div>
</div>
</div>
</div>
</div></div></main><footer class="fixed bottom-0 left-[296px] right-0 z-40 bg-surface/90 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]"><div class="max-w-[880px] mx-auto p-space-md"><div class="flex items-center bg-surface-container rounded-xl px-space-md py-space-sm"><input class="flex-1 bg-transparent text-on-surface font-body-spec text-body-spec placeholder:text-outline focus:outline-none" placeholder="Query asset records, maintenance history, or operational logs..." type="text"/><button class="w-9 h-9 flex items-center justify-center bg-primary-container text-on-primary-container hover:bg-primary transition-colors rounded-lg flex-shrink-0" type="button"><span class="material-symbols-outlined text-[20px]">arrow_upward</span></button></div></div></footer></div></body></html>
```

14. well_0001_wellhead_vs_air_temperature_line_chart

```
<!DOCTYPE html><html class="dark" lang="en" style=""><svg class="inline-defs-container" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden"></svg><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config = { darkMode: "class", theme: { extend: { "colors": { "on-primary-fixed": "#001e2c", "surface-variant": "#2f353e", "on-primary": "#00354a", "primary-fixed-dim": "#7bd0ff", "surface-bright": "#343a42", "primary": "#8ed5ff", "tertiary-fixed-dim": "#ffb2b7", "surface-container-low": "#161c24", "outline-variant": "#3e484f", "surface-dim": "#0e141c", "on-error-container": "#ffdad6", "secondary-container": "#00bd85", "on-error": "#690005", "surface-container": "#1a2028", "on-tertiary-fixed-variant": "#92002a", "secondary-fixed-dim": "#45dfa4", "outline": "#87929a", "secondary-fixed": "#68fcbf", "surface": "#0e141c", "tertiary-fixed": "#ffdadb", "on-secondary": "#003825", "error": "#ffb4ab", "surface-container-highest": "#2f353e", "background": "#0e141c", "on-tertiary-fixed": "#40000d", "inverse-on-surface": "#2b3139", "on-primary-fixed-variant": "#004c69", "on-secondary-fixed-variant": "#005137", "on-secondary-fixed": "#002114", "inverse-primary": "#00668a", "error-container": "#93000a", "surface-container-high": "#242a33", "on-secondary-container": "#00452e", "on-background": "#dde3ee", "tertiary": "#ffbcbf", "on-surface": "#dde3ee", "secondary": "#45dfa4", "on-tertiary": "#67001b", "tertiary-container": "#ff929a", "on-tertiary-container": "#8c0028", "primary-fixed": "#c4e7ff", "primary-container": "#38bdf8", "surface-tint": "#7bd0ff", "inverse-surface": "#dde3ee", "surface-container-lowest": "#090f16", "on-primary-container": "#004965", "on-surface-variant": "#bdc8d1" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-lg": "1.25rem", "space-md": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "gutter": "1.5rem", "space-sm": "0.5rem", "margin": "1.5rem" }, "fontFamily": { "body-spec": [ "IBM Plex Sans" ], "label-mono-tag": [ "IBM Plex Mono" ], "body-prose-medium": [ "IBM Plex Sans" ], "label-metric": [ "IBM Plex Sans" ], "body-spec-mono": [ "IBM Plex Mono" ], "headline-panel": [ "IBM Plex Sans" ], "headline-panel-mobile": [ "IBM Plex Sans" ], "body-prose": [ "IBM Plex Sans" ], "display-telemetry": [ "IBM Plex Mono" ] }, "fontSize": { "body-spec": [ "14px", { "lineHeight": "20px", "fontWeight": "400" } ], "label-mono-tag": [ "12px", { "lineHeight": "16px", "fontWeight": "500" } ], "body-prose-medium": [ "16px", { "lineHeight": "24px", "fontWeight": "500" } ], "label-metric": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "body-spec-mono": [ "14px", { "lineHeight": "20px", "fontWeight": "500" } ], "headline-panel": [ "20px", { "lineHeight": "28px", "letterSpacing": "-0.01em", "fontWeight": "600" } ], "headline-panel-mobile": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ], "body-prose": [ "16px", { "lineHeight": "24px", "fontWeight": "400" } ], "display-telemetry": [ "28px", { "lineHeight": "34px", "letterSpacing": "-0.01em", "fontWeight": "600" } ] } } } };</script></head><body class="bg-surface-container-lowest font-body-spec text-on-surface antialiased"><aside class="fixed left-0 top-0 h-full w-64 bg-surface-container-low flex flex-col justify-between p-space-md z-50 border-r border-surface-container-high"><div class="flex flex-col gap-space-md"><button class="w-full py-2 px-space-sm rounded bg-primary text-on-primary font-headline-panel text-xs font-semibold flex items-center justify-center gap-1.5 shadow transition-colors hover:bg-primary-container"><span class="material-symbols-outlined text-[16px]">add</span><span class="">+ New chat</span></button><div class="flex flex-col gap-1.5 mt-2"><span class="font-label-mono-tag text-[10px] uppercase tracking-wider text-on-surface-variant px-1.5">Recent chats</span><div class="flex flex-col gap-1"><a href="#" class="px-2 py-1.5 rounded bg-surface-container text-primary font-body-spec text-xs block truncate border-l-2 border-primary" title="WELL-0001 status and last inspection">WELL-0001 status and last inspection</a><a href="#" class="px-2 py-1.5 rounded text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors font-body-spec text-xs block truncate" title="Northeast Block 8 not producing">Northeast Block 8 not producing</a><a href="#" class="px-2 py-1.5 rounded text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors font-body-spec text-xs block truncate" title="Block 7 downtime, top 3">Block 7 downtime, top 3</a><a href="#" class="px-2 py-1.5 rounded text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors font-body-spec text-xs block truncate" title="WELL-0001 spills, last 4 years">WELL-0001 spills, last 4 years</a><a href="#" class="px-2 py-1.5 rounded text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors font-body-spec text-xs block truncate" title="Pump jack root-cause wells">Pump jack root-cause wells</a></div></div></div><div class="flex items-center gap-2 pt-space-sm border-t border-surface-container-high"><div class="w-7 h-7 rounded bg-primary flex items-center justify-center text-on-primary font-semibold text-xs">MT</div><div class="flex flex-col overflow-hidden"><span class="text-xs font-body-spec text-on-surface truncate">Michael Turner</span><span class="text-[10px] font-label-mono-tag text-on-surface-variant truncate">Field Engineer</span></div></div></aside><div class="pl-64 min-h-screen flex flex-col"><header class="fixed top-0 left-64 right-0 h-14 bg-surface-container-lowest/95 backdrop-blur-md z-40 border-b border-surface-container-high"><div class="w-full h-full px-space-xl flex items-center justify-between"><div class="flex items-center gap-space-md"><span class="font-headline-panel text-[16px] font-semibold text-on-surface tracking-tight">WELL-0001 Temperature History</span></div><div class="flex items-center gap-space-md"><div class="flex items-center gap-space-xs px-2.5 py-1 rounded bg-surface-container border border-outline-variant text-on-surface-variant font-label-mono-tag text-xs"><span class="">Today: 17 Oct 2026</span></div><div class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container border border-outline-variant text-on-surface font-body-spec text-xs"><span class="material-symbols-outlined text-[16px] text-primary">account_circle</span><span class="">Michael Turner</span></div></div></div></header><main class="w-full pt-14 bg-surface-container-lowest flex-1"><div class="flex flex-col w-full items-center p-space-md md:p-space-xl"><div class="w-full max-w-[880px] flex flex-col gap-space-lg"><div class="flex flex-col items-end w-full"><div class="bg-surface-container rounded-lg p-space-md max-w-[85%] border-l border-surface-container-high shadow-md"><div class="flex items-center justify-between gap-space-lg mb-space-xs pb-space-xs border-b border-surface-container-high/60"><div class="flex items-center gap-space-xs"><span class="w-1.5 h-1.5 rounded-full bg-primary"></span><span class="font-label-mono-tag text-[11px] text-on-surface-variant tracking-wider uppercase">OPERATOR // CREW-A (CONSOLE-04)</span></div><span class="font-label-mono-tag text-[11px] text-on-surface-variant">14:31:02 UTC</span></div><p class="font-body-spec text-on-surface leading-relaxed text-sm">Show a line chart of <span class="inline-flex items-center gap-0.5 px-1.5 py-0.5 rounded bg-primary-container/10 text-primary-container font-label-mono-tag text-xs font-semibold hover:bg-primary-container/20 transition-colors cursor-pointer select-none"><span class="material-symbols-outlined text-[13px]">tag</span>WELL-0001</span> wellhead temperature against air temperature for the last 13 weeks, and mark when it was not producing oil.</p></div></div><article class="relative w-full bg-surface-container-low rounded-lg p-space-lg md:p-space-xl flex flex-col gap-space-lg shadow-xl" style="box-shadow: 0 4px 20px -2px rgba(0,0,0,0.5);"><div class="absolute left-0 top-0 bottom-0 w-[2.5px] bg-primary rounded-l"></div><header class="flex flex-wrap items-center justify-between gap-space-md pb-space-sm border-b border-surface-container-high"><div class="flex items-center gap-space-md flex-wrap"><div class="flex items-center gap-space-xs"><div class="w-6 h-6 rounded bg-primary/10 flex items-center justify-center text-primary"><span class="material-symbols-outlined text-[16px]">smart_toy</span></div><span class="font-headline-panel text-[15px] font-semibold text-on-surface tracking-tight">Asset Intelligence Copilot</span></div></div><div class="flex items-center gap-space-md font-label-mono-tag text-[11px] text-on-surface-variant"><span class="">14:31:05 UTC</span></div></header><section class="font-body-prose text-on-surface text-[15px] leading-relaxed flex flex-col gap-space-sm"><p class=""><span class="inline-flex items-center px-1.5 py-0.2 rounded bg-primary-container/10 text-primary-container font-label-mono-tag text-xs font-semibold mr-1">WELL-0001</span> was not producing oil on <strong class="text-on-surface font-semibold font-label-mono-tag">8 Oct</strong> and <strong class="text-on-surface font-semibold font-label-mono-tag">15 Oct</strong>. The wellhead was only <strong class="text-secondary-container font-semibold font-label-mono-tag">3.2 °C above air</strong> on 15 Oct.</p></section><div class="bg-surface-container rounded-lg overflow-hidden flex flex-col shadow-inner"><div class="bg-surface-container-high px-space-md py-space-sm flex flex-wrap items-center justify-between gap-space-sm border-b border-surface-container-highest"><a class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container text-primary hover:bg-surface-container-high transition-colors font-label-mono-tag text-xs border-l-2 border-primary" href="#"><span class="material-symbols-outlined text-[14px]">description</span><span class="">INS-0001-0203</span></a><a class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container text-primary hover:bg-surface-container-high transition-colors font-label-mono-tag text-xs border-l-2 border-primary" href="#"><span class="material-symbols-outlined text-[14px]">description</span><span class="">CTX-0001-003</span></a></div><div class="relative w-full p-space-sm md:p-space-md overflow-x-auto bg-surface-container-lowest/80 select-none"><svg aria-label="13-week thermal telemetry line chart" class="w-full h-auto min-w-[700px] block" preserveAspectRatio="xMidYMid meet" role="img" viewBox="0 0 840 320"><defs><linearGradient id="anomalyGradient" x1="0%" x2="0%" y1="0%" y2="100%"><stop offset="0%" stop-color="#F43F5E" stop-opacity="0.18"></stop><stop offset="100%" stop-color="#F43F5E" stop-opacity="0.04"></stop></linearGradient><pattern height="20" id="subGrid" patternUnits="userSpaceOnUse" width="60"><line stroke="#1E2733" stroke-dasharray="2 4" stroke-width="0.5" x1="0" x2="60" y1="20" y2="20"></line></pattern></defs><line stroke="#1E2733" stroke-width="1" x1="48" x2="800" y1="24" y2="24"></line><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="end" x="42" y="28">80</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="start" x="806" y="28">80</text><line stroke="#1E2733" stroke-width="1" x1="48" x2="800" y1="83" y2="83"></line><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="end" x="42" y="87">60</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="start" x="806" y="87">60</text><line stroke="#1E2733" stroke-width="1" x1="48" x2="800" y1="142" y2="142"></line><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="end" x="42" y="146">40</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="start" x="806" y="146">40</text><line stroke="#1E2733" stroke-width="1" x1="48" x2="800" y1="201" y2="201"></line><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="end" x="42" y="205">20</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="start" x="806" y="205">20</text><line stroke="#263140" stroke-width="1.5" x1="48" x2="800" y1="260" y2="260"></line><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="end" x="42" y="264">0</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="11" text-anchor="start" x="806" y="264">0</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="10" font-weight="600" x="48" y="14">°C</text><text fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="10" font-weight="600" text-anchor="end" x="800" y="14">°C</text><rect fill="url(#anomalyGradient)" height="236" rx="2" width="110" x="670" y="24"></rect><line opacity="0.6" stroke="#F43F5E" stroke-dasharray="3 3" stroke-width="1.2" x1="670" x2="670" y1="24" y2="260"></line><line opacity="0.6" stroke="#F43F5E" stroke-dasharray="3 3" stroke-width="1.2" x1="780" x2="780" y1="24" y2="260"></line><g transform="translate(675, 34)"><rect fill="#121820" height="20" rx="3" stroke="#F43F5E" stroke-width="1" width="100" x="0" y="0"></rect><circle cx="8" cy="10" fill="#F43F5E" r="3"></circle><text fill="#F43F5E" font-family="'IBM Plex Mono', monospace" font-size="9" font-weight="600" letter-spacing="0.02em" x="16" y="14">Not producing</text></g><path d="M 72 162.3 L 129 159.7 L 186 156.1 L 243 160.2 L 300 164.1 L 357 168.8 L 414 173.2 L 471 178.5 L 528 186.8 L 585 194.8 L 642 202.4 L 699 209.2 L 756 214.5" fill="none" stroke="#38BDF8" stroke-dasharray="4 3" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path><g fill="#38BDF8" opacity="0.9"><circle cx="72" cy="162.3" r="2.5"></circle><circle cx="129" cy="159.7" r="2.5"></circle><circle cx="186" cy="156.1" r="2.5"></circle><circle cx="243" cy="160.2" r="2.5"></circle><circle cx="300" cy="164.1" r="2.5"></circle><circle cx="357" cy="168.8" r="2.5"></circle><circle cx="414" cy="173.2" r="2.5"></circle><circle cx="471" cy="178.5" r="2.5"></circle><circle cx="528" cy="186.8" r="2.5"></circle><circle cx="585" cy="194.8" r="2.5"></circle><circle cx="642" cy="202.4" r="2.5"></circle><circle cx="699" cy="209.2" r="2.5"></circle><circle cx="756" cy="214.5" r="3" stroke="#0E141C" stroke-width="1"></circle></g><path d="M 72 50.5 L 129 46.7 L 186 44.3 L 243 48.1 L 300 52.9 L 357 56.4 L 414 59.1 L 471 64.1 L 528 71.2 L 585 77.9 L 642 86.2 L 699 203.6 L 756 205.1 L 756 260 L 72 260 Z" fill="url(#anomalyGradient)" opacity="0.1"></path><path d="M 72 50.5 L 129 46.7 L 186 44.3 L 243 48.1 L 300 52.9 L 357 56.4 L 414 59.1 L 471 64.1 L 528 71.2 L 585 77.9 L 642 86.2 L 699 203.6 L 756 205.1" fill="none" stroke="#FB923C" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path><g fill="#FB923C"><circle cx="72" cy="50.5" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="129" cy="46.7" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="186" cy="44.3" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="243" cy="48.1" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="300" cy="52.9" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="357" cy="56.4" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="414" cy="59.1" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="471" cy="64.1" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="528" cy="71.2" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="585" cy="77.9" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="642" cy="86.2" r="3.5" stroke="#121820" stroke-width="1.5"></circle><circle cx="699" cy="203.6" r="4.5" stroke="#F43F5E" stroke-width="2"></circle><circle cx="756" cy="205.1" r="5" stroke="#F43F5E" stroke-width="2.5"></circle></g><g fill="#8B98A8" font-family="'IBM Plex Mono', monospace" font-size="10" text-anchor="middle"><line stroke="#263140" stroke-width="1" x1="72" x2="72" y1="260" y2="266"></line><text x="72" y="278">23 Jul</text><line stroke="#263140" stroke-width="1" x1="129" x2="129" y1="260" y2="266"></line><text x="129" y="278">30 Jul</text><line stroke="#263140" stroke-width="1" x1="186" x2="186" y1="260" y2="266"></line><text x="186" y="278">6 Aug</text><line stroke="#263140" stroke-width="1" x1="243" x2="243" y1="260" y2="266"></line><text x="243" y="278">13 Aug</text><line stroke="#263140" stroke-width="1" x1="300" x2="300" y1="260" y2="266"></line><text x="300" y="278">20 Aug</text><line stroke="#263140" stroke-width="1" x1="357" x2="357" y1="260" y2="266"></line><text x="357" y="278">27 Aug</text><line stroke="#263140" stroke-width="1" x1="414" x2="414" y1="260" y2="266"></line><text x="414" y="278">3 Sep</text><line stroke="#263140" stroke-width="1" x1="471" x2="471" y1="260" y2="266"></line><text x="471" y="278">10 Sep</text><line stroke="#263140" stroke-width="1" x1="528" x2="528" y1="260" y2="266"></line><text x="528" y="278">17 Sep</text><line stroke="#263140" stroke-width="1" x1="585" x2="585" y1="260" y2="266"></line><text x="585" y="278">24 Sep</text><line stroke="#263140" stroke-width="1" x1="642" x2="642" y1="260" y2="266"></line><text x="642" y="278">1 Oct</text><line stroke="#F43F5E" stroke-width="1.5" x1="699" x2="699" y1="260" y2="266"></line><text fill="#F43F5E" font-weight="600" x="699" y="278">8 Oct</text><line stroke="#F43F5E" stroke-width="1.5" x1="756" x2="756" y1="260" y2="266"></line><text fill="#F43F5E" font-weight="600" x="756" y="278">15 Oct</text></g><text fill="#8B98A8" font-family="'IBM Plex Sans', sans-serif" font-size="11" font-weight="500" letter-spacing="0.04em" text-anchor="middle" x="414" y="302">Inspection date (2026)</text><line opacity="0.8" stroke="#38BDF8" stroke-dasharray="2 2" stroke-width="1" x1="756" x2="756" y1="24" y2="260"></line><g filter="drop-shadow(0 4px 6px rgba(0,0,0,0.5))" transform="translate(562, 82)"><rect fill="#1A222D" height="114" rx="4" stroke="#38BDF8" stroke-width="1" width="180" x="0" y="0"></rect><rect fill="#242a33" height="24" rx="4" width="180" x="0" y="0"></rect><text fill="#DDE3EE" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" x="10" y="16">15 Oct 2026 · Wk 13</text><circle cx="14" cy="38" fill="#FB923C" r="3.5"></circle><text fill="#8B98A8" font-family="'IBM Plex Sans', sans-serif" font-size="11" x="24" y="42">Wellhead:</text><text fill="#FB923C" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" text-anchor="end" x="170" y="42">18.6 °C</text><circle cx="14" cy="56" fill="#38BDF8" r="3"></circle><text fill="#8B98A8" font-family="'IBM Plex Sans', sans-serif" font-size="11" x="24" y="60">Ambient Air:</text><text fill="#38BDF8" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" text-anchor="end" x="170" y="60">15.4 °C</text><line stroke="#263140" stroke-width="1" x1="10" x2="170" y1="69" y2="69"></line><text fill="#8B98A8" font-family="'IBM Plex Sans', sans-serif" font-size="11" font-weight="500" x="24" y="83">Difference (ΔT):</text><text fill="#FBBF24" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="700" text-anchor="end" x="170" y="83">+3.2 °C</text><rect fill="rgba(244, 63, 94, 0.15)" height="16" rx="2" stroke="rgba(244, 63, 94, 0.4)" stroke-width="0.8" width="160" x="10" y="92"></rect><circle cx="18" cy="100" fill="#F43F5E" r="2.5"></circle><text fill="#F43F5E" font-family="'IBM Plex Mono', monospace" font-size="9" font-weight="600" letter-spacing="0.02em" x="26" y="104">STATUS: NOT PRODUCING OIL</text></g></svg></div><div class="px-space-md py-space-sm bg-surface-container-high/40 border-t border-surface-container-high flex items-center gap-space-xs text-xs text-on-surface-variant font-label-mono-tag"><span class="material-symbols-outlined text-[15px] text-primary">info</span><span class="">Wellhead is <strong class="text-on-surface text-secondary-container">3.2 °C above air</strong> on 15 Oct. Only the difference from air counts.</span></div></div><div class="flex flex-col gap-space-xs pt-space-xs"><span class="font-label-mono-tag text-[10px] text-on-surface-variant tracking-wider uppercase">Evidentiary Record Sources:</span><div class="flex flex-wrap items-center gap-space-sm"><a class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container text-primary hover:bg-surface-container-high transition-colors font-label-mono-tag text-xs border-l-2 border-primary" href="#"><span class="material-symbols-outlined text-[14px]">description</span><span class="">INS-0001-0203</span></a><a class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container text-primary hover:bg-surface-container-high transition-colors font-label-mono-tag text-xs border-l-2 border-primary" href="#"><span class="material-symbols-outlined text-[14px]">description</span><span class="">CTX-0001-003</span></a></div></div><footer class="pt-space-sm border-t border-surface-container-high flex flex-wrap items-center justify-between gap-space-md font-label-mono-tag text-xs text-on-surface-variant"><div class="flex items-center gap-1.5 flex-wrap"><span class="">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div><div class="flex items-center gap-1"><button class="p-1.5 rounded hover:bg-surface-container text-on-surface-variant hover:text-on-surface transition-colors" title="Copy raw synthesis" type="button"><span class="material-symbols-outlined text-[17px]">content_copy</span></button><button class="p-1.5 rounded hover:bg-surface-container text-on-surface-variant hover:text-secondary transition-colors" title="Validate output" type="button"><span class="material-symbols-outlined text-[17px]">thumb_up</span></button><button class="p-1.5 rounded hover:bg-surface-container text-on-surface-variant hover:text-error transition-colors" title="Report anomaly discrepancy" type="button"><span class="material-symbols-outlined text-[17px]">thumb_down</span></button></div></footer></article><div class="w-full bg-surface-container rounded-lg p-space-sm border-t border-surface-container-high shadow-lg"><form class="flex items-center gap-space-sm" onsubmit="event.preventDefault();"><div class="flex items-center pl-space-sm text-on-surface-variant"><span class="material-symbols-outlined text-[20px] text-primary">terminal</span></div><input class="flex-1 bg-surface-container-lowest text-on-surface placeholder:text-on-surface-variant/60 font-body-spec text-sm px-space-md py-2.5 rounded focus:outline-none focus:ring-1 focus:ring-primary transition-all" placeholder="Ask Copilot: 'Run choke manifold pressure correlation on WELL-0001' or query SCADA event bus..." type="text"><button class="bg-primary hover:bg-primary-container text-on-primary-fixed w-10 h-10 rounded flex items-center justify-center transition-colors cursor-pointer" type="submit"><span class="material-symbols-outlined text-[20px] text-on-primary-fixed">arrow_forward</span></button></form></div></div></div></main></div>

</body></html>
```

15. well_status_card_asset_intelligence
```
<!DOCTYPE html><html class="dark" lang="en" style=""><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Asset Intelligence - Assistant Message Component Spec</title>
<!-- Google Fonts: IBM Plex Sans & IBM Plex Mono -->
<link href="https://fonts.googleapis.com" rel="preconnect">
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&amp;family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest"></script>
<script id="tailwind-config">
tailwind.config = {
darkMode: 'class',
theme: {
extend: {
colors: {
bg: '#0B0F14',
surface: '#121820',
'raised-surface': '#1A222D',
border: '#263140',
hairline: '#1E2733',
'primary-text': '#E6EDF3',
'secondary-text': '#8B98A8',
'disabled-text': '#5B6675',
'signal-cyan': '#38BDF8',
'status-ok': '#34D399',
'status-warn': '#FBBF24',
'status-crit': '#F43F5E',
'status-unconfirmed': '#A78BFA',
'status-neutral': '#94A3B8',
},
fontFamily: {
sans: ['"IBM Plex Sans"', 'sans-serif'],
mono: ['"IBM Plex Mono"', 'monospace'],
}
}
}
}
</script>
<style>
body {
background-color: #0B0F14;
color: #E6EDF3;
font-family: 'IBM Plex Sans', sans-serif;
}
.mono-num {
font-family: 'IBM Plex Mono', monospace;
font-variant-numeric: tabular-nums;
}
/* Custom tooltip styling */
.has-tooltip:hover .tooltip-box {
opacity: 1;
visibility: visible;
transform: translateY(-4px);
}
</style>
<meta content="web_standard" name="shell-type"></head>
<body class="min-h-screen p-6 md:p-12 flex flex-col items-center justify-start antialiased selection:bg-[#38BDF8]/20 selection:text-[#38BDF8]">
<!-- Context / Component Stage Header -->
<header class="w-full max-w-[880px] mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#263140] pb-4"><div class="flex items-center gap-3">
<h1 class="text-lg font-semibold tracking-tight text-[#E6EDF3]">Well Status Card</h1>
</div>
<div class="flex items-center gap-2 font-mono text-xs">
<span class="px-2.5 py-1 rounded bg-[#121820] border border-[#263140] text-[#8B98A8]">
Today: <span class="text-[#E6EDF3]">17 Oct 2026</span>
</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-[#121820] border border-[#263140] text-[#8B98A8]">
<span class="material-symbols-outlined text-[14px] text-[#38BDF8]">person</span>
<span class="text-[#E6EDF3]">Michael Turner</span>
</span>
</div></header>
<!-- Query Context Visual (User Question Plate) -->
<div class="w-full max-w-[880px] mb-4 flex justify-end">
<div class="max-w-[620px] rounded-[10px] bg-[#1A222D] border border-[#263140] px-4 py-3 text-sm text-[#E6EDF3] leading-relaxed shadow-sm">
<div class="flex items-center justify-between gap-4 mb-1">
<span class="text-[11px] font-mono uppercase tracking-wider text-[#8B98A8] flex items-center gap-1.5">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="user" aria-hidden="true" class="lucide lucide-user w-3 h-3 stroke-[1.5]"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> Operator Query
</span>
<span class="text-[11px] font-mono text-[#5B6675]">14:28:11 UTC</span>
</div>
<p class="">
Which rules has <span class="inline-flex items-center px-1.5 py-0.2 rounded bg-[#38BDF8]/10 text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-xs font-medium cursor-pointer hover:bg-[#38BDF8]/20 transition-colors">WELL-0001</span> broken in the last 12 months, and what is still open?
</p>
</div>
</div>
<!-- MAIN COMPONENT: Assistant Message Report Block (880px wide) -->
<main class="w-full max-w-[880px] bg-[#121820] border border-[#263140] rounded-[10px] p-5 relative transition-all shadow-xl" style="border-left: 2px solid #38BDF8;"><div class="flex flex-col w-full">
<!-- Operational Spec Context Bar -->
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 mb-4 border-b border-[#263140]"><div class="flex items-center gap-2">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-[4px] bg-[#1A222D] border border-[#263140] text-[11px] font-mono tracking-wider text-[#38BDF8] uppercase">
<span class="material-symbols-outlined text-[13px]">terminal</span>
COMPONENT SPEC // WELL-STATUS-CARD
</span>
<span class="text-xs font-mono text-[#8B98A8]">· Asset Intelligence Copilot</span>
</div>
<div class="flex items-center gap-2 font-mono text-[11px] text-[#5B6675]">
<span class="">WEEKLY INSPECTION CYCLE</span>
</div></div>
<!-- Operator Query Plate -->
<div class="w-full flex justify-end mb-4">
<div class="w-full max-w-[620px] bg-[#1A222D] border border-[#263140] rounded-[10px] p-[14px]">
<div class="flex items-center justify-between gap-4 mb-1.5">
<span class="text-[11px] font-mono uppercase tracking-wider text-[#8B98A8] flex items-center gap-1.5">
<span class="material-symbols-outlined text-[14px] text-[#8B98A8]">person</span>
OPERATOR QUERY
</span>
<span class="text-[11px] font-mono text-[#5B6675]">14:26:10 UTC</span>
</div>
<p class="text-sm font-sans text-[#E6EDF3] leading-relaxed">
Is <span class="inline-flex items-center px-1.5 py-0.5 rounded-[6px] bg-[#121820] text-[#38BDF8] border border-[#38BDF8]/40 font-mono text-xs font-medium cursor-pointer hover:bg-[#38BDF8]/10 transition-colors">WELL-0001</span> producing oil right now?
</p>
</div>
</div>
<!-- Primary Assistant Report Container -->
<div class="w-full bg-[#121820] border border-[#263140] rounded-[10px] p-5 relative" style="border-left: 2px solid #38BDF8;">
<!-- Engine Header & Meta Bar -->
<div class="flex items-center justify-between pb-3 mb-3 border-b border-[#1E2733] font-mono text-xs text-[#8B98A8]">
<div class="flex items-center gap-2">
<span class="text-[#38BDF8] font-semibold tracking-wider flex items-center gap-1">
<span class="material-symbols-outlined text-[15px]">precision_manufacturing</span>
ASSET INTELLIGENCE ENGINE
</span>
<span class="text-[#5B6675]">/</span>
<span class="text-[11px]">DIAGNOSTIC REPORT</span>
</div>
<div class="flex items-center gap-2 text-[11px] text-[#5B6675]"><span class="">DIAGNOSTIC REPORT</span></div>
</div>
<!-- Direct Answer Statement -->
<div class="text-base font-sans text-[#E6EDF3] leading-[1.55] mb-4">
No. <span class="font-mono font-medium text-[#38BDF8] bg-[#1A222D] px-1.5 py-0.5 rounded-[6px] border border-[#263140]">WELL-0001</span> is not producing oil. Wellhead is only <span class="font-mono font-medium text-[#FBBF24]">3.2 °C</span> above air, below the T200 limit. Planned shut-in since <span class="font-mono text-[#E6EDF3]">7 Oct</span> for rod string replacement, back around <span class="font-mono text-[#E6EDF3]">20 Oct</span> (note by Jake Morales).
</div>
<!-- Inline Status Card: Shut-in / Not Producing -->
<div class="w-full bg-[#161C24] border border-[#263140] rounded-[10px] p-5 relative overflow-hidden" style="border-top: 4px solid #FBBF24;">
<!-- Card Row 1: Identification & Primary Status Badge -->
<div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 pb-4 border-b border-[#1E2733]">
<div class="flex flex-col">
<div class="flex items-center gap-2">
<span class="text-[12px] font-mono uppercase tracking-[0.04em] text-[#8B98A8]">WELL-0001</span>
<span class="px-1.5 py-0.2 rounded bg-[#1A222D] border border-[#263140] text-[10px] font-mono text-[#5B6675]">API #42-301-34201</span>
</div>
<h2 class="text-xl font-semibold font-sans text-[#E6EDF3] mt-0.5 tracking-tight">Well 0001</h2>
<span class="text-sm font-sans text-[#8B98A8] mt-0.5">Southwest Block 23 · T200</span>
</div>
<!-- Warning Status Pill -->
<div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-[6px] border border-[#FBBF24] self-start sm:self-auto" style="background-color: rgba(251, 191, 36, 0.12);">
<span class="material-symbols-outlined text-[16px] text-[#FBBF24]">pause_circle</span>
<span class="font-sans font-semibold text-sm text-[#FBBF24] tracking-wide uppercase">Not producing oil</span>
</div>
</div>
<!-- Card Row 2: Telemetry Metrics & Delta Gauge -->
<div class="py-4 grid grid-cols-1 md:grid-cols-12 gap-4 items-center"><div class="md:col-span-12 flex flex-col justify-center"><div class="text-[12px] font-sans font-semibold uppercase tracking-[0.04em] text-[#8B98A8] flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-[#8B98A8]">thermostat</span>Wellhead above air</div><div class="flex items-baseline gap-2"><span class="text-[28px] font-mono font-semibold tabular-nums text-[#FBBF24] leading-tight">3.2 °C</span></div></div></div>
<!-- Card Row 3: Operational Badges with Triple-Redundancy -->
<div class="pt-3 pb-4 flex flex-wrap items-center gap-2"><div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] border border-[#FBBF24] text-xs font-sans font-medium" style="background-color: rgba(251, 191, 36, 0.12);">
<span class="material-symbols-outlined text-[14px] text-[#FBBF24]">schedule</span>
<span class="text-[#FBBF24]">Planned shut-in</span>
</div>
<div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] border border-[#94A3B8] text-xs font-sans font-medium" style="background-color: rgba(148, 163, 184, 0.12);">
<span class="material-symbols-outlined text-[14px] text-[#94A3B8]">search</span>
<span class="text-[#94A3B8]">Suggest field check</span>
</div></div>
<!-- Card Row 4: Last Inspection Metadata & Direct Link -->
<div class="pt-3.5 border-t border-[#1E2733] flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
<div class="flex items-center flex-wrap gap-2">
<span class="text-[11px] font-mono uppercase tracking-wider text-[#8B98A8]">LAST INSPECTION:</span>
<a class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#263140] font-mono text-[11px] font-medium transition-colors" href="#INS-0001-0203">
<span class="material-symbols-outlined text-[12px]">fact_check</span>
INS-0001-0203
</a>
<span class="font-mono text-[#E6EDF3]">15 Oct 2026</span>
<span class="text-[#5B6675]">·</span>
<span class="text-[#8B98A8]">by Ryan Brooks</span>
</div>

</div>
</div>
<!-- Assistant Message Sources & Evidence Rail -->
<div class="mt-4 pt-3.5 border-t border-[#1E2733] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
<div class="flex items-center flex-wrap gap-2 text-xs">
<span class="text-[11px] font-mono uppercase text-[#8B98A8] tracking-wider">EVIDENCE SOURCES:</span>
<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] border border-[#263140] text-[#38BDF8] font-mono text-[11px]">
<span class="material-symbols-outlined text-[12px]">description</span> INS-0001-0203
</span>
<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] border border-[#263140] text-[#38BDF8] font-mono text-[11px]"><span class="material-symbols-outlined text-[12px]">sticky_note_2</span> CTX-0001-003</span>
</div>
<!-- Action Cluster -->
<div class="flex items-center gap-1.5 self-end sm:self-auto text-[#8B98A8]">
<button aria-label="Copy Output" class="p-1.5 rounded-[4px] hover:bg-[#1A222D] hover:text-[#E6EDF3] transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">content_copy</span>
</button>
<button aria-label="Helpful" class="p-1.5 rounded-[4px] hover:bg-[#1A222D] hover:text-[#E6EDF3] transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">thumb_up</span>
</button>
<button aria-label="Unhelpful" class="p-1.5 rounded-[4px] hover:bg-[#1A222D] hover:text-[#E6EDF3] transition-colors" type="button">
<span class="material-symbols-outlined text-[16px]">thumb_down</span>
</button>
<div class="h-3.5 w-[1px] bg-[#263140] mx-1"></div>
<button class="inline-flex items-center gap-1 px-2 py-1 rounded-[4px] bg-[#1A222D] hover:bg-[#263140] text-xs font-mono text-[#8B98A8] hover:text-[#E6EDF3] border border-[#263140] transition-colors" type="button">
<span class="material-symbols-outlined text-[13px]">edit_note</span>
Correct this
</button>
</div>
</div>
<!-- Inference Telemetry Line -->
<div class="mt-2.5 flex items-center justify-between text-[11px] font-mono text-[#5B6675]"><span class="">gemma-4-26b-a4b-it - 1.4 s - tools: well_status</span></div>
</div>
<!-- Operational Variant Reference Stage: Producing Well State -->
<div class="w-full mt-8 pt-5 border-t border-[#263140]">
<div class="flex items-center justify-between mb-3">
<div class="flex items-center gap-2">
<span class="text-xs font-mono font-semibold uppercase tracking-wider text-[#8B98A8]">
VARIANT SPECIFICATION // PRODUCING WELL STATE
</span>
<span class="text-[11px] text-[#5B6675]">· Normal telemetry comparison model</span>
</div>
<span class="text-[11px] font-mono text-[#34D399] flex items-center gap-1">
<span class="w-1.5 h-1.5 rounded-full bg-[#34D399]"></span> OK STATE
</span>
</div>
<!-- Variant Card: WELL-0042 (Producing) -->
<div class="w-full bg-[#161C24] border border-[#263140] rounded-[10px] p-5 relative overflow-hidden" style="border-top: 4px solid #34D399;">
<!-- Variant Row 1 -->
<div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 pb-4 border-b border-[#1E2733]">
<div class="flex flex-col"><div class="flex items-center gap-2"><span class="text-[12px] font-mono uppercase tracking-[0.04em] text-[#8B98A8]">WELL-0164</span><span class="px-1.5 py-0.2 rounded bg-[#1A222D] border border-[#263140] text-[10px] font-mono text-[#5B6675]">API #42-301-44910</span></div><h3 class="text-xl font-semibold font-sans text-[#E6EDF3] mt-0.5 tracking-tight">Well 0164</h3><span class="text-sm font-sans text-[#8B98A8] mt-0.5">Northeast Block 8 · T200</span></div>
<!-- OK Status Pill -->
<div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-[6px] border border-[#34D399] self-start sm:self-auto" style="background-color: rgba(52, 211, 153, 0.12);">
<span class="material-symbols-outlined text-[16px] text-[#34D399]">play_arrow</span>
<span class="font-sans font-semibold text-sm text-[#34D399] tracking-wide uppercase">Producing oil</span>
</div>
</div>
<!-- Variant Row 2: Metrics -->
<div class="py-4 grid grid-cols-1 md:grid-cols-12 gap-4 items-center"><div class="md:col-span-12 flex flex-col justify-center"><div class="text-[12px] font-sans font-semibold uppercase tracking-[0.04em] text-[#8B98A8] flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-[#8B98A8]">thermostat</span>Wellhead above air</div><div class="flex items-baseline gap-2"><span class="text-[28px] font-mono font-semibold tabular-nums text-[#34D399] leading-tight">21.1 °C</span></div></div></div>
<!-- Variant Row 3: Badges -->
<div class="pt-3 pb-4 flex flex-wrap items-center gap-2"><div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] border border-[#FBBF24] text-xs font-sans font-medium" style="background-color: rgba(251, 191, 36, 0.12);">
<span class="material-symbols-outlined text-[14px] text-[#FBBF24]">schedule</span>
<span class="text-[#FBBF24]">Planned shut-in</span>
</div>
<div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-[6px] border border-[#94A3B8] text-xs font-sans font-medium" style="background-color: rgba(148, 163, 184, 0.12);"><span class="material-symbols-outlined text-[14px] text-[#34D399]">verified</span>
<span class="text-[#34D399]">Weekly inspection pass</span></div></div>
<!-- Variant Row 4: Inspection Footer -->
<div class="pt-3.5 border-t border-[#1E2733] flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
<div class="flex items-center flex-wrap gap-2">
<span class="text-[11px] font-mono uppercase tracking-wider text-[#8B98A8]">LAST INSPECTION:</span>
<a class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#263140] font-mono text-[11px] font-medium transition-colors" href="#INS-0042-0199">
<span class="material-symbols-outlined text-[12px]">fact_check</span>
INS-0042-0199
</a>
<span class="font-mono text-[#E6EDF3]">14 Oct 2026</span>
<span class="text-[#5B6675]">·</span>
<span class="text-[#8B98A8]">by Jessica Reed</span>
</div>
<span class="text-[11px] font-mono text-[#34D399] flex items-center gap-1">
<span class="material-symbols-outlined text-[13px]">check_circle</span>
SYSTEM CONGRUENT
</span>
</div>
</div>
</div>
</div></main>
<!-- SECTION: Flag Variants Documentation & Showcase -->
<section aria-labelledby="flag-variants-heading" class="w-full max-w-[880px] mt-10 pt-6 border-t border-[#263140]">
<div class="flex items-center justify-between mb-4">
<div class="flex items-center gap-2">
<h3 class="text-xs font-mono font-semibold uppercase tracking-wider text-[#8B98A8]" id="flag-variants-heading">
Flag Variants
</h3>
<span class="text-[11px] text-[#5B6675]">· Operational indicator banners specified by the design system</span>
</div>
<span class="text-[11px] font-mono text-[#8B98A8]">3 STATES PRESENTED</span>
</div>
<div class="flex flex-col gap-3">
<!-- Variant 1: CONFLICT (Warning - Amber) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#FBBF24]"></span>
CONFLICT FLAG (Warning State · 12% Tinted Fill · 1px Solid Border)
</span>
<span class="text-[#5B6675]">split-arrows icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#FBBF24]/[0.12] border border-[#FBBF24] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#FBBF24] flex items-center justify-center">
<!-- split-arrows icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="git-fork" aria-hidden="true" class="lucide lucide-git-fork w-4 h-4 stroke-[1.5]"><circle cx="12" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><circle cx="18" cy="6" r="3"></circle><path d="M18 9v2c0 .6-.4 1-1 1H7c-.6 0-1-.4-1-1V9"></path><path d="M12 12v3"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#FBBF24] flex-shrink-0">CONFLICT</span>
<span class="text-[#E6EDF3] leading-tight font-normal">Inspection note 'Pump jack not moving.' (Tyler Hughes) disagrees with the corrected reading of 41.0 C. Please confirm.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors" href="#INS-0164-0205">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="clipboard-check" aria-hidden="true" class="lucide lucide-clipboard-check w-3 h-3 stroke-[1.5]"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"></rect><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><path d="m9 14 2 2 4-4"></path></svg> INS-0164-0205
</a>
</div>
</article>
</div>
<!-- Variant 2: UNCONFIRMED (Violet - Dashed Border) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#A78BFA]"></span>
UNCONFIRMED FLAG (Violet State · 12% Tinted Fill · 1px DASHED Border)
</span>
<span class="text-[#5B6675]">question icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#A78BFA]/[0.12] text-xs" style="border: 1px dashed #A78BFA;">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#A78BFA] flex items-center justify-center">
<!-- question icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="help-circle" aria-hidden="true" class="lucide lucide-help-circle w-4 h-4 stroke-[1.5]"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><path d="M12 17h.01"></path></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#A78BFA] flex-shrink-0">UNCONFIRMED</span>
<span class="text-[#E6EDF3] leading-tight font-normal">Tyler Hughes says WELL-0175 is running fine. The 15 Oct inspection shows 0.4 C above air. Kept on record, awaiting confirmation.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0">
<span class="text-[11px] font-mono text-[#8B98A8] uppercase tracking-wider hidden md:inline">Source:</span>
<a class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] hover:bg-[#263140] text-[#38BDF8] border border-[#38BDF8]/30 font-mono text-[11px] font-medium transition-colors" href="#INS-0175-0205">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="clipboard-check" aria-hidden="true" class="lucide lucide-clipboard-check w-3 h-3 stroke-[1.5]"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"></rect><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><path d="m9 14 2 2 4-4"></path></svg> INS-0175-0205
</a>
</div>
</article>
</div>
<!-- Variant 3: NO CAUSE (Neutral - Empty Circle Icon) -->
<div class="rounded-[10px] bg-[#121820] border border-[#263140] p-3.5 flex flex-col gap-2">
<div class="text-[11px] font-mono uppercase text-[#8B98A8] flex items-center justify-between">
<span class="flex items-center gap-1.5">
<span class="w-2 h-2 rounded-full bg-[#94A3B8]"></span>
NO CAUSE FLAG (Neutral State · 12% Tinted Fill · 1px Solid Border)
</span>
<span class="text-[#5B6675]">empty-circle icon</span>
</div>
<article class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-[8px] bg-[#94A3B8]/[0.12] border border-[#94A3B8] text-xs">
<div class="flex items-center gap-2.5 min-w-0">
<div class="flex-shrink-0 text-[#94A3B8] flex items-center justify-center">
<!-- empty-circle icon -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" data-lucide="circle" aria-hidden="true" class="lucide lucide-circle w-4 h-4 stroke-[1.5]"><circle cx="12" cy="12" r="10"></circle></svg>
</div>
<span class="font-mono font-semibold uppercase tracking-wider text-[#94A3B8] flex-shrink-0">NO CAUSE</span>
<span class="text-[#E6EDF3] leading-tight font-normal">No recorded reason for the stop at WELL-0175. Suggest a field check.</span>
</div>
<div class="flex items-center gap-1.5 flex-shrink-0 self-end sm:self-auto pl-6 sm:pl-0"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[6px] bg-[#1A222D] text-[#94A3B8] border border-[#263140] font-mono text-[11px]">
<span class="material-symbols-outlined text-[12px]">search</span>
Suggest field check
</span></div>
</article>
</div>
</div>
</section>
<!-- Technical Spec Footer -->
<footer class="w-full max-w-[880px] mt-8 text-center text-xs font-mono text-[#5B6675] pb-8 border-t border-[#1E2733] pt-4 flex flex-col sm:flex-row justify-between items-center gap-2">
<div class="">ASSET INTELLIGENCE COPILOT · DESIGN SYSTEM REV 1.0</div>
<div class="text-[#8B98A8]">IBM PLEX SANS &amp; MONO · 4PX SYSTEM · NO DROP SHADOWS</div>
</footer>
<script>
// Initialize Lucide icons
lucide.createIcons();
</script>

</body></html>
```