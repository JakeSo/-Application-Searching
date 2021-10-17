import random

import nqueens


def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    current = initBoard
    T = 1000
    print("Initial board:")
    initBoard.printBoard()
    h = nqueens.numAttackingQueens(current)
    print("h-value: " + str(h))
    while (T >= T_Threshold and h > 0):
        T = f(T, decayRate)

        sucStates = nqueens.getSuccessorStates(current)

        b = random.randint(0, len(sucStates) - 1)

        if (nqueens.numAttackingQueens(sucStates[b]) < h):
            current = sucStates[b]

        h = nqueens.numAttackingQueens(current)
    print("Final board:")
    current.printBoard()
    print("h-value: " + str(h))


def f(T, decayRate):
    return T * decayRate


def runTests():
    print('#' * 20)
    print("Simulated Annealing:")
    print("Decay rate: 0.5; Threshold: 1e-08")
    print('#' * 20)
    b = nqueens.Board(4)
    for x in range(10):
        b.rand()
        simulatedAnnealing(b, 0.5, 1 * 10 ^ -8)
