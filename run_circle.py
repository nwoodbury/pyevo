from pyevo.circle_board import CircleBoard
from pyevo.agents import (TitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.imitation_game import ImitationGame


if __name__ == '__main__':
    agents = {
        'left': {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
                 'color': 'g'},
        'right': {'name': 'Always Defect', 'class': AlwaysDefectAgent,
                  'color': 'r'},
        'center': {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
                   'color': 'b'},
    }
    board = CircleBoard(agents)

    # fig = plt.figure(figsize=(12, 12))
    # board.draw(plt, fig)
    # plt.show()

    payoffs = prisoners_dilemma()

    game = ImitationGame(board, payoffs, 'circle_01')
    game.run(100)
