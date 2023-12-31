class solution:
    def __init__(self, s):
        self.s = s
    def check(self):
        if self.s == self.s[::-1]:
            return True
        else:
            return False
s = "abba"
print(int(solution(s).check()))