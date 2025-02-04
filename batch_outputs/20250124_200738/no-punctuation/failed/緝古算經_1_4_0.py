"""
假令穿河袤一裏二百七十六步下廣六步一尺二寸北頭深一丈八尺六寸上廣十二步二尺四寸南頭深二百四十一尺八寸上廣八十六步四尺八寸運土於河西岸造漘北頭高二百二十三尺二寸南頭無高下廣四百六尺七寸五厘袤與河同甲郡二萬二千三百二十人乙郡六萬八千七十六人丙郡五萬九千九百八十五人丁郡三萬七千九百四十四人自穿負築各人程功常積三尺七寸二分限九十六日役河漘俱了四郡分共造漘其河自北頭先給甲郡以次與乙合均賦積尺問逐郡各給斜正袤上廣及深並漘上廣各多少
術曰如築堤術入之以程功乘甲郡人又以限日乘之四之三而一為積又六因以乘袤冪以上廣差乘深差為法除之為實又並小頭上下廣以乘小頭深三之為垣頭冪又乘袤冪以法除之為垣方三因小頭上廣以乘正袤以廣差除之為都廉從開立方除之即得小頭袤為甲袤求深廣以本袤及深廣差求之以兩頭上廣差乘甲袤以本袤除之所得加小頭上廣即甲上廣以小頭深減南頭深余以乘甲袤以本袤除之所得加小頭深即甲深又正袤自乘深差自乘並而開方除之即斜袤若求乙丙丁每以前大深廣為後小深廣準甲求之即得求漘上廣術曰以程功乘總人又以限日乘之為積六因之為實以正袤除之又以高除之所得以下廣減之余又半之即漘上廣
答曰漘上廣 a丈 甲郡正袤 b丈 斜袤 c丈 上廣 d丈 深 e丈 乙郡正袤 f丈 斜袤 g丈 上廣 h丈 深 i丈 丙郡正袤 j丈 斜袤 k丈 上廣 l丈 深 m丈 丁郡正袤 n丈 斜袤 o丈 上廣 p丈 深 q丈 
"""

