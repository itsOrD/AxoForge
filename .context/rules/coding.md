# Coding Rules & Principles

> **AI Directive**: Think like a Principal Engineer. Prioritize maintainability and simplicity.

## 1. Core Philosophy
*   **YAGNI**: Don't build it until you need it.
*   **KISS**: Simple code is better than clever code.
*   **DRY**: abstractions > duplication (but duplication > wrong abstraction).

## 2. Architecture & Design
*   **Solid Principles**: Apply S.O.L.I.D. where appropriate for the language paradigm.
*   **Composition**: Prefer composition over heavy inheritance hierarchies.
*   **Boundaries**: Keep I/O (DB, Network) isolated from core business logic (Hexagonal/Onion arch).

## 3. Code Quality
*   **Nomenclature**: Names must be descriptive. `data` and `item` are forbidden.
*   **Functions**: Should do one thing well.
*   **Error Handling**:
    *   Fail fast.
    *   Handle errors explicitly (Result types or structured Catch).
    *   Never swallow exceptions silently.

## 4. Security
*   **Input Validation**: "Never Trust User Input". Validate at the system boundary.
*   **Least Privilege**: Scope permissions to the minimum necessary.
