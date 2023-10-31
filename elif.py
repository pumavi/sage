score=int(input('score:'))
if(score<35):
    print('poor student')
elif(score==35 and score<70):
    print('average sturdent')
elif(score>70 and score<=100):
    print('good student')
else:
    print('invalid number')
