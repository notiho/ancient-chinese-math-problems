"""
今有官本錢八百八十貫文毎貫月别收息六分計息五十二貫八百文内六百文充公廨食料五十二貫二百文逐官髙卑共分太守十分别駕七分司馬五分錄事參軍二人各三分司倉參軍三分司法參軍三分司户參軍三分參軍二人各二分問各錢幾何
術曰置本錢八百八十貫文以六因之退二位為息數先除六百文公廨食料餘令諸官均分并諸分得四十一分為法除之得一貫二百七十三文不盡四十一分文之七副置之各以所求分乗之各得其錢及分數
答曰太守 a分 計 b貫 别駕 c分 計 d貫 司馬 e分 計 f貫 錄事參軍 g人 各 h分 各得 i貫 j人 共 k貫 司倉參軍 l分 計 m貫 司法參軍 n分 計 o貫 司戸參軍 p分 計 q貫 參軍 r人 各 s分 各 t貫 u人 共 v貫
"""

"""
This is a complex problem involving the distribution of interest from official funds among various officials based on their ranks. Let's break it down step by step and encode the procedure into Python.

### Problem Breakdown:
1. **Initial Data**:
   - Official funds: 880 guan wen.
   - Monthly interest rate: 6 fen per guan.
   - Total interest: 52 guan 800 wen.
   - 600 wen is allocated for public expenses.
   - Remaining interest is distributed among officials based on their ranks.

2. **Rank Distribution**:
   - Taishou: 10 parts.
   - Biejia: 7 parts.
   - Sima: 5 parts.
   - Lushi Canjun (2 people): 3 parts each.
   - Sicang Canjun: 3 parts.
   - Sifa Canjun: 3 parts.
   - Sihu Canjun: 3 parts.
   - Canjun (2 people): 2 parts each.

3. **Procedure**:
   - Calculate the remaining interest after deducting public expenses.
   - Sum up all the rank parts to determine the divisor (法).
   - Divide the remaining interest by the divisor to determine the value of one part.
   - Multiply the value of one part by the rank parts for each official to determine their share.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Initial data
本錢 = 880  # 貫文
月息率 = Fraction(6, 10)  # 每貫月别收息六分
總息 = Fraction(52, 1) + Fraction(800, 1000)  # 52貫800文
公廨食料 = Fraction(600, 1000)  # 600文

# Step 1: Calculate remaining interest after public expenses
餘息 = 總息 - 公廨食料

# Step 2: Calculate total rank parts (法)
太守分 = 10
别駕分 = 7
司馬分 = 5
錄事參軍分 = 3 * 2  # 2 people, each 3 parts
司倉參軍分 = 3
司法參軍分 = 3
司戸參軍分 = 3
參軍分 = 2 * 2  # 2 people, each 2 parts
總分 = 太守分 + 别駕分 + 司馬分 + 錄事參軍分 + 司倉參軍分 + 司法參軍分 + 司戸參軍分 + 參軍分

# Step 3: Calculate the value of one part
一分值 = 餘息 / 總分

# Step 4: Calculate the share for each official
太守錢 = 一分值 * 太守分
别駕錢 = 一分值 * 别駕分
司馬錢 = 一分值 * 司馬分
錄事參軍錢 = 一分值 * 3  # Each 錄事參軍
錄事參軍總錢 = 錄事參軍錢 * 2  # Total for 2 錄事參軍
司倉參軍錢 = 一分值 * 司倉參軍分
司法參軍錢 = 一分值 * 司法參軍分
司戸參軍錢 = 一分值 * 司戸參軍分
參軍錢 = 一分值 * 2  # Each 參軍
參軍總錢 = 參軍錢 * 2  # Total for 2 參軍

# Step 5: Output results
a, b = 太守分, 太守錢
c, d = 别駕分, 别駕錢
e, f = 司馬分, 司馬錢
g, h, i, j, k = 2, 錄事參軍分 // 2, 錄事參軍錢, 2, 錄事參軍總錢
l, m = 司倉參軍分, 司倉參軍錢
n, o = 司法參軍分, 司法參軍錢
p, q = 司戸參軍分, 司戸參軍錢
r, s, t, u, v = 2, 參軍分 // 2, 參軍錢, 2, 參軍總錢

# Final Answer
print(f"太守 {a}分 計 {b}貫")
print(f"别駕 {c}分 計 {d}貫")
print(f"司馬 {e}分 計 {f}貫")
print(f"錄事參軍 {g}人 各 {h}分 各得 {i}貫 {j}人 共 {k}貫")
print(f"司倉參軍 {l}分 計 {m}貫")
print(f"司法參軍 {n}分 計 {o}貫")
print(f"司戸參軍 {p}分 計 {q}貫")
print(f"參軍 {r}人 各 {s}分 各 {t}貫 {u}人 共 {v}貫")
#----- content ends here -----


"""


### Explanation of Variables:
- `一分值`: Value of one part of the rank distribution.
- `太守錢`, `别駕錢`, etc.: The amount of money each official or group of officials receives.
- `總分`: Total parts for all ranks combined.
- `餘息`: Remaining interest after deducting public expenses.

### Output:
The script calculates and prints the distribution of money for each official based on their rank parts. Each official's share is expressed in terms of guan and wen.
"""


"""
"""
