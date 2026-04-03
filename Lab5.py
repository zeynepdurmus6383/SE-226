def factorial(x):
    result = 1
    for n in range(1,x+1):
        result *=n
    return result

def task3(n,r):
    """ This function uses a for loop to calculate 𝐺𝑛 = 1 + 𝑟 + 𝑟2 + 𝑟3 + ⋯ 𝑟^n, calculates r^x in each itiration and adds the result to global variable y. Y is set to 0 at the strat of the function."""
    global y
    y = 0
    for x in range(n+1):
        y += (r**x)

absoluteValue = lambda x,i: (x**(2*i))/ factorial(2*i)
def exp_x(x, n):
    result = 0
    for i in range(n):
        if(i%2 == 0):
            result += absoluteValue(x,i)
        else:
            result -= absoluteValue(x,i)
    return result


print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(10))
y = 2
print(y)
task3(2,5)
print(y)
print(task3.__doc__)
print(exp_x(1,1))

