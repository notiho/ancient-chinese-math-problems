"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a valley and determining the distance a person can transport the soil and the number of workers required. Let's break it down step by step according to the procedure.

### Problem Setup:
- The valley has an upper width of 2 zhang (20 chi), a length of 7 zhang (70 chi), a lower width of 8 chi, a length of 4 zhang (40 chi), and a depth of 6 zhang 5 chi (65 chi).
- The task is to calculate the volume of the valley, the distance a person can transport the soil, and the number of workers required.

### Procedure:
1. **Volume Calculation**:
   - The valley's volume is calculated using the trapezoidal prism formula:
     \[
     V = \frac{(上廣 \times 上袤 + 下廣 \times 下袤)}{2} \times 深
     \]

2. **Distance a Person Can Transport**:
   - Multiply the volume of one cartload of soil by the distance traveled in steps to get the "實" (product).
   - Add the round-trip distance and the loading/unloading distance (1 li = 300 steps).
   - Multiply by 6 (6 people per cart) to get the divisor ("法").
   - Divide to find the distance a person can transport.

3. **Number of Workers Required**:
   - Divide the total volume by the distance a person can transport to find the number of workers.

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the valley
上廣 = 20  # 2丈 = 20尺
上袤 = 70  # 7丈 = 70尺
下廣 = 8   # 8尺
下袤 = 40  # 4丈 = 40尺
深 = 65    # 6丈5尺 = 65尺

# Step 1: Calculate the volume of the valley
積 = Fraction((上廣 * 上袤 + 下廣 * 下袤), 2) * 深  # Volume in cubic chi
積 = int(積)  # Convert to integer for simplicity

# Step 2: Calculate the distance a person can transport
一車積尺 = 100  # Assume 1 cartload = 100 cubic chi
程行步數 = 300  # Distance traveled in steps (1 li = 300 steps)
往來步數 = 2 * 程行步數  # Round-trip distance
載輸間 = 300  # Loading/unloading distance (1 li = 300 steps)
法 = (往來步數 + 載輸間) * 6  # Divisor (法)
實 = 一車積尺 * 程行步數  # Product (實)
人到 = Fraction(實, 法)  # Distance a person can transport in chi

# Step 3: Calculate the number of workers required
用徒 = Fraction(積, 人到)  # Number of workers required

# Convert results to mixed fractions for clarity
人到_mixed = divmod(int(Fraction.as_integer_ratio(人到)[0]), Fraction.as_integer_ratio(人到)[1])
用徒_mixed = divmod(int(Fraction.as_integer_ratio(用徒)[0]), Fraction.as_integer_ratio(用徒)[1])

# Outputs
a = 人到  # Distance a person can transport
b = 用徒  # Number of workers required

print(f"人到 {a} 尺")
print(f"用徒 {b} 人")


"""


---

### Explanation of Outputs:
- `a`: The distance a person can transport the soil in chi.
- `b`: The number of workers required to transport the soil.

This code follows the procedure described in the problem and calculates the required values step by step.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 50/9
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 10062"""
