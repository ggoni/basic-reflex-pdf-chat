# tutrflxapp.py
import reflex as rx
from tutrflxapp import style
from tutrflxapp.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Haga una pregunta...",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Pregunte",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        rx.span("Prototipo"),
        rx.heading("El Bot de Alumnos UDD", color="blue"),
        chat(),
        action_bar(),
        padding_x="2em",
        padding_y="3em",
        z_index=999
    )


app = rx.App()
app.add_page(index)
app.compile()
