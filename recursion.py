
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n -2)

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


if __name__ == "__main__":

    print(sum(5))
    
    print(fib(10))