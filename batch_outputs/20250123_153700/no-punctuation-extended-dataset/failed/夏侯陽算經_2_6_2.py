"""
今有官本錢八百八十貫文毎貫月别收息六分計息五十二貫八百文内六百文充公廨食料五十二貫二百文逐官髙卑共分太守十分别駕七分司馬五分錄事參軍二人各三分司倉參軍三分司法參軍三分司户參軍三分參軍二人各二分問各錢幾何
術曰置本錢八百八十貫文以六因之退二位為息數先除六百文公廨食料餘令諸官均分并諸分得四十一分為法除之得一貫二百七十三文不盡四十一分文之七副置之各以所求分乗之各得其錢及分數
答曰太守 a分 計 b貫 别駕 c分 計 d貫 司馬 e分 計 f貫 錄事參軍 g人 各 h分 各得 i貫 j人 共 k貫 司倉參軍 l分 計 m貫 司法參軍 n分 計 o貫 司戸參軍 p分 計 q貫 參軍 r人 各 s分 各 t貫 u人 共 v貫
"""

"""
This is a complex problem involving the distribution of interest from official funds among various officials based on their ranks. Let's break it down step by step and implement the procedure in Python.


"""


from fractions import Fraction

# 官本錢八百八十貫文
本錢 = 880

# 每貫月别收息六分
月息率 = Fraction(6, 100)

# 計息五十二貫八百文
息錢 = 本錢 * 月息率

# 內六百文充公廨食料
公廨食料 = Fraction(600, 1000)  # 600文 = 0.6貫

# 息錢扣除公廨食料
剩餘息錢 = 息錢 - 公廨食料

# 各官分配比例
分配比例 = {
    "太守": 10,
    "别駕": 7,
    "司馬": 5,
    "錄事參軍": 3 * 2,  # 2人, each 3分
    "司倉參軍": 3,
    "司法參軍": 3,
    "司戸參軍": 3,
    "參軍": 2 * 2,  # 2人, each 2分
}

# 計算總分
總分 = sum(分配比例.values())

# 每分的錢
每分錢 = 剩餘息錢 / 總分

# 各官分配結果
結果 = {}
for 官, 分 in 分配比例.items():
    錢 = 每分錢 * 分
    結果[官] = {
        "分": 分,
        "錢": 錢,
    }

# 輸出結果
for 官, 資訊 in 結果.items():
    print(f"{官}: {資訊['分']}分, 計 {資訊['錢']}貫")


"""


### Explanation of the Code:
1. **Initial Setup**:
   - The principal amount is `880貫`.
   - The monthly interest rate is `6分` (6%).
   - The total interest is calculated as `本錢 * 月息率`.

2. **Deduction for Public Expenses**:
   - `600文` (0.6貫) is deducted from the interest for public expenses.

3. **Distribution Ratios**:
   - The distribution ratios for each official are provided in the problem.
   - For officials with multiple people (e.g., 錄事參軍 and 參軍), their total share is calculated by multiplying their individual share by the number of people.

4. **Total Shares**:
   - The total shares (`總分`) are calculated by summing up all the distribution ratios.

5. **Money per Share**:
   - The remaining interest is divided by the total shares to calculate the money per share (`每分錢`).

6. **Distribution**:
   - Each official's share of the money is calculated by multiplying their share ratio by the money per share.

7. **Output**:
   - The results are printed for each official, showing their share ratio and the amount of money they receive.

This code calculates the exact distribution of the interest among the officials based on the given procedure. Let me know if you need further clarification or adjustments!
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'
Missing variable in output: 'i'
Missing variable in output: 'j'
Missing variable in output: 'k'
Missing variable in output: 'l'
Missing variable in output: 'm'
Missing variable in output: 'n'
Missing variable in output: 'o'
Missing variable in output: 'p'
Missing variable in output: 'q'
Missing variable in output: 'r'
Missing variable in output: 's'
Missing variable in output: 't'
Missing variable in output: 'u'
Missing variable in output: 'v'"""
