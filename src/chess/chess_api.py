import requests

CHESS_API_BASE_URL = "https://api.chess.com/pub"

HEADERS = {
    "User-Agent": "ChessApp/1.0",
    "Accept": "application/json",
}

def get_player_profile(username: str):
    """Fetches the profile of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_player_stats(username: str):
    """Fetches the statistics of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}/stats"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()