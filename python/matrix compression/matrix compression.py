# 获取矩阵数据
def getData(filepath:list):
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

if __name__ == "__main__":
    filepath = "../code/python/matrix compression/input.txt"
    matrix = getData(filepath)
    print(matrix)