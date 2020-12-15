studentnum = int(input())
# 请在此添加代码，填入for循环遍历学生人数的代码
# ********** Begin *********#
for student in range(0, studentnum, 1):
    # ********** End **********#
    sum = 0
    subjectscore = []
    inputlist = input()
    for i in inputlist.split(','):
        result = i
        subjectscore.append(result)
    # 请在此添加代码，填入for循环遍历学生分数的代码
    # ********** Begin *********#
    for score in subjectscore:
        # ********** End **********#
        score = int(score)
        sum = sum + score
    print("第%d位同学的总分为:%d" % (student, sum))



