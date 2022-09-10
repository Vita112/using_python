'''quiz_1
BMI = weight / (height**2)
过低：低于18.5; 正常：18.5~23.9; 过重：24~27.9； 肥胖：高于28
输入体重和身高，输出相应的BMI值和体重肥胖程度判断结果
'''
weight = eval(input('please enter your weight(kg): '))
height = eval(input('please enter your height(m): '))

bmi = weight / height ** 2
print(f'Your BMI is {bmi:.1f}.')
if bmi < 18.5:
    print('too thin.')
elif bmi < 24:
    print('normal.')
elif bmi < 28:
    print('overweight.')
else:
    print('fat.')

'''quiz_2
按照公式C= 5/9×(F-32) ，将华氏温度转换成摄氏温度，并产生一张 华氏0~300度与对应摄氏温度之间的对照表
'''
for f in range(0,301,20):
    c = 5/9 * (f-32)
    print(f'{f}f ={c:.0f}c')

'''
角谷猜想：对于一个正整数，若为偶数，则除以2；若为奇数，则乘以3加1，得到的新数按照刚才的规则继续，则若干次后得到的结果为1'''
n = int(input('please enter an integer: '))
while n != 1:
    if n%2 == 0:
        print(f'{n}/2 = {n//2}')
        n //= 2
    else:
        print(f'{n}*3+1 = {n*3+1}.')
        n = n*3+1


'''
输入n，用递推法求 1+2！+3！+......+n!的和并输出。'''
n = int(input('Please enter a number to calculate n!:'))
res = term = 1
for i in range(2, n+1):
    term *= i
    res += term
print(f'result = {res}')

'''
求解1-4这4个数字可以组成多少个无重复的三位数，按照从小到大的顺序输出这些数字。'''
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i!=j and i!=k and j!=k:
                print(100*i+10*j+k)

'''
验证：一个三位整数是37的倍数，则整个整数循环左移后得到的另两个3位数也是37的倍数'''
for num in range(100, 200):
    if num%37 == 0:
        new_num1 = num%100*10 + num//100
        new_num2 = num%10*100 + num//10
        if new_num1 % 37 != 0 or new_num2 % 37 != 0:
            print("It's a false proposition.")
            break
else:
    print("It's a true proposition.")




'''
如果一个数字等于它的因子之和，则称该数字为完数。计算1000以内的所有完数，并输出'''
for i in range(1, 10):
    init = 0
    for j in range(1, i):
        if i%j == 0:
            init += j
    if init == i:
        print(i)
        print("Its factors are: ")
        for j in range(1, i):
            if i%j == 0:
                print(j, end='\n')


'''
验证哥德巴赫猜想之一：2000以内的正偶数(>=4)都能分解为两个质数之和。每个偶数显示为4=2+2样的形式
质数==素数：大于1的自然数中，除了1和其本身之外，不能被其他自然数整除的数'''

import math

def prime(x):
    if x == 1:
        return False
    n = int(math.sqrt(x))
    for i in range(2, n+1):
        if x%i == 0:
            return False  # 能够被整除，不是素数
    return True

def GC(n):
    k = 3
    while k < n:
        t = n-k
        if t<k:
            break
        if prime(k) and prime(t):
            return k,t
        k += 2

num_8 = int(input('Enter a number between 1~2000: '))
if num_8 > 4:
    a,b = GC(num_8)
    print(f'{num_8} = {a}+{b}')
elif num_8 == 4:
    print(f'4 = 2+2')