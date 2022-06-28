def get_data(filepath):
    '''
        get information of binary tree
        
        return sequence of binary tree and its type
        1.preordered sequence
        2.middle sequence
        3.postordered sequence    
    '''
    
    sequence = []
    file = open(filepath)
    if file is None:
        print("open file failed")
        return sequence
    while True:
        _sequence = file.readline()
        _sequence = _sequence[:-1]
        # 文件读取结束标记
        if _sequence[0] == '#':
            break
        _sequence = _sequence.split(' ')
        for i in range(len(_sequence)):
            _sequence[i] = int(_sequence[i])
        sequence.append(_sequence)
    return sequence