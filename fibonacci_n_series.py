from os import *
from sys import *
from collections import *
from math import *
 
MOD = 10**9 + 7
 
# Matrix multiplication function
def multiply(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result
 
# Matrix exponentiation function
def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return multiply(half_power, half_power)
    else:
        return multiply(matrix, matrix_power(matrix, n - 1))
 
# Calculate Nth Fibonacci number using matrix exponentiation
def fibonacciNumber(n):
    if n <= 2:
        return 1
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

