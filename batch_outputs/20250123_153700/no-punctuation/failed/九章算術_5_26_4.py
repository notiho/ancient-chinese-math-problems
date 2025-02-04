"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
荅曰七萬六百六十六尺太半尺
負土往來七十步其二十步上下棚除棚除二當平道五踟躕之間十加一載輸之間三十步定一返一百四十步土籠積一尺六寸秋程人功行五十九里半問人到積尺用徒各幾何
術曰以一籠積尺乘程行步數為實往來上下棚除二當平道五置定往來步數十加一及載輸之間三十步以為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

"""
Suppose there is a basin-shaped pond. The upper width is 6 zhang, the upper length is 8 zhang. 
The lower width is 4 zhang, the lower length is 6 zhang. The depth is 2 zhang.
Question: what is the volume in cubic chi?

Answer: 76066.5 cubic chi.

The workers carry soil back and forth for 70 bu. Of these, 20 bu are for the upper and lower shelves.
The shelves are equivalent to 2 bu of flat ground. For the hesitation in between, 10 bu are added.
For the loading and unloading interval, 30 bu are added. A round trip is 140 bu.
Each soil basket holds 1 chi 6 cun of soil. In autumn, a worker can travel 59.5 li.
Question: how much soil does one worker transport, and how many workers are needed to move the total soil?

The procedure says: Multiply the volume of one basket of soil by the total number of steps traveled to obtain the dividend.
For the divisor, place the round-trip steps, add 10 for hesitation, and add 30 for the loading and unloading interval.
Divide the dividend by the divisor to obtain the amount of soil transported by one worker.
Divide the total soil volume by the soil transported by one worker to obtain the number of workers required.

Answer: one worker transports *a* cubic chi, and *b* workers are required.
"""

# 上廣六丈袤八丈下廣四丈袤六丈深二丈
上廣 = 6
上袤 = 8
下廣 = 4
下袤 = 6
深 = 2

# 計算池的積
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤
池積 = Fraction((上積 + 下積) * 深, 2)  # 使用梯形公式計算體積

# 積轉換為立方尺
池積尺 = 池積 * 1000  # 1丈³ = 1000尺³

# 土籠積一尺六寸
土籠積 = Fraction(1, 1) + Fraction(6, 10)  # 1尺6寸 = 1.6尺³

# 秋程人功行五十九里半
程行 = Fraction(59, 1) + Fraction(1, 2)  # 59.5里
程行步數 = 程行 * 300  # 1里 = 300步

# 往來上下棚除二當平道五踟躕之間十加一載輸之間三十步
往來步數 = 70
棚除步數 = 20
棚除當平道 = Fraction(棚除步數, 2) * 5
踟躕步數 = 10
載輸步數 = 30
定步數 = 往來步數 + 棚除當平道 + 踟躕步數 + 載輸步數

# 計算一人所到的土積
實 = 土籠積 * 程行步數
一人所到土積 = Fraction(實, 定步數)

# 計算需要的工人數
用徒 = Fraction(池積尺, 一人所到土積)

# 答案
a = 一人所到土積
b = 用徒


"""
Variable 'a' has wrong value. Expected: 204, Actual: 357/2
Variable 'b' has wrong value. Expected: 53000/153, Actual: 48000/119"""
