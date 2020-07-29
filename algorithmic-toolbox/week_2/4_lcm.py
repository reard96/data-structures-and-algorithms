# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_recursive(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd_recursive(b, a_prime)

def lcm_smart(a, b):
    gcd = gcd_recursive(a, b)

    if gcd == 1:
        return a*b
    else:
        return a*b // gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_smart(a, b))