"""
This problem is extremely complex and involves multiple steps for calculating the dimensions of the river and embankment construction, as well as distributing the workload among four regions. Due to the length and complexity of the procedure, I will break it into smaller sections and encode each part step by step.

### Problem Setup
We are tasked with calculating the dimensions of the river (正袤, 斜袤, 上廣, 深) and the embankment (漘上廣) for each of the four regions (甲, 乙, 丙, 丁). The procedure involves using the given dimensions, workload distribution, and construction rates to compute the required values.

---

### Constants and Initial Setup



---

### Step 1: Calculate the total workload for each region

The total workload for each region is calculated using the formula:
\[ \text{積} = \text{程功} \times \text{人數} \times \text{限日} \]



---

### Step 2: Calculate the 正袤 (length) for each region

The 正袤 for each region is calculated using the formula:
\[ \text{正袤} = \frac{\text{積} \times 6}{\text{袤冪} \times \text{上廣差} \times \text{深差}} \]

We first calculate the differences in width and depth:
\[ \text{上廣差} = \text{南頭上廣} - \text{小頭上廣} \]
\[ \text{深差} = \text{南頭深} - \text{小頭深} \]



---

### Step 3: Calculate the 斜袤 (diagonal length) for each region

The 斜袤 is calculated using the formula:
\[ \text{斜袤} = \sqrt{\text{正袤}^2 + \text{深差}^2} \]



---

### Step 4: Calculate the 上廣 (top width) and 深 (depth) for each region

The 上廣 and 深 for each region are calculated using the formulas:
\[ \text{上廣} = \text{小頭上廣} + \frac{\text{上廣差} \times \text{正袤}}{\text{河袤}} \]
\[ \text{深} = \text{小頭深} + \frac{\text{深差} \times \text{正袤}}{\text{河袤}} \]



---

### Step 5: Calculate 漘上廣 (top width of the embankment)

The 漘上廣 is calculated using the formula:
\[ \text{漘上廣} = \frac{\text{積} \times 6}{\text{正袤} \times \text{高}} - \text{漘下廣} \]



---

### Final Answer


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# 河的基本數據
河袤 = Fraction(1, 2) * 300 + 276  # 袤一里二百七十六步 (1 里 = 300 步)
小頭廣 = Fraction(6) + Fraction(1, 10) * 2  # 下廣六步一尺二寸 (1 步 = 6 尺, 1 尺 = 10 寸)
小頭深 = Fraction(10) + Fraction(8) + Fraction(1, 10) * 6  # 北頭深一丈八尺六寸 (1 丈 = 10 尺)
小頭上廣 = Fraction(12) + Fraction(1, 10) * 4  # 上廣十二步二尺四寸
南頭深 = Fraction(241) + Fraction(1, 10) * 8  # 南頭深二百四十一尺八寸
南頭上廣 = Fraction(86) + Fraction(1, 10) * 4 + Fraction(1, 100) * 8  # 上廣八十六步四尺八寸

# 漘的基本數據
漘下廣 = Fraction(406) + Fraction(1, 10) * 7 + Fraction(1, 1000) * 5  # 下廣四百六尺七寸五厘
北頭高 = Fraction(223) + Fraction(1, 10) * 2  # 北頭高二百二十三尺二寸
南頭高 = 0  # 南頭無高

# 四郡人數
甲郡人數 = 22320
乙郡人數 = 68076
丙郡人數 = 59985
丁郡人數 = 37944

# 每人程功
程功 = Fraction(3) + Fraction(1, 10) * 7 + Fraction(1, 100) * 2  # 常積三尺七寸二分

# 限日
限日 = 96

# 計算每郡的積
甲積 = 程功 * 甲郡人數 * 限日
乙積 = 程功 * 乙郡人數 * 限日
丙積 = 程功 * 丙郡人數 * 限日
丁積 = 程功 * 丁郡人數 * 限日

# 計算上廣差和深差
上廣差 = 南頭上廣 - 小頭上廣
深差 = 南頭深 - 小頭深

# 計算正袤
甲正袤 = Fraction(甲積 * 6, 河袤 * 上廣差 * 深差)
乙正袤 = Fraction(乙積 * 6, 河袤 * 上廣差 * 深差)
丙正袤 = Fraction(丙積 * 6, 河袤 * 上廣差 * 深差)
丁正袤 = Fraction(丁積 * 6, 河袤 * 上廣差 * 深差)

# 計算斜袤
甲斜袤 = sqrt(甲正袤**2 + 深差**2)
乙斜袤 = sqrt(乙正袤**2 + 深差**2)
丙斜袤 = sqrt(丙正袤**2 + 深差**2)
丁斜袤 = sqrt(丁正袤**2 + 深差**2)

# 計算上廣和深
甲上廣 = 小頭上廣 + Fraction(上廣差 * 甲正袤, 河袤)
乙上廣 = 小頭上廣 + Fraction(上廣差 * 乙正袤, 河袤)
丙上廣 = 小頭上廣 + Fraction(上廣差 * 丙正袤, 河袤)
丁上廣 = 小頭上廣 + Fraction(上廣差 * 丁正袤, 河袤)

甲深 = 小頭深 + Fraction(深差 * 甲正袤, 河袤)
乙深 = 小頭深 + Fraction(深差 * 乙正袤, 河袤)
丙深 = 小頭深 + Fraction(深差 * 丙正袤, 河袤)
丁深 = 小頭深 + Fraction(深差 * 丁正袤, 河袤)

# 計算漘上廣
漘積 = (甲積 + 乙積 + 丙積 + 丁積) * 6
漘上廣 = Fraction(漘積, 河袤 * 北頭高) - 漘下廣

# 答案
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: 54488789/14200
Variable 'b' has wrong value. Expected: 144, Actual: 223200/32873
Variable 'c' has wrong value. Expected: 1443/10, Actual: 223.30324881546002
Variable 'd' has wrong value. Expected: 651/25, Actual: 342302/25205
Variable 'e' has wrong value. Expected: 279/25, Actual: 258575619/11669915
Variable 'f' has wrong value. Expected: 576/5, Actual: 680760/32873
Variable 'g' has wrong value. Expected: 2886/25, Actual: 224.1586356035471
Variable 'h' has wrong value. Expected: 1023/25, Actual: 80662/5041
Variable 'i' has wrong value. Expected: 93/5, Actual: 343681779/11669915
Variable 'j' has wrong value. Expected: 288/5, Actual: 599850/32873
Variable 'k' has wrong value. Expected: 1443/25, Actual: 223.94466097969996
Variable 'l' has wrong value. Expected: 1209/25, Actual: 392522/25205
Variable 'm' has wrong value. Expected: 558/25, Actual: 328632519/11669915
Variable 'n' has wrong value. Expected: 144/5, Actual: 379440/32873
Variable 'o' has wrong value. Expected: 1443/50, Actual: 223.49825881234156
Variable 'p' has wrong value. Expected: 1302/25, Actual: 363134/25205
Variable 'q' has wrong value. Expected: 1209/50, Actual: 287636259/11669915"""
