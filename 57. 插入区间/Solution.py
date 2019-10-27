class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: return [newInterval]
        left = 0
        right = len(intervals) - 1
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
        if newInterval[0] > intervals[-1][0]:
            intervals.append(newInterval)
        else:
            intervals.insert(left, newInterval)
        res = [intervals[0][:]]
        for inter in intervals:
            if inter[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter[:])
        return res