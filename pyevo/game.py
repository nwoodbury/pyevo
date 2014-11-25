

class Game:
    """
    Defines the dynamics of an evolutionary game. To be inherited to define
    rules of imitator dynamics or replicator dynamics.
    """

    def __init__(self, board, payoffs):
        self.board = board
        self.payoffs = payoffs

    def run(self):
        """
        Runs the game, animating the results.
        """
        pass
