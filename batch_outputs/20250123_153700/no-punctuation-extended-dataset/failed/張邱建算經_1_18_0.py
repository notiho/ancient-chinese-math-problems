"""
今有生絲一斤練之折五兩練絲一斤染之出三兩今有生絲五十六斤八兩七分兩之四問染得㡬何
術曰置一斤兩數以折兩數減之餘乗今有絲斤兩之數又以出兩數併一斤兩數乗之為實一斤兩數自乗為法實如法得一兩數
答曰 a斤
"""

"""
Suppose there is 1 jin of raw silk. When refined, it loses 5 liang.
When 1 jin of refined silk is dyed, it produces 3 liang.
Now suppose there are 56 jin, 8 liang, and 7/10 of a liang of raw silk.
Question: how much dyed silk is obtained?

The procedure says: Place the number of liang in 1 jin, subtract the number of liang lost during refining.
Multiply the remainder by the total number of jin and liang of raw silk.
Then, add the number of liang produced when dyeing to the number of liang in 1 jin, and multiply this by the result.
Take the square of the number of liang in 1 jin as the divisor.
Divide the result by the divisor to obtain the number of jin of dyed silk.

Answer: *a* jin.
"""

from fractions import Fraction

# Constants
一斤兩數 = 16  # 1 jin = 16 liang
折兩數 = 5     # Loss during refining
出兩數 = 3     # Yield during dyeing

# Raw silk: 56 jin, 8 liang, 7/10 liang
生絲 = 56 * 一斤兩數 + 8 + Fraction(7, 10)

# Step 1: Subtract the loss during refining
餘 = 一斤兩數 - 折兩數

# Step 2: Multiply the remainder by the total raw silk
絲斤兩數 = 餘 * 生絲

# Step 3: Add the dyeing yield to the number of liang in 1 jin, then multiply
實 = (出兩數 + 一斤兩數) * 絲斤兩數

# Step 4: Square the number of liang in 1 jin as the divisor
法 = 一斤兩數 ** 2

# Step 5: Divide the result by the divisor to get the number of jin of dyed silk
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 330847/7168, Actual: 1890823/2560"""
