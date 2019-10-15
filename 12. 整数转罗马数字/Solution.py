class Solution:
    def intToRoman(self, num: int) -> str:
        remain = num
        roman = ''
        
        while not remain == 0:
            extracted = remain // max(10 ** (len(str(remain)) - 1), 1) * 10 ** (len(str(remain)) - 1)
            remain = remain % max(10 ** (len(str(remain)) - 1), 1)
            
            if extracted >= 1000:
                roman = roman + 'M' * (extracted//1000)
            elif extracted == 900:
                roman = roman + 'CM'
            elif 500 <= extracted < 900:
                roman = roman + 'D' + 'C' * (extracted//100-5)
            elif extracted == 400:
                roman = roman + 'CD'
            elif 100 <= extracted < 400:
                roman = roman + 'C' * (extracted//100)
            elif extracted == 90:
                roman = roman + 'XC'
            elif 50 <= extracted < 90:
                roman = roman + 'L' + 'X' * (extracted//10-5)
            elif extracted == 40:
                roman = roman + 'XL'
            elif 10 <= extracted < 40:
                roman = roman + 'X' * (extracted//10)
            elif extracted == 9:
                roman = roman + 'IX'
            elif 5 <= extracted < 9:
                roman = roman + 'V' + 'I' * (extracted-5)
            elif extracted == 4:
                roman = roman + 'IV'
            else:
                roman = roman + 'I' * extracted
                
        return roman