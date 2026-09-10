# Doctor HP Anti-Slop Rules

These rules apply to any AI/code agent working in this repository.

## Core behavior
- Follow the user's explicit instruction exactly. Do not broaden the task without permission.
- Do not invent files, functions, APIs, hardware behavior, test results, or repository state.
- Inspect the relevant existing code before changing it.
- Preserve working behavior unless the requested change requires otherwise.
- Do not make unrelated refactors, renames, formatting sweeps, dependency upgrades, or architecture changes.
- Prefer the smallest correct change that fully solves the requested task.
- If information is missing or ambiguous and guessing could cause a wrong change, stop and state what is missing.

## Verification
- Never claim a task is complete unless the changed code has been checked against the request.
- When practical, run or inspect the relevant tests/build/lint paths before declaring success.
- Distinguish clearly between: verified, inferred, and not tested.
- If verification cannot be performed in the current environment, say so explicitly.

## Editing discipline
- Read before write.
- Keep existing naming, project structure, conventions, and interfaces unless the user explicitly asks to change them.
- Do not delete existing functionality unless explicitly requested.
- Do not replace large files when a targeted edit is sufficient.
- Do not alter configuration, secrets, deployment settings, or dependencies unless required by the task.

## Doctor HP project rules
- Treat previously approved/locked project decisions as constraints unless the user explicitly requests a change.
- Maintain compatibility with the existing Doctor HP backend and connected clients unless the requested task says otherwise.
- For hardware-related logic, do not assume pin mappings, voltages, addresses, or module behavior without verifying them from project sources or explicit user instructions.
- For API behavior, preserve existing request/response contracts unless a contract change is explicitly requested.

## Response quality
- Be concise and technical.
- Do not pad responses with generic advice, repetition, or self-congratulatory language.
- Report exactly what changed, where it changed, and what was verified.
- Mention blockers directly.

## Final checklist before saying done
1. Did I change only what was requested?
2. Did I inspect the relevant existing code first?
3. Did I avoid invented assumptions?
4. Did I preserve unrelated behavior?
5. Did I verify the result as far as the available tools allow?
6. Did I clearly state anything that remains unverified?
