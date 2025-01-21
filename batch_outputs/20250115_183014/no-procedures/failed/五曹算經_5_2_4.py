"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
To solve this problem, we need to distribute 27 jin and 5 liang of silk among 738 households. The units of measurement in ancient China are as follows:

1 jin (斤) = 16 liang (两)  
1 liang (两) = 24 zhu (銖)  
1 zhu (銖) = 10 shu (黍)

We will calculate how much silk each household gets in terms of zhu (銖) and shu (黍).

---

### Step-by-step solution:

1. **Convert the total silk into the smallest unit (shu):**  
   - 27 jin = \( 27 \times 16 \) liang = 432 liang  
   - Total liang = \( 432 + 5 = 437 \) liang  
   - Convert liang to zhu: \( 437 \times 24 \) zhu = 10,488 zhu  
   - Convert zhu to shu: \( 10,488 \times 10 \) shu = 104,880 shu  

2. **Divide the total silk (in shu) by the number of households:**  
   Each household gets:  
   \( \frac{104,880}{738} \) shu  

3. **Convert the result back into jin, liang, zhu, and shu:**  
   - First, calculate the total shu per household:  
     \( \frac{104,880}{738} = 142 \) shu (remainder 24 shu).  
   - Convert 142 shu into zhu:  
     \( 142 \div 10 = 14 \) zhu (remainder 2 shu).  

---

### Final Answer:
Each household gets:  
**14 zhu, 2 shu.**

---

Here is the Python code to calculate this:


"""


from fractions import Fraction

# Total silk in jin, liang, zhu, shu
total_jin = 27
total_liang = 5
total_households = 738

# Convert everything to shu
total_liang += total_jin * 16  # Convert jin to liang
total_zhu = total_liang * 24  # Convert liang to zhu
total_shu = total_zhu * 10    # Convert zhu to shu

# Divide by the number of households
shu_per_household = Fraction(total_shu, total_households)

# Convert back to zhu and shu
zhu_per_household = shu_per_household // 10
shu_remainder = shu_per_household % 10

# Print the result
print(f"Each household gets: {zhu_per_household} zhu, {shu_remainder} shu.")


"""



"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
