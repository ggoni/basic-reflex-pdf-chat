import reflex as rx
from tutrflxapp.state import State
from tutrflxapp.components import qa


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )
