"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
This problem involves calculating the total number of items in a square bundle based on its external perimeter. Let's break it down and translate it into Python code.

The procedure is described as follows:
1. Take the external perimeter of the square bundle.
2. Perform a specific calculation to determine the total number of items in the bundle.

The procedure involves:
- Subtracting 8 from the left digit of the perimeter.
- Adding the right digit to the result.
- Repeating this process until the calculation is complete, then adding 1 to the result.

Here is the Python implementation:


"""

#----- content starts here -----

# 方物一束外周 (external perimeter of the square bundle)
外周 = 32  # Example value given in the problem

# Initialize the calculation
result = 0

# Perform the calculation as described in the procedure
while 外周 > 0:
    左位 = 外周 // 10  # Extract the left digit
    右位 = 外周 % 10   # Extract the right digit
    外周 = 左位        # Update the perimeter to the left digit
    result += (左位 - 8) + 右位  # Perform the subtraction and addition

# Add 1 to the result as per the procedure
result += 1

# The total number of items in the bundle
a = result
print(f"Total items in the bundle: {a}枚")
#----- content ends here -----


"""


### Explanation:
- `外周` is the external perimeter of the square bundle.
- The loop extracts the left and right digits of the current perimeter, performs the calculation, and updates the perimeter.
- The process continues until the perimeter is reduced to 0.
- Finally, 1 is added to the result to obtain the total number of items.

### Example:
For an external perimeter of 32:
- Left digit = 3, Right digit = 2
- Calculation: (3 - 8) + 2 = -3
- Add 1 to the result: -3 + 1 = -2 (This is the total number of items in the bundle).

If you have additional clarifications or corrections to the procedure, feel free to share!
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: -7"""
