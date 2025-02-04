"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
To solve this problem, let's carefully translate the ancient procedure into Python code.


"""

#----- content starts here -----

# 方物一束外周，一市有三十二枚
外周 = 32

# 術曰：重置二位左位減八餘加右位，至盡虛加一，即得
# Explanation:
# - "重置二位" means to split the number into two digits (left and right).
# - "左位減八餘加右位" means subtract 8 from the left digit and add the right digit.
# - "至盡虛加一" means repeat until no digits remain, then add 1.

# Step-by-step calculation
left_digit = 外周 // 10  # Extract the left digit
right_digit = 外周 % 10  # Extract the right digit

# Perform the operation: left_digit - 8 + right_digit
result = (left_digit - 8) + right_digit

# Add 1 as per the procedure
a = result + 1

# Output the result
a
#----- content ends here -----


"""


This code follows the ancient procedure step by step and calculates the result `a`.
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: -2"""
