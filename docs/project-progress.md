# Project Progress

## Overview

Sanaap Test Kit is being set up as a web-based internal test toolkit. The goal is to let the team create and run different file/test cases through a web service, with browser automation handled by Playwright.

## Work Completed

- Created a Python project targeting Python 3.12.
- Created the `docs/` directory for project notes and architecture documentation.
- Added initial dependencies in `pyproject.toml`:
  - `fastapi`
  - `uvicorn[standard]`
  - `playwright`
  - `pytest`
  - `pytest-playwright`
  - `httpx`
  - `pydantic-settings`
  - `python-dotenv`
- Bootstrapped `pip` inside the local `.venv`.
- Installed the initial dependencies into `.venv`.
- Added `uv.lock` to lock dependency resolution.
- Created a minimal Playwright entrypoint in `main.py` that launches Chromium and opens:

```text
https://develop-car-portal.iranianpooshesh.com/
```

- Added `.gitignore` for Python, virtualenvs, Playwright output, environment files, IDE files, and OS noise.
- Initialized a local Git repository.
- Created the initial commit.
- Added the GitHub remote:

```text
https://github.com/shahriyar888/sanaap_test_toolkit.git
```

- Pushed the initial commit to GitHub on the `master` branch.

## Current Run Command

```bash
.venv/bin/python main.py
```

If Playwright browser binaries are missing, install Chromium first:

```bash
.venv/bin/python -m playwright install chromium
```

## Next Steps

- Decide the first web-service API shape for creating and running test cases.
- Add the initial FastAPI application structure.
- Add Playwright browser binary setup notes or automation.
- Add the first test-case model and a simple run endpoint.
