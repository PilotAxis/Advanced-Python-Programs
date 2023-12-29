class solution:
    def print2largest(arr, n):
        b = list(set(arr))
        b.sort()
        if len(b) > 1 :
            return b[-2]
        return -1
    
n = 6
arr = [1, 2, 3, 4, 5, 6]
print(solution.print2largest(arr, n))