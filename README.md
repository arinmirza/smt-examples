# Solving Knight's Tour Problem using z3-Solver

## Usage
Run the python script with the following optional parameters:

    python3 knights-tour.py --rows 3 --cols 10 --x 0 --y 0 --closed true

`rows` and `cols` determine the size of the chessboard. `x` and `y` are the starting coordinates of the knight, where `x` and `y` are the starting row and column, respectively. If `closed` is set to true, solver will try to find a closed knight's tour.

Note that anything more than 30 cells take an indefinite amount of time to solve. Otherwise please wait for at least a couple of minutes.

## Requirements and Dependencies
* Python 3
* The z3-solver package must be installed, use `pip install z3-solver`

## Resources and Links

### SAT/SMT Language and Z3-Solver

- [SAT/SMT with Examples by Dennis Yurichev](https://yurichev.com/writings/SAT_SMT_by_example.pdf)
- [SMT-LIBv2 Language and Tools Tutorial](https://www.lri.fr/~conchon/TER/2013/2/SMTLIB2.pdf)
- [Z3 Tutorial on Rise4Fun](https://rise4fun.com/Z3/tutorial/guide) or [alternatively as PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.225.8231&rep=rep1&type=pdf)
- [Z3Py Tutorial for Python, includes short implementations for Sudoku and Eight Queens problems](https://www.notion.so/arinmirza/Project-Z3-Theorem-Solver-08065fa6f1a0450b8c943e3ba5456c16#77361ec737ee471888cd5709d8e0ec6f)
- [Z3Py API Namespace Reference](https://z3prover.github.io/api/html/namespacez3py.html)
- [Breadth First Traversal of a Directed Graph in Z3](https://medium.com/@rvprasad/sat-encoding-breadth-first-traversal-of-directed-graph-b571fc68c1af)

### Solving Sudoku and Related Problems

- [**(Paper)** Generating Sudoku Puzzles as an Inverse Problem](https://sites.math.washington.edu/~morrow/mcm/team2306.pdf)
- [How to generate sudoku boards with unique solutions](https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions)
- [E-Matching Problem explained, simplifying expressions that essentially mean the same thing](https://www.cs.upc.edu/~oliveras/espai/smtSlides/michal.pdf)
- [Einführung in die Aussagen- und Predikatenlogik, slides from TUM Diskrete Strukturen](https://www7.in.tum.de/um/courses/ds/ws1819/files/slides/_slides_3_logik-handout.pdf)

## Other

- [Personal Homepage of Dennis Yurichev](https://yurichev.com/)
- [Bit Manipulation Tricks](http://www.goldsborough.me/bits/c++/low-level/problems/2015/10/11/23-52-02-bit_manipulation)
