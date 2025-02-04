"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Problem Breakdown:

1. **First Part: Calculating the volume of the valley (冥谷積):**
   - The valley has an irregular shape, so we calculate its volume using the formula for a trapezoidal prism:
     \[
     V = \frac{(上廣 + 下廣)}{2} \times 深 \times 袤
     \]

2. **Second Part: Calculating the total transportation effort:**
   - Total volume to transport: \( 52,000 \, \text{chi} \) (given in the problem).
   - Each cart carries \( 34 \, \text{chi} \, 7 \, \text{cun} = 34 + \frac{7}{10} \, \text{chi} \).
   - Each trip covers \( 2 \, \text{li} \) (round trip: \( 1 \, \text{li} \) to destination and back).
   - Total distance traveled: \( 58 \, \text{li} \).
   - 6 people share one cart.

   We calculate:
   - How much volume each person transports in total.
   - How many workers (徒) are needed to complete the task.

---

### Python Code:


"""


from fractions import Fraction

# Part 1: Calculate the volume of the valley
上廣 = 2 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
袤1 = 7 * 10   # Convert zhang to chi
袤2 = 4 * 10   # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to total chi

# Volume of the valley (冥谷積)
積 = Fraction((上廣 + 下廣), 2) * 深 * Fraction((袤1 + 袤2), 2)

# Part 2: Calculate transportation effort
總積 = 52000  # Total volume to transport (given in problem)
車載 = Fraction(34, 1) + Fraction(7, 10)  # Volume carried by one cart per trip
程行 = 58  # Total distance in li
載輸 = 2    # Round trip distance in li
每車人數 = 6  # Number of people sharing one cart

# Total trips needed
總車次 = Fraction(總積, 車載)

# Total trips per person
每人車次 = 總車次 / 每車人數

# Total volume transported per person
人到 = 每人車次 * 車載

# Total workers needed
用徒 = 總車次 * 載輸 / 程行

# Results
print(f"人到 a尺: {人到}")
print(f"用徒 b人: {用徒}")


"""


---

### Explanation of Results:

1. **人到 a尺 (Volume transported per person):**
   This is the total volume each person is responsible for transporting, calculated based on the number of trips they make and the volume carried by the cart.

2. **用徒 b人 (Total workers needed):**
   This is the total number of workers required to complete the task, considering the total trips, round trip distance, and total distance traveled.


"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
