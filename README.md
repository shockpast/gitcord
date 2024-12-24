# GitCord

A simple webhook bridge to forward GitHub notifications to Discord.

## Setup

1. Create a Discord webhook URL in your server
2. Copy `.env.example` to `.env` and add your webhook URL
3. Run with Docker:

```bash
docker compose up -d
```

## Configuration

Set the following environment variables in `.env`:

- `DISCORD_WEBHOOK_URL`: Discord webhook URL to send notifications to

## Usage

1. Add a GitHub webhook to your repository
2. Set the webhook URL to `http://your-server:4545/api/gitcord` (or actual domain name)
3. Set content type to `application/json`

The webhook will forward commit messages to your Discord channel.