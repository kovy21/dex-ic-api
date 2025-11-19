from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from typing import Optional
from Modules.functions import get_prompt_answer

app = FastAPI()

@app.post("/questions_prompt/")
async def post_question_prompt(user_name: str, contact_name: str, relationship_type: str, contact_frequency: str, # Mandatory parameters
                               reason_for_contact: Optional[str] = None, hobbies: Optional[str] = None, topics: Optional[str] = None): # Optional parameters can be added with default values

    try:
        prompt_result = get_prompt_answer(user_name, contact_name, relationship_type, contact_frequency, reason_for_contact, hobbies, topics)
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "An error occurred while processing the request."}
    
    return prompt_result

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="DEX-IC API Documentation")