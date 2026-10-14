---
version: alpha
name: rub-around
description: "ASSUMPTION: Proposed visual identity; existing brand guidance is UNKNOWN."
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

## Overview

[REQUIREMENTS.md](REQUIREMENTS.md) owns behavior and workflows for student campus navigation, including visual and mobility access needs. This document follows the [official DESIGN.md format](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md).

ASSUMPTION: A calm, spacious presentation with a single dark color and a directional mark suits this project. All tokens and styling below are proposed design choices. Existing institutional brand guidance is UNKNOWN; adoption of this visual direction is TO BE DECIDED (DQ-1).

## Colors

Use only `primary` (dark teal) and `surface` (white). These are the complete permitted foreground/background pairs, including reversed use:

| Foreground | Background | Contrast | Uses |
| --- | --- | --- | --- |
| `primary` | `surface` | 11.55:1 | Text, labels, essential borders, focus outlines, route graphics, logo |
| `surface` | `primary` | 11.55:1 | Primary action text and symbols |

Ratios are calculated from opaque sRGB values; displayed values are rounded. Both pairs exceed the required WCAG 2.2 AA thresholds: 4.5:1 for normal text, 3:1 for large text, and 3:1 for necessary UI boundaries, focus indicators, and graphics. See [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

Keep these pairs in every interaction state. Use shape, weight, or explicit text to distinguish meaning. Do not introduce reduced opacity, tints, gradients, or image backgrounds. Any essential graphic or label over a map needs an opaque `surface` backing. Focus outlines use `primary` with a `surface` gap so they contrast with both the control and its surroundings.

## Typography

Use the proposed system sans-serif tokens: `heading` for section titles, `body` for route information and entered values, and `label` for field labels and actions. Keep room and building identifiers intact. Labels remain visible outside inputs; text wraps and scales without clipping. Interface languages are UNKNOWN (DQ-2).

## Layout

ASSUMPTION: A reading order of route inputs followed by route results supports the documented workflows. Use `sm` within related content, `md` around controls, and `lg` between groups. Let content reflow with available space. Device targets are UNKNOWN; breakpoints and route presentation are TO BE DECIDED (DQ-2, DQ-3).

## Elevation & Depth

Use a flat presentation with whitespace, typography, and `primary` borders on `surface` to establish hierarchy. Omit shadows and translucent layers.

## Shapes

Use `rounded.control` for fields and buttons. The proposed logo is one continuous bent directional path, drawn in `primary` on an opaque `surface` background. Preserve its proportions and background. Its geometry is symbolic; campus geometry is UNKNOWN. Minimum display size and surrounding clearance are TO BE DECIDED (DQ-5).

## Components

These patterns describe presentation only; unresolved workflow behavior remains in REQUIREMENTS.md.

| Pattern | Requirement basis | Presentation |
| --- | --- | --- |
| Route inputs | FR-1.1, FR-1.2, FR-2.1 | Distinct visible labels for starting room and destination; keep manual room entry easy to find. |
| Route result | FR-1.1–FR-1.4, FR-3.1 | Group the returned route with its origin and destination. Route representation and building/level notation are TO BE DECIDED (DQ-3). |
| Indoor route | FR-4.1 | Apply the shared route styling to an offered indoor route. Weather triggers and unavailable-route behavior remain OQ-2 and OQ-3. |
| Elevator route | FR-5.1 | Apply the shared route styling to an offered elevator route. Mobility controls and safer-path terminology are TO BE DECIDED (DQ-4). |
| Map suggestion | FR-6.1 | Use persistent field labels and a clearly labeled submission action. Fields and post-submission presentation are TO BE DECIDED (DQ-6). |

Use `button-primary` for the principal action and `field` for editable values. Give fields an essential `primary` boundary. Hover, pressed, and focus treatments retain the permitted color pairs; focus also has a distinct outline. Exact control and focus geometry are TO BE DECIDED (DQ-5).

## Do's and Don'ts

- Preserve building and room identifiers; use explicit labels alongside meaningful symbols.
- Keep all essential text, graphics, control boundaries, and focus indicators within the audited color pairs.
- Keep the logo as one mark with its embedded white background.
- Do not treat contrast validation as complete WCAG conformance; broader accessibility scope remains OQ-6.
- Do not resolve routing priorities, failure behavior, suggestion handling, authentication, or "mark the app" through styling; use the corresponding requirements open questions.

## Open Questions

- **DQ-1** Existing university brand rules are UNKNOWN. Is this proposed identity appropriate, or must it follow supplied brand guidance? Adoption is TO BE DECIDED.
- **DQ-2** Supported devices and interface languages are UNKNOWN. Which must the layouts and copy cover? Breakpoints are TO BE DECIDED.
- **DQ-3** Route representation and building/level transition notation are TO BE DECIDED. What presentation satisfies FR-3.1 and OQ-4?
- **DQ-4** Visual aids, mobility-control presentation, and safer-path terminology are TO BE DECIDED pending OQ-5 and OQ-6. What additional accessibility guidance must shape them?
- **DQ-5** Control sizes, focus-outline geometry, logo minimum size, and logo clearance are TO BE DECIDED. What dimensions pass accessibility and legibility checks on the supported targets?
- **DQ-6** Suggestion fields and validation, failure, and submission-state presentation are TO BE DECIDED pending OQ-3, OQ-8, and OQ-9. Which states and content must the design cover?
