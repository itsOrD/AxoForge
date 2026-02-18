# Agent Skills Registry

> **AI Directive**: Executable capabilities available in this environment.

## 1. Standard commands
*   **Build**: `{{BUILD_COMMAND}}`
*   **Test**: `{{TEST_COMMAND}}`
*   **Lint**: `{{LINT_COMMAND}}`

## 2. Database capabilities
*   **Migration**: `{{MIGRATION_COMMAND}}`
    *   *Rule*: Always inspect the generated migration file.

## 3. Scaffolding
*   **New Module**: `{{SCAFFOLD_COMMAND}}` (if available for framework).

## 4. Analysis
*   **Log Analysis**: Read `{{LOG_DIR}}` files.
*   **Static Analysis**: Run `{{STATIC_ANALYSIS_TOOL}}`.
