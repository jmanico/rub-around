---
version: alpha
name: rub-around
description: "Independent campus navigation identity with accessible native presentation."
colors:
  primary: "#143E4A"
  surface: "#FFFFFF"
typography:
  heading:
    fontFamily: "system-ui, sans-serif"
    fontSize: 1.5rem
    fontWeight: 700
    lineHeight: 1.25
  body:
    fontFamily: "system-ui, sans-serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "system-ui, sans-serif"
    fontSize: 1rem
    fontWeight: 700
    lineHeight: 1.5
rounded:
  control: 0.5rem
spacing:
  sm: 0.5rem
  md: 1rem
  lg: 1.5rem
components:
  content:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    padding: "{spacing.lg}"
  heading:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.heading}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "{spacing.md}"
  field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "{spacing.sm}"
---

# Design

This file owns the visual and frontend language. Product actions and outcomes are defined by [REQUIREMENTS.md](REQUIREMENTS.md), rendering technology by [AQ-8](ARCHITECTURE.md#aq-8), and rendering/security enforcement by [SC-011](SECURITY.md#sc-011). The frontmatter is the sole definition of the named design tokens.

## Brand

### DQ-1

**RESOLVED.** Adopt the existing identity as an independent project, without implying university endorsement or assuming institutional branding permission. The existing [logo.svg](logo.svg) is a symbolic bent directional path, not a depiction of campus geography. Preserve its proportions and embedded background. No university crest or substitute official mark is used.

## Colors and States

Use only the frontmatter's `primary` and `surface` colors, in either foreground/background order. Both opaque sRGB combinations have a rounded contrast ratio of 11.55:1. Use `primary` on `surface` for text, labels, essential borders, focus outlines, route graphics and the logo; reverse the pair for principal actions. State changes use shape, weight and explicit text. Do not introduce tints, gradients, reduced opacity, image backgrounds or translucent layers.

Essential map labels and route graphics have an opaque `surface` backing. Focus uses a `primary` outline separated from the control by a `surface` gap. The full accessibility target is owned by DQ-4; palette contrast alone is not a conformance result.

## Typography and Layout

### DQ-2

**RESOLVED.** Use the system sans-serif heading, body and label tokens. In the native adapter, one token `rem` maps to 16 platform layout units before user font scaling; system font selection maps to the platform default. Font sizes scale with the user's settings, while spacing and corner radii use the unscaled layout-unit conversion. Line-height multipliers apply to the scaled text size. Do not cap system font scaling.

Use `sm` within a group, `md` around controls and `lg` between groups. Keep a single reading column below 600 layout units. At 600 or more, map and instructions may sit side by side with inputs first in accessibility order. Keep content usable at 320 layout units wide, in portrait and landscape, without requiring horizontal scrolling of text. Map panning is independent of text reflow.

Use a flat layout: whitespace, type and essential borders establish hierarchy; no shadows. Labels remain visible outside fields. Preserve complete building and room identifiers; wrap at surrounding whitespace rather than truncating identifiers. Languages and supported product surfaces are FR-8.1/FR-8.2, not separate design decisions.

## Route Presentation

### DQ-3

**RESOLVED.** The reading order is starting point, destination, route options, primary route action, result summary, numbered instructions, then optional map detail. Keep manual room entry prominent. The result groups its origin, destination, total distance, map revision and instructions together.

Provide a text-first route with an optional floor map and explicit level selector. Use the template “Building {name}, level {local label}” on both sides of a cross-building transition, with a connecting arrow and an explanation when floor labels differ without a physical level change. Curly single-brace terms here are format parameters, not missing decisions.

Use numbered segments, strong route strokes, directional arrows and labeled stairs/elevator/ramp symbols. Floor changes receive their own instruction. The map has labeled zoom and floor buttons as alternatives to gestures. Selected markers have an outline and text label, never a color-only distinction. Failure and stale-route semantics are FR-1.7/FR-8.4; their presentation uses an inline status panel beside retained route inputs.

## Accessibility

### DQ-4

**RESOLVED.** Adopt WCAG 2.2 Level AA success criteria as the project accessibility target, applied to native software using [WCAG2ICT guidance](https://www.w3.org/TR/wcag2ict-22/). WCAG2ICT is interpretive guidance, not a separate certification. Use at least 4.5:1 normal-text contrast and 3:1 large-text/essential-nontext contrast; the palette is defined above. Preserve explicit labels alongside meaningful symbols.

All route and report tasks must work with VoiceOver and TalkBack. Give controls accessible names, roles, values and state; put focus on the first invalid field after submission and announce result/status changes without repeatedly interrupting speech. Provide a complete text alternative to map-only information. Support text at 200% and the largest platform accessibility size with reflow, reduce-motion settings, keyboard/switch navigation, visible focus and no focus traps.

Present separate labeled toggles for the mobility and lighting options defined by FR-5.1–FR-5.4, with a short description of each option's limits. Do not use “safe route” as a blanket reassurance. Screen-reader instructions are the default visual-aid alternative; no automatic spoken turn-by-turn tracking is included.

Acceptance: execute AC-03, AC-04, AC-05, AC-06, AC-09 and AC-11 with both screen readers; verify scaling, contrast, focus order, gesture alternatives, reduced motion and keyboard/switch navigation on both supported OS minima and current releases. Record a criterion-by-criterion applicability result, including reasons for inapplicable criteria. Test with visually impaired and mobility-impaired participants before public release. No accessibility test has yet been run against an application.

## Geometry

### DQ-5

**RESOLVED.** Controls have a minimum 48-by-48 layout-unit hit area with at least 8 units between separate targets. Focus outlines are 2 units thick with a 2-unit background gap, never clipped. The logo is at least 32-by-32 units with 8 units of clear space on every side. Keep the frontmatter corner-radius token. These are design dimensions; verify their platform rendering through DQ-4 rather than claiming dimensions alone establish accessibility.

## Components and Interaction

### DQ-6

**RESOLVED.** Use `button-primary` for the principal screen action and `field` for editable values, with a visible essential boundary. Hover, pressed, disabled and focused states retain the permitted palette; disabled actions include a reason when the reason is not apparent from adjacent text.

| Pattern | Presentation | Behavior owner |
| --- | --- | --- |
| Route inputs | Distinct persistent labels, suggestions beneath the active field, explicit selection focus | FR-2.1–FR-2.6 |
| Route result | DQ-3 summary, numbered steps and optional floor map | FR-1.1–FR-5.5 |
| Weather and mobility | Labeled selections with explanatory text | FR-4.1–FR-5.4 |
| Problem mark | “Report a problem” action, selected location preview, category and description fields | FR-6.1–FR-6.5 |
| Submission | Editing, field-error, submitting, receipt and retry panels; retained draft stays visible | FR-6.6–FR-6.8 |
| Report history | State label, observed time and review reason; no color-only status | FR-6.9–FR-6.13 |
| Sign-in | Explain why sign-in is needed at the report action; email field then one code field with paste/autofill | FR-7.1–FR-7.6 |
| Account deletion | Explicit confirmation naming the account and explaining the product outcome | FR-7.7–FR-7.9 |
| Offline/service failure | Persistent status panel, dated map label and labeled retry | FR-8.3–FR-8.5 |

Location permission is requested from a student-initiated “Use my location” action after a concise purpose explanation; denial leaves the manual-entry control visible. Show submitted text as ordinary text, without rich text or clickable links. External legal/attribution links use a clearly labeled system-browser action. Enforcement of those rendering and outbound-link boundaries is authored in SC-002/SC-011; this paragraph defines only the visible interaction.

All DQ decisions are resolved. Their original cross-domain inputs now reference their owners rather than repeating platforms, API contracts, authorization or routing policy here.
