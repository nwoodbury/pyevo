

class Agent:
    """
    General class defining an agent playing in the game. This class should
    be inherited, and function `update()` should be overwritten.

    Note, for agent security (and no cheating), only the Agent class will have
    an `__init__` function. No agent subclass can be allowed to have its own
    `__init__`.



    Parameters
    ----------
    color : matplotlib color
        Colors are to be determined by the game. Each agent class should have
        its own unique color.

        See http://matplotlib.org/api/colors_api.html for all possible
        matplotlib colors. It may be a good idea to stick with the string
        colors (e.g. 'b', 'g', 'r', 'y', etc.)

    Attributes
    ----------
    last : str in {'C', 'D'}
        'C' if this agent's last move was to cooperate, 'D' if it was to
        defect. Initializes to 'C' on turn 0 for all agents (this should not
        be changed for any derived agents, that would be sneaky and possibly
        self-defeating).

        Note that, in order to prevent cheating, the game will update this
        attribute after the agent has made its move. No need to update it
        in the `update` function.
    color : matplotlib color
        Set by the parameter to the `__init__` function.
    """

    def __init__(self, color):
        self.last = 'C'
        self.color = color

    def update(self, enemy):
        """
        Determines and returns the next move made by this agent.

        Parameters
        ----------
        enemy : Agent
            The enemy that the agent will be playing THIS round.
        """
        raise NotImplementedError()


class AlwaysCooperateAgent(Agent):

    def update(self, enemy):
        return 'C'
