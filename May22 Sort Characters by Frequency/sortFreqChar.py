class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s).most_common()
        result = ''
        for i in range(len(m)):
            alpha = m[i][0]
            r = m[i][1]
            for j in range(r):
                result+=alpha
        return result
