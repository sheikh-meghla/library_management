def sum(a, b):
    a  = a + 10
    b = b + 10

    percatage = (a + b) / 100

    for i in range(10000000000):
        percatage += i

    return percatage