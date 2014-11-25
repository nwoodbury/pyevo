import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Game:
    """
    Defines the dynamics of an evolutionary game. To be inherited to define
    rules of imitator dynamics or replicator dynamics.
    """

    def __init__(self, board, payoffs):
        self.board = board
        self.payoffs = payoffs

    def run(self, t):
        """
        Runs the game, animating the results.

        Parameters
        ----------
        t : int
            The number of timesteps for which the game will run.
        """
        fig = plt.figure(figsize=(12, 12))
        M = self.board.draw(plt, fig)
        im = plt.imshow(M, interpolation='none', origin='lower',
                        extent=(0, 29, 0, 29))

        ax = fig.gca()

        time_text = ax.text(0.02, 0.95, 'Initialization',
                            transform=ax.transAxes)
        ticks = np.arange(0, 30)
        plt.xlim((0, 29))
        plt.ylim((0, 29))
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)

        def update_fig(i):
            self.update()
            M = self.board.draw(plt, fig)
            im.set_array(M)
            time_text.set_text('t = %i' % (i + 1))
            return im, ax

        ani = animation.FuncAnimation(fig, update_fig, frames=t, blit=True,
                                      interval=100, repeat=False)
        plt.show()
