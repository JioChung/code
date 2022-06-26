'''
获取矩阵数据
'''
def get_data(filepath):
    # 打开文件
    file = open(filepath)
    # 文件打开失败
    if file is None:
        print("open file failed")
        exit(0)
    # 存储读取的矩阵信息
    matrix = []
    # 开始读取
    while True:
        # 读取一行
        _row = file.readline()
        # 去除最后的换行符
        _row = _row[:-1]
        # 读取完，break
        if len(_row) == 0:
            break
        # 将读取的一行字符在空格处分割
        _row = _row.split(' ')
        row = []
        # 将字符转换为数字
        for i in range(len(_row)):
            row.append(int(_row[i]))
        matrix.append(row)
    file.close()
    return matrix

'''
判断matrix类型：1.上三角、2.下三角、3.三对角矩阵
'''
def matrix_type(matrix:list):
    
    # 默认返回0，表示无法判断矩阵类型（一般矩阵）
    return 0;
