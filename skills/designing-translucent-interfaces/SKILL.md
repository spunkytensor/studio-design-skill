---
name: designing-translucent-interfaces
description: "Designs and reviews calm, translucent layered interfaces using a canonical system of light/dark materials, orange primary actions, typography, components, responsive layouts, and accessible motion. Use when creating or refining UI in this visual style."
license: Unlicense
---

# Translucent interface design guide

Released into the public domain under the [Unlicense](UNLICENSE), provided "AS IS", without warranty of any kind.

Build calm, precise interfaces with translucent layered surfaces, soft edge highlights and content that appears to float above the canvas. The interface is the frame, not the picture.

This is one product-neutral design system. Apply it to the host product's actual tasks and content; it does not prescribe a framework, business workflow, logo or backend. The aesthetic uses frosted glass, layered translucency and soft highlights, implemented through CSS materials rather than platform-specific APIs or physical lens simulation.

## 1. Implementation workflow

1. Identify the screen's essential content, one next action, advanced controls, and empty/loading/error/success states. Inspect the host app's existing components and accessibility conventions.
2. Implement the semantic tokens below once in the host theme layer. Reuse them everywhere; do not introduce alternative palettes or component-specific accent values.
3. Compose the screen from the material, type, component and layout rules in this guide. Put advanced controls behind **Customize** or **Advanced**.
4. Implement light, dark, System, reduced-transparency and reduced-motion behavior together, not as later cosmetic variants.
5. Verify the actual rendered and interactive states using §12. If a requested design conflicts with this guide, ask which should be canonical rather than retaining multiple design profiles.

## 2. Visual hierarchy

- Keep the user's content dominant. Use quiet neutral chrome, generous whitespace and restrained blue, peach and lavender light behind the glass.
- Use four materials: **Canvas**, **Glass**, **Glass elevated**, **Ink**. Controls use neutral fills within those materials, not extra material families.
- Show **one orange primary per view** when there is a next action. Use zero on informational or settings views without a task decision. Navigation stays neutral when the task owns the primary.
- When a sheet or dialog owns the decision, remove the underlying action's orange treatment or hide it. Never render two competing orange calls to action, including duplicate desktop/mobile controls.
- Orange focus rings are the exception to the one-orange-element rule. Semantic red error/destructive text and status dots are not decorative accents.
- Content is left-aligned inside panels. Center alignment is reserved for a focused entry moment, empty state or completion moment—not every heading, field or setting.
- Keep advanced controls out of the initial view. A quiet caption can summarize their current values; the disclosure opens in place and does not unexpectedly navigate away.

## 3. Canonical light and dark tokens

Declare these as CSS custom properties. Light is the default; override the dark column under `html[data-theme="dark"]`. Set `color-scheme` to the resolved theme so native controls match.

| Token | Light | Dark |
| --- | --- | --- |
| `--canvas` | `#D5DCE5` | `#0C0E12` |
| `--ink-1` | `#151D29` | `rgba(242,243,245,.92)` |
| `--ink-2` | `#354154` | `rgba(242,243,245,.60)` |
| `--ink-3` | `#465367` | `rgba(242,243,245,.38)` |
| `--hair` | `rgba(35,48,68,.26)` | `rgba(242,243,245,.10)` |
| `--fill` | `rgba(35,48,68,.13)` | `rgba(242,243,245,.07)` |
| `--fill-2` | `rgba(35,48,68,.20)` | `rgba(242,243,245,.12)` |
| `--glass` | `rgba(225,231,239,.88)` | `rgba(255,255,255,.08)` |
| `--glass-el` | `rgba(225,231,239,.97)` | `rgba(26,29,36,.70)` |
| `--glass-hi` | `rgba(255,255,255,.24)` | `rgba(255,255,255,.35)` |
| `--edge-top` | `rgba(255,255,255,.65)` | `rgba(255,255,255,.38)` |
| `--edge-bot` | `rgba(35,48,68,.20)` | `rgba(255,255,255,.06)` |
| `--el-shadow` | `0 20px 60px rgba(22,32,48,.16)` | `0 20px 60px rgba(0,0,0,.35)` |
| `--field` | `#CDD6E2` | `rgba(255,255,255,.08)` |
| `--field-edge` | `#596A80` | `transparent` |
| `--on-glass-pill` | `rgba(235,240,246,.80)` | `rgba(255,255,255,.14)` |
| `--nav-surface` | `#FFFFFF` | `var(--glass)` |
| `--accent` | `#F26B21` | `#FF7A33` |
| `--accent-2` | `#FFA45E` | `#FFB176` |
| `--on-accent` | `#16181D` | `#16181D` |
| `--ok` | `#236B44` | `#5CC98A` |
| `--warn` | `#806000` | `#E2B23C` |
| `--err` | `#B3332B` | `#FF7B6E` |
| `--blob-1` | `rgba(100,130,255,.38)` | `rgba(80,110,255,.34)` |
| `--blob-2` | `rgba(255,155,100,.30)` | `rgba(255,130,70,.20)` |
| `--blob-3` | `rgba(170,115,245,.30)` | `rgba(150,100,255,.28)` |

