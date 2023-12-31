def canPair(nums, k):
    # Check if the length of the array is even
    if len(nums) % 2 != 0:
        return False
    
    # Create a dictionary to store the remainder of each element when divided by k
    remainder_dict = {}
    
    # Count the remainder of each element when divided by k
    for num in nums:
        remainder = num % k
        if remainder in remainder_dict:
            remainder_dict[remainder] += 1
        else:
            remainder_dict[remainder] = 1
    
    # Check if pairs can be formed for each remainder
    for remainder in remainder_dict:
        if remainder == 0:
            # For remainder 0, there should be an even count
            if remainder_dict[remainder] % 2 != 0:
                return False
        else:
            # For other remainders, check if the complement remainder exists
            complement = k - remainder
            if complement not in remainder_dict or remainder_dict[remainder] != remainder_dict[complement]:
                return False
    
    return True

# Example usage:
nums = [9, 7, 5, 3]
k = 6
result = canPair(nums, k)
print(result)


