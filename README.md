# healthy_plan
Repo to host static content holding basic information about a high protein low carb meal plan and exercise routine

## Running locally

Requires Python 3.10-3.13 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync            # install dependencies
uv run reflex run  # start the dev server at http://localhost:3000
```

Meal and exercise content is edited directly in `src/meal_plan/meal_plan.yaml` and `src/exercise_plan/exercise_plan.yaml`.

## Building a static export

```bash
uv run reflex export --frontend-only --no-zip
```

