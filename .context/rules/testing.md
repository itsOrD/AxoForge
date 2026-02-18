# Testing Rules & Strategy

> **AI Directive**: Verify before you Trust.

## 1. Strategy: `{{TESTING_STRATEGY}}`
(Hydrate from SCAFFOLD_INTENT.md: e.g., "Testing Pyramid" or "Testing Trophy")

*   **Unit**: Test pure logic in isolation. Fast.
*   **Integration**: Test module interactions. Real DBs via Docker.
*   **E2E**: Test user flows. Black box.

## 2. TDD Protocol
1.  **Red**: Write the test to fail. (Validates the test)
2.  **Green**: Write code to pass.
3.  **Refactor**: Improve code without breaking test.

## 3. Heuristics
*   **Determinism**: A test must yield the same result 100% of the time.
*   **Isolation**: Tests should not depend on shared global state.
*   **Speed**: Unit tests should run in milliseconds.

## 4. Mocking
*   **External**: Mock 3rd party APIs (Stripe, Twilio).
*   **Internal**: Prefer *not* mocking internal dependencies (DB) in Integration tests. Use ephemeral containers.
