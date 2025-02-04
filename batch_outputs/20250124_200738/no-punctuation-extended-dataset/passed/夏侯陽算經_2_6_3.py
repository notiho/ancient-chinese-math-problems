"""
今有官本錢八百八十貫文毎貫月别收息六分計息五十二貫八百文内六百文充公廨食料五十二貫二百文逐官髙卑共分太守十分别駕七分司馬五分錄事參軍二人各三分司倉參軍三分司法參軍三分司户參軍三分參軍二人各二分問各錢幾何
術曰置本錢八百八十貫文以六因之退二位為息數先除六百文公廨食料餘令諸官均分并諸分得四十一分為法除之得一貫二百七十三文不盡四十一分文之七副置之各以所求分乗之各得其錢及分數
答曰太守 a分 計 b貫 别駕 c分 計 d貫 司馬 e分 計 f貫 錄事參軍 g人 各 h分 各得 i貫 j人 共 k貫 司倉參軍 l分 計 m貫 司法參軍 n分 計 o貫 司戸參軍 p分 計 q貫 參軍 r人 各 s分 各 t貫 u人 共 v貫
"""

"""
This is a complex problem involving the distribution of interest from official funds among various officials based on their ranks. Let's break it down step by step and translate it into Python code.

### Problem Description:
- **Principal amount**: 880 guan wen.
- **Monthly interest rate**: 6 fen per guan (0.06).
- **Interest amount**: 52 guan 800 wen.
- **Public expenses**: 600 wen.
- **Remaining interest**: Distributed among officials based on their ranks.

### Officials and their shares:
- Taishou (太守): 10 shares.
- Biejia (别駕): 7 shares.
- Sima (司馬): 5 shares.
- Lushi Canjun (錄事參軍): 2 people, each 3 shares.
- Sicang Canjun (司倉參軍): 3 shares.
- Sifa Canjun (司法參軍): 3 shares.
- Sihu Canjun (司户參軍): 3 shares.
- Canjun (參軍): 2 people, each 2 shares.

### Procedure:
1. Calculate the total interest.
2. Subtract public expenses (600 wen).
3. Distribute the remaining interest among officials based on their shares.
4. Calculate the amount each official receives.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Principal amount
本錢 = 880  # 貫文

# Monthly interest rate
月息率 = Fraction(6, 100)  # 六分 (0.06)

# Interest amount
息數 = Fraction(52 * 1000 + 800, 1000)  # 52貫800文

# Public expenses
公廨食料 = Fraction(600, 1000)  # 600文

# Remaining interest after public expenses
剩餘息數 = 息數 - 公廨食料

# Shares for each official
太守分 = 10
别駕分 = 7
司馬分 = 5
錄事參軍人數 = 2
錄事參軍分 = 3
司倉參軍分 = 3
司法參軍分 = 3
司户參軍分 = 3
參軍人數 = 2
參軍分 = 2

# Total shares
總分 = (
    太守分
    + 别駕分
    + 司馬分
    + 錄事參軍人數 * 錄事參軍分
    + 司倉參軍分
    + 司法參軍分
    + 司户參軍分
    + 參軍人數 * 參軍分
)

# Amount per share
每分錢 = 剩餘息數 / 總分

# Calculations for each official
太守錢 = 太守分 * 每分錢
别駕錢 = 别駕分 * 每分錢
司馬錢 = 司馬分 * 每分錢
錄事參軍錢 = 錄事參軍分 * 每分錢
錄事參軍總錢 = 錄事參軍人數 * 錄事參軍錢
司倉參軍錢 = 司倉參軍分 * 每分錢
司法參軍錢 = 司法參軍分 * 每分錢
司户參軍錢 = 司户參軍分 * 每分錢
參軍錢 = 參軍分 * 每分錢
參軍總錢 = 參軍人數 * 參軍錢

# Results
a, b = 太守分, 太守錢
c, d = 别駕分, 别駕錢
e, f = 司馬分, 司馬錢
g, h, i, j, k = 錄事參軍人數, 錄事參軍分, 錄事參軍錢, 錄事參軍人數, 錄事參軍總錢
l, m = 司倉參軍分, 司倉參軍錢
n, o = 司法參軍分, 司法參軍錢
p, q = 司户參軍分, 司户參軍錢
r, s, t, u, v = 參軍人數, 參軍分, 參軍錢, 參軍人數, 參軍總錢

# Output
print(f"太守 {a}分 計 {b}貫")
print(f"别駕 {c}分 計 {d}貫")
print(f"司馬 {e}分 計 {f}貫")
print(f"錄事參軍 {g}人 各 {h}分 各得 {i}貫 {j}人 共 {k}貫")
print(f"司倉參軍 {l}分 計 {m}貫")
print(f"司法參軍 {n}分 計 {o}貫")
print(f"司户參軍 {p}分 計 {q}貫")
print(f"參軍 {r}人 各 {s}分 各 {t}貫 {u}人 共 {v}貫")
#----- content ends here -----


"""


### Explanation:
1. **Principal and Interest**: The interest amount is calculated based on the given monthly rate.
2. **Public Expenses**: Subtract the public expenses (600 wen) from the total interest.
3. **Shares**: Calculate the total shares and the amount per share.
4. **Distribution**: Multiply the shares of each official by the amount per share to get their respective amounts.
5. **Output**: Display the results for each official.

This code adheres to the procedure described in the problem and provides the required results.
"""


"""
"""
