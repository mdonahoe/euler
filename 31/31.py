# Project Euler 31

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def possibles(amount_remaining, coin_index):
    coin_value = coins[coin_index]
    ways = 0
    for num_coins in range(amount_remaining / coin_value + 1):
        new_amount = amount_remaining - num_coins * coin_value
        if new_amount == 0:
            ways += 1
            return ways
        elif new_amount < 0:
            return ways
        elif coin_index > 0:
            ways += possibles(new_amount, coin_index - 1)
    return ways

print possibles(200, len(coins) - 1)
