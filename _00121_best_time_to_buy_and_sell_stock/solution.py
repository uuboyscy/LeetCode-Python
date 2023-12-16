"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_diff = 0
        sum_diff = 0
        for price_diff in map(lambda x, y: x - y, prices[1:], prices):
            sum_diff = max(price_diff, price_diff + sum_diff)
            best_diff = max(sum_diff, best_diff)

        return best_diff

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(
        Solution().maxProfit(prices)
    )