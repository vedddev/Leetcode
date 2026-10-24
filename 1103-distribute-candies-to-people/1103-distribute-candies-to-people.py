class Solution(object):
    def distributeCandies(self, candies, num_people):
        result = [0] * num_people
        amount = 1
        l = 0

        while candies > 0:
            give = min(amount, candies)
            result[l] += give
            candies -= give

            amount += 1
            l = (l + 1) % num_people
        return result