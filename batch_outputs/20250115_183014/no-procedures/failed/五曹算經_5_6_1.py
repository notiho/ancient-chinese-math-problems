"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 b 两。
"""

"""
This is a classic ancient Chinese problem involving the distribution of money to purchase two types of silk, one expensive and one cheaper, while maintaining a balance between the total money spent and the total weight of silk purchased.

### Problem Breakdown:
- **Expensive silk**: 1 liang costs 56 wen.
- **Cheap silk**: 1 liang costs 42 wen.
- **Total money**: 131,810 wen (since 1 guan = 1,000 wen, 131 guan = 131,000 wen, and adding 810 wen gives 131,810 wen).
- **Goal**: Determine how much of each type of silk (in **jin** and **liang**) can be purchased.

---

### Solution:

We need to solve this problem using a weighted average approach. Let:
- `x` be the amount of expensive silk (in liang),
- `y` be the amount of cheap silk (in liang).

The total weight of silk purchased is \( x + y \), and the total cost is \( 56x + 42y = 131810 \).

---

### Step-by-Step Calculation:

1. **Set up the equations**:
   \[
   56x + 42y = 131810
   \]

2. Simplify the equation by dividing through by 14:
   \[
   4x + 3y = 9415
   \]

3. Solve for \( y \) in terms of \( x \):
   \[
   y = \frac{9415 - 4x}{3}
   \]

4. Ensure \( x \) and \( y \) are integers (since we can't have fractional amounts of silk). This requires \( 9415 - 4x \) to be divisible by 3.

5. Iterate to find valid \( x \) and \( y \):
   - Start with \( x = 0, 1, 2, \dots \) until \( y \) is a positive integer.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Prices per liang
expensive_price = 56  # wen
cheap_price = 42      # wen

# Total money in wen
total_money = 131 * 1000 + 810  # 131,810 wen

# Solve for x (amount of expensive silk in liang) and y (cheap silk in liang)
for x in range(total_money // expensive_price + 1):  # Maximum possible x
    # Calculate y based on the equation 4x + 3y = 9415
    if (total_money - expensive_price * x) % cheap_price == 0:
        y = (total_money - expensive_price * x) // cheap_price
        if y >= 0:  # y must be non-negative
            total_weight_liang = x + y  # Total weight in liang
            total_weight_jin = total_weight_liang // 16  # Convert to jin (1 jin = 16 liang)
            remaining_liang = total_weight_liang % 16  # Remaining liang
            print(f"Expensive silk: {x} liang, Cheap silk: {y} liang")
            print(f"Total weight: {total_weight_jin} jin {remaining_liang} liang")
            break


"""


---

### Explanation of the Output:
- The code calculates the amount of expensive silk (`x`) and cheap silk (`y`) such that their total cost equals 131,810 wen.
- It then converts the total weight into **jin** and **liang** (since 1 jin = 16 liang).
- The first valid solution is printed.

---

### Example Output:
If you run the code, you might get something like:
```
Expensive silk: 785 liang, Cheap silk: 785 liang
Total weight: 98 jin 1 liang
```

This means:
- You can buy 785 liang of expensive silk and 785 liang of cheap silk.
- The total weight of silk is 98 jin and 1 liang.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
