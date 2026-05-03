# Steps to Run the App

## 1. Install Dependencies

```bash
pip install -r req.txt
```

## 2. Set Up Environment Variables

Create a `.env` file in the project root (if it doesn't exist):

```
# Add any required environment variables here
```

## 3. Authenticate Claude

Before running the app, make sure Claude Code is logged in:



## 4. Start the FastAPI Server

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`.

## 5. Send a Prompt

Use `curl` or any HTTP client to call the `/chat` endpoint:

```bash
curl -X POST "http://127.0.0.1:5000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "your prompt here"}'
```

### Example Response

```json
{
  "response": "Claude's response text here"
}
```

## 6. Interactive API Docs

FastAPI provides built-in docs at:

- Swagger UI: `http://127.0.0.1:5000/docs`
- ReDoc: `http://127.0.0.1:5000/redoc`

## 7. Claude Skills Structure

Custom skills used by the Claude agent are stored in the `.claude/skills/` folder:

```
.claude/
└── skills/
    ├── my-humanizer/
    │   └── SKILL.md       # Rewrites text to sound natural and human
    └── my-humour-creator/
        └── SKILL.md       # Generates creative humorous text
```

Each skill is a folder containing a `SKILL.md` file that defines the skill's behaviour. Skills can be invoked in prompts, e.g.:

```
Using skill 'my-humanizer' convert following text '...'
Using skill 'my-humour-creator' convert following text '...'
```
