password = 'a123456'
x = 3  # 剩餘機會
while True:
    pw = input('enter the password ')
    if pw == password:
        print('Login successfully')
        break
    else:
        x = x - 1
        print('Incorrect! You left', x, 'chance')
        if x == 0:
            break 