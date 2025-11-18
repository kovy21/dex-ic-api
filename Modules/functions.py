import os
from dotenv import load_dotenv
load_dotenv()

AICORE_CLIENT_ID = os.getenv("AICORE_CLIENT_ID")
AICORE_CLIENT_SECRET = os.getenv("AICORE_CLIENT_SECRET")
AICORE_AUTH_URL = os.getenv("AICORE_AUTH_URL")
AICORE_BASE_URL = os.getenv("AICORE_BASE_URL")
AICORE_RESOURCE_GROUP = os.getenv("AICORE_RESOURCE_GROUP")
os.environ['AICORE_CLIENT_ID'] = AICORE_CLIENT_ID
os.environ['AICORE_CLIENT_SECRET'] = AICORE_CLIENT_SECRET
os.environ['AICORE_AUTH_URL'] = AICORE_AUTH_URL
os.environ['AICORE_BASE_URL'] = AICORE_BASE_URL
os.environ['AICORE_RESOURCE_GROUP'] = AICORE_RESOURCE_GROUP

from gen_ai_hub.proxy.native.openai import chat

def base_prompt(relationship_type, contact_frequency, reason_for_contact):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"You are an app developer tasked with creating question suggestions (in Czech) that help young people re-connect with their elderly relatives." +
                            f"The relationship type is: {relationship_type}. The suggested contact frequency is: {contact_frequency}. The reason for contact is: {reason_for_contact}." +
                            f"Based on this information, generate a JSON containing one meaningful, driving question that should help them engange and re-connect and three additional, supplementary question to further engage in the conversation." +
                            f"The JSON should have the following structure: " +
                            f"{{'main_question': '...', 'additional_questions': ['...', '...', '...']}}. Do not include any line breaks." +
                            f"Ensure that the questions are open-ended and encourage storytelling and sharing of experiences."
                }
            ]
        }
    ]
    return messages

def write_prompt_messages(messages, model_name = "gpt-5"): # Models can be changed here
    """Send messages to the model and return the response."""
    kwargs = dict(model_name=model_name, messages=messages)
    response = chat.completions.create(**kwargs)
    return response.to_dict()["choices"][0]["message"]["content"]

def get_prompt_answer(relationship_type, contact_frequency, reason_for_contact):
    """Get response from GPT 5."""
    messages = base_prompt(relationship_type, contact_frequency, reason_for_contact)
    answer = write_prompt_messages(messages)
    return answer