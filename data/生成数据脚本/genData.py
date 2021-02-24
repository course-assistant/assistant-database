import random as r

a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
      '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
      '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

a2 = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
      '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
      '乾', '坤']

a3 = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
      '子', '', '', '', '', '', '', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
      '乾', '坤', '']


no = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def getNum(num):
    n = ''
    for i in range(0, num):
        n += str(r.choice(no))
        pass
    return n
    pass


def getName():
    return r.choice(a1)+r.choice(a2)+r.choice(a3)
    pass


def getSex():
    i = r.randint(0, 9)
    if(i % 2 == 0):
        return 0
        pass
    return 1
    pass


sql_format_teacher = "insert into teacher values('%s','root','%s','670B14728AD9902AECBA32E22FA4F6BD',%d,'avatar','135%s','%s@hncj.com','',1);"

sql_format_student = "insert into student values('%s','root','%s','670B14728AD9902AECBA32E22FA4F6BD',%d,'avatar','135%s','%s@hncj.com','',1);"


for i in range(40):
    print(sql_format_student % (getNum(9), getName(), getSex(), getNum(8), getNum(9)))
    pass
