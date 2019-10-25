class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        direction = 'right'
        len1, len2 = len(matrix), len(matrix[0])
        upper, bottom, left, right = -1, len1, -1, len2
        current_pos = [0, 0]
        res = []
        while bottom - upper > 1 and right - left > 1:
            print(direction)
            print(matrix[current_pos[0]][current_pos[1]], upper, bottom, left, right)
            print(res)
            if direction == 'right':
                if current_pos[1] >= right - 1:
                    upper += 1
                    direction = 'down'
                else:
                    res.append(matrix[current_pos[0]][current_pos[1]])
                    current_pos[1] += 1
            elif direction == 'down':
                if current_pos[0] >= bottom - 1:
                    right -= 1
                    direction = 'left'
                else:
                    res.append(matrix[current_pos[0]][current_pos[1]])
                    current_pos[0] += 1
            elif direction == 'left':
                if current_pos[1] <= left + 1:
                    bottom -= 1
                    direction = 'up'
                else:
                    res.append(matrix[current_pos[0]][current_pos[1]])
                    current_pos[1] -= 1
            else:
                if current_pos[0] <= upper + 1:
                    left += 1
                    direction = 'right'
                else:
                    res.append(matrix[current_pos[0]][current_pos[1]])
                    current_pos[0] -= 1
        res.append(matrix[current_pos[0]][current_pos[1]])
        return res