#!/usr/bin/python3

"""
0x08-making_change
"""


def makeChange(coins, total):

    """
    the makechane function takes two arguments
    coins a list of coin value you have
    total: the amount you want to make using given coins
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for sub_total in range(coin, total + 1):
            dp[sub_total] = min(dp[sub_total], dp[sub_total - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
