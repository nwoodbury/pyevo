pyevo
=====

CS 670 Lab 2 - Evolutionary Dynamics

## Installation ##

Install `ffmpeg` (required to save animations). For linux:

        sudo add-apt-repository ppa:jon-severinsson/ffmpeg
        sudo apt-get update
        sudo apt-get install ffmpeg
        sudo apt-get install frei0r-plugins

Clone `pyevo` into the directory of choice:

        git clone https://github.com/nwoodbury/pyevo

Navigate to the new `pyevo` directory:

        cd pyevo

Install `pyevo` with:

        python setup.py develop --user

## Testing ##

All test cases should be run before committing any changes. To run all the
test cases:

        python setup.py test

## A Note on Agents ##

In the project documentation, the following 4 agents are defined based on
what "the other agent" does in the previous round:

1. Always Cooperate: Plays Cooperate every round
2. Always Defect: Plays Defect every round
3. Tit-for-Tat: Plays the same thing that the "other agent" did on the last
round.
4. Not-Tit-for-Tat: Plays the opposite thing that the "other agent" did on the
last round.

The project specification is ambiguous on whether the "other agent" is defined
as the agent that my agent is playing this round or whether it is the agent
played in the last round. We define "other agent" as the agent my agent is
playing THIS round.

## Running a Game ##

To date, there are two games defined (both on imitation dynamics). They are
as follows:

1. Quad: Starts each of the four agents in its own corner.
    - To run:

            python run_quad.py

    - Variations to try: (Comment out and define a new definition for `quads`,
      starting line 10):
        * Re-order the agents (swap the agents on the east or swap the agents
          in the south)
        * Make one agent take up more than one quad (duplicate the agent's
          entry in the list). Try diagonal or adjacent quads that are
          the same agent.

2. Circle: Based on quads, but the east and west sides each only have one agent
type. in addition, the center agents have been replaced with a third agent
type.
    - To run:

            python run_circle.py

    - Variations to try: (comment and define a new definition for `agents`,
      starting line 10).
        * Try different agents in differnt locations
        * Involve Not-Tit-for-Tat in the mix
        * Implement a variation with quads instead of sides

3. Equal Populations: This is a replicator dynamic game instead of an
imitator dynamic game.
    - To run:

        python run_eqpop.py

    - Variations to try: (comment out and define a new definition for `agents`)
        * Play with different initial populations (can't think of much else
          to try).

## Defining a New Game ##

Copy either `run_circle.py` or `run_quads.py` and change the details. The work
flow of the game should not change much (though it may a little when we add
replication dynamics).

## Initializing a Board ##

For imitation dynamics, the initial state of the board is what drives all game
variations. To create a custom board, the following tips should be useful.

* Each type of initial board configuration should be defined in its own
subclass which inherits either from `Board` (which the `QuadsBoard` class does)
or another subclass of `Board` (see the `CircleBoard` class, it inherits from
`QuadsBoard` rather than `Board`). Notice that the two types of game described
above each are driven by a board subclass (Quad defined in `quad_board.py`
and Circle defined in `circle_board.py`).

* The board must understand all agents that are on it at the beginning. This
information is stored in a dictionary called `agent_defs`, which names each
agent and defines the class that builds it and its color on the board. See
the documentation in `board.py`, starting line 14 for more information on
this attribute. See also lines 40-47 of quads.py for an example of how a board
subclass sets this variable. It will need to be set explicitely in all
subclasses.

* Once the board understands all agent types, a new agent can be created by
calling `init_agent(name)`, where `name` is the name given to the agent.
This function is available to all `Board` subclasses. See line 79 of `board.py`
for further documentation.

* The `Board` class and all its subclasses must contain a 30x30 2d array, where
each element is an `Agent` subclass. The `Board` class does not explicitely
initialize this array for now, it must be explicitely created (see lines
50-63 in `quad_board.py`). However, once created, an agent can be changed
by calling `set_agent(x, y, agent)`, available to all `Board` subclasses and
defined on line 39 of board.py. A work flow may be to do something similar
to lines 50-63 in `quad_board.py`, but fill every spot with a dummy agent,
and then go back and add more agents at desired places using `set_agent`.
This is done in `circle_board.py`, which first initializes a quad board,
and then replaces the agents in the circle with new agents (see lines
47-53 of `circle_board.py`)

* A possible, but impractical method of initializing the board would to be
to explicitely set what the agent should be at each of the 900 locations. It
is better to batch create sections of the board using for loops.

## TODO ##

* Add other payoffs (stag hunt, battle of the sexes)
* Use Gamma instead of time steps to define length of the game and compute
  payoffs.
* More experiments. Some to try:
    - A map of always cooperate and one or two always defect starting in a
      corner.
    - 1/4 one, 3/4 another
    - ...
