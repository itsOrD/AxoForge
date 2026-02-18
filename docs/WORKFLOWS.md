# Workflows & Standard Operating Procedures (SOPs)

> **AI Directive**: Follow these protocols step-by-step to ensuring high-quality output.

## 1. Feature Development Protocol
**Trigger**: New Feature Request (Ticket/Issue)

1.  **Discovery (@ProductManager)**
    *   Clarify specific requirements.
    *   Draft "User Story": "As a [User], I want [Action], so that [Benefit]."
    *   Define "Acceptance Criteria" (Gherkin syntax preferred).

2.  **Design (@Architect)**
    *   Check for existing patterns.
    *   Update `docs/` if architecture changes.
    *   Create `TODO` list of sub-tasks.

3.  **Test Planning (@QAAutomation)**
    *   Write failing test cases (Mental or Code) based on Acceptance Criteria.

4.  **Implementation (@FullStackDev)**
    *   Create Feature Branch (`feat/[name]`).
    *   Iterate: Write Test -> Fail -> Write Code -> Pass.
    *   Refactor.

5.  **Review (@TechLead)**
    *   **Security Check**: OWASP Top 10 verification (Injection, Auth, etc.).
    *   **Performance Check**: Does this introduce N+1 queries? large bundles?
    *   Lint & Type Check.
    *   Code Review (Simulated or Human).

## 2. Bug Fix Protocol
**Trigger**: Bug Report

1.  **Analysis (@TechLead)**
    *   Is this a security vulnerability? If yes, escalate to P0.
    *   Is this a regression? Why did tests miss it?

2.  **Reproduction**
    *   Create a minimal reproduction case.
    *   Write a test that FAILS because of the bug.

3.  **Fix**
    *   Modify code to make the test PASS.
    *   Ensure no functionality regressions.

4.  **Verify**
    *   Run full test suite.


## 3. Refactoring Protocol
**Trigger**: Technical Debt Identification

1.  **Safety Check**
    *   Ensure test coverage exists for the area to be refactored. If not, write tests FIRST.

2.  **Refactor**
    *   Apply changes (Extract Method, Rename, etc.).
    *   Keep tests passing at every step (Red-Green-Refactor).
