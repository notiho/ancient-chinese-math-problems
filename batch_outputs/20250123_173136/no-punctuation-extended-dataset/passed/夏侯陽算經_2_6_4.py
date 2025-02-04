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
   - Interest for the month: 52 guan 800 wen.
   - 600 wen is allocated for public expenses.
   - The remaining interest is distributed among officials based on their rank.

2. **Rank Distribution**:
   - Taishou (Governor): 10 parts.
   - Biejia (Deputy): 7 parts.
   - Sima (Military Advisor): 5 parts.
   - Lushi Canjun (Recorder Assistant): 2 people, each 3 parts.
   - Sancang Canjun (Warehouse Assistant): 3 parts.
   - Sifa Canjun (Judicial Assistant): 3 parts.
   - Sihu Canjun (Household Assistant): 3 parts.
   - Canjun (General Assistants): 2 people, each 2 parts.

3. **Procedure**:
   - Calculate the total number of parts (41 parts).
   - Divide the remaining interest (after deducting public expenses) by the total parts to find the value of one part.
   - Multiply the value of one part by the number of parts for each official to determine their share.

### Python Code:


"""


from fractions import Fraction

# Initial data
本錢 = 880  # guan wen
月息率 = Fraction(6, 10)  # 6 fen per guan
月息 = Fraction(52, 1) + Fraction(800, 1000)  # 52 guan 800 wen
公廨食料 = Fraction(600, 1000)  # 600 wen

# Remaining interest after public expenses
剩餘息 = 月息 - 公廨食料

# Rank distribution
太守分 = 10
别駕分 = 7
司馬分 = 5
錄事參軍分 = 3 * 2  # 2 people, each 3 parts
司倉參軍分 = 3
司法參軍分 = 3
司户參軍分 = 3
參軍分 = 2 * 2  # 2 people, each 2 parts

# Total parts
總分 = 太守分 + 别駕分 + 司馬分 + 錄事參軍分 + 司倉參軍分 + 司法參軍分 + 司户參軍分 + 參軍分

# Value of one part
一分值 = 剩餘息 / 總分

# Calculate shares for each rank
太守錢 = 一分值 * 太守分
别駕錢 = 一分值 * 别駕分
司馬錢 = 一分值 * 司馬分
錄事參軍錢 = 一分值 * 3  # Each
錄事參軍總錢 = 錄事參軍錢 * 2  # Total for 2 people
司倉參軍錢 = 一分值 * 司倉參軍分
司法參軍錢 = 一分值 * 司法參軍分
司户參軍錢 = 一分值 * 司户參軍分
參軍錢 = 一分值 * 2  # Each
參軍總錢 = 參軍錢 * 2  # Total for 2 people

# Output results
a = 太守分
b = 太守錢
c = 别駕分
d = 别駕錢
e = 司馬分
f = 司馬錢
g = 2  # Number of 錄事參軍
h = 3  # Parts for each 錄事參軍
i = 錄事參軍錢
j = 2  # Number of 錄事參軍
k = 錄事參軍總錢
l = 司倉參軍分
m = 司倉參軍錢
n = 司法參軍分
o = 司法參軍錢
p = 司户參軍分
q = 司户參軍錢
r = 2  # Number of 參軍
s = 2  # Parts for each 參軍
t = 參軍錢
u = 2  # Number of 參軍
v = 參軍總錢

# Print results
print(f"太守 {a}分 計 {b}貫")
print(f"别駕 {c}分 計 {d}貫")
print(f"司馬 {e}分 計 {f}貫")
print(f"錄事參軍 {g}人 各 {h}分 各得 {i}貫 {j}人 共 {k}貫")
print(f"司倉參軍 {l}分 計 {m}貫")
print(f"司法參軍 {n}分 計 {o}貫")
print(f"司户參軍 {p}分 計 {q}貫")
print(f"參軍 {r}人 各 {s}分 各 {t}貫 {u}人 共 {v}貫")


"""


### Explanation:
1. **Interest Calculation**:
   - The monthly interest is calculated as `52 guan 800 wen`.
   - After deducting `600 wen` for public expenses, the remaining interest is distributed.

2. **Rank Distribution**:
   - Each official's share is proportional to their rank's parts.
   - The value of one part is calculated by dividing the remaining interest by the total parts.

3. **Output**:
   - The results are displayed for each official, including their parts, individual share, and total share for groups of officials.
"""


"""
"""
