# app.py
import asyncio, os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

current_dir = os.path.dirname(os.path.abspath(__file__))


class PromptRequest(BaseModel):
    prompt: str


def run_query(prompt: str) -> str:
    """Synchronous wrapper around the async query."""
    options = ClaudeAgentOptions(
        cwd=current_dir,
        setting_sources=["user", "project"],
        allowed_tools=["Skill", "Read", "Write", "Bash"],
    )

    async def _inner():
        result = []
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        result.append(block.text)
        return "\n".join(result)

    return asyncio.run(_inner())


@app.post("/chat")
def chat(request: PromptRequest):
    response = run_query(request.prompt)
    return JSONResponse(content={"response": response})


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
