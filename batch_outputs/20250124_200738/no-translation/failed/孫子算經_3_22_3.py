"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
To solve this problem, let's carefully follow the procedure described in the "術" (method). Here's the Python code:


"""

#----- content starts here -----

# 方物一束外周，一市有三十二枚
外周 = 32

# 術曰：重置二位左位減八餘加右位，至盡虛加一，即得
# Initialize variables
重置 = 外周
積 = 0

while 重置 > 0:
    # Extract the leftmost digit and the remaining digits
    左位 = 重置 // 10
    右位 = 重置 % 10

    # Left digit minus 8, add the right digit
    餘 = max(0, 左位 - 8) + 右位

    # Update the total
    積 += 餘

    # Update 重置 for the next iteration
    重置 = 左位

# Add 1 at the end as per the method
積 += 1

# Result
a = 積
#----- content ends here -----


"""


This code follows the procedure described in the problem. The variable `a` will contain the final result, which is the total number of items in the bundle.
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: 6"""
