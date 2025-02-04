"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a given area (25,281 bu²) to determine the side length of a square field. The ancient Chinese "開方術" (square root extraction method) is described in detail, but we will translate the procedure into Python code for clarity and precision.

### Problem Explanation:
We are tasked with finding the side length of a square field given its area. The ancient method involves iterative approximation, division, and adjustment to find the square root.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

def 開方術(積):
    """
    Implements the ancient Chinese square root extraction method.
    Input: 積 (the area of the square field, in bu²)
    Output: The side length of the square field (in bu)
    """
    # Step 1: Initialize variables
    實 = 積  # The given area
    借算 = 1  # Start with an initial guess for the side length
    while 借算 ** 2 <= 實:
        借算 += 1
    借算 -= 1  # Adjust to the largest 借算 such that 借算² <= 實

    # Step 2: Compute the initial 法 (divisor)
    法 = 2 * 借算

    # Step 3: Iteratively refine the result
    餘 = 實 - 借算 ** 2  # Initial remainder
    while 餘 != 0:
        副 = 餘 // 法  # Compute the next digit of the square root
        借算 = 借算 * 10 + 副  # Update the side length
        餘 = (餘 % 法) * 10  # Update the remainder
        法 = 法 * 10 + 2 * 副  # Update the divisor

    return 借算

# 積二萬五千二百八十一步
積 = 25281

# Compute the side length
a = 開方術(積)
print(f"方為 {a} 步。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Initialization**:
   - Start with the given area (`積`).
   - Use an initial guess (`借算`) for the side length.

2. **Iterative Approximation**:
   - Find the largest integer `借算` such that `借算² <= 積`.
   - Compute the divisor (`法`) and refine the side length iteratively.

3. **Termination**:
   - The process stops when the remainder (`餘`) becomes zero, meaning the square root has been fully extracted.

4. **Output**:
   - The final value of `借算` is the side length of the square field.

---

### Result:
For an area of 25,281 bu², the side length of the square field is approximately:

```
方為 159 步。
```

This matches the expected result based on the ancient method.
"""


"""
"""
