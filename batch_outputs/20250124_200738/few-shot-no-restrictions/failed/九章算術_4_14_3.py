"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a given area, expressed in steps (步), using an ancient Chinese square root extraction method. The area is \( 564,752 \frac{1}{4} \) steps. Below is the Python implementation of the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction

# Given area (積): 564,752 1/4 steps
積 = Fraction(564752, 1) + Fraction(1, 4)

# 開方術 (Square root extraction method)
def 開方(積):
    # Step 1: Initialize
    實 = 積  # Place the area as the dividend
    超一等 = 0  # Placeholder for the current digit of the square root
    定法 = 0  # Placeholder for the divisor
    面 = 0  # Placeholder for the result (square root)
    
    # Step 2: Iteratively extract the square root
    while 實 > 0:
        # Borrow one digit (step) from the dividend
        超一等 += 1
        借算 = 超一等
        
        # Calculate the divisor (法)
        法 = 2 * 面 + 借算
        
        # Check if the divisor can divide the dividend
        if 法 * 借算 <= 實:
            # Update the result (square root)
            面 = 面 * 10 + 借算
            
            # Subtract the square of the borrowed digit from the dividend
            實 -= 法 * 借算
            
            # Update the 定法 (final divisor)
            定法 = 法
        else:
            # If the divisor cannot divide the dividend, reduce the borrowed digit
            超一等 -= 1
    
    # Step 3: Handle fractional part if the square root is not exact
    if 實 > 0:
        面 = 面 + Fraction(實, 定法)
    
    return 面

# Calculate the square root
a = 開方(積)

# Output the result
print(f"Square root of the area: {a} 步")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initialization**:
   - The given area \( 564,752 \frac{1}{4} \) is converted into a `Fraction` to handle the fractional part accurately.
   - Variables are initialized to store the intermediate results during the square root extraction process.

2. **Square Root Extraction**:
   - The algorithm iteratively "borrows" digits (steps) to approximate the square root.
   - The divisor is calculated based on the current approximation of the square root.
   - If the divisor can divide the remaining dividend, the square root is updated, and the dividend is reduced.
   - If the divisor cannot divide the dividend, the borrowed digit is reduced.

3. **Handling Fractional Part**:
   - If the square root is not exact, the fractional part is calculated by dividing the remaining dividend by the final divisor.

4. **Output**:
   - The result is printed as the square root of the area in steps.

### Example Output:
For the given area \( 564,752 \frac{1}{4} \), the program will output the square root in steps (步).
"""


"""
Timed out"""
