"""Exercise plan data and page content, loaded from exercise_plan.yaml."""

from pathlib import Path

import reflex as rx
import yaml

DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

CONFIG_PATH = Path(__file__).parent / "exercise_plan.yaml"

with CONFIG_PATH.open() as config_file:
    EXERCISE_PLAN: dict = yaml.safe_load(config_file)


def get_day_workout(day: str) -> dict:
    """Return the workout configured for the given day (case-insensitive)."""
    return EXERCISE_PLAN.get(day.lower(), {})


def exercise_row(exercise: dict) -> rx.Component:
    return rx.hstack(
        rx.text(exercise["name"], weight="bold"),
        rx.spacer(),
        rx.text(f"{exercise['sets']} x {exercise['reps']}", color_scheme="gray"),
        width="100%",
    )


def workout_card(workout: dict) -> rx.Component:
    if workout.get("rest"):
        return rx.card(
            rx.text("Rest day - recover and stay mobile.", color_scheme="gray"),
            width="100%",
        )

    cardio_options = workout.get("cardio_options") or []

    return rx.card(
        rx.vstack(
            *[exercise_row(exercise) for exercise in workout.get("exercises", [])],
            *[
                rx.text(f"Option: {option}", color_scheme="gray")
                for option in cardio_options
            ],
            spacing="2",
            width="100%",
        ),
        width="100%",
    )


def day_workout_section(day: str) -> rx.Component:
    workout = get_day_workout(day)
    return rx.vstack(
        rx.heading(f"{day.capitalize()} - {workout.get('focus', 'Rest')}", size="5"),
        workout_card(workout),
        spacing="3",
        width="100%",
    )


def exercise_plan_content() -> rx.Component:
    return rx.vstack(
        *[day_workout_section(day) for day in DAYS],
        spacing="6",
        width="100%",
    )
