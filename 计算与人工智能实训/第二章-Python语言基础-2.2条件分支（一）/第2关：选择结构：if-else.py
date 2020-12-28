workYear = int(input())
# 请在下面填入如果workYear < 5的判断语句
# ********** Begin *********#
if workYear < 5:
    # ********** End ***********#
    print("工资涨幅为0")
# 请在下面填入如果workYear >= 5 and workYear < 10的判断语句
# ********** Begin *********#
elif workYear >= 5 and workYear < 10:
    # ********** End ***********#
    print("工资涨幅为5%")
# 请在下面填入如果workYear >= 10 and workYear < 15的判断语句
# ********** Begin *********#
elif workYear >= 10 and workYear < 15:
    # ********** End ***********#
    print("工资涨幅为10%")
# 请在下面填入当上述条件判断都为假时的判断语句
# ********** Begin *********#
else:
    # ********** End ***********#
    print("工资涨幅为15%")
