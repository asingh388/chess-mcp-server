from mcp.server.fastmcp import FastMCP
from .chess_api import get_player_profile, get_player_stats

mcp = FastMCP("chess.com")

@mcp.tool()
def fetch_player_profile(username: str):
    """Fetches the profile of a chess player by username."""
    return get_player_profile(username)

@mcp.tool()
def fetch_player_stats(username: str):
    """Fetches the statistics of a chess player by username."""
    return get_player_stats(username)

def main():
    mcp.run()

if __name__ == "__main__":
    main()