Use primary ink for normal content, secondary ink for captions/help/quiet actions, hair for internal separators, fill for controls and fill-2 for neutral hover/pressed emphasis. Dark tertiary ink is for decoration and disabled states only, never real captions or instructions. Light placeholders use opaque tertiary ink; dark placeholders use secondary ink.

The light theme is lower-glare grey-blue glass over a colored canvas, anchored by **white navigation**. Do not turn it into white cards on a white page. Dark elevated glass has deliberately higher opacity than ordinary glass; do not lower it to make overlays look more transparent.

## 4. Material construction

### Canvas

Use `--canvas` for the page and content-stage backing. Add a static, pointer-inert decorative layer behind the UI, fixed with inset −12% and `filter: blur(48px)`. Its background is:

```css
background:
  radial-gradient(38% 42% at 14% 12%, var(--blob-1), transparent 72%),
  radial-gradient(34% 40% at 88% 18%, var(--blob-2), transparent 72%),
  radial-gradient(46% 46% at 55% 100%, var(--blob-3), transparent 72%);
```

Keep these alphas at or below their tokens. Check stacking contexts so the decoration stays visible behind the panels without covering or tinting the user's content. Do not animate the color field.

### Glass

- Background `var(--glass)`, radius 24 px, `position: relative`.
- Standard backdrop filter and any vendor-prefixed equivalent required by supported browsers: `blur(24px) saturate(160%)`.
- Inner highlight: `inset 0 1px 0 var(--glass-hi)`.
- Edge: pointer-inert absolute `::before`, inset 0, inherited radius, padding 1 px and `linear-gradient(180deg, var(--edge-top), var(--edge-bot))`. Cut out the center with content-box/full-box masks using exclude/xor composition. The edge overlaps the highlight; it is not an extra outside border pixel.
- Sheen on large surfaces: pointer-inert `::after` with a `118deg` white gradient, .07 alpha at 0%, clear at 38% and 62%, .035 at 100%. Keep foreground content above the sheen. Never apply it to text or individual icons.
- Ordinary panels have no external drop shadow. Do not add a border and grey shadow to every container.

### Glass elevated

Use `--glass-el`, 40 px blur with 160% saturation, the same edge/sheen, and the inset highlight plus `--el-shadow`. Reserve it for popovers, sheets, decisions and text-heavy surfaces over busy content. Keep glass nesting to at most **panel → overlay**. Never place text directly on blurred imagery without elevated material beneath it.

### Solid and unsupported-filter modes

For reduced transparency, override glass/elevated backgrounds to `#E1E7EF` in light; `#181B22` / `#1E222B` in dark. Light navigation stays white. Remove both prefixed and unprefixed backdrop filters from panels, overlays, pills and modal backdrops. Make translucent control/status surfaces opaque where needed to maintain readability. Layout, hierarchy and focus styling must not change.

Use the same opaque material fallback when backdrop filtering is unavailable. Keep the decorative canvas behind opaque panels; never make essential content depend on translucency, masks or gradients being supported.

## 5. Accent, status and control states

