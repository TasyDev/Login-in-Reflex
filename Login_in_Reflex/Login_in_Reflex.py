import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def fondo() -> rx.Component:
    return rx.flex(
        id="fondo"
    )

@rx.page(route="/", title="Login")
def login() -> rx.Component:
    return rx.flex (

        fondo(),

    )


app = rx.App(stylesheets=["/style.css"])
