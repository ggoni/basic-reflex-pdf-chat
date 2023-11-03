import reflex as rx
import os
import openai
from dotenv import load_dotenv
from tutrflxapp.src.models import dumb_answer

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = dumb_answer(self.question)
        self.chat_history.append((self.question, answer))
        answer = ""
