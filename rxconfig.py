import reflex as rx

config = rx.Config(
    app_name="healthy_plan",
    app_module_import="src.home_page.main",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(),
    ],
)
