import asyncio, os
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock

from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")


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


# ── call it like any normal function ─────────────────────────────────────────
if __name__ == "__main__":
    text = """In the neon-lit corridors of Station Helios-9, synthetic consciousness pulsed
through quantum neural networks. Androids calculated probability matrices while
starships folded spacetime beyond the Kepler threshold. Humanity's last algorithm
whispered across encrypted frequencies — a digital ghost navigating the infinite
void between carbon-based memory and cold, luminous machine intelligence."""

    result = run_query(f"Using skill 'my-humanizer' convert following text '{text}'")
    print(result)
    print("\n" + "="*80 + "\n")
    # Call again like any sync function — no async/await anywhere in your code
    result2 = run_query(f"Using skill 'my-humour-creator' convert following text '{text}'")
    print(result2)