from matplotlib.colors import ColorConverter


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

    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

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
        self.board[x][y] = agent

    def at(self, x, y):
        """
        Returns the agent at (x, y).
        """
        return self.board[x][y]

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
        return M

    def init_agent(self, name):
        """
        Returns an initialized agent that is defined under `name` in
        `self.agent_defs`.

        Parameters
        ----------
        name : str
            The name of the agent to initialized. Must be a key in
            `self.agents_def`

        Return
        ------
        agent : Agent
            The initialized agent, with a color initialized to be consistent
            with the color of all other agents of the same class.
        """
        return self.agent_defs[name]['class'](
            self.agent_defs[name]['color'], name)

    def get_opposite_dir(self, dir):
        """
        Gets the direction opposite of what is given.

        Parameters
        ----------
        dir : str in {'N', 'NE', 'E', etc.}

        Returns
        -------
        dir : str in {'N', 'NE', 'E', etc.}
            The opposite direction; e.g. if dir is N, returns S.
        """
        return {
            'N': 'S',
            'NE': 'SW',
            'E': 'W',
            'SE': 'NW',
            'S': 'N',
            'SW': 'NE',
            'W': 'E',
            'NW': 'SE'
        }[dir]

    def get_coord_at_dir(self, x, y, dir):
        """
        Gets the coordinates of the point at dir from (x, y).
        N is +y, E is +x/

        For example, if x = 5, y = 10, dir = NE, returns (6, 11).

        If either x or y leaves the board, returns None in its place.

        Parameters
        ----------
        x : int [0, 30)
        y : int [0, 30)
        dir : str in {'N', 'NE', 'E', etc.}

        Returns
        -------
        x : int [0, 30) or None
        y : int [0, 30) or None
        """
        if 'N' in dir:
            y += 1
        if 'S' in dir:
            y -= 1
        if 'E' in dir:
            x += 1
        if 'W' in dir:
            x -= 1

        if x < 0 or x >= 30 or y < 0 or y >= 30:
            return None, None
        return x, y