- Primary fill: `linear-gradient(135deg, var(--accent-2), var(--accent))`, text `--on-accent`, subtle inset top highlight. **Never white text on orange.** Keep the gradient on hover; use the highlight for restrained feedback, not a new hue or glow.
- Selected segments use `--on-glass-pill`; active switches, selected-item outlines, edited dots, progress bars and scrubbers use ink. Selection is not another orange highlight.
- Status pills use a 7 px `--ok`, `--warn` or `--err` dot with readable words. Success and warning text stay neutral. Do not turn status fills into saturated banners.
- **Red destructive-action text and error text are allowed.** Use `--err` on a neutral/transparent surface with clear wording; errors explain recovery. If text contrast fails against a busy background, strengthen the surface rather than invent another red. Keep Cancel neutral: dismissal is not deletion.
- Confirm irreversible actions; do not disguise a destructive control as the routine orange next step. An irreversible confirmation may have a red-text decision button and no orange action.
- Neutral hover uses `--fill-2` or a subtly brighter edge. No lift, scale bounce, external shadow change or colored shadow. Active/selected states remain discernible without relying on hover.
- Disabled controls stay in place with reduced emphasis, typically .5 opacity and a non-actionable cursor. Explain the blocking reason in readable adjacent text; disabling must not hide the only explanation.
- On every interactive control use `:focus-visible` with **2 px solid `--accent`, offset 2 px**. Preserve the outline outside clipped/scrolling containers and never remove focus styling for aesthetics.
- Where the accent outline does not reach 3:1 against the adjacent surface—including the canonical light canvas and glass—add a **2 px high-contrast neutral companion ring using `--ink-1`** outside the orange outline. Keep both rings visible and unclipped; the neutral ring must reach at least 3:1 against its adjacent colors. Verify the combined indicator in both themes, over actual composited backgrounds, and in solid mode. Preserve existing material highlights when adding the ring; this focus-only treatment is not a decorative drop shadow.

## 6. Typography, icons and copy

Use a **neutral sans-serif with a tall x-height and open letterforms** for UI and display, with `system-ui, sans-serif` fallbacks. Use a **readable monospace** with a `monospace` fallback and tabular digits for quantitative metadata such as durations, dates, costs and sizes. Supply valid licensed font assets when bundling; do not assume proprietary fonts are available.

| Role | Size | Line height | Tracking | Weight |
| --- | --- | --- | --- | --- |
| Hero | 3.5 rem | 1.05 | −.03 em | 600 |
| Title | 2 rem | 1.15 | −.02 em | 600 |
| Section | 1.25 rem | 1.3 | −.01 em | 600 |
| Body | 1 rem | 1.55 | 0 | 400 |
| Label | .875 rem | 1.4 | 0 | 500 |
| Caption | .75 rem | 1.4 | .01 em | 400, secondary ink |
| Quantitative metadata | .8125 rem mono | 1.4 | 0 | 400, tabular |

Use weights **400/500/600**, choosing no more than two weight roles in one screen where practical. Sentence case everywhere; no all-caps labels, eyebrow labels, or an accented word inside a headline. Keep body lines under 70 characters. Let text wrap and grow with zoom instead of truncating essential instructions.

Icons: 18 px default, 14 px small, 22 px large; unfilled strokes at 1.75 px with round caps/joins, using current ink color. Their interactive target remains at least 44 × 44 px. Icon-only buttons require accessible names; do not use an unexplained gear instead of the word Customize.

Tile selection: use a compact 24 × 24 px checkbox at the upper right, centered within an invisible 44 × 44 px label hit area inset 8 px from the tile edges. Never surround it with a visible badge, glass panel, oversized background, border, or shadow. Preserve accessible names, keyboard focus, and checked/disabled states in both themes.

Name actions by their outcome: “Create collection”, “Apply changes”, “Download file”, not “Submit”. Keep lifecycle language consistent: “Apply changes” → “Applying changes” → “Changes applied”. Errors state what happened and what to do next. Avoid jargon, unexplained identifiers, filler and decorative arrows appended to labels. Only claim “Saved”, completion or autosave when the underlying behavior supports it. The design system must not invent product functionality.

## 7. Layout and responsive rules

