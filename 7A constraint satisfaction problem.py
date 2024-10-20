from simpleai.search import CspProblem,backtrack
variables=('A','B','C','D')
domain={
    'A':['Red','green','blue'],
    'B':['Red','green','blue'],
    'C':['Red','green','blue'],
    'D':['Red','green','blue']
    }
def diff_color(variables,values):
    return values[0]!=values[1]
contraints={
    (('A','B'),diff_color),
    (('A','C'),diff_color),
    (('A','D'),diff_color),
    (('C','D'),diff_color),
    (('B','C'),diff_color),
    }
problem=CspProblem(variables,domain,contraints)
solution=backtrack(problem)
print(solution)

