class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        direction = 'right'
        len1 = len2 = n
        upper, bottom, left, right = -1, len1, -1, len2
        current_pos = [0, 0]
        res = [[0 for _ in range(len1)] for _ in range(len2)]
        count = 1
        while bottom - upper > 1 and right - left > 1:
            if direction == 'right':
                if current_pos[1] >= right - 1:
                    upper += 1
                    direction = 'down'
                else:
                    res[current_pos[0]][current_pos[1]] = count
                    count += 1
                    current_pos[1] += 1
            elif direction == 'down':
                if current_pos[0] >= bottom - 1:
                    right -= 1
                    direction = 'left'
                else:
                    res[current_pos[0]][current_pos[1]] = count
                    count += 1
                    current_pos[0] += 1
            elif direction == 'left':
                if current_pos[1] <= left + 1:
                    bottom -= 1
                    direction = 'up'
                else:
                    res[current_pos[0]][current_pos[1]] = count
                    count += 1
                    current_pos[1] -= 1
            else:
                if current_pos[0] <= upper + 1:
                    left += 1
                    direction = 'right'
                else:
                    res[current_pos[0]][current_pos[1]] = count
                    count += 1
                    current_pos[0] -= 1
        res[current_pos[0]][current_pos[1]] = count
        return res