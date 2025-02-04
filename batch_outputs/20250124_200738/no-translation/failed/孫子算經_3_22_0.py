"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
To solve this problem, let's carefully interpret the procedure and translate it into Python code:


"""

#----- content starts here -----

# 方物一束外周，一市有三十二枚
外周 = 32

# 術曰：重置二位左位減八餘加右位，至盡虛加一，即得
# Start with the given 外周
積 = 0
while 外周 > 0:
    左位 = 外周 // 10  # Extract the leftmost digit
    右位 = 外周 % 10   # Extract the rightmost digit
    外周 = 左位        # Update 外周 to the leftmost digit
    積 += 左位 - 8 + 右位  # Perform the operation as described

# 至盡虛加一
積 += 1

# Result
a = 積
#----- content ends here -----


"""


This code follows the procedure described in the problem. The result `a` will give the total number of items in the bundle.
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: -7"""
