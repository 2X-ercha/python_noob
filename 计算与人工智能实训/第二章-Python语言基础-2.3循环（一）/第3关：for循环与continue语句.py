absencenum = int(input())
studentname = []
inputlist = input()
for i in inputlist.split(','):
    result = i
    studentname.append(result)
count = 0
# 请在此添加代码，填入循环遍历studentname列表的代码
# ********** Begin *********#
for student in studentname:
    # ********** End **********#
    count += 1
    if (count == absencenum):
        # 在下面填入continue语句
        # ********** Begin *********#
        continue
        # ********** End **********#
    print(student, "的试卷已阅")