- Use an 8 px base grid, with 4 px fine adjustments. Typical component padding 16/20/24 px; larger section gaps 32/48/64 px.
- Desktop top bar: 60 px high, 30 px capsule radius, fixed 16 px from top and sides. Reserve its space so it never covers headings or focused controls.
- Standard content: max width 1280 px, horizontal padding 24 px, starts around 116 px from the top. Focused entry panel: max width 760 px, padding `36px 36px 28px`. Settings/read-heavy column: max width 880 px.
- Collection grid: 3 equal `minmax(0, 1fr)` columns, 24 px column gap and 32 px row gap. At ≤1024 px use 2 columns; at ≤600 px use **1 column** with 24 px gaps.
- Optional detail workspace: 320 px inspector plus a flexible content stage, 16 px gap. At ≤1024 px move the inspector behind a labeled disclosure; keep the user's content visible. Do not add an inspector or timeline to products that do not need one.
- At ≤600 px: content gutters 16 px, panel padding 28 × 20 px, title 1.75 rem, hero `clamp(2rem, 8vw, 3.5rem)`. Stack paired fields and full-width segments. Adapt navigation without shrinking touch targets or producing horizontal overflow.
- On phones, popovers and side sheets become **bottom sheets** with 12 px side gutters, 20 px inner padding, and an internally scrollable body. Keep their header, dismissal and footer reachable at short viewport heights and with the keyboard open.
- Pin the phone task primary near the bottom with **12 px symmetric side gutters**, 48 px minimum height, and bottom offset `max(12px, env(safe-area-inset-bottom))`. Reserve matching page padding. When a sheet owns the task, its footer holds the only primary and the underlying pinned action disappears.
- Place viewport-fixed actions outside backdrop-filter/transform containing blocks, using the host's overlay/portal mechanism where available. Do not accidentally anchor the “fixed” button to a scrolling glass panel.
- Use dynamic viewport sizing and safe areas; work down to **360 px** wide. Long labels, text zoom and the on-screen keyboard must not obscure controls. Center portrait content with canvas beside it rather than stretching or cropping it to fill the phone.

## 8. Component recipes

| Component | Anatomy and dimensions |
| --- | --- |
| Top bar | Glass with `--nav-surface`, quiet navigation, left-aligned identity/back/title, optional neutral status, and only the view's primary if it belongs here |
| Button | Capsule, ≥44 px target/height, 18 px horizontal padding, .9375 rem/500; large 48 px with 24 px horizontal padding; primary weight 600; quiet background transparent |
| Icon button | At least 44 × 44 px, centered ink icon, accessible name; neutral selected/pressed state |
| Segmented control | Neutral capsule track, 3 px inset, 2 px gap, 2–4 named choices; ≥44 px targets, selected on-glass pill, correct pressed/selected semantics |
| Switch | 44 × 26 px visual track, 20 px thumb, ink when on; wrap in ≥44 px target and expose checked state with an associated label |
| Field | Radius 16, `--field`, 1 px `--field-edge`, inner highlight, padding 12 × 16, minimum 48 px; large multiline field at least 112 px desktop / 140 px phone and resizable |
| Dropdown | Trigger and **each opened option ≥48 px high**, option padding 12 × 16, text 1 rem/1.5; wrap long labels; scroll long menus within the viewport; never shrink option targets for compact or desktop layouts |
| Status pill | 28 px visual height, padding 0 × 11, neutral on-glass background, .8125 rem/500, optional 7 px semantic dot; expand target if clickable |
| Grouped list | Rows ≥52 px, label .9375 rem/500 with caption underneath, right-aligned control, separators only between rows; roomy settings rows ≥66 px |
| Thumbnail row | ≥44 px high, 52 × 30 px thumbnail, short label/caption, neutral selected pill and optional 7 px ink edited dot |
| Content tile | 16:9 thumbnail viewport, radius 20, no external shadow; title below with 14 px top and 6 px bottom gap, then one caption line; no redundant card wrapper |
| Popover | 420 px maximum desktop width, radius 24, 20 px padding, elevated, anchored near its trigger and clamped to viewport; quiet close action |
| Sheet | 440 px desktop width, radius 24, 24 px padding, elevated; body scrolls, footer has quiet Cancel and the decision action; bottom-sheet geometry on phones |
| Notice | Radius 16, padding 16, neutral fill, .875 rem/1.5; explicit error/recovery copy, optional red error text, no saturated banner |

