from pyevo.custom_board_50_50 import CustomBoard
from pyevo.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.imitation_game import ImitationGame

if __name__ == '__main__':
    # Define the agents to be in each quad
    quads = [
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'}
    ]

    # Initialize the board
    board = CustomBoard(quads)

    # Select the payoffs used in this game
    payoffs = prisoners_dilemma()

    # Initialize the game
    game = ImitationGame(board, payoffs, 'custom_01')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game.run(100)
