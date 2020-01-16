class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [0] * len(ratings)
        right = [0] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        summ = 0
        for i in range(len(ratings)):
            if left[i] == right[i] == 0:
                summ += 1
            else:
                summ += max(left[i], right[i]) + 1
        return summ