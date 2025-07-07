import chess
import chess.pgn
import io
import google.generativeai as genai

# === DON'T SHARE THIS! Keep your key private ===
genai.configure(api_key="AIzaSyBm7QN2AspC3HI93pBUxTC6ONQXTlm2omc")

board = chess.Board()

def gemini_suggest_move(fen: str, level: int = 3):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
You are a strong chess engine. Analyze this chess position and suggest the best move for the side to play.

FEN: {fen}

Respond ONLY with the best move in UCI format (e.g., e2e4, g1f3, e7e5). Do not explain or add anything else.
"""

    try:
        response = model.generate_content(prompt)
        move_text = response.text.strip().split()[0]
        return move_text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None

def selectmove(depth):
    fen = board.fen()
    move = gemini_suggest_move(fen, depth)

    try:
        if move:
            candidate = chess.Move.from_uci(move)
            if candidate in board.legal_moves:
                return candidate.uci()
    except:
        pass

    print("Gemini gave invalid move or failed. Using fallback.")
    return list(board.legal_moves)[0].uci()

def call_AI(pgn, level):
    global board
    if not pgn:
        board = chess.Board()
    else:
        game = chess.pgn.read_game(io.StringIO(pgn)).end()
        board = game.board()
    return selectmove(level)

if __name__ == "__main__":
    print("Gemini move:", call_AI("", 3))
