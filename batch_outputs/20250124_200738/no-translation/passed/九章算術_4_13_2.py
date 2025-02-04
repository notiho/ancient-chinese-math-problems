"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a given area (積) using an ancient Chinese method of "開方術" (square root extraction). Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 置積為實
積 = 71824

# 開方術
def 開方術(積):
    # 借一算步之，超一等
    借算 = 0
    while (借算 + 1) ** 2 <= 積:
        借算 += 1

    # 議所得，以一乘所借一算為法，而以除
    法 = 2 * 借算
    餘數 = 積 - 借算 ** 2

    # 若開之不盡者為不可開，當以面命之
    if 餘數 == 0:
        return 借算

    # 若實有分者，通分內子為定實
    分子 = 餘數
    分母 = 法

    # 乃開之，訖，開其母報除
    分數 = Fraction(分子, 分母)

    # 若母不可開者，又以母乘定實，乃開之，訖，令如母而一
    return 借算 + 分數

# 計算結果
a = 開方術(積)
print(f"方為 {a} 步。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **置積為實**: The given area (積) is set as the input.
2. **借一算步之，超一等**: Find the largest integer (借算) whose square is less than or equal to the area.
3. **議所得，以一乘所借一算為法，而以除**: Compute the divisor (法) and the remainder (餘數).
4. **若開之不盡者為不可開，當以面命之**: If the remainder is zero, the square root is an integer.
5. **若實有分者，通分內子為定實**: If there is a remainder, compute the fractional part of the square root.
6. **乃開之，訖，開其母報除**: Return the result as a mixed number (integer part + fractional part).

### Result:
For 積 = 71824, the square root (方) is calculated as `a` steps.
"""


"""
"""
