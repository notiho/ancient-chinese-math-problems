"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
This problem involves determining the price ratio of two types of arrows (expensive and cheap) when given the total cost and total quantity. Let's break it down and encode the solution step by step.

---

### Problem Description:
- Total money spent: 980 qian.
- Total arrows purchased: 5820 arrows.
- The goal is to determine the price ratio of expensive arrows to cheap arrows and calculate how many arrows correspond to each price.

---

### Procedure:
1. **Reverse the ratio method (反其率術)**:
   - Let the price ratio of expensive arrows to cheap arrows be \( a : b \), where \( a \) and \( b \) are integers.
   - Use the total money and total arrows to determine the ratio.

2. **Steps**:
   - Use the total money as the divisor (法, "the rule").
   - Use the total arrows as the dividend (實, "the fact").
   - Divide the total arrows by the total money to find the ratio of arrows per qian.
   - If the division is not exact, adjust the ratio by reducing the divisor and increasing the dividend until the ratio becomes clear.

3. **Calculate the number of arrows for each price**:
   - Multiply the ratio by the total money to determine how many arrows correspond to each price.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent (in qian)
total_money = 980

# Total arrows purchased
total_arrows = 5820

# Step 1: Calculate the base ratio of arrows per qian
ratio = Fraction(total_arrows, total_money)

# Step 2: Simplify the ratio into integers (expensive : cheap)
# The ratio gives us how many arrows correspond to 1 qian.
# For example, if the ratio is 3/2, then 3 expensive arrows cost the same as 2 cheap arrows.
expensive_per_qian = ratio.numerator  # a
cheap_per_qian = ratio.denominator    # b

# Step 3: Calculate the number of arrows for each price
# Total arrows for expensive type
expensive_arrows = expensive_per_qian * total_money

# Total arrows for cheap type
cheap_arrows = cheap_per_qian * total_money

# Output the results
a = expensive_per_qian
b = cheap_per_qian
c = expensive_arrows
d = cheap_arrows

print(f"The ratio is {a} expensive arrows per {b} cheap arrows per qian.")
print(f"The total is {c} expensive arrows and {d} cheap arrows.")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `a` and `b`: The ratio of expensive arrows to cheap arrows per qian.
- `c` and `d`: The total number of expensive and cheap arrows, respectively.

---

### Example Output:
If the ratio is \( 3 : 2 \), the output will be:
```
The ratio is 3 expensive arrows per 2 cheap arrows per qian.
The total is 2940 expensive arrows and 1960 cheap arrows.
```

This matches the problem's requirements and provides the breakdown of the expensive and cheap arrows.
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 291
Variable 'b' has wrong value. Expected: 5, Actual: 49
Variable 'c' has wrong value. Expected: 5520, Actual: 285180
Variable 'd' has wrong value. Expected: 6, Actual: 48020"""
