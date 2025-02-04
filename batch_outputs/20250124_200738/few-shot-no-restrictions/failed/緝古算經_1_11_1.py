"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a complex problem involving the calculation of dimensions for a square granary and a circular pit, given a certain volume of grain. Let's break it down step by step and translate the procedure into Python code.

### Problem Explanation:
- There are 3072 **shi** of grain.
- A square granary and a circular pit are to be constructed.
- The diameter of the circular pit is equal to the side length of the square granary.
- The square granary is 2 chi deeper than the circular pit.
- The square granary is 3 chi shorter than the height of the circular pit.
- Both the granary and the pit are filled completely, and the total volume of grain is exactly used up.

We need to calculate:
- The side length of the square granary (方, `a`),
- The diameter of the circular pit (徑, `a`),
- The height of the square granary (高, `b`),
- The depth of the circular pit (深, `c`).

### Procedure:
The procedure involves solving a cubic equation derived from the relationships between the volumes of the granary and the pit. The steps are encoded below.

---


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given data
粟 = 3072  # 粟 in 石
粟尺 = 粟 * 10  # Convert 石 to cubic 尺 (1 石 = 10 cubic 尺)

# Constants in the procedure
三十五 = 35
二十五 = 25
一十四 = 14

# Step 1: Calculate the rate (率)
率 = Fraction(三十五 * 粟尺, 二十五)

# Step 2: Define the unknowns
方 = symbols('方')  # Side length of the square granary (also the diameter of the circular pit)

# Step 3: Calculate the cubic equation
# 多自乘 (方^2)
多自乘 = 方**2

# 並多少乘之 (方^2 * 方)
多自乘乘方 = 多自乘 * 方

# Multiply by 14 and divide by 25
多自乘乘方調整 = Fraction(一十四 * 多自乘乘方, 二十五)

# Subtract from the rate
實 = 率 - 多自乘乘方調整

# Step 4: Calculate the formula for 方 (square granary side length)
方法 = Fraction(一十四 * 多自乘, 二十五) + 多自乘

# Step 5: Calculate the formula for 廉法 (circular pit depth)
廉法 = Fraction(一十四 * 方, 二十五) + 方

# Step 6: Solve the cubic equation
cubic_eq = Eq(實, 0)
方解 = solve(cubic_eq, 方)

# Step 7: Calculate the dimensions
for 方值 in 方解:
    if 方值 > 0:  # Only consider positive solutions
        方 = 方值
        徑 = 方  # Diameter of the circular pit is equal to the side length of the square granary
        高 = 方 + Fraction(3, 10)  # The height of the square granary is 3 chi shorter than the circular pit
        深 = 方 - Fraction(2, 10)  # The depth of the circular pit is 2 chi deeper than the square granary
        break

# Convert results to 丈 (1 丈 = 10 尺)
a = 方 / 10
b = 高 / 10
c = 深 / 10

# Final answer
print(f"方徑各 {a} 丈，高 {b} 丈，深 {c} 丈。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion**: The total grain volume is converted from **shi** to cubic **chi**.
2. **Rate Calculation**: The rate (率) is calculated using the given constants.
3. **Cubic Equation**: A cubic equation is derived based on the relationships between the square granary and the circular pit.
4. **Solving the Equation**: The cubic equation is solved to find the side length of the square granary (方).
5. **Dimension Calculation**: Using the relationships, the height (高) and depth (深) are calculated.
6. **Unit Conversion**: The results are converted from **chi** to **zhang** for the final answer.

### Final Answer:
The program will output:
```
方徑各 a 丈，高 b 丈，深 c 丈。
```

Where `a`, `b`, and `c` are the calculated dimensions.
"""


"""
Code error: both arguments should be Rational instances"""
