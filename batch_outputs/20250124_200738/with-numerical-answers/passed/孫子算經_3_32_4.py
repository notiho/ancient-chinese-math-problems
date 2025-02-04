"""
今有出門望見九堤，堤有九木，木有九枝，枝有九巢，巢有九禽，禽有九雛，雛有九毛，毛有九色。問：各幾何？
術曰：置九堤以九乘之，得木之數；又以九乘之，得枝之數；又以九乘之，得巢之數；又以九乘之，得禽之數；又以九乘之，得雛之數；又以九乘之，得毛之數；又以九乘之，得色之數。
答曰：木 a(=81)枝 ， b(=729) 巢， c(=6561) 禽， d(=59049) 雛， e(=531441) 毛， f(=4782969) 色， g(=43046721) 。
"""

#----- content starts here -----
"""
Suppose one goes out and sees 9 dikes. Each dike has 9 trees, each tree has 9 branches, each branch has 9 nests, each nest has 9 birds, each bird has 9 chicks, each chick has 9 feathers, and each feather has 9 colors.
Question: how many of each are there?

The procedure says: Place the 9 dikes and multiply by 9 to obtain the number of trees.
Then multiply by 9 again to obtain the number of branches.
Then multiply by 9 again to obtain the number of nests.
Then multiply by 9 again to obtain the number of birds.
Then multiply by 9 again to obtain the number of chicks.
Then multiply by 9 again to obtain the number of feathers.
Then multiply by 9 again to obtain the number of colors.

Answer: *a*(=81) trees, *b*(=729) branches, *c*(=6561) nests, *d*(=59049) birds, *e*(=531441) chicks, *f*(=4782969) feathers, *g*(=43046721) colors.
"""

# 置九堤
堤 = 9

# 以九乘之，得木之數
木 = 堤 * 9

# 又以九乘之，得枝之數
枝 = 木 * 9

# 又以九乘之，得巢之數
巢 = 枝 * 9

# 又以九乘之，得禽之數
禽 = 巢 * 9

# 又以九乘之，得雛之數
雛 = 禽 * 9

# 又以九乘之，得毛之數
毛 = 雛 * 9

# 又以九乘之，得色之數
色 = 毛 * 9

# Assigning the results
a = 木          # 81
b = 枝          # 729
c = 巢          # 6561
d = 禽          # 59049
e = 雛          # 531441
f = 毛          # 4782969
g = 色          # 43046721#----- content ends here -----

"""
"""
