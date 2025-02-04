"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a given area (71,824 bu²) to determine the side length of a square field. The procedure described is an ancient Chinese method for extracting square roots, which is iterative and involves successive approximations. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 積七萬一千八百二十四步
積 = 71824

# 開方術
def 開方(積):
    # 置積為實
    實 = 積

    # 初始設置
    借算 = 0  # 借一算步之
    定法 = 0  # 定法
    副 = 0    # 副
    折法 = 0  # 折法

    # 超一等，議所得
    while 借算 ** 2 <= 實:
        借算 += 1
    借算 -= 1  # 找到最大的借算，使其平方不超過實

    # 以一乘所借一算為法，而以除
    法 = 2 * 借算
    餘 = 實 - 借算 ** 2

    # 若餘數為 0，則開方完成
    if 餘 == 0:
        return 借算

    # 若餘數不為 0，繼續開方
    while True:
        # 倍法為定法
        定法 = 法

        # 折法而下
        折法 = 1

        # 復置借算步之如初
        while (定法 + 折法) * 折法 <= 餘:
            折法 += 1
        折法 -= 1  # 找到最大的折法，使其乘積不超過餘數

        # 更新副
        副 = 副 * 10 + 折法

        # 更新餘數
        餘 -= (定法 + 折法) * 折法

        # 更新法
        法 = 法 * 10 + 2 * 折法

        # 若餘數為 0，則開方完成
        if 餘 == 0:
            break

        # 若餘數不為 0，繼續迭代
        if 法 > 實:
            break

    # 返回結果
    return Fraction(副, 1)

# 計算結果
a = 開方(積)
print(f"方為 {a} 步。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initialization**: The given area (`積`) is set as the starting value (`實`). Variables for the iterative process (`借算`, `定法`, `副`, `折法`) are initialized.
2. **Finding the Initial Approximation**: The largest integer (`借算`) whose square is less than or equal to the area is determined.
3. **Iterative Refinement**: The method iteratively refines the square root by:
   - Doubling the current approximation (`法`) to form the divisor.
   - Finding the largest possible digit (`折法`) that satisfies the condition.
   - Updating the remainder (`餘`) and the approximation (`副`).
4. **Termination**: The process stops when the remainder becomes zero or when further refinement is not possible.
5. **Result**: The final approximation (`副`) is returned as the square root.

### Answer:
The side length of the square field is `a` bu.
"""


"""
"""
