'''
使用字典为某平台创建用户信息 (包括用户名和密码)：新用户创建账号，要求不能与老用户重名；老用户则可以使用用户名和密码登录。
'''
def new_users(user_info_dict):
    name = str(input('Please enter user name: '))
    if name in user_info_dict.keys():
        print('User name is used, please choose another one!')
    else:
        pw = str(input('Enter your password please.'))


def old_users(user_info_dict):
    name, password = str(input('Please enter user name: ')), input('Please enter password: ')
    if password == user_info_dict[name]:
        print(f'{name}, welcome back!')
    else:
        print('incorrect password!')
        password = input('Please enter password: ')

def login():
    option = '''
            (N)ew User Login
            (O)ld User Login
            (E)xit'''
    enter = str(input('Please enter your option(New, O or E)'))


# 在lst中查找是否存在两数之和等于n，若存在， 则返回两数下标；否则返回-1.
def two_num_sum(n, lst):
    d = {}
    for i in range(len(lst)):
        d[lst[i]] = i   # 创建数值-下标对
    for i in range(len(lst)):
        if n - lst[i] in d:
            return i, d[n-lst[i]]
    return -1







if __name__ == '__main__':
    lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
    n = int(input('Please enter a number: '))
    print(two_num_sum(n, lst))
