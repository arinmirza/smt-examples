from z3 import *
import pprint, math
import sys, argparse

# This implementation is influenced by the related example of Dennis Yurichev, please see https://yurichev.com/writings/SAT_SMT_by_example.pdf#page=523

# Parser Settings
parser = argparse.ArgumentParser()
parser.add_argument('--rows', help='Number of rows of the chessboard')
parser.add_argument('--cols', help='Number of columns of the chessboard')
parser.add_argument('--x', help='Start x-coordinate of the knight')
parser.add_argument('--y', help='Start y-coordinate of the knight')
parser.add_argument('--closed', help='Whether the tour needs to be closed or not. If the knight ends on a square that is one knight\'s move from the beginning square, the tour is closed, otherwise it is open.')

# Chessboard Configurations
args = parser.parse_args()
row_count = int(args.rows) if args.rows else 5
col_count = int(args.cols) if args.cols else 5
start_cell_row = int(args.x) if args.x else 0
start_cell_col = int(args.y) if args.y else 0
closed_tour = bool(args.closed) if args.closed else False
cell_count = row_count * col_count

# Initialize z3 solver
solver = Solver()

# Indices start from 0 and None denotes an index outside of the board
def coord_to_index(row, col):
	if row < 0 or col < 0:
		return None
	if row >= row_count or col >= col_count:
		return None
	return row * col_count + col

# The adjacency graph G contains the reachable cells from each cell
# There are at max 8 cells which are reachable from a knights current position
# . . . . . . .
# . . 8 . 1 . .
# . 7 . . . 2 .
# . . . K . . .
# . 6 . . . 3 .
# . . 5 . 4 . .
# . . . . . . .

G = {}

for row in range(row_count):
	for col in range(col_count):
		current = coord_to_index(row, col)
		adjacents = []

		adjacents.append(coord_to_index(row-2, col+1))
		adjacents.append(coord_to_index(row-1, col+2))
		adjacents.append(coord_to_index(row+1, col+2))
		adjacents.append(coord_to_index(row+2, col+1))
		adjacents.append(coord_to_index(row+2, col-1))
		adjacents.append(coord_to_index(row+1, col-2))
		adjacents.append(coord_to_index(row-1, col-2))
		adjacents.append(coord_to_index(row-2, col-1))

		# Remove the None coordinates, which lie outside of the board
		adjacents = [x for x in adjacents if x != None]
		G[current] = adjacents

# We use one-hot bitvectors with a length equal to the number of cells on the board
# The position of the set bit (counting from right) in a vector will denote the visit time of the cell

# Example for a 4x4 board:
# If V[7] = '0000000000001000' this means the cell with the index 7 was visited at step 3
V = [BitVec('Vector_%d' % i, cell_count) for i in range(cell_count)]

# The starting cell will always be visited at step 0, i.e V[0] = '0000000000000001'
starting_cell = coord_to_index(start_cell_row, start_cell_col)
solver.add(V[starting_cell] == BitVecVal(1, cell_count))


# Assert bitvectors to be distinct, this will ensure that every cell is visited exactly once
solver.add(Distinct(V))


# Assert each bitvector to be reachable from a valid last position
# A cell j is visited right after another cell i, if V[j] = 2 * V[i]
# For the case of a closed tour, we used V[j] = rotate_left(V[i]) instead
for i in range(cell_count):
	if not closed_tour and i == starting_cell:
		continue
	adjacents = [RotateLeft(V[j], 1) for j in G[i]]
	or_clause = [V[i] == a for a in adjacents]
	solver.add(Or(*or_clause))

# In a closed tour, all valid solutions have to consist of exclusively one-hot vectors, z3 finds that for us
# However, in the case of a non-closed tour, this is not true anymore. 
# Hence, we assert all vectors to be a power of two
if not closed_tour:
	for v in range(cell_count):
		twos_powers = [2**i for i in range(cell_count)]
		or_clause = [V[v] == t for t in twos_powers]
		solver.add(Or(*or_clause))

print("Solving, this may take long.")

# Solve and print
if solver.check() == unsat:
	print("unsat")
	exit(0)

m = solver.model()

for row in range(row_count):
	for col in range(col_count):
		index = coord_to_index(row, col)
		value = math.log(m[V[index]].as_long(), 2)
		print("%2d " % value, end='')
	print("")
