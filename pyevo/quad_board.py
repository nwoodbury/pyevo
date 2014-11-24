from pyevo.board import Board


class QuadBoard(Board):
    """
    Puts a different agent in each corner (can duplicate agents in corners).

    Parameters
    ----------
    quads : array of dicts
        An array containing dictionaries. Each dictionary conains three
        attributes, 'name', 'color' and 'class'. 'name' defines the name of
        the agent (use the same name in different quadrents of the array to
        use the same agent in different corners) 'class' tells the board which
        agent class goes in the given position, and 'color' tells the board
        what color to draw that agent.

        The array contains 4 elements, the first defines the agents in the
        top-left corner of the board, the second defines the agents in the
        top-right, the third defines the agents in the bottom-left and the
        fourth defines the agents in the bottom right.

        For example, let
        quads = [
            {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
             'color': 'b'},
            {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
             'color', 'm'},
            {'name': 'Always Cooperate', class': AlwaysCooperateAgent,
             'color': 'g'},
            {'name': 'Always Defect', 'class': AlwaysDefectAgent,
             'color': 'r'}
        ]
        This puts Tit-for-Tat agents, drawn blue, in the top left corner of
        the board, magenta Not-Tit-for-Tat agents in the top right corner, etc.
    """

    def __init__(self, quads):
        self.agent_defs = {}
        for quad in quads:
            assert 'name' in quad
            assert 'class' in quad
            assert 'color' in quad
            name = quad['name']
            self.agent_defs[name] = {}
            self.agent_defs[name]['color'] = quad['color']
            self.agent_defs[name]['class'] = quad['class']

        self.board = []
        for x in range(30):
            row = []
            for y in range(30):
                if x < 15:
                    if y < 15:
                        row.append(self.init_agent(quads[2]['name']))
                    else:
                        row.append(self.init_agent(quads[3]['name']))
                else:
                    if y < 15:
                        row.append(self.init_agent(quads[0]['name']))
                    else:
                        row.append(self.init_agent(quads[1]['name']))
            self.board.append(row)
