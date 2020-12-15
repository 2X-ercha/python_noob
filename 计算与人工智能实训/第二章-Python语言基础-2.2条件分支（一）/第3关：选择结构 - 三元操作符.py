jimscore = int(input())
jerryscore = int(input())
#请在此添加代码，判断若jim的得分jimscore更高，则赢家为jim。若jerry的得分jerryscore更高，则赢家为jerry并输出赢家的名字。
#********** Begin *********#
winner='jim' if jimscore>jerryscore else 'jerry'
#********** End **********#
print(winner)
