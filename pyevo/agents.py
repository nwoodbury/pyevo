

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
            The enemy that the agent will be playing THIS round. If the agent
            uses info from the agent played in the last round, then it must
            store that agent in its own state. Should not be storing anytime
            older than that.

        Returns
        -------
        action : str in {'C', 'D'}
            The action made by this agent, whether it is to cooperate or to
            defect.
        """
        raise NotImplementedError()


class AlwaysCooperateAgent(Agent):
    """
    An agent that always cooperates, regardless of what the other agents do.
    """

    def update(self, enemy):
        """
        Determines and returns the next move made by this agent, which is to
        always cooperate.

        See the documentation for `Agent.update()` for more details.
        """
        return 'C'


class AlwaysDefectAgent(Agent):
    """
    An agent that always defects, regardless of what the other agents do.
    """

    def update(self, enemy):
        """
        Determines and returns the next move made by this agent, which is to
        always defect.

        See the documentation for `Agent.update()` for more details.
        """
        return 'D'


class TitForTatAgent(Agent):
    """
    An agent that plays the same thing that the present enemy played on the
    last move (as opposed to the move that the last enemy played when matched
    with this agent, which is what the `GrudgeTitForTatAgent` does.)
    """

    def update(self, enemy):
        """
        Determines and returns the next move made by this agent, which is to
        do what the last enemy did.

        See the documentation for `Agent.update()` for more details.
        """
        return enemy.last


class NotTitForTatAgent(Agent):
    """
    An agent that plays the opposite thing that the present enemy played on the
    last move (as opposed to the move that the last enemy played when matched
    with this agent, which is what the `GrudgeNotTitForTatAgent` does.)
    """

    def update(self, enemy):
        """
        Determines and returns the next move made by this agent, which is to
        do what the last enemy did.

        See the documentation for `Agent.update()` for more details.
        """
        if enemy.last == 'C':
            return 'D'
        else:
            return 'C'
