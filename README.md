
# Real-time Chat Application with WebSockets

This is a real-time chat application built using Django, Channels (for WebSocket support), and WebSockets. The application allows users to send and receive messages instantly.

## Features
- User sign-up and login functionality.
- Real-time chat using WebSockets.
- User-friendly interface with collapsible user menu.
- Message storage in the database.

## Prerequisites

- Python 3.x
- Django
- Django Channels
- Redis (for WebSocket support)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate your dependencies.

For **Windows**:

```bash
python -m venv venv
venv\Scripts ctivate
```

For **Linux/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python dependencies using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Install Redis

For WebSocket functionality, you need to have Redis installed and running locally. You can install Redis as follows:

- **Windows**: Download Redis from [here](https://github.com/microsoftarchive/redis/releases) and follow the installation steps.
- **Linux/macOS**: Use your package manager to install Redis.
  - For **Ubuntu**: `sudo apt-get install redis-server`
  - For **macOS**: `brew install redis`

Start Redis server:

```bash
redis-server
```

### 5. Apply Migrations

Run the Django migrations to set up the database.

```bash
python manage.py migrate
```

### 6. Start the Server

Finally, start the Django development server.

```bash
python manage.py runserver
```

Your application should now be running at `http://127.0.0.1:8000/`.

### 7. Access the Chat Application

Once the server is running, open your browser and go to the URL specified above to start using the chat application.

### 8. Testing the Application

- You can sign up and log in as a user.
- Open multiple browser windows/tabs to test real-time messaging.
- When a user sends a message, it should appear instantly in other users' windows.

## Contributions

Feel free to fork this project, make changes, and submit a pull request. Contributions are welcome!

