import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


n1 = int(input("enter first"))

n2 = int(input("enter second"))

suma = add(n1, n2)

subtract = sub(n1, n2)

print(f"Sum is f{suma} and difference is f{subtract}")
