from timeit import default_timer as timer

Tabuleiro = input ("Tabuleiro:")
Tabuleiro = int(Tabuleiro)

start = timer()
def restriction(col, Q):
    return col in Q or \
           any(abs(col - x) == len(Q) - i for i, x in enumerate(Q))

def agent(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution + [i + 1]
                     for solution in solutions
                     for i in range(Tabuleiro)
                     if not restriction(i + 1, solution))
    return solutions


answers = agent(Tabuleiro)
first_answer = next(answers)
print(first_answer)

end = timer()
print(end - start)
