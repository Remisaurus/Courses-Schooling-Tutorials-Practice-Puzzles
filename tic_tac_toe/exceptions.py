# Check play.py for starting simple console game.

class InvalidGameState(Exception):
    """Raised when the game state is invalid."""
    
class InvalidMove(Exception):
    """Raised when the move is invalid."""
    
class UnknownGameScore(Exception):
    """Raised when the game score is unknown. (often game will be in progress)"""