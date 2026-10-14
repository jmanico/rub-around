# Security

## Secure-Coding Inputs

- **Read:** [REQUIREMENTS.md](REQUIREMENTS.md), including Required Requirement Inputs, FR-1.1–FR-6.1, and OQ-1–OQ-10. Confirmed workflows include campus routing, a typed-room origin independent of GPS, indoor and elevator routes, and student map change suggestions. Authentication, roles, and privacy/regulatory obligations are **UNKNOWN**. Student identification is not an established data entity.
- **Read:** [DESIGN.md](DESIGN.md), including Components, Do's and Don'ts, and DQ-2–DQ-6. Route inputs, results, and suggestions have presentation patterns; device support, route representation, and suggestion fields/states remain unresolved. Browser behavior and rendering technology are **UNKNOWN**.
- **Read:** [ARCHITECTURE.md](ARCHITECTURE.md), including Required Architecture Inputs, Architecture and Decisions, Components and Flows, Dependency Rules, and AQ-1–AQ-10. Node.js and React Native for iOS/Android are confirmed technology choices; their versions are **UNKNOWN**. All component boundaries are explicitly **PROPOSED**. Built-in HTTP handling, HTTPS JSON, SQLite, module ownership, persistence interfaces, and request-scoped location/context handling are proposals, not confirmed enforcement mechanisms.
- **Missing:** Existing repository-root `SECURITY.md`; no prior `SC-###` or `OD-###` IDs were available to preserve.
- **Read:** The supplied security notes propose anonymous map-only access, valid student identification before a map-change submission, and GDPR applicability from identification combined with geolocation. These notes do not establish requirements. Their relationship to unresolved authentication, suggestion behavior, data collection, and legal obligations is **TO BE DECIDED** ([OD-009](#od-009), [OD-010](#od-010), [OD-012](#od-012)).
- **Material source mismatches:** ARCHITECTURE.md AQ-1 confirms iOS/Android while REQUIREMENTS.md does not establish target surfaces and DESIGN.md DQ-2 leaves them unknown. DESIGN.md Colors names WCAG 2.2 AA contrast thresholds while REQUIREMENTS.md OQ-6 leaves version and overall conformance unresolved; ARCHITECTURE.md AQ-8 records this mismatch. Resolution remains **TO BE DECIDED** ([OD-002](#od-002), [OD-013](#od-013)).

REQUIREMENTS.md owns behavior, users, data, integrations, and compliance; DESIGN.md owns interaction, rendering, and browser behavior; ARCHITECTURE.md owns components, interfaces, flows, and trust boundaries. Missing facts and proposed choices do not establish rule or pack applicability.

## Selected Manicode Prompts

Corpus root used for resolution: `/Users/jmanico/Dropbox/github/aegis/secure-coding-knowledge`. All corpus paths below are relative to this absolute root. Candidate manifests, prompt scope statements, source scope records, `README.md`, `content/README.md`, and `content/preamble.md` were read. Resolution used `scripts/resolve_prompt.py --json` for each candidate and for a diagnostic combined composition.

**Direct selection evidence**

- **`js/nodejs/26` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md Required Architecture Inputs and AQ-1 confirm Node.js but no release line. [OD-001](#od-001).
  Prompt: `content/js/nodejs/26/prompt.md`; source: `content/js/nodejs/26/sources.md`.
- **`js/react-native/0.87` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md Required Architecture Inputs and AQ-1 confirm React Native but no version. Device/presentation alignment remains AQ-8 and DESIGN.md DQ-2. [OD-002](#od-002).
  Prompt: `content/js/react-native/0.87/prompt.md`; source: `content/js/react-native/0.87/sources.md`.
- **`js/fastify/5.12` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md Frameworks and API and AQ-1 leave the HTTP framework open and only propose built-in Node.js HTTP handling. Fastify and its version are **UNKNOWN**. [OD-003](#od-003).
  Prompt: `content/js/fastify/5.12/prompt.md`; source: `content/js/fastify/5.12/sources.md`.
- **`jvm/android-sdk/37` — BLOCKED; selection TO BE DECIDED.** Android is confirmed in ARCHITECTURE.md Required Architecture Inputs, but SDK, compile/target/runtime scope, supported OS versions, and passkey use are **UNKNOWN** (AQ-1, AQ-8, AQ-9). This pack's Android 17/API 37 scope is not established by naming Android. [OD-004](#od-004).
  Prompt: `content/jvm/android-sdk/37/prompt.md`; source: `content/jvm/android-sdk/37/sources.md`.
- **`swift/ios-sdk/27` — BLOCKED; selection TO BE DECIDED.** iOS is confirmed in ARCHITECTURE.md Required Architecture Inputs, but SDK, toolchain, deployment targets, and passkey use are **UNKNOWN** (AQ-1, AQ-8, AQ-9). This pack's Xcode 27/iOS SDK 27 scope is unconfirmed. [OD-004](#od-004).
  Prompt: `content/swift/ios-sdk/27/prompt.md`; source: `content/swift/ios-sdk/27/sources.md`.
- **`js/zod/4` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md proposes parsing/validation responsibilities, but establishes no validation library or version; request and suggestion contracts remain AQ-6/AQ-7. [OD-005](#od-005).
  Prompt: `content/js/zod/4/prompt.md`; source: `content/js/zod/4/sources.md`.
- **`js/prisma/7.10` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md Persistence and Routing Model and AQ-2 leave database/driver selection open. Proposed SQLite storage does not confirm Prisma or its version. [OD-006](#od-006).
  Prompt: `content/js/prisma/7.10/prompt.md`; source: `content/js/prisma/7.10/sources.md`.
- **`infra/dockerfile/1` — BLOCKED; selection TO BE DECIDED.** ARCHITECTURE.md Required Architecture Inputs and AQ-2 leave deployment unknown. Dockerfile syntax 1, BuildKit, and Linux container use are not confirmed. [OD-007](#od-007).
  Prompt: `content/infra/dockerfile/1/prompt.md`; source: `content/infra/dockerfile/1/sources.md`.

**Selected ordered composition:** Empty. No direct or transitive pack is **SELECTED**.

**Preamble, separately:** `content/preamble.md` resolves before packs, once per composition. It has no manifest or separate source file. It supplies application guidance, not missing project facts or an independently eligible implementation rule. No pack composition is activated here.

**Evaluated dependency-first orders:** These are candidate-resolution results, not selected compositions. `D` marks a directly requested candidate and `T` a transitive pack. Shared parents are deduplicated by the resolver.

1. Node.js: `js/javascript/ES2026` (T) → `js/nodejs/26` (D).
2. React Native: `js/javascript/ES2026` (T) → `js/react/19` (T) → `js/typescript/7` (T) → `js/react-native/0.87` (D).
3. Fastify: `js/javascript/ES2026` (T) → `js/nodejs/24` (T) → `js/typescript/7` (T) → `js/fastify/5.12` (D).
4. Android SDK: `jvm/kotlin/2.4` (T) → `jvm/android-sdk/37` (D).
5. iOS SDK: `swift/swift/6.4` (T) → `swift/ios-sdk/27` (D).
6. Zod: `js/javascript/ES2026` (T) → `js/typescript/7` (T) → `js/zod/4` (D).
7. Prisma: `js/javascript/ES2026` (T) → `js/nodejs/24` (T) → `js/typescript/7` (T) → `js/prisma/7.10` (D).
8. Dockerfile: `infra/dockerfile/1` (D); no parent packs.

**Transitive eligibility and provenance:** All six parents are **BLOCKED**, pending [OD-008](#od-008) and their direct candidates' decisions. Each listed pack's `manifest.json`, beside its prompt/source files, establishes its declared includes. These includes do not establish the project's dependencies.

- **`js/javascript/ES2026`:** Language edition and host/API coverage are **UNKNOWN**. Browser/DOM guidance does not become applicable merely through Node.js or React Native.
  Prompt: `content/js/javascript/ES2026/prompt.md`; source: `content/js/javascript/ES2026/sources.md`.
- **`js/nodejs/24`:** Included by Fastify and Prisma, but the project has no confirmed Node.js release line. Neither 24 nor the direct candidate 26 is selected.
  Prompt: `content/js/nodejs/24/prompt.md`; source: `content/js/nodejs/24/sources.md`.
- **`js/react/19`:** Included by React Native; React version and applicable rendering host are **UNKNOWN**. DOM, server rendering, and server-function applicability are unconfirmed.
  Prompt: `content/js/react/19/prompt.md`; source: `content/js/react/19/sources.md`.
- **`js/typescript/7`:** Included by React Native, Fastify, Zod, and Prisma; project TypeScript use/version and toolchain compatibility are **UNKNOWN**. This prompt specifically scopes its guidance to 7.0.x.
  Prompt: `content/js/typescript/7/prompt.md`; source: `content/js/typescript/7/sources.md`.
- **`jvm/kotlin/2.4`:** Included by Android SDK; project Kotlin use/version and native-module scope are **UNKNOWN**.
  Prompt: `content/jvm/kotlin/2.4/prompt.md`; source: `content/jvm/kotlin/2.4/sources.md`.
- **`swift/swift/6.4`:** Included by iOS SDK; project Swift use/version and native-module scope are **UNKNOWN**.
  Prompt: `content/swift/swift/6.4/prompt.md`; source: `content/swift/swift/6.4/sources.md`.

**Unresolved composition differences:** In the combined diagnostic, direct `js/nodejs/26` mechanically replaces the `js/nodejs/24` parents declared by Fastify and Prisma. That resolver precedence establishes neither project selection nor compatibility; the difference remains [OD-008](#od-008). The React Native source record also explicitly leaves TypeScript 7 integration and complete ES2026 host support unproven. No runtime substitution or compatibility conclusion is adopted.

## Secure-Coding Rules

No rule is **ACTIVE**: eligible version-scoped guidance and confirmed enforcement points are unavailable. The preamble does not fill those gaps. These stable IDs reserve blocked coverage; the entries are not implementation instructions.

**SC-001 — Server request handling**

- **Status:** BLOCKED
- **Dependency:** Runtime/framework selection, confirmed receiving components, request contracts, and resource budgets remain unresolved ([OD-001](#od-001), [OD-003](#od-003), [OD-008](#od-008), [OD-011](#od-011), [OD-012](#od-012)). ARCHITECTURE.md Frameworks and API and AQ-1/AQ-2 do not establish parsing APIs, transport configuration, or limits.

**SC-002 — Mobile data and local state**

- **Status:** BLOCKED
- **Dependency:** React Native version, native platform scope, approved client boundaries, retained data, and rendering behavior are unresolved ([OD-002](#od-002), [OD-008](#od-008), [OD-010](#od-010), [OD-011](#od-011), [OD-013](#od-013)). ARCHITECTURE.md AQ-8/AQ-9 and DESIGN.md DQ-2/DQ-3 do not establish storage or permission mechanisms.

**SC-003 — Native passkeys**

- **Status:** BLOCKED
- **Dependency:** Passkey adoption, identity policy, SDK/toolchain versions, platform applicability, and client/server authentication interfaces are unconfirmed ([OD-004](#od-004), [OD-008](#od-008), [OD-009](#od-009), [OD-011](#od-011)). REQUIREMENTS.md OQ-10 and ARCHITECTURE.md AQ-9 do not establish passkeys; a student-ID note does not select them.

**SC-004 — Route and suggestion validation**

- **Status:** BLOCKED
- **Dependency:** Validation technology, confirmed receiving boundaries, accepted fields, identifier semantics, rejection behavior, and bounds are unresolved ([OD-001](#od-001), [OD-003](#od-003), [OD-005](#od-005), [OD-008](#od-008), [OD-011](#od-011), [OD-012](#od-012)). See REQUIREMENTS.md OQ-8/OQ-9, DESIGN.md DQ-6, and ARCHITECTURE.md AQ-6/AQ-7.

**SC-005 — Data-access safety**

- **Status:** BLOCKED
- **Dependency:** Database/driver/ORM selection, eligible composition, confirmed persistence interfaces, data fields, and retention are unresolved ([OD-001](#od-001), [OD-006](#od-006), [OD-008](#od-008), [OD-010](#od-010), [OD-011](#od-011), [OD-012](#od-012)). ARCHITECTURE.md Persistence and Routing Model and DR-3/DR-4 remain proposed; query APIs and transaction mechanisms are unconfirmed.

**SC-006 — Container build and runtime controls**

- **Status:** BLOCKED
- **Dependency:** Container adoption, platform, builder/runtime scope, and deployment enforcement points are unknown ([OD-007](#od-007), [OD-011](#od-011)). ARCHITECTURE.md AQ-2 supplies no container configuration or build/runtime authority.

**SC-007 — Anonymous access and student eligibility**

- **Status:** BLOCKED
- **Dependency:** The meaning of anonymous map-only access, permitted operations, student eligibility, validity evidence, and enforcement boundaries are unresolved ([OD-001](#od-001), [OD-003](#od-003), [OD-008](#od-008), [OD-009](#od-009), [OD-011](#od-011)). REQUIREMENTS.md FR-6.1/OQ-10 and ARCHITECTURE.md Authentication and Session Boundary do not authorize adopting the security notes as an access policy.

**SC-008 — Identification and location privacy**

- **Status:** BLOCKED
- **Dependency:** Student-identification collection, location handling/linkage, applicable legal obligations, permitted uses, storage/disclosure/retention policy, and enforcement points are unknown ([OD-010](#od-010), [OD-011](#od-011), [OD-014](#od-014)). REQUIREMENTS.md Required Requirement Inputs and ARCHITECTURE.md AQ-5/AQ-9 do not establish the notes' GDPR assertion or a retention period.

**SC-009 — Suggestion and canonical-map integrity**

- **Status:** BLOCKED
- **Dependency:** Approved data ownership, submission semantics, canonical-map update authority, persistence mechanism, and validation contracts are unresolved ([OD-001](#od-001), [OD-006](#od-006), [OD-008](#od-008), [OD-009](#od-009), [OD-011](#od-011), [OD-012](#od-012)). REQUIREMENTS.md FR-6.1 defines suggestions; ARCHITECTURE.md's separate suggestion storage and DR-3/DR-4 are proposed, and AQ-7 establishes no moderation/publishing component.

**SC-010 — Map, weather, and positioning inputs**

- **Status:** BLOCKED
- **Dependency:** Sources/providers, data contracts, external interfaces, accepted destinations, trust policy, and failure behavior are unresolved ([OD-001](#od-001), [OD-003](#od-003), [OD-008](#od-008), [OD-011](#od-011), [OD-014](#od-014)). REQUIREMENTS.md FR-2.1/FR-4.1 and ARCHITECTURE.md AQ-3/AQ-5 establish workflows, not integration mechanisms.

**SC-011 — Rendering and browser behavior**

- **Status:** BLOCKED
- **Dependency:** React Native and inherited pack applicability, approved presentation boundaries, map/route rendering, content formats, and any browser or embedded-web scope are unresolved ([OD-002](#od-002), [OD-008](#od-008), [OD-011](#od-011), [OD-013](#od-013)). DESIGN.md Components/DQ-2/DQ-3/DQ-6 and ARCHITECTURE.md AQ-8 do not establish HTML sinks, WebViews, or browser-origin policies.

**SC-012 — Authentication and session lifecycle**

- **Status:** BLOCKED
- **Dependency:** Whether authentication/sessions exist, credential/provider choices, native authentication scope, lifecycle rules, sensitive-data handling, and enforcement points are unresolved ([OD-001](#od-001), [OD-002](#od-002), [OD-003](#od-003), [OD-004](#od-004), [OD-008](#od-008), [OD-009](#od-009), [OD-010](#od-010), [OD-011](#od-011)). REQUIREMENTS.md OQ-10 and ARCHITECTURE.md AQ-9 do not establish passwords, tokens, cookies, or session mechanisms.

## Open Security Decisions

### OD-001

- **Unresolved:** Node.js release line is **UNKNOWN**; selection is **TO BE DECIDED** (ARCHITECTURE.md Required Architecture Inputs; AQ-1).
- **Evidence needed:** An authoritative architecture decision naming the server runtime version scope and execution environments before choosing runtime-specific guidance.
- **Affected:** SC-001, SC-004, SC-005, SC-007, SC-009, SC-010, SC-012. Candidate: `js/nodejs/26`; transitive `js/nodejs/24` also awaits OD-008.
- **Owner:** UNKNOWN.

### OD-002

- **Unresolved:** React Native version and supported client targets are **UNKNOWN**. Reconciliation of ARCHITECTURE.md's iOS/Android choices with REQUIREMENTS.md's source gap and DESIGN.md DQ-2 is **TO BE DECIDED** (AQ-1/AQ-8).
- **Evidence needed:** Architecture version scope and supported platforms, with requirements/design alignment for the client surfaces.
- **Affected:** SC-002, SC-011, SC-012. Candidate: `js/react-native/0.87`.
- **Owner:** UNKNOWN.

### OD-003

- **Unresolved:** HTTP framework selection is **TO BE DECIDED**. ARCHITECTURE.md's supplied framework value is Node.js; built-in HTTP handling is only proposed. Fastify adoption/version are **UNKNOWN** (Frameworks and API; AQ-1).
- **Evidence needed:** An architecture decision naming the HTTP implementation and version scope, receiving interfaces, transport ownership, and any intermediary/proxy boundary.
- **Affected:** SC-001, SC-004, SC-007, SC-010, SC-012. Candidate: `js/fastify/5.12`.
- **Owner:** UNKNOWN.

### OD-004

- **Unresolved:** Passkey adoption, Android SDK scope, iOS SDK/toolchain scope, supported OS/deployment targets, and native integration mechanisms are **UNKNOWN**; selections are **TO BE DECIDED** (REQUIREMENTS.md OQ-10; ARCHITECTURE.md AQ-1/AQ-8/AQ-9).
- **Evidence needed:** Requirements establishing authentication behavior and architecture confirming platform versions, native integration boundaries, and server verification interfaces. Platform targets alone do not establish passkeys.
- **Affected:** SC-003, SC-012. Candidates: `jvm/android-sdk/37`, `swift/ios-sdk/27`; parents remain OD-008.
- **Owner:** UNKNOWN.

### OD-005

- **Unresolved:** Validation library/version are **UNKNOWN**; selection is **TO BE DECIDED**. Proposed API validation does not select Zod (ARCHITECTURE.md Frameworks and API; AQ-6/AQ-7).
- **Evidence needed:** Architecture-confirmed validation implementation and version scope; contract definitions and failure behavior from OD-012.
- **Affected:** SC-004. Candidate: `js/zod/4`.
- **Owner:** UNKNOWN.

### OD-006

- **Unresolved:** Database, driver, ORM use/version, and persistence interfaces are **TO BE DECIDED**; workload and environment are **UNKNOWN** (ARCHITECTURE.md Persistence and Routing Model; AQ-2). SQLite is proposed and does not establish Prisma use.
- **Evidence needed:** Architecture-confirmed storage technology/version, access interfaces, ownership, and transaction/integrity requirements grounded in approved data contracts.
- **Affected:** SC-005, SC-009. Candidate: `js/prisma/7.10`.
- **Owner:** UNKNOWN.

### OD-007

- **Unresolved:** Container use, deployment environment, builder/runtime, and platform are **UNKNOWN**; container selection is **TO BE DECIDED** (ARCHITECTURE.md Required Architecture Inputs; AQ-2).
- **Evidence needed:** Architecture-confirmed deployment/build boundaries and, if adopted, Dockerfile syntax, BuildKit, and Linux-container applicability. No image, user, permission, or resource value is established.
- **Affected:** SC-006. Candidate: `infra/dockerfile/1`.
- **Owner:** UNKNOWN.

### OD-008

- **Unresolved:** Transitive technology/version applicability and compatibility are **UNKNOWN**; composition choices are **TO BE DECIDED**. Fastify/Prisma declare Node.js 24 while the direct runtime candidate names 26. The corpus resolver's substitution does not settle that difference. React Native's source record also does not establish TypeScript 7 integration or complete ES2026 host support.
- **Evidence needed:** Authoritative architecture confirmation of actual language/compiler/runtime versions and host surfaces, plus verified version-specific compatibility evidence for every intended composition. Resolve the Node.js parent difference without treating dependency order as compatibility evidence. Establish each prompt's applicable native, browser, server, or toolchain scope before activating its rules.
- **Affected:** All version-dependent rule coverage. Parents: `js/javascript/ES2026`, `js/nodejs/24`, `js/react/19`, `js/typescript/7`, `jvm/kotlin/2.4`, `swift/swift/6.4`.
- **Owner:** UNKNOWN.

### OD-009

- **Unresolved:** Authentication, anonymous permissions, student-ID validity/verification, and session needs are **UNKNOWN** in REQUIREMENTS.md Required Requirement Inputs/OQ-10 and ARCHITECTURE.md AQ-9. The notes prescribe anonymous map-only use and valid student identification for a map change; adopting or reconciling those statements is **TO BE DECIDED**. A suggestion and a canonical map edit are not established as the same operation.
- **Evidence needed:** Requirements defining actors and permitted operations, the meaning and evidence of student eligibility, and submission versus editing behavior; architecture confirming identity authority and enforcement/lifecycle interfaces. Provider and credential choices remain unresolved.
- **Affected:** SC-003, SC-007, SC-009, SC-012. Passkey candidates remain conditional on OD-004.
- **Owner:** UNKNOWN.

### OD-010

- **Unresolved:** Student-identification collection and linkage to location are **UNKNOWN**; applicable privacy/regulatory obligations and collection, use, disclosure, logging, and retention policies are **TO BE DECIDED**. The notes assert GDPR applicability, while REQUIREMENTS.md leaves privacy/regulatory constraints unknown and ARCHITECTURE.md AQ-9 leaves retention unresolved.
- **Evidence needed:** Requirements defining actual personal-data processing, applicable obligations and their verified basis, permitted recipients/uses, and required lifecycle behavior; architecture defining the corresponding data flows, storage, diagnostics, and enforcement boundaries. No GDPR mechanism, legal basis, or retention value is selected here.
- **Affected:** SC-002, SC-005, SC-008, SC-012; any identity/location-related control.
- **Owner:** UNKNOWN.

### OD-011

- **Unresolved:** Confirmed implementation/enforcement points are **UNKNOWN**. ARCHITECTURE.md Components and Flows explicitly labels every component boundary proposed; its transport, storage, dependency rules, and diagrams remain proposed. Adoption is **TO BE DECIDED**.
- **Evidence needed:** Architecture decisions establishing components, interfaces, flows, ownership, and enforcement boundaries for the approved workflows, including transport and diagnostics where applicable. A SUPPORTED responsibility alone does not establish component or technology approval.
- **Affected:** SC-001–SC-012; activation and observable verification of every implementation rule.
- **Owner:** UNKNOWN.

### OD-012

- **Unresolved:** Route/suggestion schemas, identifier handling, routing outcomes, submission lifecycle, map-update authority, resource budgets, and persistence outcomes are **TO BE DECIDED** (REQUIREMENTS.md OQ-1/OQ-3/OQ-5/OQ-8/OQ-9; DESIGN.md DQ-3/DQ-6; ARCHITECTURE.md AQ-2/AQ-3/AQ-4/AQ-6/AQ-7).
- **Evidence needed:** Requirements defining accepted data and observable success/failure behavior; design defining validation/submission states; architecture establishing contracts, map/suggestion write authority, bounds, and persistence semantics. The notes' phrase "submit a map change" needs reconciliation with FR-6.1's suggestion workflow.
- **Affected:** SC-001, SC-004, SC-005, SC-009. No moderation or publishing mechanism is inferred.
- **Owner:** UNKNOWN.

### OD-013

- **Unresolved:** Route/map renderer, content formats, native presentation, and browser/embedded-web behavior are **UNKNOWN** or **TO BE DECIDED** (DESIGN.md DQ-2–DQ-6; ARCHITECTURE.md AQ-8). Web-oriented design tokens versus native presentation, and WCAG 2.2 AA contrast wording versus REQUIREMENTS.md OQ-6, remain recorded source mismatches.
- **Evidence needed:** Design/requirements reconciliation of device and accessibility scope, plus architecture/design confirmation of renderer, content sinks, and any browser or embedded-web surface. Browser controls cannot be selected from a web-style design token or inherited React prompt alone.
- **Affected:** SC-002, SC-011; output handling and any browser-specific controls.
- **Owner:** UNKNOWN.

### OD-014

- **Unresolved:** Map/weather/positioning sources, providers, formats, trust policy, permitted uses, destinations, and connectivity behavior are **UNKNOWN**; integration mechanisms are **TO BE DECIDED** (REQUIREMENTS.md Required Requirement Inputs/OQ-2; ARCHITECTURE.md AQ-3/AQ-5).
- **Evidence needed:** Requirements confirming integration behavior and data use; architecture confirming external interfaces, accepted data and destination scope, provenance/update authority, and failure contracts. FR-2.1 confirms GPS-independent manual origin entry, not a particular positioning implementation.
- **Affected:** SC-008, SC-010; external-input validation, outbound requests, location flows, and map provenance.
- **Owner:** UNKNOWN.
