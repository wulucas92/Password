password = 'a123456'
x = 3  # 剩餘機會
while x > 0:
    x = x - 1
    pw = input('enter the password ')
    if pw == password:
        print('Login successfully')
        break
    else:
        print('Incorrect!')
        if x > 0:
            print('You left', x, 'chance')
        else:
            print('You dont have more chance!')