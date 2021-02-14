#// This is the function for pulling the common values
def intersection(s1,s2):
    common_values = set(s1) & set(s2)
    print("These are the values that the two lists have in common", common_values)
    return common_values;

print("Welcome to my Intersection assignment. Please enter a series of numbers with or without decimals with spaces to seperate them:")
#// Set 1 input (float because user may choose to use decimal numbers)
s1 = [float (set1_var2) for set1_var2 in input().split()]
print("Please enter the values for the next set :)")
#// Set 2 input
s2 = [float (set2_var2) for set2_var2 in input().split()]
#// Calling the function
intersection(s1,s2)
#part 2
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
# part 3
a = ["*", " ", "* "]
#Top of the triangle
def main(n):
    print((a[1]*(n)) + a[0])
    runs = 1
    s = n - 2
    sr = 0
    while runs < n:
        if s < 1:
            print(" *", sr*a[1], a[0])
            break
        else:
            print (s*a[1], a[0], sr*a[1], a[0]) # Print each line as loops
            
            s = s - 1
            runs = runs + 1
            sr = sr + 1
        #print(s)
    #bottom piece of triangle
    print(a[0]*(n))
    #end of bottom

print("Welcome to Part 3 of my assignment!!!\n")
n = int(input("Please enter the amount of rows you wish to have\n within your triangle:"))
main(n)