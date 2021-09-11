
'''
计算整除的概率
input:
    start: 开始位置
    end: 结束位置
    divide_list: 需要被整除的列表 egs:[4,9] 4∩9
return:
    随机选一个数整除的概率
'''
def calDivideProb(start, end, divide_list):
    total_num = 0
    for i in range(start,end+1):
        ok = 1
        for num in divide_list:
            if(i % num != 0):
                ok = 0
        total_num  = total_num + ok
    print(total_num)
    return total_num/(end-start+1)


if __name__ == '__main__':
    print(calDivideProb(1,1000000,[4,6,9]))

