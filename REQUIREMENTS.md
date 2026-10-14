# Requirements

## Required Requirement Inputs

- Project purpose: Indoor and outdoor campus navigation for students at Rub University in Bochum, Germany.
- Primary users / actors: Students, including students with visual impairments and students with physical impairments who need elevators or safer paths.
- Core workflows: Find the shortest route to a campus room or outdoor area; obtain indoor routes during rain or similar weather; navigate connections between building levels; obtain routes using elevators or safer paths; submit map change suggestions; type a current room as a route starting point when GPS is unavailable.
- Business objects / data entities: Campus, buildings, building levels, rooms, outdoor areas, walkways, elevators, routes, maps, map change suggestions, weather conditions.
- External integrations: GPS is mentioned; specific positioning and weather integrations are UNKNOWN.
- Authentication / roles: UNKNOWN.
- Regulatory or privacy constraints: UNKNOWN.

## Functional Requirements

### Campus routing

- **FR-1.1** The system MUST provide students with routes to campus rooms.
- **FR-1.2** The system MUST provide students with routes to outdoor campus areas.
- **FR-1.3** The system MUST provide routes through indoor campus paths.
- **FR-1.4** The system MUST provide routes through outdoor campus paths.

### Starting location

- **FR-2.1** The system MUST use a current room typed by a student as the route starting point without requiring an available GPS position.

### Building levels

- **FR-3.1** The system MUST provide routes across inter-building walkways connecting different floor numbers in the respective buildings.

### Weather routing

- **FR-4.1** The system MUST offer an indoor route when it is raining and such a route is available.

### Mobility support

- **FR-5.1** The system MUST offer routes that use elevators for changes between floors to students who need elevators, where such routes exist.

### Map change suggestions

- **FR-6.1** The system MUST let students submit suggestions for changes to the campus map.

## Non-Functional Requirements

WCAG accessibility is requested, but its version and conformance level are unspecified. A testable conformance requirement depends on OQ-6.

## Open Questions

- **OQ-1** How is "shortest" measured, and how does it interact with weather and mobility requirements?
- **OQ-2** Which weather conditions besides rain trigger indoor routing, and how is weather determined?
- **OQ-3** What should happen when no route exists, including when indoor routing or elevator access cannot be satisfied?
- **OQ-4** How must a route communicate the different building levels at walkway transitions?
- **OQ-5** What makes a path "safer," and which mobility needs beyond elevator use must routing accommodate?
- **OQ-6** Which WCAG version and conformance level are required, and what visual aids must be provided?
- **OQ-7** What does "mark the app" mean, and what action must it let a student perform?
- **OQ-8** What information must a map change suggestion include, and what happens after submission?
- **OQ-9** How should unknown or ambiguous typed room identifiers be handled?
- **OQ-10** Is authentication required for any workflow, and which actions require distinct permissions?
