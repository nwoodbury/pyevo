import math
from pyevo.quad_board import QuadBoard


class CircleBoard(QuadBoard):
    """
    Simulates three agents, one taking the left half, one taking the right,
    and a third taking a circular region in the middle.

    Parameters
    ----------
    agents : dictionary
        A dictionary defining the agents. For example, let

        agents = {
            'left': {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
                     'color': 'g'},
            'right': {'name': 'Always Defect', 'class': AlwaysDefectAgent,
                      'color': 'r'},
            'center': {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
                       'color': 'b'},
        }

        This puts an Always Cooperate agent (green) on the left half, an
        Always Defect agent (red) on the right half, and a Tit-for-Tat agent
        (blue) in the middle.
    radius : number
        The radius of agents around the circle to fill with the center agent.
    """

    def __init__(self, agents, radius=9):
        # Build a 'quad board' where the top-left and bottom left are the same,
        # and likewise for the right
        quads = [agents['left'], agents['right'], agents['left'],
                 agents['right']]
        QuadBoard.__init__(self, quads)

        # The quad board defines the left and right agents, but not the center.
        # We define the center now
        centername = agents['center']['name']
        self.agent_defs[centername] = {
            'color': agents['center']['color'],
            'class': agents['center']['class']
        }

        # Now replace the agents in the center with the desired agents
        for x in range(30):
            for y in range(30):
                cx = x - 14
                cy = y - 14
                if math.sqrt(cx * cx + cy * cy) <= radius:
                    agent = self.init_agent(centername)
                    self.set_agent(x, y, agent)
