import input_output as io
import equation_solver as solver

#get input from user
s = io.get_equation()
print(s)
#solve the input
solver.solve(s)
#if solved
    #print back the result
#else
    #print reason why it's unsolvable

#try again
