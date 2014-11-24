from pyevo.quad_board import QuadBoard
from pyevo.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
import matplotlib.pyplot as plt


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

    plt.figure()
    board.draw(plt)
    plt.show()
