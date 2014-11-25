from pyevo.circle_board import CircleBoard
from pyevo.agents import (TitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.imitation_game import ImitationGame


if __name__ == '__main__':
    # Define the agents to be used
    agents = {
        'left': {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
                 'color': 'g'},
        'right': {'name': 'Always Defect', 'class': AlwaysDefectAgent,
                  'color': 'r'},
        'center': {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
                   'color': 'b'},
    }

    # Initialize the board
    board = CircleBoard(agents)

    # Select the payoffs used in this game
    payoffs = prisoners_dilemma()

    # Initialize the game
    game = ImitationGame(board, payoffs, 'circle_01')

    # Run the game over 100 time steps, results will be saved in out/circle_01/
    game.run(100)
