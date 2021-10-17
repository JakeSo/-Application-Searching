import random

import nqueens


def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    current = initBoard
    T = 100
    print("Initial board:")
    h = nqueens.numAttackingQueens(current)
    print("h-value: " + str(h))
    initBoard.printBoard()
    print()

    while True:
        T = f(T, decayRate)

        if T <= T_Threshold:
            break

        sucStates = nqueens.getSuccessorStates(current)

        b = random.randint(0, len(sucStates) - 1)

        if (nqueens.numAttackingQueens(sucStates[b]) < h):
            current = sucStates[b]

        h = nqueens.numAttackingQueens(current)

        if h == 0:
            break
    print("Final board:")
    print("h-value: " + str(h))
    current.printBoard()
    return h



def f(T, decayRate):
    return T * decayRate


def runTests():
    print('#' * 20)
    print("Simulated Annealing:")
    print("Decay rate: 0.5; Threshold: 1e-08")
    print('#' * 20)
    sizes = [4, 8, 16]
    for i in sizes:
        print('-' * 20)
        print("Board size: " + str(i))
        print('-'* 20)
        b = nqueens.Board(i)
        h = 0
        for x in range(10):
            print("Run #" + str(x + 1))
            b.rand()
            h += simulatedAnnealing(b, 0.5, 1e-08)
            print()
        print("Average h-value: " + str(h/10) + "\n")
