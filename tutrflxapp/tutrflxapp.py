# tutrflxapp.py
import reflex as rx
from tutrflxapp import style
from tutrflxapp.state import State


MY_COLOR = "rgb(107,99,246)"


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
        rx.vstack(
            rx.span("Prototipo"),
            rx.heading("El Bot de Alumnos UDD", color="black"),
            rx.heading("Chatea con tus documentos", color="black", size="sm"),
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Elija sus archivos en pdf",
                        color=MY_COLOR,
                        bg="white",
                        border=f"1px solid {MY_COLOR}",
                    ),
                    rx.text(
                        "O arrastre y suelte sus archivos aquí",
                    ),
                ),
                multiple=True,
                accept={
                    "application/pdf": [".pdf"]
                },
                max_files=5,
                disabled=False,
                on_keyboard=True,
                border=f"1px dotted {MY_COLOR}",
                padding="5em",
            ),
            rx.button(
                "Cargar",
                on_click=lambda: State.handle_upload(
                    rx.upload_files(),

                ),
            ),
            rx.span("Archivos subidos:"),
            rx.span(" "),
            rx.responsive_grid(
                rx.foreach(
                    State.files,
                    lambda files: rx.vstack(
                        rx.text(files, as_="i", font_size="0.5em"),
                    ),
                ),
                columns=[2],
                spacing="1em",
            ),
            padding="2em",
        ),
        chat(),
        action_bar(),
        padding_x="1em",
        padding_y="1em",
        z_index=999
    )


app = rx.App()
app.add_page(index)
app.compile()
