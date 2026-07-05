# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A static site built with [Reflex](https://reflex.dev) (Python web framework, compiles to React) that displays a high-protein/low-carb meal plan and exercise routine. There is no backend/database — all content is authored in two YAML files and rendered client-side.

## Commands

Dependencies are managed with `uv` (see `uv.lock`, `pyproject.toml`).

```bash
uv sync                 # install dependencies into .venv
uv run reflex run       # run the dev server (hot reload) at localhost:3000
uv run reflex export    # build static export
```

There are no linting or test commands configured in this repo.

## Architecture

- `rxconfig.py` is the Reflex app config; it points `app_module_import` at `src.home_page.main`, which is the actual app entry point (not `src/healthy_plan/`, despite the package name in `pyproject.toml`).
- `src/home_page/main.py` defines the three routes (`/`, `/meal-plan`, `/exercise-plan`), the shared `page_shell`/`nav_bar` layout, and instantiates `app = rx.App()`. The `/` route ("Today") composes content from both other modules for the current weekday.
- `src/meal_plan/` and `src/exercise_plan/` are parallel, self-contained modules. Each follows the same pattern:
  - A YAML file (`meal_plan.yaml` / `exercise_plan.yaml`) keyed by lowercase weekday (`monday`...`sunday`), loaded once at import time into a module-level dict (`MEAL_PLAN` / `EXERCISE_PLAN`).
  - A `get_day_*(day)` accessor that lowercases the lookup key.
  - Reflex component builder functions (e.g. `meal_card`, `workout_card`) that render one entry, composed into a `day_*_section(day)` and a full `*_content()` for the dedicated plan page.
- To change plan content (meals/workouts), edit the YAML files directly — no code changes needed as long as the existing keys (`name`, `meal`, `calories`, `protein_g`, `carbs_g`, `fat_g` for meals; `focus`, `rest`, `exercises`/`cardio_options` for workouts) are preserved.
- When adding a new day-of-week section or a new top-level page, mirror the existing pattern in both `meal_plan` and `exercise_plan` and register any new route in `src/home_page/main.py`'s `TABS` list and `app.add_page` calls.
