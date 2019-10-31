class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = len(words[0])
        count = 1
        one_line = words[0]
        for i in range(1, len(words)):
            if length + len(words[i]) + 1 <= maxWidth:
                length += len(words[i]) + 1
                count += 1
            else:
                break
        remain_blank = maxWidth - length + count - 1
        next_batch = words[count:]
        print(length, count, one_line, remain_blank, next_batch)
        if next_batch == []:
            for i in range(1, count):
                one_line += ' ' + words[i]
                remain_blank -= 1
            return [one_line + ' ' * remain_blank]
        else:
            for i in range(1, count):
                blank_count = remain_blank//(count-i)+1 if remain_blank%(count-i)!=0 else remain_blank//(count-i)
                one_line += ' ' * blank_count + words[i]
                remain_blank -= blank_count
            one_line += ' ' * remain_blank
            return [one_line] + self.fullJustify(next_batch, maxWidth)