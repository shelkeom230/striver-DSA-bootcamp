import sys
import threading, math as m


def check_powerof2(n):
    """
        Logic:

    A power of 2 has only one '1' in binary.

    n & (n-1) clears the lowest set bit. If result is 0, then n was a power of 2."""
    return n > 0 and (n & (n - 1)) == 0


def count_setbits(n):
    return bin(n).count("1")


def count_set_bits(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt


# get the ith bit - 0 indexed from right
def get_ithbit(n, i):
    return (n >> i) & 1


# set ith bit to 1
def set_ithbittoone(n, i):
    n |= 1 << i
    return n


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def main():
    sys.stdin = open("preprationSheet Sprint1 easy/input.txt", "r")
    sys.stdout = open("preprationSheet Sprint1 easy/output.txt", "w")
    input = sys.stdin.readline

    # Example usage:
    n = int(input())

    print(sieve(n))


threading.Thread(target=main).start()
