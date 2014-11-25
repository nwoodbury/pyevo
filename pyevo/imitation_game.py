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
            2. Update agent states.
            3. Each agent evaluates its own average payoff with that of the
               others. Determines which strategy to switch to (doesn't
               switch yet, lets all others make the same evaluation).
            4. Each agent switches to the new agent
        """

        # Play agents against neighbors to compute payoffs
        for x in range(30):
            for y in range(30):
                self.play_agent(x, y)

        # Update agent state
        for x in range(30):
            for y in range(30):
                agent = self.board.at(x, y)
                agent.last_against = agent.curr_against
                agent.curr_against = {}

        # Find neighbors with highest payoffs (including self)
        for x in range(30):
            for y in range(30):
                self.find_best_neighbor(x, y)

        # Update to new agent
        for x in range(30):
            for y in range(30):
                agent = self.board.at(x, y)
                self.board.set_agent(x, y, agent.next_agent)

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

        agent = self.board.at(x, y)
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

        agent = self.board.at(x, y)
        enemy = self.board.at(nx, ny)

        agent.last = agent.last_against[dir]
        enemy.last = enemy.last_against[opposite]

        agent_action = agent.update(enemy)
        enemy_action = enemy.update(agent)

        agent.curr_against[dir] = agent_action
        payoff = self.payoffs[agent_action][enemy_action]

        return payoff

    def find_best_neighbor(self, x, y):
        """
        Updates the agent at x, y to imitate the neighbor agent with the
        best payoff (considers itself as a neighbor). Tie goes to first
        neighbor observed with best payoff.
        """
        agent = self.board.at(x, y)
        best_payoff = agent.curr_payoff
        best_agent = agent.name
        for dir in self.board.dirs:
            nx, ny = self.board.get_coord_at_dir(x, y, dir)
            if nx is None or ny is None:
                continue
            enemy = self.board.at(nx, ny)
            if enemy.curr_payoff >= best_payoff:
                best_payoff = enemy.curr_payoff
                best_agent = enemy.name

        if x == 14 or x == 15 or y == 14 or y == 15:
            print '(%i, %i) %s -> %s' % (x, y, agent.name, best_agent)

        new_agent = self.board.init_agent(best_agent)
        # Update state of new agent to curr agent
        new_agent.last = agent.last
        new_agent.last_against = agent.last_against
        new_agent.curr_against = agent.curr_against
        agent.next_agent = new_agent
