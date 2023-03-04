from pulp import *

problema = LpProblem("Aplicacion_Minimizar", LpMinimize)

x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

problema += 10*x + 30*y 
problema += x + 5*y >= 15
problema += 5*x + y >= 15

problema.solve()

print("El valor optimo se encuentra en x={} y y={}".format(x.varValue,y.varValue))
print("P({},{}) = 10({}) + 30({}) = {}".format(x.varValue,y.varValue,x.varValue,y.varValue,(10*x.varValue+30*y.varValue)))

