"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
The problem involves finding the side length of a square field given its area. This is essentially a square root calculation. The ancient Chinese method for extracting square roots is described in the procedure, and we will follow it step by step.

### Problem:
There is an area of 71,824 bu. Question: what is the side length of the square field?

### Procedure:
The procedure for extracting square roots ("開方術") is as follows:
1. Place the area as the dividend (實).
2. Borrow one counting rod (算) and shift it one place to the left (超一等).
3. Estimate the first digit of the root (議所得).
4. Multiply the estimated root by itself and subtract it from the dividend.
5. Double the root obtained so far to form the divisor (倍法為定法).
6. Continue the process by estimating the next digit, multiplying, subtracting, and updating the divisor.
7. If the square root cannot be completed exactly, express the result as a fraction.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# 積七萬一千八百二十四步
積 = 71824

# 開方術
def 開方(積):
    # 置積為實
    實 = 積
    
    # Initialize variables
    根 = 0  # The square root being calculated
    借算 = 0  # The borrowed number (current digit being calculated)
    定法 = 0  # The current divisor (doubled root so far)
    
    while 實 > 0:
        # 超一等: Shift the dividend one place to the left
        實 *= 100  # Equivalent to shifting two decimal places
        
        # 議所得: Estimate the next digit of the root
        for 借算 in range(9, -1, -1):
            # Multiply the borrowed digit by itself and add to the current root
            候根 = 根 * 20 + 借算
            if 候根 * 借算 <= 實:
                break
        
        # Update the root
        根 = 根 * 10 + 借算
        
        # Subtract the square of the borrowed digit from the dividend
        實 -= 候根 * 借算
        
        # 倍法為定法: Double the root so far to form the new divisor
        定法 = 根 * 2
    
    # If there is a remainder, express the result as a fraction
    if 實 > 0:
        分子 = 實
        分母 = 定法
        分數 = Fraction(分子, 分母)
        return 根 + 分數
    else:
        return 根

# Calculate the square root
a = 開方(積)
print(f"荅曰： {a}步。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initialization**: The area (`積`) is set as the dividend (`實`). The square root (`根`) starts at 0.
2. **Shifting**: The dividend is multiplied by 100 to simulate shifting two decimal places (超一等).
3. **Estimation**: The next digit of the root is estimated by iterating from 9 to 0 (議所得).
4. **Subtraction**: The square of the estimated digit is subtracted from the dividend.
5. **Doubling**: The root obtained so far is doubled to form the new divisor (倍法為定法).
6. **Fraction Handling**: If there is a remainder, the result is expressed as a fraction.

### Answer:
The side length of the square field is `a` bu.
"""


"""
Timed out"""
