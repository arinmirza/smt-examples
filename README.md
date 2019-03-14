# Solving Knight's Tour Problem using z3-Solver

## Usage
Run the python script with the following optional parameters:

    python3 knights-tour.py --rows 3 --cols 10 --x 0 --y 0 --closed true

`rows` and `cols` determine the size of the chessboard. `x` and `y` are the starting coordinates of the knight, where `x` and `y` are the starting row and column, respectively. If `closed` is set to true, solver will try to find a closed knight's tour.

Note that anything more than 30 cells take an indefinite amount of time to solve. Otherwise please wait for at least a couple of minutes.

## Requirements and Dependencies
* Python 3
* The z3-solver package must be installed, use `pip install z3-solver`
