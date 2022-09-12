import string
import random
from collections import Counter

# 1. convert string to float
def str2float(sen):
    float_num = float(sen.split(":")[1])
    return print(float_num)


# 2. offset the string
# flag: 1->循环左移；2->循环右移。n:位移长度
def move_substr(sen, flag, n):
    if n > len(sen):
        return -1
    else:
        if flag == 1:
            return sen[n:] + sen[:n]
        else:
            return sen[-n:] + sen[:-n]


# 3. 按字母表顺序统计 字符串中26个字母出现的次数 (忽略大小写)
# ord(): return an integer representing the Unicode character.
def count_char(sen):
    vec = [0]*26
    for i in range(len(sen)):
        # constrain to within [a-z]
        if sen[i] >= 'a' and sen[i] <= 'z':
            # locate the position of given char
            vec[ord(sen[i]) - ord('a')] += 1
    return vec

# 4. 从键盘接收整数n∈[1,9],对于1-100之间的整数，删除包含n并且能被n整除的数，输出所有满足条件的数，每满10个数换行。
def quiz_4(division):
    cnt = 0
    res_str = ''
    print('The result of quiz 4: ')
    for i in range(1, 101):
        s = str(i)
        if i%division != 0 and s.find(str(division)) == -1:
            res_str = res_str + s + ','
            cnt += 1
            if cnt%10 == 0:
                print(res_str[:-1])
                res_str = ''
    if len(res_str) != 0:
        print(res_str[:-1])

# 5. 使用.randint生成500行 1-100之间的随机整数，存入random.txt中，寻找这些整数中的众数。
def quiz_5(file_path):
    with open(file_path, 'w+', encoding='utf-8') as f:
        cnt = 0
        while cnt < 500:
            f.write(str(random.randint(1,100)) + '\n')
            cnt += 1
        f.seek(0)
        lines = f.readlines()
    nums = [int(num.strip()) for num in lines]
    x = dict(Counter(nums))
    dic_sort_list = sorted(x.items(), key=lambda x:x[1], reverse=True)
    print(dic_sort_list[0][0])


# 6. article.txt为一篇英文文章，文中标点符号仅包含"," 、"."、 "!"、 "?"和"..."，请找出最长单词并输出。
def quiz_6(file):
    with open(file, 'r', encoding='utf-8') as f:
        sents = f.readlines()
    result_sents = []
    for sent in sents:
        table = sent.maketrans(string.punctuation, " "*len(string.punctuation))
        sent = sent.translate(table)
        words = sent.split()
        result_sents += words

    print(result_sents)
    result_sents.sort(key=len, reverse=True)  # longest comes to first
    long_len = len(result_sents[0])
    for word in result_sents:
        if len(word) == long_len:
            print(word)


# 7. 对文件Blowing in the wind.txt文件，执行操作：
# a,文件头部插入歌名：Blowin‘ in the wind; b,在歌名后插入Bob Dylan;
# c, 在文件末尾加上1962 by Warner Bros. Inc. d, 打印文件到屏幕上。

def insert_line(lines):
    lines.insert(0, "Blowin' in the wind\n")
    lines.insert(1, 'Bob Dylan\n')
    lines.append("\n1962 by Warner Bros. Inc.")
    return ''.join(lines)





if __name__ == '__main__':
    print('answer of quiz 1: \n')
    quiz1_str = 'My moral standing  is: 0.98765'
    str2float(quiz1_str)

    # quiz 2
    print('answer of quiz 2: \n')
    sen, flag, n = input('Enter the "string, flag, n": ').split(",")
    result = move_substr(sen, int(flag), int(n))
    if result != -1:
        print(result)
    else:
        print('The n is too large.')

    # quiz 3
    print('answer of quiz 3: \n')
    sen_3 = 'Hope is a good thing.'
    sen_3 = sen_3.lower()
    print(count_char(sen_3))

    # quiz 4
    print('answer of quiz 4: \n')
    num_4 = int(input('Enter a number of [1,9] for division in quiz 4: '))
    quiz_4(num_4)

    # quiz 5
    print('answer of quiz 5: \n')
    file_5 = 'random.txt'
    quiz_5(file_5)

    # quiz 6
    print('answer of quiz 6: \n')
    file_6 = 'week02_quiz06.txt'
    quiz_6(file_6)

    # quiz 7
    print('answer of quiz 7: \n')
    file_7 ='Blowing in the wind.txt'
    with open(file_7, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        quiz7_str = insert_line(lines)
        print(quiz7_str)
        f.seek(0)
        f.write(quiz7_str)



