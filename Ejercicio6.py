from pulp import *

problema = LpProblem("Ejercicio_6", LpMaximize)

x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

problema += 4*x + 6*y 
problema += 2*x + y <= 180
problema += x + 2*y <= 160
problema += x + y <= 100

problema.solve()

print("El valor optimo se encuentra en x={} y y={}".format(x.varValue,y.varValue))
print("P({},{}) = 4({}) + 6({}) = {}".format(x.varValue,y.varValue,x.varValue,y.varValue,(4*x.varValue+6*y.varValue)))

