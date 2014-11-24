from pyevo.agents import (Agent,
                          AlwaysCooperateAgent,
                          AlwaysDefectAgent,
                          TitForTatAgent)


class TestAlwaysCooperateAgent(object):

    def test_enemy_cooperated(self):
        enemy = Agent('b')
        enemy.last = 'C'
        agent = AlwaysCooperateAgent('b')
        assert agent.update(enemy) == 'C'

    def test_enemy_defected(self):
        enemy = Agent('b')
        enemy.last = 'D'
        agent = AlwaysCooperateAgent('b')
        assert agent.update(enemy) == 'C'


class TestAlwaysDefectAgent(object):

    def test_enemy_cooperated(self):
        enemy = Agent('b')
        enemy.last = 'C'
        agent = AlwaysDefectAgent('b')
        assert agent.update(enemy) == 'D'

    def test_enemy_defected(self):
        enemy = Agent('b')
        enemy.last = 'D'
        agent = AlwaysDefectAgent('b')
        assert agent.update(enemy) == 'D'


class TestTitForTatAgent(object):

    def test_enemy_cooperated(self):
        enemy = Agent('b')
        enemy.last = 'C'
        agent = TitForTatAgent('b')
        assert agent.update(enemy) == 'C'

    def test_enemy_defected(self):
        enemy = Agent('b')
        enemy.last = 'D'
        agent = TitForTatAgent('b')
        assert agent.update(enemy) == 'D'
