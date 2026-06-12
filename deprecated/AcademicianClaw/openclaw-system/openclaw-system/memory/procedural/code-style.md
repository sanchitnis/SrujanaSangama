# Code Style Preferences
_Last updated: [YYYY-MM-DD] | Managed by: Memory Steward_
_Loaded by: Code Architect before every code generation task_

---

## Primary Languages
- 

## Preferred Frameworks & Libraries

| Language | Frameworks | Preferred Libraries |
|----------|-----------|---------------------|
| Python | FastAPI, Flask | pandas, numpy, requests, pydantic |
| JavaScript | — | — |
| [other] | — | — |

## Project Structure Conventions
- Directory layout preference: 
- Config management: [env vars / .env / YAML / TOML]
- Dependency management: [pip+requirements.txt / poetry / conda]

## Code Style

| Aspect | Preference |
|--------|-----------|
| Indentation | 4 spaces (Python) / 2 spaces (JS) |
| Line length max | 88 chars (black default) |
| Naming — variables | snake_case |
| Naming — classes | PascalCase |
| Naming — constants | UPPER_SNAKE |
| Docstrings | Google style |
| Type hints | Always (Python 3.10+) |
| Comments | Inline for non-obvious logic; docstrings for all public functions |

## Error Handling
- Style: exceptions (not return codes)
- Always use descriptive exception messages
- Log errors before re-raising
- No bare `except:` clauses

## Testing
- Framework: pytest
- Coverage target: 80%+
- Test file naming: `test_[module].py`
- Prefer: unit tests + integration tests, minimal mocking

## Anti-Patterns (Never Generate)
- Hardcoded credentials or secrets
- SQL string concatenation (use parameterised queries)
- Global mutable state
- Functions > 40 lines without refactoring
- Magic numbers without named constants

## Version Control
- Commit message style: [conventional commits / imperative / free-form]
- Branch naming: feature/[name], fix/[name], chore/[name]

## Patterns Inferred from Edits
_[Auto-populated by Memory Steward]_
- 
