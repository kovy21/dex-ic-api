from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from Modules.functions import get_prompt_answer

app = FastAPI()

@app.post("/questions_prompt/")
async def post_question_prompt(relationship_type: str, contact_frequency: str, reason_for_contact: str):

    try:
        prompt_result = get_prompt_answer(relationship_type, contact_frequency, reason_for_contact)
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "An error occurred while processing the request."}
    
    return prompt_result

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="DEX-IC API Documentation")