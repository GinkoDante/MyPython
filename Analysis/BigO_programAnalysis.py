# Big O analysis allows us to classify our functions based on
# number of operations and cases of input data

# O(1): Constant
# O(log n): Logarithmic
# O(n): Linear
# O(n log n): Log Linear [Most good sorting algorithms]
# O(n^2): Quadratic
# O(n^3): Cubic
# O(2^n): Exponential

def Qudaratic(n):
    a = 5
    b = 6
    c = 18

    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j

    for k in range(n):
        w = a*k + 45
        v = b * b

d = 33


# The T(n) = 3 (assignments) + 3n^2 (nested for loops + assignments) + 2n(for loop) + 1 (assignment)