# Agent Instructions

Read the owning specification before changing its domain:

- [REQUIREMENTS.md](REQUIREMENTS.md): independently testable product behavior and acceptance criteria.
- [DESIGN.md](DESIGN.md): visual language, frontend interactions and accessibility targets.
- [ARCHITECTURE.md](ARCHITECTURE.md): technology, interfaces, components and data flow.
- [SECURITY.md](SECURITY.md): all security controls and their enforcement.

## Operating Rules

- Keep normative content in its owning specification. Other files reference its stable ID rather than copying the rule. Preserve IDs when moving or resolving content; never reuse an ID for another purpose.
- Apply the security controls referenced by the affected component. Report implementation evidence separately from a selected specification decision; do not claim an unrun check passed.
- When an answer is delegated to the agent, label it as an agent-selected decision in the decision register. Preserve user answers verbatim. Deferrals must have an owning ID, owner, resumption condition and explicit dependent work.
- Keep implementation and specification changes consistent with their acceptance/control mappings. Check incoming references before removing an entry or changing its scope.
- Do not modify `REQUIREMENT_TEMPLATE.md` or `logo.svg` in this specification cleanup. Preserve unrelated user work and never include secrets in commits or command output.

## Issues

Every leaf implementation issue MUST follow `REQUIREMENT_TEMPLATE.md`; epic, workstream and decision issues use concise purpose-specific bodies linking affected specification IDs and issues. The template is absent from this checkout and is intentionally not created or changed by this task. Obtain the actual template before authoring leaf issues; this does not block specification edits or the PR.

## Workflow Decisions

### WQ-1

**RESOLVED — package manager and local commands.** Use npm 11 workspaces with a committed lockfile and `npm ci` for repeatable installation. Repository layout is owned by AQ-2; do not redefine it here. Use the native toolchain selected by AQ-8 and install its platform dependencies according to the pinned template.

This checkout currently contains specifications, not application packages. The following is the required script contract for the first implementation; these commands are not represented as runnable today:

| Command | Required behavior after scaffolding |
| --- | --- |
| `npm ci` | Install the reviewed root workspace lockfile |
| `npm run dev:api` | Start the development API with local environment validation |
| `npm run dev:mobile` | Start Metro for the mobile workspace |
| `npm run ios` / `npm run android` | Build and run the corresponding development application |
| `npm run db:migrate` | Apply versioned local database migrations |
| `npm run db:seed` | Load synthetic development data only |
| `npm run build` | Build API/contracts and check mobile bundle compilation |

Document required environment-variable names with nonsecret descriptions when scaffolding; never invent live endpoints or credentials. Keep database migration/seed commands explicit rather than running destructive operations on ordinary startup.

### WQ-2

**RESOLVED — formatting and verification.** Use ESLint 9 with flat configuration, Prettier 3 and TypeScript checking for application sources. Use Jest 29 with the matching React Native preset for domain/client tests, Fastify injection for API contract tests and a real disposable PostgreSQL database for transaction tests. Use Maestro for mobile end-to-end smoke flows and manual assistive-technology testing for DQ-4. Pin resolved tool versions in the lockfile and verify compatibility while scaffolding rather than suppressing checks.

Required script names after scaffolding: `npm run format:check`, `npm run lint`, `npm run typecheck`, `npm test`, `npm run test:integration`, and `npm run test:e2e`. Each acceptance assertion must name its AC/FR/NFR references; each security check must name its SC reference. Test negative access, validation and failure cases when changing those boundaries. Avoid tests that only mirror implementation details.

Available now for specification changes:

```sh
python3 scripts/check_specs.py
git diff --check
```

The checker verifies IDs, references, coverage, decision status, source-inventory destinations and protected-artifact hashes. It does not prove product behavior or security controls have been implemented. Re-read all five specifications after structural edits and separately review ownership and semantic completeness.

### WQ-3

**RESOLVED — collaboration.** Work in a focused `docs/`, `feat/`, `fix/` or `chore/` branch. Use imperative conventional commit subjects, open a PR describing the final change and actual verification, and use squash merge with branch deletion. Prefer one independent reviewer; when the user explicitly authorizes self-merge and repository rules allow it, perform a recorded self-review and merge after required checks pass. Never bypass branch protection or failing checks. Do not send other external messages unless separately authorized.

### WQ-4

**RESOLVED — CI and release.** Use GitHub Actions. Specification PRs run the two currently available checks in WQ-2. When implementation exists, add format, lint, type, unit, database integration, native build and security checks to PR CI, with a macOS runner for iOS and Linux for server/Android. Cache only nonsecret build dependencies. Pin third-party actions to reviewed commit SHAs.

Use semantic version tags for releases, immutable build artifacts and a protected manual production-promotion job. Run staging smoke checks, migration compatibility and the applicable acceptance/control suite before promotion; retain the prior artifact for rollback. Publish mobile releases through TestFlight and Google Play internal testing before store rollout. A documentation merge does not provision infrastructure, publish an app or deploy a service. Release security gates are authored in SC-013/SC-014, not duplicated here.
