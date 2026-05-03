# FastAPI + Claude Agent SDK

A FastAPI server that exposes a `/chat` endpoint backed by the Claude Agent SDK. Supports custom Claude skills for text humanization and humour generation.

## Project Structure

```
.
├── app.py                  # FastAPI application entry point
├── req.txt                 # Python dependencies
├── sample.env              # Example environment variables
├── .claude/
│   └── skills/
│       ├── my-humanizer/
│       │   └── SKILL.md    # Rewrites text to sound natural and human
│       └── my-humour-creator/
│           └── SKILL.md    # Generates creative humorous text
```

## Prerequisites

- Python 3.9+
- Claude Code CLI authenticated (run `claude` and log in)

## Installation

```bash
pip install -r req.txt
```

## Configuration

Copy `sample.env` to `.env` and fill in your values:

```bash
cp sample.env .env
```

| Variable | Description |
|---|---|
| `CLAUDE_CODE_USE_BEDROCK` | Set to `1` to use AWS Bedrock |
| `AWS_REGION` | AWS region for Bedrock |
| `ANTHROPIC_MODEL` | Model ID to use |
| `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` | AWS region for fast model |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Default Haiku model ID |
| `AWS_BEARER_TOKEN_BEDROCK` | AWS bearer token for Bedrock |

## Running the Server

```bash
python app.py
```

The server starts at `http://127.0.0.1:5000`.

## Usage

### Send a prompt

```bash
curl -X POST "http://127.0.0.1:5000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "your prompt here"}'
```

**Response:**

```json
{
  "response": "Claude's response text here"
}
```

### Using Skills

Skills can be invoked directly in your prompt:

```bash
# Humanize AI-generated text
curl -X POST "http://127.0.0.1:5000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Using skill '\''my-humanizer'\'' convert following text '\''Your text here'\''"}'

# Generate humorous text
curl -X POST "http://127.0.0.1:5000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Using skill '\''my-humour-creator'\'' convert following text '\''Your text here'\''"}'
```

## API Docs

FastAPI provides interactive docs at:

- Swagger UI: `http://127.0.0.1:5000/docs`
- ReDoc: `http://127.0.0.1:5000/redoc`

## Dependencies

| Package | Purpose |
|---|---|
| `fastapi` | Web framework |
| `uvicorn` | ASGI server (installed with fastapi) |
| `python-dotenv` | Load environment variables from `.env` |
| `claude-agent-sdk` | Claude Agent SDK for querying Claude |