Use native interactive elements, not styled spans. Associate fields with labels and help/error text. Popovers for immediate edits should not invent an extra primary; confirmation sheets own the view's decision. Keep controls visible and usable during loading; show real progress within or adjacent to the initiating action without shifting its geometry.

For dropdowns, measure the **open option rows**, not just the closed field. Ordinary OS-rendered
`option` elements may ignore padding and height. Prefer customizable native selects using
`appearance: base-select` on both the control and `::picker(select)` in supporting browsers;
retain the platform picker elsewhere. If uniform row sizing is required on an unsupported
platform, use an accessible tested listbox rather than claiming native option CSS guarantees it.
Keep selection, focus, and disabled states distinct using ink/fill tokens in both themes.
Verify touch selection, arrow keys, Enter, Escape, disabled options, long-label wrapping and
scrolling on short viewports. No dense or hover-only menu variant is allowed.

Closed dropdowns also need cross-engine verification: use explicit 48 px height and minimum
height, `flex-shrink: 0`, and readable text even in dense editor inspectors. Where customizable
selects are unsupported, remove OS trigger styling with `appearance: none` and any
vendor-prefixed equivalent required by supported browsers, and supply a visible caret;
preserve the native picker semantics. Measure actual editor, settings, and compact controls
across supported browser engines and operating systems. A passing popup test in one engine
is not proof that a closed control in another engine or operating system has usable dimensions.


### Vertical rhythm in tabbed inspectors

All sibling editing tabs use the same rhythm, including advanced sections and uploads:
16 px between control groups, 8 px between a visible label and its control, and zero
outer margins on field wrappers. Let the parent gap own spacing; never combine a
16 px wrapper margin with a 16 px parent gap. Stack setting-row labels above controls
in narrow inspectors, using the same label typography as ordinary fields.

Single-line inputs, select triggers and upload fields have a 48 px border-box height.
Buttons and slider targets are at least 44 px. Controls use 1 rem text with 1.5 line
height. Ordinary multiline fields start at 112 px desktop / 140 px phone; their
content may make them taller. Content-fitting prompt fields are an explicit exception:
fit every wrapped line plus one blank line on opening, editing and width changes.
Do not force them to a shared fixed height or add an embedded scrollbar. The complete
inspector scrolls vertically when its content exceeds its available height.

Verify every sibling tab in both themes at desktop and phone widths. Measure computed
wrapper margins, parent gaps, label gaps, and actual control bounding boxes, including
native selects and file inputs. Check expanded advanced controls, long labels, long
prompts, short panels and text zoom. Equal sizing refers to matching control types,
not forcing textareas, sliders, buttons and media players to the same height.

### Imagery and optional time-based controls

Preserve image/video aspect ratios. Use contain for full-content previews; crop collection thumbnails only when it does not misrepresent the item. Portrait thumbnails can sit over a softly blurred copy of themselves; keep that backdrop decorative. Titles and descriptive text sit outside the image; overlaid status text needs a sufficiently opaque material beneath it.

When a product genuinely needs a timeline, use a glass transport strip with tabular time, neutral controls, compact thumbnails, ink selection/playhead and a scrubber. Desktop thumbnails may be 72 px high; mobile reduces them to 48 px and simplifies the transport. Keep interaction targets ≥44 px even when tracks are visually thinner. Dragging and scrubbing follow the pointer directly with no easing.

Do not alter the colors or typography of user-created content merely to match the chrome. Use the host's identity subtly; this system requires no mascot, fixed corner logo or watermark.

## 9. Overlays and state transitions

- Use in-place disclosures and non-modal popovers for optional controls. Keep the triggering context and main content visible.
- Use side sheets for reviewing decisions on desktop; reserve content space where possible rather than hiding the main content. Use bottom sheets on phones.
- Use modal dialogs for consequential approvals and irreversible deletion, not routine navigation or editing. Desktop decisions may be centered, max width 560 px, padding 28 px; phone decisions use bottom-sheet presentation with modal semantics.
- Modal backdrop: restrained dark dimming, `rgba(12,14,18,.48)`; optional 4 px blur only in normal-transparency mode. Contain focus, make the background inert, support Escape when safe, and restore focus to the opener. Non-modal overlays must not falsely trap focus or mark the whole page inert.
- Opening an overlay must not reset work. Preserve pending input through dismissal according to the host product's actual save/commit semantics. Explain destructive consequences before confirmation.
- Empty: concise explanation and the view's next action. Loading: honest stage/status. Error: what failed and recovery. Success: outcome and relevant next step, not confetti or competing actions.
- Progress uses actual measured values or stage-based language and elapsed time. Never invent percentages or durations. Live announcements are throttled to meaningful changes rather than every tick.

