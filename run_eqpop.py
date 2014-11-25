from pyevo.population import Population
from pyevo.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo.payoffs import prisoners_dilemma
from pyevo.replication_game import ReplicationGame


if __name__ == '__main__':
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 225
        },
        'Not-Tit-For-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 225
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 225
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 225
        }
    }
    pop = Population(agents)

    payoffs = prisoners_dilemma()

    game = ReplicationGame(pop, payoffs, 'eqpop_01')
    game.run(100)
