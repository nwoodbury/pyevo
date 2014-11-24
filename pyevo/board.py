from matplotlib.colors import ColorConverter
import numpy as np


class Board:
    """
    Defines the board of the game, containing functions to update the agents
    and draw each frame as the animation progresses.

    The init function, defining the initial state of the board, should be
    defined in a subclass inheriting this class.

    Attributes
    ----------
    agent_defs : dictionary
        A dictionary mapping agent names (string) to class and color. For
        example, the dictionary:

        agent_defs = {
            'Tit-for-Tat': {
                'class': TitForTatAgent,
                'color': 'b'
            },
            'Always Cooperate': {
                'class': AlwaysCooperate,
                'color': 'g'
            }
        }

        defines 2 agents, Tit-for-Tat and Always Cooperate, which are the
        only agents that can exist on the board. Further, it points to the
        class defining the agent and the color which the agent should be drawn.

    board : 2-dimensional array
        A 30-30 array containing agents.
    """

    def set_agent(self, x, y, agent):
        """
        Sets the agent at (x, y) to agent.

        Parameters
        ----------
        x : int [0, 30)
            The x coordinate.
        y : int [0, 30)
            The y coordinate.
        agent : Agent
            The agent to set at (x, y)
        """
        assert x >= 0
        assert x < 30
        assert y >= 0
        assert y < 30
        self.board[x][y] == agent

    def draw(self, plt, fig):
        """
        Draws the present state of the board.
        """
        M = []
        colors = ColorConverter().colors
        for x in range(30):
            row = []
            for y in range(30):
                agent = self.board[x][y]
                rgb = colors[agent.color]
                row.append(rgb)
            M.append(row)

        plt.imshow(M, interpolation='nearest', origin='lower',
                   extent = (0, 29, 0, 29))
        ax = fig.gca()
        ticks = np.arange(0.5, 30.5, 1.0)
        plt.xlim((-0.5, 29.5))
        plt.ylim((-0.5, 29.5))
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ticklabels = [i + 1 for i in range(30)]
        ax.set_xticklabels(ticklabels)
        ax.set_yticklabels(ticklabels)
        plt.grid()


    def init_agent(self, name):
        """
        Returns an initialized agent that is defined under `name` in
        `self.agent_defs`.

        Return
        ------
        agent : Agent
            The initialized agent, with a color initialized to be consistent
            with the color of all other agents of the same class.
        """
        return self.agent_defs[name]['class'](self.agent_defs[name]['color'])
