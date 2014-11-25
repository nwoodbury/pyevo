import random


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
        """
        Initializes and returns a new agent of type name.
        """
        return self.agent_defs[name]['class']('w', name)

    def update(self):
        """
        Runs a round of the replication dynamics. Does this by

            1. Collecting a list of all agents currently in the game.
            2. Iterate over each agent and compete it against a random agent.
                - The agent either stays the same type or replicates the type
                  of the enemy, depending on which received the higher payoff.
                - Note that each agent competes against the population before
                  the update made in this round, not during (therefore, each
                  has the same odds of competing against the same type of
                  agent).
        """
        # Collect agents from current agents
        agent_list = []
        for name, lst in self.agents.iteritems():
            agent_list += lst
            self.agents[name] = []

        for agent in agent_list:
            self.compete_agent(agent, agent_list)

    def compete_agent(self, agent, agent_list):
        enemy_i = random.randint(0, 899)
        enemy = agent_list[enemy_i]

        agent_action = agent.update(enemy)
        enemy_action = enemy.update(agent)

        agent_payoff = self.payoffs[agent_action][enemy_action]
        enemy_payoff = self.payoffs[enemy_action][agent_action]

        if agent_payoff >= enemy_payoff:
            best_agent = agent.name
        else:
            best_agent = enemy.name

        new_agent = self.init_agent(best_agent)
        new_agent.last = agent_action
        self.agents[best_agent].append(new_agent)

    def draw():
        pass
