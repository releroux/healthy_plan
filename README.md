# healthy_plan
Repo to host static content holding basic information about a high protein low carb meal plan and exercise routine

## Running locally

Requires Python 3.10-3.13 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync            # install dependencies
uv run reflex run  # start the dev server at http://localhost:3000
```

Meal and exercise content is edited directly in `src/meal_plan/meal_plan.yaml` and `src/exercise_plan/exercise_plan.yaml`.

## Deploying to GitHub Pages

The site is published at https://releroux.github.io/healthy_plan/. GitHub Pages serves the static export from the root of the `gh_pages` branch, while `main` holds the source. Whenever you change the YAML meal/exercise plans (or any other source change) on `main`, redeploy with:

```bash
# 1. commit your changes on main first
git checkout main
git add -A && git commit -m "Update plan"

# 2. bring the updated source onto gh_pages and rebuild the export
git checkout gh_pages
git checkout main -- src rxconfig.py pyproject.toml uv.lock reflex.lock
rm -rf .web
REFLEX_FRONTEND_PATH=/healthy_plan uv run reflex export --frontend-only --no-zip --env prod

# 3. replace the old build output at the branch root with the new one
cp -R .web/build/client/healthy_plan/. .
rm -f healthy_plan.html healthy_plan.html.gz
git rm -rq src rxconfig.py pyproject.toml uv.lock reflex.lock
rm -rf src rxconfig.py pyproject.toml uv.lock reflex.lock .web

# 4. commit and push the refreshed site
git add -A
git commit -m "Rebuild static export"
git push origin gh_pages

# 5. go back to main for further work
git checkout main
```

`REFLEX_FRONTEND_PATH=/healthy_plan` is required because GitHub Pages serves this project under the `/healthy_plan/` subpath — without it, asset URLs resolve to the domain root and 404.
