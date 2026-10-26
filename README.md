# Real-Time Chat Application

A real-time, one-to-one chat application built with **Django** and **Django Channels**. Users sign up and sign in with their email address, pick another user, and exchange messages instantly over WebSockets. Every message is stored in the database, so the conversation history is there when a room is reopened.

## Features

- Real-time messaging over WebSockets
- One-to-one chat rooms, created automatically the first time two users talk
- Persistent message history stored with Django models
- Email-based sign-up and sign-in
- User profiles with phone, gender, country and interests
- Online/offline status, updated on login and logout
- Django admin for managing users, profiles, interests, rooms and messages

## Tech Stack

| Component | Purpose |
| --- | --- |
| Python | Application logic |
| Django 4.2 | Web framework and ORM |
| Django Channels 4 | WebSocket handling and the channel layer |
| Daphne 4 | ASGI server (also powers `runserver`) |
| Django REST Framework 3.14 | `APIView`s and serializers for sign-up and sign-in |
| SQLite | Default database |

## Project Structure

```
chat/
├── README.md
├── req.txt                     # Python dependencies
└── chat_project/
    ├── manage.py
    ├── chat_project/           # Project settings, URLs, ASGI/WSGI config
    │   ├── settings.py
    │   ├── urls.py
    │   └── asgi.py             # HTTP + WebSocket protocol routing
    ├── chat_auth/              # Sign-up, sign-in, logout, user profiles
    │   ├── models.py           # Profile, Interest
    │   ├── serializers.py
    │   ├── views.py
    │   └── templates/
    └── chat_app/               # Chat rooms and messaging
        ├── models.py           # RoomNames, MessageHistory
        ├── consumers.py        # ChatConsumer (WebSocket)
        ├── routing.py          # WebSocket URL routes
        ├── views.py
        └── templates/chat/
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/rutujakadam0204/chat.git
cd chat

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r req.txt
```

> **Note:** `twisted-iocpsupport` only installs on Windows. On Linux or macOS, remove that line from `req.txt` (or install it with `grep -v twisted-iocpsupport req.txt | pip install -r /dev/stdin`).

### Set up the database

```bash
cd chat_project
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
```

### Run the server

```bash
python manage.py runserver
```

Because `daphne` is in `INSTALLED_APPS`, `runserver` starts an ASGI server that handles both HTTP and WebSocket traffic. Open <http://127.0.0.1:8000/> in your browser.

## Usage

1. Go to `http://127.0.0.1:8000/` and sign up with your name, email, password and profile details.
2. Sign in with your email and password. You will be taken to `/chat/`.
3. Choose a user from the list to open a chat room with them.
4. Type a message. It appears straight away for both users and is saved to the history.

To try it on your own machine, create two accounts and sign in to each one in a separate browser (or a private window).

## Routes

### HTTP

| URL | View | Description |
| --- | --- | --- |
| `/` | `SignIn` | Sign-in / sign-up page (GET), sign in (POST) |
| `/sign-up` | `Signup` | Create a user and profile (POST) |
| `/logout` | `user_logout` | Log out and mark the user offline |
| `/chat/` | `index` | List of other users (login required) |
| `/chat/<user_id>/` | `room` | One-to-one chat room with that user (login required) |
| `/admin/` | Django admin | Admin site |

### WebSocket

| URL | Consumer |
| --- | --- |
| `ws/chat/<room_name>/` | `ChatConsumer` |

Message the client sends:

```json
{ "message": "Hello!", "sender": 1 }
```

Message broadcast to everyone in the room:

```json
{ "message": "Hello!" }
```

## Data Models

- **`Interest`** (`chat_auth`): an interest a user can pick, such as a hobby.
- **`Profile`** (`chat_auth`): a one-to-one extension of `User` with `is_online`, `phone`, `gender`, `country` and `interests`.
- **`RoomNames`** (`chat_app`): a chat room between `my_user` and `other_user`, identified by `group_name`.
- **`MessageHistory`** (`chat_app`): a message with its `room`, `sender`, `text` and `sent_date`.

## How It Works

1. A user opens `/chat/<user_id>/`. The view looks up the room for that pair of users, creates it if it does not exist, and renders the saved message history.
2. The browser opens a WebSocket connection to `ws/chat/<room_name>/`.
3. `ChatConsumer` accepts the connection and adds it to the `chat_<room_name>` group on the channel layer.
4. When a message arrives, the consumer saves it to `MessageHistory` with its room and sender.
5. The consumer broadcasts the message to the room group.
6. Every connected client in the room receives the message through its WebSocket.

## Configuration and Production Notes

The settings in `chat_project/chat_project/settings.py` are meant for development. Before deploying:

- **Channel layer:** the project uses `InMemoryChannelLayer`, which works with only one process. For multiple workers, switch to Redis (`channels-redis` is already in `req.txt`):

  ```python
  CHANNEL_LAYERS = {
      "default": {
          "BACKEND": "channels_redis.core.RedisChannelLayer",
          "CONFIG": {"hosts": [("127.0.0.1", 6379)]},
      }
  }
  ```

- **Security:** load `SECRET_KEY` from an environment variable, set `DEBUG = False`, and fill in `ALLOWED_HOSTS`. WebSocket connections are checked against `ALLOWED_HOSTS` by `AllowedHostsOriginValidator`.
- **Server:** run the app with Daphne:

  ```bash
  daphne -b 0.0.0.0 -p 8000 chat_project.asgi:application
  ```

- **Database:** replace SQLite with PostgreSQL or another production database.
