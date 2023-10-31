salary=int(input('enter your salary='))
age=int(input('enter your age='))
if(salary>=20000 or age<=25):
    loan=int(input('whats your required loan amount='))
    if(loan>50000):
        print('maximum loan is 50000')
    else:
        print('you are eligible for loan') 
else:
    print('you are not eligible for loan amount')

