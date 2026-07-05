"""Home page: app entry point, navigation, and today's overview."""

from datetime import datetime

import reflex as rx

from src.exercise_plan.exercise import (
    day_workout_section,
    exercise_plan_content,
)
from src.meal_plan.meal import day_meals_section, meal_plan_content

TABS = [
    ("home", "Today", "/"),
    ("meal", "Meal Plan", "/meal-plan"),
    ("exercise", "Exercise Plan", "/exercise-plan"),
]


def nav_bar(active: str) -> rx.Component:
    return rx.hstack(
        *[
            rx.link(
                rx.button(
                    label,
                    variant="solid" if key == active else "soft",
                ),
                href=href,
            )
            for key, label, href in TABS
        ],
        spacing="3",
        width="100%",
        padding_y="1em",
    )


def page_shell(title: str, active: str, content: rx.Component) -> rx.Component:
    return rx.container(
        rx.vstack(
            nav_bar(active),
            rx.heading(title, size="7"),
            content,
            spacing="4",
            width="100%",
            padding="2em",
        ),
        max_width="800px",
    )


def index() -> rx.Component:
    today = datetime.now().strftime("%A")
    return page_shell(
        f"Today - {today}",
        "home",
        rx.vstack(
            day_meals_section(today),
            day_workout_section(today),
            spacing="6",
            width="100%",
        ),
    )


def meal_plan_page() -> rx.Component:
    return page_shell("Meal Plan", "meal", meal_plan_content())


def exercise_plan_page() -> rx.Component:
    return page_shell("Exercise Plan", "exercise", exercise_plan_content())


app = rx.App(enable_state=False)
app.add_page(index, route="/", title="Today")
app.add_page(meal_plan_page, route="/meal-plan", title="Meal Plan")
app.add_page(exercise_plan_page, route="/exercise-plan", title="Exercise Plan")
