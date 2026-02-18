# Technology Stack & Hard Constraints

> **AI Directive**: These are **IMMUTABLE** constraints. Hydrated from `SCAFFOLD_INTENT.md`.

## Core Runtime
*   **Language**: `{{LANGUAGE}}`
*   **Runtime/Version**: `{{RUNTIME_VERSION}}`

## Frameworks
*   **Web Framework**: `{{WEB_FRAMEWORK}}`
*   **Database Interface**: `{{DATABASE_INTERFACE}}` (ORM/Driver)

## Infrastructure
*   **Container**: Docker
*   **Orchestration**: `{{ORCHESTRATION_TOOL}}` (default: Docker Compose)

## Tooling
*   **Package Manager**: `{{PACKAGE_MANAGER}}`
*   **Linter/Formatter**: `{{LINTER}}`
*   **Test Runner**: `{{TEST_RUNNER}}`

## Forbidden Patterns
*   ❌ No circular dependencies.
*   ❌ No committing secrets / credentials.
*   ❌ No direct database queries in UI components (if applicable).
