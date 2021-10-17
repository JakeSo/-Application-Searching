import nqueens
import random


def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    current = initBoard
    T = 1000

    while True:
        h = nqueens.numAttackingQueens(current)

        if T <= T_Threshold or h == 0:
            return current

        T = f(T, decayRate)

        sucStates = nqueens.getSuccessorStates(current)

        b = random.randint(0, len(sucStates) - 1)

        if (nqueens.numAttackingQueens(sucStates[b]) < h):
            current = sucStates[b]


def f(T, decayRate):
    return T * decayRate


# Test stuff

bo = nqueens.Board(5)
bo.rand()
bo.printBoard()
print(nqueens.numAttackingQueens(bo))

bo = simulatedAnnealing(bo, 0.5, 0.00000001)

bo.printBoard()
print(nqueens.numAttackingQueens(bo))