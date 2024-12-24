import os

from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
import requests
import uvicorn

load_dotenv("./.env")

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

app = FastAPI()

@app.post("/api/gitcord")
async def github_webhook(request: Request):
  if not DISCORD_WEBHOOK_URL:
    raise HTTPException(status_code=500, detail="Discord webhook URL not configured")

  if request.headers.get("content-type") != "application/json":
    raise HTTPException(status_code=400, detail="Invalid content type")

  payload = await request.json()

  try:
    repository = payload.get("repository", {})
    commits = payload.get("commits", {})
    sender = payload.get("sender", {})

    if not repository or not sender or not commits:
      raise HTTPException(status_code=400, detail="Invalid payload")

    repository_name = repository.get("name", "unknown")
    repository_path = repository.get("full_name", "unknown")

    sender_name = sender.get("login", "unknown")
    sender_avatar = sender.get("avatar_url", "unknown")

    commit = commits[0]
    commit_message = commit.get("message", "unknown")
    commit_hash = payload.get("after", "unknown")

    message = {
      "content": f"{commit_message}\n{commit_hash} @ [/{repository_name}](<https://github.com/{repository_path}>)",
      "username": sender_name,
      "avatar_url": sender_avatar
    }

    response = requests.post(
      DISCORD_WEBHOOK_URL,
      json=message
    )
    response.raise_for_status()

    return {"status": "success"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=4545)