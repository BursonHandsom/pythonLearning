my_name = 'Zed A. Shaw'
my_age = 35			# not a lie
my_height = 74		# inches
my_weight = 180		# lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# print("Let's talk about %s." % my_eyes)
# print("He's %d inches tall." % my_height)
# print("He's %d pounds heavy." % my_weight)
# print("Actually that's not too heavy.")
# print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
# print("His teeth are usually %s depending on the coffee" % my_teeth)

# # 当变量是整形时，格式化弄成浮点型会发生什么：会发生转换
# print("He's %f inches tall." % my_height)

# # 当变量是浮点型时，格式化弄成整型会发生什么：会发生转换
# fnum = 1.5
# print("%d" % fnum)

# # 多变量传入时，按顺序传入
# print("If I add %d, %d, and %d I get %d." % (
#       my_age, my_height, my_weight,
#       my_age + my_height + my_weight)
#       )

# %r是什么意思
print("test %r test %r" % (my_weight, my_eyes))

'''
操作% [(name)][flags][width].[precision]typecode
(name):
    为命名
flags:
    +	表示右对齐，
    -	表示左对齐。
    ‘ ’	表示在正数的左侧填充一个空格，从而与负数对齐。
    0	则表示用0填充从而与负数对齐
width
    表示显示宽度
precision
    表示小数点后精度
'''
# print("%3f" % 2)
