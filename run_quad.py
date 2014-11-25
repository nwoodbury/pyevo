from pyevo.quad_board import QuadBoard
from pyevo.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.imitation_game import ImitationGame


if __name__ == '__main__':
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},
        {'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}
    ]
    board = QuadBoard(quads)

    # fig = plt.figure(figsize=(12, 12))
    # board.draw(plt, fig)
    # plt.show()

    payoffs = prisoners_dilemma()

    game = ImitationGame(board, payoffs, 'quad_01')
    game.run(100)
