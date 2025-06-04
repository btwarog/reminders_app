# Wika Reminders

A simple Telegram bot that sends periodic reminders.

## Setup

### Prerequisites
- Docker and Docker Compose installed
- Telegram Bot Token (get it from [@BotFather](https://t.me/botfather))
- Telegram Chat ID

### Configuration

1. Create a `.env` file in the project root with the following content:
```
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
```
## Running with Docker

### Build and run using Docker Compose

```bash
docker compose up -d
```

This will build the Docker image and start the container in detached mode.

### View logs

```bash
docker logs wika-reminders
```

### Stop the container

```bash
docker compose down
```

## Running without Docker

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| BOT_TOKEN | Telegram Bot Token | (required) |
| CHAT_ID | Telegram Chat ID | (required) |