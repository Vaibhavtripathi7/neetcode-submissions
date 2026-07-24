class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""; 
        for i in s: 
            if (i == " "):
                continue
            elif (i == "?"):
                continue
            else: 
                a = a + i

        # two pointer method: 
        count = 0

        for i, j in zip(range(0, len(a)), range(len(a)-1, -1, -1)):
            if a[i] == a[j]:
                count += 1
            else:
                return False
        if (count == len(a)):
            return True

