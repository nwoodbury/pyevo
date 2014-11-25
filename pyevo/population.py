

class Population:
    """
    Defines a population of agents for the replicator dynamics.

    Parameters
    ----------
    agent_defs : dict
        Defines the agents that exist in the population, including levels.
        For example:

            agent_defs = {
                'Tit-for-Tat': {
                    'class': TitForTatAgent,
                    'color': 'b',
                    'number': 400
                },
                'Always Cooperate': {
                    'class': AlwaysCooperate,
                    'color': 'g'
                    'number': 500
                }
            }

        This creates two agents, 400 in 'Tit-for-Tat' and 500 in
        'Always Cooperate' at the beginning of the simulation, and lets the
        game know how to create these agents. When drawn, 'Tit-for-Tat' will
        have a green bar and 'Always Cooperate' will have a blue bar.

        Note that the sum of number of all agents must equal 900.
    """

    def __init__(self, agent_defs):
        self.agent_defs = agent_defs
        assert sum([adef['number'] for name, adef in agent_defs.iteritems()]) \
            == 900

        self.agents = {}
        for name, adef in agent_defs.iteritems():
            self.agents[name] = []
            for i in range(adef['number']):
                self.agents[name].append(self.init_agent(name))

    def init_agent(self, name):
        return self.agent_defs[name]['class']('w', name)

    def update(self):
        pass

    def draw():
        pass
