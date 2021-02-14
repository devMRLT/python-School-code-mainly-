def gregoryLiebniz(numiterations):
    #// Start off sequence at 0
    pi_algo = 0
    #// Loop for calcing the pi value
    for n in range(0, numiterations):
        pi_algo += ((4 * (-1)**n)/(2*n + 1))
    #//rounding Script to 6 deciaml
    #//Out put the final value in a statement
    print("The value of pie is ", round(pi_algo,6), "after", numiterations, "iterations.")
    return pi_algo;

print("Welcome to part 2 of my assignment. \n Please enter the number of iterations:")
numiterations = int(input())
gregoryLiebniz(numiterations)