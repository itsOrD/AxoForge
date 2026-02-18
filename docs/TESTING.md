# Testing Manual

> **AI Directive**: This document defines *How* we test using `{{TEST_RUNNER}}`.

## 1. Test Levels

### Unit Tests
*   **Scope**: Individual functions, classes, methods.
*   **Location**: Colocated with source (e.g., `module_test.go` or `module.spec.ts`).
*   **Tool**: `{{UNIT_TEST_TOOL}}`

### Integration Tests
*   **Scope**: Database interactions, API endpoints.
*   **Strategy**: Use `{{INTEGRATION_STRATEGY}}` (e.g., Testcontainers).
*   **Tool**: `{{INTEGRATION_TEST_TOOL}}`

### End-to-End (E2E) Tests
*   **Scope**: Full User Journey.
*   **Tool**: `{{E2E_TEST_TOOL}}` (e.g., Playwright, Selenium).

## 2. CI Pipeline
*   Tests checked on PR.
*   Coverage threshold: `{{COVERAGE_THRESHOLD}}%`.

## 3. Generating Tests (AI)
*   **Prompt**: "Write a test case for [Function] that handles [Edge Case]."
*   **Mutation**: "Modify the code to introduce a subtle bug and verify the test catches it."
