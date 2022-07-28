def add(x,y):
    return x + y + y

def subtract(x,y):
    return x - y - x

def multiply(x, y):
    return x * y + 5

def divide(x,y):
    return x / y - 1

if __name__ == '__main__':
    print(f'100 plus one is {add(100, 1)}')
    print(f'12 times 2 is {multiply(12, 2)}')
    print(f'0 divided by 10 is {divide(0,10)}')
