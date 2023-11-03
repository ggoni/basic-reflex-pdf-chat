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
    files: list[str]

    async def handle_upload(
            self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the files var.
            self.files.append(file.filename)

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = dumb_answer(self.question)
        self.chat_history.append((self.question, answer))
        self.question = ""
        yield  # This clears the input field after the question is asked.