## 10. Theme and accessibility preferences

Offer **System / Light / Dark** as a neutral segmented control. Resolve System through `prefers-color-scheme`, respond to live OS changes, and persist explicit choices using the host app's preference mechanism. Validate stored values; missing/invalid values fall back to System. Handle unavailable storage without breaking the current visit. Resolve appearance before first paint where practical to avoid a light/dark flash.

Honor `prefers-reduced-transparency` and `prefers-reduced-motion` automatically. Optional manual reduction controls may request more reduction but must not silently override an OS accessibility request. Represent effective state consistently, for example with `data-solid="1"` and `data-motion="reduce"`; implement the styles rather than treating attributes as sufficient.

Meet WCAG 2.2 AA: normal text ≥4.5:1, large text ≥3:1, and meaningful non-text controls/focus indicators ≥3:1 against adjacent colors. Measure actual composited glass over busy content in both themes. Token values alone are not a contrast certification. Keep visible labels, programmatic names, logical keyboard order, status words and ≥44 px targets. Support keyboard operations equivalent to pointer interactions and retain essential content at zoom/reflow.

## 11. Motion and anti-patterns

Motion is restrained and tied to user actions. At most one 300 ms ease-out settle on page load. Overlays may enter with opacity and scale .96 → 1 over 220 ms using `cubic-bezier(0.2, 0.8, 0.2, 1)`. Do not animate canvas blobs, loop glints or add hover lift. Reduced motion removes animations/transitions and smooth scrolling entirely; all states remain understandable instantly.

Reject: competing orange actions; white text on orange; neon glow; colored drop shadows; decorative gradient headlines; deep stacks of glass; text over busy imagery without elevated backing; identical bordered/shadowed cards everywhere; all-caps or eyebrow labels; heavier-than-600 UI labels; red Cancel; advanced settings exposed by default; nonfunctional cosmetic controls; inaccessible tiny targets; fabricated progress; source-product workflows or branding imposed on an unrelated app.

## 12. Verification and delivery

1. Run the host app's relevant build/type/interaction checks using isolated fixtures. Do not trigger paid services or modify production content just to obtain screenshots.
2. Render **light and dark at 1440 × 900 and 390 × 844**. Check 360 px width, short viewports, text zoom, and both sides of 1024/600 px breakpoints.
3. Include populated content, empty/loading/error/disabled states and every changed overlay. Inspect elevated text over the busiest representative content, not only a blank canvas.
4. Exercise theme selection, persisted reload, System following live OS changes, storage failure, reduced transparency, reduced motion and the unsupported-filter fallback. Check computed styles and layout, not just preference attributes.
5. Count orange primary actions; inspect focus visibility, red error/destructive contrast, loaded fonts, content aspect ratios, no horizontal overflow, safe-area footer clearance and keyboard-open behavior.
6. Tab through controls, activate them by keyboard, dismiss overlays with Escape and confirm focus restoration. Verify modal background inertness, field/error associations, selected states and meaningful progress announcements.
7. Capture and **inspect** desktop/mobile screenshots. Fix rendering errors and inspect new captures. Report checks actually run, any limitations and a representative inspected screenshot or preview link for UI work. Documentation-only changes need structural/content validation, not a claim that a UI was tested.

## Implementation brief

> Implement [screen/component] using this translucent interface design guide. Layer 1 contains [essentials]; Customize contains [advanced controls]. The view's one primary is “[verb + object]”. Reuse the canonical light/dark material tokens, sans-serif/mono type scale, neutral selection, subtle sheen and 2 px focus ring. Use one-column phone layouts, bottom sheets and a safe-area-aware pinned task primary. Preserve actual product behavior, honor accessibility preferences, and inspect both themes on desktop and phone using isolated fixtures.
