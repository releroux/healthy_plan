"""Meal plan data and page content, loaded from meal_plan.yaml."""

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

CONFIG_PATH = Path(__file__).parent / "meal_plan.yaml"

with CONFIG_PATH.open() as config_file:
    MEAL_PLAN: dict = yaml.safe_load(config_file)


def get_day_meals(day: str) -> list[dict]:
    """Return the list of meals configured for the given day (case-insensitive)."""
    return MEAL_PLAN.get(day.lower(), [])


def meal_card(meal: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.text(meal["name"], weight="bold"),
                rx.spacer(),
                rx.badge(f"{meal['calories']} kcal"),
                width="100%",
            ),
            rx.text(meal["meal"], color_scheme="gray"),
            rx.hstack(
                rx.badge(f"P {meal['protein_g']}g", color_scheme="green"),
                rx.badge(f"C {meal['carbs_g']}g", color_scheme="orange"),
                rx.badge(f"F {meal['fat_g']}g", color_scheme="blue"),
            ),
            align_items="start",
            spacing="2",
        ),
        width="100%",
    )


def day_meals_section(day: str) -> rx.Component:
    return rx.vstack(
        rx.heading(day.capitalize(), size="5"),
        *[meal_card(meal) for meal in get_day_meals(day)],
        spacing="3",
        width="100%",
    )


def meal_plan_content() -> rx.Component:
    return rx.vstack(
        *[day_meals_section(day) for day in DAYS],
        spacing="6",
        width="100%",
    )
