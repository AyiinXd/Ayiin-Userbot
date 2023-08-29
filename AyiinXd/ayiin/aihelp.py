# (C) 2020-2023 by TgCatUB@Github.


import openai
from AyiinXd import CMD_HELP
from .. import var

openai.api_key = var.OPENAI_API_KEY
conv = {}

def gen_resp(input_text, chat_id):
    global conv
    model = "gpt-3.5-turbo"
    system_message = None
    messages = conv.get(chat_id, [])
    if system_message and not messages:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": input_text})
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        generated_text = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": generated_text})
        conv[chat_id] = messages
    except Exception as e:
        generated_text = f"`Error generating GPT response: {str(e)}`"
    return generated_text


def gen_edited_resp(input_text, instructions):
    try:
        response = openai.Edit.create(
            model="text-davinci-edit-001",
            input=input_text,
            instruction=instructions,
        )
        edited_text = response.choices[0].text.strip()
    except Exception as e:
        edited_text = f"Error generating GPT edited response`: {str(e)}`"
    return edited_text



