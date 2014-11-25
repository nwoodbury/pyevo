from pyevo.quad_board import QuadBoard
from pyevo.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.imitation_game import ImitationGame


if __name__ == '__main__':
    # Define the agents to be in each quad
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},  # NW
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},  # NE
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},  # SW
        {'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}   # SE
    ]

    # Initialize the board
    board = QuadBoard(quads)

    # Select the payoffs used in this game
    payoffs = prisoners_dilemma()

    # Initialize the game
    game = ImitationGame(board, payoffs, 'quad_01')

    # Run the game over 100 time steps, results will be saved in out/quad_01/
    game.run(100)
