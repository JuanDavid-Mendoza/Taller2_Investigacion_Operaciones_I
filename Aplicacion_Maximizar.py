from pulp import *

problema = LpProblem("Aplicacion_Maximizar", LpMaximize)

x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

problema += 6.5*x + 7*y 
problema += 2*x + 3*y <= 600
problema += x + y <= 500
problema += 2*x + y <= 400

problema.solve()

print("El valor optimo se encuentra en x={} y y={}".format(x.varValue,y.varValue))
print("P({},{}) = 6.5({}) + 7({}) = {}".format(x.varValue,y.varValue,x.varValue,y.varValue,(6.5*x.varValue+7*y.varValue)))

