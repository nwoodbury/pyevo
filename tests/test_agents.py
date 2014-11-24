from pyevo.agents import (Agent,
                          AlwaysCooperateAgent,
                          AlwaysDefectAgent,
                          TitForTatAgent,
                          NotTitForTatAgent,
                          GrudgeTitForTatAgent,
                          GrudgeNotTitForTatAgent)


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


class TestNotTitForTatAgent(object):

    def test_enemy_cooperated(self):
        enemy = Agent('b')
        enemy.last = 'C'
        agent = NotTitForTatAgent('b')
        assert agent.update(enemy) == 'D'

    def test_enemy_defected(self):
        enemy = Agent('b')
        enemy.last = 'D'
        agent = NotTitForTatAgent('b')
        assert agent.update(enemy) == 'C'


class TestGrudgeTitForTatAgent(object):

    def test_first_move_c(self):
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeTitForTatAgent('b')
        assert agent.update(currenemy) == 'C'

    def test_first_move_d(self):
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeTitForTatAgent('b')
        assert agent.update(currenemy) == 'C'

    def test_cc(self):
        lastenemy = Agent('b')
        lastenemy.last = 'C'
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'C'

    def test_cd(self):
        lastenemy = Agent('b')
        lastenemy.last = 'C'
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'C'

    def test_dc(self):
        lastenemy = Agent('b')
        lastenemy.last = 'D'
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'D'

    def test_dd(self):
        lastenemy = Agent('b')
        lastenemy.last = 'D'
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'D'


class TestGrudgeNotTitForTatAgent(object):

    def test_first_move_c(self):
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeNotTitForTatAgent('b')
        assert agent.update(currenemy) == 'D'

    def test_first_move_d(self):
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeNotTitForTatAgent('b')
        assert agent.update(currenemy) == 'D'

    def test_cc(self):
        lastenemy = Agent('b')
        lastenemy.last = 'C'
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeNotTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'D'

    def test_cd(self):
        lastenemy = Agent('b')
        lastenemy.last = 'C'
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeNotTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'D'

    def test_dc(self):
        lastenemy = Agent('b')
        lastenemy.last = 'D'
        currenemy = Agent('b')
        currenemy.last = 'C'
        agent = GrudgeNotTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'C'

    def test_dd(self):
        lastenemy = Agent('b')
        lastenemy.last = 'D'
        currenemy = Agent('b')
        currenemy.last = 'D'
        agent = GrudgeNotTitForTatAgent('b')
        agent.update(lastenemy)
        assert agent.update(currenemy) == 'C'
