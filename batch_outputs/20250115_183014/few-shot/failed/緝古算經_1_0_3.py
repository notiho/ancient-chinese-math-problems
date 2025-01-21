"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese astronomical calculation involving the position of the moon at a specific time. Let's carefully translate the procedure into Python code step by step.

### Problem Description:
Suppose today is the first day of the 11th month at midnight. The sun is at **斗** (Dipper) 10 degrees and 480/7000 of a degree. The following constants are given:
- **章歲** (Zhang Sui): 700 (also called 行分法, "movement divisor").
- **朔月行定分** (Fixed movement of the new moon): 9000.
- **朔日定小余** (Small remainder of the new moon day): 10000.
- **日法** (Solar divisor): 20000.

The procedure calculates the position of the moon at midnight on the first day of the month.

---

### Procedure:
1. Subtract **朔月行定分** from **章歲**, and multiply the remainder by **朔日定小余**.
2. Divide the result by **日法**. The integer part is the **先行分** (initial movement), and the remainder is noted.
   - If the remainder is greater than or equal to half of **日法**, round up the **先行分** by 1.
3. If **先行分** exceeds **日行分** (daily movement divisor, equivalent to **日法**), convert it into degrees and fractions of a degree.
4. Subtract the sun's position at midnight (**朔日夜半日所在度分**) from the moon's position.
   - If the degrees are insufficient, add the degrees of the previous constellation (**往宿度**).
   - If the fractions are insufficient, borrow 1 degree and convert it into fractions to subtract.
5. The result is the moon's position at midnight.

---

### Python Code:


"""


from fractions import Fraction

# Constants
章歲 = 700  # Zhang Sui
朔月行定分 = 9000  # Fixed movement of the new moon
朔日定小余 = 10000  # Small remainder of the new moon day
日法 = 20000  # Solar divisor
朔日夜半日所在度 = 10  # Sun's position in degrees
朔日夜半日所在分 = Fraction(480, 7000)  # Sun's position in fractions of a degree

# Step 1: 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# Step 2: 余以乘朔日定小余
乘積 = 余 * 朔日定小余

# Step 3: 滿日法而一，為先行分
先行分 = 乘積 // 日法  # Integer part
餘分 = 乘積 % 日法  # Remainder

# 半法已上收成一，已下者棄之
if 餘分 >= 日法 / 2:
    先行分 += 1

# Step 4: 若先行分滿日行分而一，為度分
度 = 先行分 // 日法  # Degrees
分 = Fraction(先行分 % 日法, 日法)  # Fractions of a degree

# Step 5: 以減朔日夜半日所在度分
月度 = 度 - 朔日夜半日所在度
月分 = 分 - 朔日夜半日所在分

# 若度分不足減，加往宿度
if 月分 < 0:
    月度 -= 1
    月分 += 1  # Borrow 1 degree (converted to fractions)

# 若度不足減，加往宿度 (assumes 30 degrees in a constellation)
if 月度 < 0:
    月度 += 30

# Final Answer
a = 月度 + 月分


"""


---

### Explanation of Variables:
- `章歲`: The total divisor for the movement.
- `朔月行定分`: The fixed movement of the new moon.
- `朔日定小余`: The small remainder for the new moon day.
- `日法`: The solar divisor.
- `朔日夜半日所在度` and `朔日夜半日所在分`: The sun's position at midnight in degrees and fractions of a degree.
- `先行分`: The initial movement of the moon.
- `度` and `分`: The moon's position in degrees and fractions of a degree.
- `月度` and `月分`: The final calculated position of the moon.

---

### Final Answer:
The moon is at **a** degrees in **斗** (Dipper).
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 55227/2800"""
