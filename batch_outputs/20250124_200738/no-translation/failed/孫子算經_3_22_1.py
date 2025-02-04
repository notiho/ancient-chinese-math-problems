"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
To solve this problem, we need to follow the procedure described in the ancient text. Here's the Python code:


"""

#----- content starts here -----

# 方物一束外周，一市有三十二枚
外周 = 32

# 術曰：重置二位左位減八餘加右位，至盡虛加一，即得
# Initialize variables
重置 = 外周
左位 = 重置 // 10  # Extract the left digit
右位 = 重置 % 10    # Extract the right digit

# Perform the calculation
左位減八餘加右位 = (左位 - 8) + 右位

# 至盡虛加一，即得
a = 左位減八餘加右位 + 1

# Answer
a枚 = a
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: -2"""
