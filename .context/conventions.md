# Conventions & Style Guide

> **AI Directive**: Follow the idiomatic style of `{{LANGUAGE}}`.

## 1. File Organization
*   **Colocation**: Keep related units (tests, types, impl) together.
*   **Naming**: Follow the language standard (e.g., `snake_case` for Python, `camelCase` for JS/Go).

## 2. Comments
*   **Docstrings**: All public APIs must have documentation strings.
*   **Why > What**: Explain the *intent* and *constraints*, not the syntax.
*   **TODOs**: Must include an owner or a ticket reference.

## 3. Configuration
*   **Environment**: All config must be 12-factor app compliant (via ENV vars).
*   **Constants**: No magic numbers/strings in code. Extract to constant definitions.

## 4. Version Control
*   **Atomic Commits**: One logical change per commit.
*   **Semantic Messages**: See `.context/rules/git.md`.
