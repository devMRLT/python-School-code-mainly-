


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