from pyevo.game import Game
import matplotlib.pyplot as plt
import numpy as np


class ReplicationGame(Game):
    """
    Defines a game running replication dynamics. Takes the same parameters as
    `Game`, but note that `board` should actually be an initialized
    `Population` object.
    """

    def update(self):
        """
        Updates a single round of the game.
        """
        pass

    def run(self, t, interval=1, fps=2):
        """
        Runs the game, creating animations. Overrides the base function in
        `Game`.
        """
        fig = plt.figure(figsize=(12, 12))
        ax = plt.gca()

        xs = np.arange(len(self.board.agents))
        width = 0.5
        labels = [name for name in self.board.agents.keys()]
        colors = [self.board.agent_defs[name]['color'] for name
                  in labels]

        ys = [len(self.board.agents[name]) for name in labels]
        bar = ax.bar(xs + width, ys, width, color=colors)
        ax.set_xticks(xs + 3 / 2.0 * width)
        ax.set_xticklabels(labels)
        plt.ylabel('Number of Agents')

        time_text = ax.text(0.02, 0.95, 'Initialization',
                            transform=ax.transAxes)

        plt.show()
