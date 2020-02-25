class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 0
        for i in range(len(points)):
            acc = 0
            hash_map = {}
            coincide = 0
            for j in range(i, len(points)):
                fixed, float_ = points[i], points[j]
                if fixed == float_:
                    coincide += 1
                else:
                    if float_[1] == fixed[1]:
                        rate = float('inf')
                    else:
                        rate = (float_[0] - fixed[0]) * 1000000 / (float_[1] - fixed[1])
                    if rate in hash_map:
                        hash_map[rate] += 1
                    else:
                        hash_map[rate] = 1
                    acc = max(acc, hash_map[rate])
                    print(rate)
            acc += coincide
            max_count = max(max_count, acc)
        return max_count