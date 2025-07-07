# ChessVerse

ChessVerse is a web-based chess platform built with Django, allowing users to play multiplayer chess games against other players or single-player games against an AI opponent powered by python-chess and enhanced with Google’s Gemini AI. The application supports real-time gameplay using WebSockets, a responsive chessboard interface, and persistent game storage in SQLite. Features include game creation, joining, resignation, and viewing ongoing/completed games.

## Features
- Multiplayer chess with real-time move synchronization via WebSockets.
- Single-player mode against an AI opponent, integrating python-chess and Gemini AI for intelligent move generation.
- User authentication for secure game access.
- Interactive chessboard with drag-and-drop moves, powered by Chess.js and Chessboard.js.
- Persistent game state storage in SQLite, with FEN and PGN tracking.
- Real-time opponent status updates (online/offline) and game outcome handling (checkmate, draw, resignation).
- Responsive UI with Bootstrap styling and modals for game events.

## Prerequisites
Before setting up ChessVerse, ensure you have the following installed:
- **Python 3.8+**: [Download](https://www.python.org/downloads/)
- **Redis**: For WebSocket group messaging.
  - **Ubuntu**: `sudo apt-get install redis-server`
  - **macOS**: `brew install redis`
  - **Windows**: Use Docker (`docker run -d -p 6379:6379 redis`) or a Windows-compatible Redis build.
- **pip**: Python package manager (included with Python).
- **Google Gemini API Key**: Obtain from [Google AI Studio](https://ai.google.dev/) for AI features.

## Installation

### Clone the Repository
Clone ChessVerse to your local machine:
```bash
git clone https://github.com/mrmadness49/chessverse.git
cd chessverse
```

### Set Up a Virtual Environment
Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Install Python Dependencies
Install required Python packages:
```bash
pip install django channels channels-redis python-chess[uci,gaviota] google-generativeai python-dotenv
```

### Install JavaScript Libraries
ChessVerse uses CDN-hosted JavaScript libraries in `game.html`. If you prefer local files:
1. Create a `static` directory in the project root or `chess` app directory.
2. Download or use npm to install:
   ```bash
   npm install chess.js chessboard-js reconnecting-websocket jquery bootstrap
   ```
3. Place files in `static/js/` and `static/css/` (e.g., `chess.min.js`, `chessboard-0.3.0.min.css`).
4. Run `python manage.py collectstatic` to gather static files.




## Contributing
Contributions are welcome! Fork the repository, make changes, and submit a pull request. Ensure tests pass and follow the project’s coding style.

## License
[MIT License](LICENSE) - feel free to use, modify, and distribute.