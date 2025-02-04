"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
This problem involves calculating the total number of items in a square bundle based on its outer perimeter. The procedure described is a bit cryptic, but it essentially outlines a method to compute the total number of items in the bundle. Here's how we can interpret and encode the solution in Python:

### Problem Breakdown:
1. **Given**: A square bundle with an outer perimeter of 32 items (枚).
2. **Question**: What is the total number of items in the bundle (積)?
3. **Procedure**:
   - Start with the perimeter (32 items).
   - Perform a series of operations:
     - Subtract 8 from the leftmost digit.
     - Add the rightmost digit.
     - Repeat until the number is exhausted.
     - Add 1 to the result at the end.

### Python Implementation:


"""

#----- content starts here -----

# Given perimeter
outer_perimeter = 32

# Procedure to calculate the total number of items
def calculate_total_items(perimeter):
    # Convert the perimeter to a string for digit manipulation
    digits = list(str(perimeter))
    total = 0
    
    while digits:
        # Step 1: Take the leftmost digit and subtract 8
        left_digit = int(digits.pop(0))  # Remove the leftmost digit
        left_digit -= 8
        
        # Step 2: Add the rightmost digit (if any)
        if digits:
            right_digit = int(digits.pop(-1))  # Remove the rightmost digit
        else:
            right_digit = 0
        
        # Add the adjusted left digit and right digit to the total
        total += max(0, left_digit) + right_digit
    
    # Step 3: Add 1 to the result
    total += 1
    
    return total

# Calculate the total number of items
a = calculate_total_items(outer_perimeter)

# Output the result
print(f"The total number of items in the bundle is: {a} 枚.")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input**: The outer perimeter (32 items).
2. **Digit Manipulation**:
   - The leftmost digit is reduced by 8.
   - The rightmost digit is added to the result.
   - This process continues until all digits are processed.
3. **Final Adjustment**: Add 1 to the total at the end.
4. **Output**: The total number of items in the bundle.

### Example Calculation:
For an outer perimeter of 32:
- Leftmost digit: 3 → 3 - 8 = -5 (ignored since it's negative).
- Rightmost digit: 2 → Add 2.
- Add 1 to the result.
- Total = 2 + 1 = 3.

Thus, the total number of items in the bundle is **3 枚**.
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: 3"""
