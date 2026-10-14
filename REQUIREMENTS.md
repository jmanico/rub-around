# Requirements

This file owns externally observable product behavior and acceptance criteria. Technology is owned by [ARCHITECTURE.md](ARCHITECTURE.md); presentation and accessibility targets by [DESIGN.md](DESIGN.md); security controls by [SECURITY.md](SECURITY.md).

## Required Requirement Inputs

- Purpose: help students navigate the indoor and outdoor campus of Ruhr University Bochum, Germany.
- Actors: anonymous visitors, account holders, moderators, and the project operator. Students with visual or physical impairments are primary users.
- Domain objects: campus, buildings, levels, rooms, outdoor destinations, paths, elevators, routes, maps, problem reports, weather selections, accounts, and review outcomes.
- Workflow scope: routing, manual origins, cross-building transitions, indoor and step-free choices, and marking map problems. The requirements below define each behavior.
- Integrations and identity implementation: [AQ-5](ARCHITECTURE.md#aq-5) and [AQ-9](ARCHITECTURE.md#aq-9).
- Decision provenance: OQ-7, OQ-11, and the anonymous-access portion of OQ-10 record direct user answers. Remaining choices were delegated to the assistant. All decisions are recorded in [decision-register.json](decision-register.json).

## Functional Requirements

Each numbered requirement is independently testable. “Must” denotes an acceptance condition, not an assertion that software already exists.

### Campus routing

- **FR-1.1** The system must return a route to a mapped campus room when a qualifying route exists.
- **FR-1.2** The system must return a route to a mapped outdoor campus destination when a qualifying route exists.
- **FR-1.3** A route must be able to traverse mapped indoor paths.
- **FR-1.4** A route must be able to traverse mapped outdoor paths.
- **FR-1.5** Among qualifying routes, the system must minimize total traversed length in meters; equal-length results must use a deterministic ordering.
- **FR-1.6** The system must exclude closed or staff-only paths from student routes.
- **FR-1.7** When no qualifying route exists, the system must return `no_route` with the unsatisfied constraint and must not present a nonqualifying route as usable.
- **FR-1.8** Removing an indoor preference must require an explicit student action; mobility constraints must never be relaxed automatically.
- **FR-1.9** The route must identify the map revision used to calculate it.

### Starting location and identifiers

- **FR-2.1** The system must accept a typed current room as the origin without a GPS position.
- **FR-2.2** A room lookup with no match must return `not_found` and leave the student's entry available for correction.
- **FR-2.3** A room lookup with multiple matches must return a choice of building, level, and room for each match; routing must wait for a selection.
- **FR-2.4** A student may request their current outdoor position; if it cannot be obtained, manual origin entry must remain available.
- **FR-2.5** The system must ask the student to confirm the mapped starting point suggested from an outdoor position before routing.
- **FR-2.6** A position must not be used to infer the student's indoor floor or room.

- **FR-2.7** Room lookup must ignore surrounding whitespace and letter case, normalize Unicode to NFC, and match only canonical labels or explicitly maintained aliases.
- **FR-2.8** A location fix older than 60 seconds or with horizontal accuracy worse than 30 m must be rejected as `position_unusable` while retaining manual entry.

### Building levels

- **FR-3.1** The system must support walkways whose endpoints have different floor labels in their respective buildings.
- **FR-3.2** Each cross-building transition must identify both endpoint buildings and their local floor labels, even when no stairs or elevator are involved.

### Weather

- **FR-4.1** When rain is selected, the system must offer an entirely indoor route if one exists for the selected endpoints and mobility constraints.
- **FR-4.2** Students must be able to select rain, snow/ice, strong wind, or no adverse weather; each adverse condition must enable the indoor preference.
- **FR-4.3** Weather selection must be manual in the first release; the app must not claim to have detected current weather.
- **FR-4.4** Students must be able to choose an indoor route without selecting adverse weather.

### Mobility

- **FR-5.1** When elevator access is selected, the route must use elevators for changes between floors wherever a qualifying route exists.
- **FR-5.2** The step-free profile must exclude stairs and require verified step-free access, width of at least 0.90 m, and slope no greater than 6% for every path segment; level changes must use a verified operating elevator or qualifying ramp.
- **FR-5.3** A segment without evidence for a required mobility attribute must not qualify for that mobility profile.
- **FR-5.4** The “well-lit paths” option must exclude outdoor segments without verified lighting; the app must not describe it as a guarantee of personal safety.
- **FR-5.5** Confirmed closures and elevator outages must affect new routes after the next map revision is published.
- **FR-5.6** An elevator without an operating confirmation in the preceding 24 hours must not qualify for an elevator-dependent route.

### Problem reports

- **FR-6.1** Signed-in students must be able to submit map change suggestions as problem reports.
- **FR-6.2** A report must identify one of these categories: obstacle, obstruction, incorrect map item, elevator outage, or other map error.
- **FR-6.3** A report must identify its location by selecting a map item, placing a point on a selected building level, or selecting a room from search results.
- **FR-6.4** A report must include a description of 10–1,000 characters and an observed time no later than submission; observations more than seven days old must be rejected.
- **FR-6.5** The first release must reject attachments, HTML, and additional report fields outside the published contract.
- **FR-6.6** A successful submission must return a receipt and the `submitted` state only after the report has been saved durably.
- **FR-6.7** A failed submission must leave the draft available in the current app session and offer retry without claiming success.
- **FR-6.8** Repeating an identical submission with the same idempotency key within 24 hours must return its original receipt; reuse with different content must return `conflict`.
- **FR-6.9** Reporters must be able to see only their own reports and review states: `submitted`, `under_review`, `accepted`, or `rejected`.
- **FR-6.10** An unreviewed report must not change the public map or routing results.
- **FR-6.11** A moderator must be able to accept or reject a report with a reason and, upon acceptance, publish a validated map revision.
- **FR-6.12** A temporary closure must remain excluded from routing until a moderator verifies reopening; a timer must not silently reopen it.
- **FR-6.13** The reporter must be able to read the review reason in the app; report-status email updates are outside the first-release scope.

### Access and accounts

- **FR-7.1** Anonymous visitors must be able to view the map and get directions.
- **FR-7.2** Anonymous attempts to report a problem or access protected report operations must return `unauthenticated` without a write.
- **FR-7.3** Anyone who verifies control of an email address may report problems; university enrollment proof and student-ID collection are not required.
- **FR-7.4** Account holders must be denied map publication and report moderation unless assigned the moderator role.
- **FR-7.5** Only the operator may grant or revoke moderator access.
- **FR-7.6** Sign-in must support entering a one-time emailed code and must return a generic failure for an invalid or expired code.
- **FR-7.7** Signing out must invalidate the current session; deleting an account must invalidate every session.
- **FR-7.8** Account holders must be able to request an export of their account/report data and deletion in the app; export must be available within 30 days and active-system personal data deletion must finish within 30 days.
- **FR-7.9** Account deletion must remove report attribution; accepted map facts may remain without reporter identity or free text.

- **FR-7.10** Accounts must be deleted after 12 months of inactivity, with an account-lifecycle email notice 30 days before deletion; signing in cancels that scheduled inactivity deletion.
- **FR-7.11** A moderator must not publish a map change based solely on their own report; another moderator must independently verify it.

### Availability and platform behavior

- **FR-8.1** The first release must support iPhone and Android phones; a browser app and tablet-specific experience are outside this release.
- **FR-8.2** The interface must be available in German and English, using the device language when supported and German otherwise, with a manual language switch.
- **FR-8.3** Without connectivity, the most recently downloaded public map must remain viewable with its revision date and an offline label.
- **FR-8.4** Offline route calculation and report submission must be unavailable with an explanation; previously calculated directions must be labeled stale and must not be presented as a fresh route.
- **FR-8.5** When the service is unavailable, the app must show a retry action without discarding the current route inputs.
- **FR-8.6** A request exceeding published bounds must receive `invalid_input`, `payload_too_large`, or `rate_limited` as appropriate; it must not cause a partial write.

- **FR-8.7** Supported OS versions must start at iOS 18 and Android 13 (API 33); installation on earlier systems must be excluded.

## Non-Functional Requirements

- **NFR-1** On the capacity fixture defined by [AQ-2](ARCHITECTURE.md#aq-2), route API latency must be at most 1 second at the 95th percentile during a 15-minute run at the specified steady load.
- **NFR-2** Monthly route/map API availability must be at least 99.5%, measured by external checks every minute; announced maintenance counts as downtime.
- **NFR-3** A published map revision must become available to online clients within 60 seconds.
- **NFR-4** Recovery after service/database loss must restore service within four hours with at most 24 hours of lost durable data.
- **NFR-5** Release accessibility acceptance must satisfy the target and tests owned by [DQ-4](DESIGN.md#dq-4).
- **NFR-6** Route use must not create an account-linked location history or stored disability profile.
- **NFR-7** Personal-data processing must implement the privacy obligations and release evidence owned by [OD-010](SECURITY.md#od-010).
- **NFR-8** Public maps must display the attribution and coverage metadata supplied with the published dataset; unmapped areas must not be represented as surveyed routes.

## Acceptance Coverage

These are required tests, not executed results. Each test must contain a separate assertion for each mapped requirement.

| Acceptance ID | Requirements | Fixture or observation |
| --- | --- | --- |
| AC-01 | FR-1.1, FR-1.2, FR-1.3, FR-1.4, FR-1.5, FR-1.6, FR-1.9 | Small graph with indoor/outdoor paths, equal costs, closure and restricted edge; compare result to independently enumerated paths. |
| AC-02 | FR-1.7, FR-1.8, FR-4.1, FR-4.2, FR-4.3, FR-4.4 | Disconnect or expose a required segment; exercise every weather choice and explicit preference removal. |
| AC-03 | FR-2.1, FR-2.2, FR-2.3, FR-2.4, FR-2.5, FR-2.6, FR-2.7, FR-2.8 | Denied location permission, no match, duplicate room labels, inaccurate position and indoor position. |
| AC-04 | FR-3.1, FR-3.2 | Connect building A level 2 to building B level 1 at the same physical elevation. |
| AC-05 | FR-5.1, FR-5.2, FR-5.3, FR-5.4, FR-5.5, FR-5.6 | Stairs, ramps, width/slope boundary values, absent evidence, outage, lighting and a new revision. |
| AC-06 | FR-6.1, FR-6.2, FR-6.3, FR-6.4, FR-6.5 | Each category/location variant; exact length/time bounds; attachment, markup and extra-field rejection. |
| AC-07 | FR-6.6, FR-6.7, FR-6.8 | Database commit failure, response loss, identical retry and conflicting retry. |
| AC-08 | FR-6.9, FR-6.10, FR-6.11, FR-6.12, FR-6.13 | Two reporters, moderator transitions, map publication and closure reopening. |
| AC-09 | FR-7.1, FR-7.2, FR-7.3, FR-7.4, FR-7.5, FR-7.6, FR-7.11 | Anonymous, verified, unverified, moderator and revoked-role requests; email code failure. |
| AC-10 | FR-7.7, FR-7.8, FR-7.9, FR-7.10, NFR-6, NFR-7 | Revocation, export, deletion and inspection of persisted personal data using controlled clocks. |
| AC-11 | FR-8.1, FR-8.2, FR-8.3, FR-8.4, FR-8.5, FR-8.6, FR-8.7 | Both platforms, both languages, airplane mode, server failure and exceeded bounds. |
| AC-12 | NFR-1, NFR-2, NFR-3, NFR-4 | Load run, synthetic uptime accounting, revision propagation and timed restore drill. |
| AC-13 | NFR-5 | Design acceptance suite in DQ-4 on supported platform minima and current OS releases. |
| AC-14 | NFR-8 | Dataset attribution, source-license manifest and visibly incomplete coverage. |

## Resolved Decisions

Stable IDs remain referenceable; no open requirements decisions remain.

| ID | Status | Authoritative entries |
| --- | --- | --- |
| <a id="oq-1"></a>OQ-1 | RESOLVED | FR-1.5, FR-1.8, FR-5.1–FR-5.4 |
| <a id="oq-2"></a>OQ-2 | RESOLVED | FR-4.1–FR-4.4 |
| <a id="oq-3"></a>OQ-3 | RESOLVED | FR-1.7, FR-1.8, FR-8.5 |
| <a id="oq-4"></a>OQ-4 | RESOLVED | FR-3.1, FR-3.2 |
| <a id="oq-5"></a>OQ-5 | RESOLVED | FR-5.1–FR-5.6 |
| <a id="oq-6"></a>OQ-6 | RESOLVED | NFR-5; target owned by DQ-4 |
| <a id="oq-7"></a>OQ-7 | RESOLVED — user | FR-6.1–FR-6.3 |
| <a id="oq-8"></a>OQ-8 | RESOLVED | FR-6.4–FR-6.13 |
| <a id="oq-9"></a>OQ-9 | RESOLVED | FR-2.2, FR-2.3 |
| <a id="oq-10"></a>OQ-10 | RESOLVED — user access boundary; delegated account policy | FR-7.1–FR-7.11 |
| <a id="oq-11"></a>OQ-11 | RESOLVED — user platforms; delegated release scope | FR-8.1 |
| <a id="oq-12"></a>OQ-12 | RESOLVED | FR-7.8, FR-7.9, FR-7.10, NFR-6, NFR-7 |
| <a id="oq-13"></a>OQ-13 | RESOLVED | FR-2.4–FR-2.6 |
| <a id="oq-14"></a>OQ-14 | RESOLVED | FR-8.3, FR-8.4 |
| <a id="oq-15"></a>OQ-15 | RESOLVED | FR-6.3 |
