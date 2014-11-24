pyevo
=====

CS 670 Lab 2 - Evolutionary Dynamics

## Installation ##

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
