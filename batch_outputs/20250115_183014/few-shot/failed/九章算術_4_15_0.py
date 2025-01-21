"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a very large number using an ancient Chinese method for extracting square roots. The procedure is detailed and involves iterative steps to approximate the square root. Below is the Python implementation of the procedure:


"""


"""
Suppose there is a volume of 3,970,215,625 bu.
Question: what is the side length of the square?

The procedure for extracting square roots says:
1. Place the volume as the dividend.
2. Borrow one counting rod and place it, skipping one position (i.e., divide the number into groups of two digits from the right).
3. Estimate the first digit of the root. Multiply this digit by itself to form the divisor, and divide the first group of digits by this divisor.
4. After the division, double the divisor to form the "fixed divisor."
5. Subtract the square of the estimated digit from the first group of digits, bring down the next group of digits, and repeat the process.
6. If the root cannot be fully extracted (i.e., there is a remainder), the square root is not exact, and the result is expressed as a fraction.
7. If the dividend has fractions, convert them to a common denominator and proceed as above.
8. If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root of the product.

The answer says: *a* bu.
"""

from fractions import Fraction

# Initialize the given volume
積 = 3970215625

# Step 1: Place the volume as the dividend
實 = 積

# Step 2: Borrow one counting rod and group digits into pairs
實_str = str(實)
實_groups = [int(實_str[max(0, i - 2):i]) for i in range(len(實_str), 0, -2)][::-1]

# Initialize variables
root = 0  # The square root being calculated
remainder = 0  # The remainder after each step

# Step 3: Iteratively calculate the square root
for group in 实_groups:
    # Bring down the next group of digits
    remainder = remainder * 100 + group

    # Estimate the next digit of the root
    divisor = root * 20  # Double the current root
    next_digit = 0
    while (divisor + next_digit) * next_digit <= remainder:
        next_digit += 1
    next_digit -= 1

    # Update the root and remainder
    root = root * 10 + next_digit
    remainder -= (divisor + next_digit) * next_digit

# If there is a remainder, express the result as a fraction
if remainder > 0:
    fractional_part = Fraction(remainder, 10 ** (2 * len(實_groups)))
    a = root + fractional_part
else:
    a = root

# Output the result
a


"""


### Explanation of the Code:
1. **Grouping Digits**: The number is divided into groups of two digits from the right, as per the ancient method.
2. **Iterative Root Extraction**: The square root is calculated digit by digit. At each step, the divisor is updated, and the next digit of the root is estimated.
3. **Handling Remainders**: If the square root is not exact, the remainder is expressed as a fraction.
4. **Final Result**: The result is either an integer or a fraction, depending on whether the square root is exact.

### Answer:
The result `a` represents the side length of the square in bu.
"""


"""
Code error: name '实_groups' is not defined"""
