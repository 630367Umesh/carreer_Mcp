from fastapi import APIRouter
from pydantic import BaseModel
from agent.career_agent import handle_career_agent

router = APIRouter()

class UserRequest(BaseModel):
    user_input: str
    chat_history: list[str] = []

@router.post("/mcp")
async def mcp_handler(request: UserRequest):
    """
    MCP router: Determines which agent handles the input.
    """
    # Simple keyword-based routing logic
    input_lower = request.user_input.lower()

    if "resume" in input_lower:
        return {"response": "🔧 Resume Agent triggered (not implemented yet)"}
    else:
        result = handle_career_agent(request.user_input, request.chat_history)
        return {"response": result}
