class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(lambda x: int(x), version1.split('.')))
        version2 = list(map(lambda x: int(x), version2.split('.')))
        while len(version1) < len(version2):
            version1.append(0)
        while len(version1) > len(version2):
            version2.append(0)
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
        return 0