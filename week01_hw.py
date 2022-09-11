'''
寻找第6个默尼森数

经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
'''

# decide if is a prime
def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def func(num):
    prime = 1
    for i in range(num):
        while True:
            prime += 1
            if is_prime(prime):
                M = 2**prime - 1
                if is_prime(M):
                    print(f'{prime}, {M}')
                    i += 1
                    break

func(6)
