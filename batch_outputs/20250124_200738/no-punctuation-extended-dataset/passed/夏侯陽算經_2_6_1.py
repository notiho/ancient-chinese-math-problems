"""
今有官本錢八百八十貫文毎貫月别收息六分計息五十二貫八百文内六百文充公廨食料五十二貫二百文逐官髙卑共分太守十分别駕七分司馬五分錄事參軍二人各三分司倉參軍三分司法參軍三分司户參軍三分參軍二人各二分問各錢幾何
術曰置本錢八百八十貫文以六因之退二位為息數先除六百文公廨食料餘令諸官均分并諸分得四十一分為法除之得一貫二百七十三文不盡四十一分文之七副置之各以所求分乗之各得其錢及分數
答曰太守 a分 計 b貫 别駕 c分 計 d貫 司馬 e分 計 f貫 錄事參軍 g人 各 h分 各得 i貫 j人 共 k貫 司倉參軍 l分 計 m貫 司法參軍 n分 計 o貫 司戸參軍 p分 計 q貫 參軍 r人 各 s分 各 t貫 u人 共 v貫
"""

"""
This is a complex problem involving the distribution of interest from official funds among various officials according to their ranks. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
1. **Initial Data**:
   - Official funds: 880 guan wen.
   - Monthly interest rate: 6 fen per guan (0.06 per guan).
   - Interest for the month: 52 guan 800 wen.
   - 600 wen is allocated for public expenses.

2. **Distribution**:
   - Remaining interest after deducting public expenses is distributed among officials based on their rank.
   - Total shares for distribution: 41 shares.

3. **Officials and Shares**:
   - Taishou (Governor): 10 shares.
   - Biejia (Deputy): 7 shares.
   - Sima (Military Advisor): 5 shares.
   - Lushi Canjun (Administrative Assistants): 2 people, each 3 shares.
   - Sancang Canjun (Warehouse Assistant): 3 shares.
   - Sifa Canjun (Judicial Assistant): 3 shares.
   - Sihu Canjun (Household Assistant): 3 shares.
   - Canjun (Assistants): 2 people, each 2 shares.

4. **Procedure**:
   - Calculate the remaining interest after deducting public expenses.
   - Divide the remaining interest by the total shares (41) to determine the value of one share.
   - Multiply the value of one share by the number of shares for each official to determine their allocation.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Initial data
本錢 = 880  # 貫文
月息率 = Fraction(6, 100)  # 每貫月别收息六分
月息 = 本錢 * 月息率  # 計息
公廨食料 = Fraction(600, 1000)  # 600文 = 0.6貫
餘息 = 月息 - 公廨食料  # 餘息

# Shares for distribution
總分 = 41  # 總分數
一分之值 = 餘息 / 總分  # 每一分的價值

# Officials and their shares
太守分 = 10
别駕分 = 7
司馬分 = 5
錄事參軍人數 = 2
錄事參軍分 = 3
司倉參軍分 = 3
司法參軍分 = 3
司戸參軍分 = 3
參軍人數 = 2
參軍分 = 2

# Calculations
太守錢 = 太守分 * 一分之值
别駕錢 = 别駕分 * 一分之值
司馬錢 = 司馬分 * 一分之值
錄事參軍錢 = 錄事參軍分 * 一分之值
錄事參軍總錢 = 錄事參軍錢 * 錄事參軍人數
司倉參軍錢 = 司倉參軍分 * 一分之值
司法參軍錢 = 司法參軍分 * 一分之值
司戸參軍錢 = 司戸參軍分 * 一分之值
參軍錢 = 參軍分 * 一分之值
參軍總錢 = 參軍錢 * 參軍人數

# Results
a = 太守分
b = 太守錢
c = 别駕分
d = 别駕錢
e = 司馬分
f = 司馬錢
g = 錄事參軍人數
h = 錄事參軍分
i = 錄事參軍錢
j = 錄事參軍人數
k = 錄事參軍總錢
l = 司倉參軍分
m = 司倉參軍錢
n = 司法參軍分
o = 司法參軍錢
p = 司戸參軍分
q = 司戸參軍錢
r = 參軍人數
s = 參軍分
t = 參軍錢
u = 參軍人數
v = 參軍總錢

# Output
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


---

### Explanation of the Code:
1. **Interest Calculation**:
   - The monthly interest is calculated as `本錢 * 月息率`.
   - Deduct the public expenses (`公廨食料`) from the interest to get the remaining interest (`餘息`).

2. **Share Value**:
   - The value of one share is calculated by dividing the remaining interest by the total shares (`41`).

3. **Distribution**:
   - Each official's allocation is calculated by multiplying their shares by the value of one share.

4. **Output**:
   - The results are printed for each official, showing their shares and the corresponding amount of money.

This code adheres to the procedure described in the problem and provides the required outputs for each official.
"""


"""
"""
