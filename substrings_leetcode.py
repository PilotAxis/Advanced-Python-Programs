def check_substring(s):
    ans = -1
    for left in range(len(s)):
        for right in range(left + 1, len(s)):
            if s[left] == s[right]:
                ans = max(ans, right - left - 1)
    return ans

S = input("Type a string: ")
print(check_substring(S))