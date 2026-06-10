from chatbot.llm import model
from chatbot.prompt import SYSTEM_PROMPT
from chatbot.memory import chat_history

from chatbot.output_parser import (
    person_parser,
    event_parser
)


def get_response(user_input):

    chat_history.append(
        f"User: {user_input}"
    )

    recent_history = chat_history[-10:]

    full_prompt = SYSTEM_PROMPT + "\n"
    full_prompt += "\n".join(recent_history)

    response_text = ""

    try:

        for chunk in model.stream(full_prompt):

            print(chunk.content, end="", flush=True)

            response_text += chunk.content

    except Exception as e:

        print(f"\nError: {e}")
        return ""

    chat_history.append(
        f"AI: {response_text}"
    )

    return response_text


def extract_person(text):

    prompt = f"""
Extract the person's information.

Text:
{text}

{person_parser.get_format_instructions()}
"""

    try:

        response = model.invoke(prompt)

        return person_parser.parse(
            response.content
        )

    except Exception as e:

        return f"Parser Error: {e}"


def extract_datetime(text):

    prompt = f"""
Extract the task and datetime.

Current date is 2026-06-09.

Text:
{text}

{event_parser.get_format_instructions()}
"""

    try:

        response = model.invoke(prompt)

        return event_parser.parse(
            response.content
        )

    except Exception as e:

        return f"Parser Error: {e}"