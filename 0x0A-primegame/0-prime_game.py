#!/usr/bin/python3

""" Prime Game Algorithm Python """


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_game(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    turn = 0  # 0 for Maria, 1 for Ben
    while primes:
        prime = primes.pop(0)
        primes = [p for p in primes if p % prime != 0]
        turn = 1 - turn  # Switch turn
    return 1 - turn  # Return the winner of the game


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"
