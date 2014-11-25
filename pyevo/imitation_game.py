from pyevo.game import Game


class ImitationGame(Game):
    """
    Runs a game using the imitation dynamics
    """

    def update(self):
        """
        Updates a single round of the game.

        The phases of the round are as follows:
            1. Each agent first plays against all of its neighbors. Payoffs are
               calculated as the average of payoffs against all neighbors
               played (thus border agents are roughly equal to inner agents).
            2. Each agent evaluates its own average payoff with that of the
               others. Switches to best strategy.
        """

        # Play agents against neighbors to compute payoffs
        for x in range(30):
            for y in range(30):
                self.play_agent(x, y)

        # Find neighbors with highest payoffs (including self), imitate.
        pass

    def play_agent(self, x, y):
        """
        Plays the agent at (x, y) against all 8 neighbors.
        """
        count = 0
        payoffs = 0
        for dir in self.board.dirs:
            payoff = self.play_against(x, y, dir)
            if payoff is not None:
                count += 1
                payoffs += payoff

        agent = self.board[x][y]
        agent.last_against = agent.curr_against
        agent.curr_against = {}
        agent.curr_payoff = payoffs / float(count)

    def play_against(self, x, y, dir):
        """
        Plays the agent at (x, y) against the neighbor at dir.

        Returns
        -------
        payoff : number
            The payoff to the agent at (x, y) received by playing ag
        """
        nx, ny = self.board.get_coord_at_dir(x, y, dir)
        if nx is None or ny is None:
            return None
        opposite = self.board.get_opposite_dir(dir)

        agent = self.board[x][y]
        enemy = self.board[nx][ny]

        agent.last = agent.last_against[dir]
        enemy.last = enemy.last_against[opposite]

        agent_action = agent.update(enemy)
        enemy_action = enemy.update(agent)

        agent.curr_against[dir] = agent_action
        return self.payoffs[agent_action][enemy_action]
