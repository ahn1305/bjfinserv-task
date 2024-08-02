from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PostRequestData(BaseModel):
    data: List[Union[str, int]]

@app.api_route("/bfhl", methods=["GET", "POST"])
async def bfhl(request: Request, post_request: PostRequestData = None):
    if request.method == "GET":
        return {"operation_code": 1}

    elif request.method == "POST":
        try:
            full_name = "john_doe"
            dob = "17091999"
            user_id = f"{full_name}_{dob}"
            email = "john@xyz.com"
            roll_number = "ABCD123"

            numbers = []
            alphabets = []

            for item in post_request.data:
                if isinstance(item, str) and item.isalpha():
                    alphabets.append(item)
                else:
                    numbers.append(str(item))  

            highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else ""

            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": [highest_alphabet] if highest_alphabet else []
            }
        except Exception as e:
            response = {
                "is_success": False,
                "error": str(e)
            }

        return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
