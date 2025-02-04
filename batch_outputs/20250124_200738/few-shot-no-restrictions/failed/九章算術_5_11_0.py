"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

"""
### Problem Explanation:
The problem involves calculating the amount of labor required for a task and determining the length of work that can be completed by a group of workers who arrive early. Here's the breakdown:

1. **First Part**: The total labor required is given as 33,582 person-units of work, with a small remainder of 14 chi and 4 cun (尺 and 寸). This is based on the "autumn standard" (秋程), where the total work is 300 chi.

2. **Second Part**: If 1,000 workers arrive early, we need to calculate how much length (袤) of the task they can complete.

---

### Solution:


"""

#----- content starts here -----

from fractions import Fraction

# 秋程人功三百尺
秋程 = 300  # Total length in chi (尺)

# 總人功
總人功 = 33582  # Total person-units of work
餘尺 = 14 + Fraction(4, 10)  # Remaining work in chi (14 chi and 4 cun)

# 一千人先到
先到人數 = 1000  # Number of workers who arrive early

# 計算每人功尺數
每人功 = Fraction(秋程, 總人功)  # Work completed by one person in chi

# 以一人功尺數，乘先到人數為實
實 = 每人功 * 先到人數  # Total work completed by the early workers in chi

# 假設渠上下廣而半之 (渠的寬度)
渠上廣 = 1  # Upper width of the canal (in chi)
渠下廣 = 1  # Lower width of the canal (in chi)
渠平均廣 = Fraction(渠上廣 + 渠下廣, 2)  # Average width of the canal (in chi)

# 渠的深度
渠深 = 1  # Depth of the canal (in chi)

# 以深乘之為法
法 = 渠平均廣 * 渠深  # The divisor (法) based on the canal's dimensions

# 實如法得袤尺
袤 = 實 / 法  # Length of the canal completed by the early workers in chi

# Convert 袤 to 丈 (1 丈 = 10 尺)
a = 袤 / 10  # Length in zhang (丈)

# Output the result
a
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **秋程人功**: The total work required is 33,582 person-units, with a small remainder of 14 chi and 4 cun.
2. **每人功**: Calculate how much work one person can complete in chi.
3. **實**: Multiply the work per person by the number of early workers to get the total work completed by them.
4. **渠平均廣**: The average width of the canal is calculated as the average of the upper and lower widths.
5. **法**: The divisor is the product of the average width and depth of the canal.
6. **袤**: Divide the total work completed by the divisor to get the length of the canal completed in chi.
7. **Convert to 丈**: Since 1 zhang = 10 chi, divide the result by 10 to get the length in zhang.

---

### Final Answer:
The length of the canal completed by the early workers is `a` 丈.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 5000/5597"""
