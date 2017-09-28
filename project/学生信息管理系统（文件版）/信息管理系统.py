import json


def save(data):
    #dumps是将元素为字典的列表转化成str格式，loads是将str转化成元素为字典的列表格式。
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open('students.txt', 'w+', encoding='utf-8') as f:
        f.write(s)


def load():
    with open('students.txt', 'r', encoding='utf-8') as f:
        s = f.read() #s为一个字符串
        #print(type(s))
        #print(s)
        return json.loads(s) #返回一个列表对象，其中列表的每一个元素为一个字典


def print_student(s):
    result = 'id：{}\n姓名：{}\n性别：{}\n分数：{}\n备注：{}\n' \
        .format(s['id'], s['name'], s['sex'], s['score'], s['remark'])
    print(result)


def error():
    print('Are you out your mind?')


def input_student(s):
    s['name'] = input('名字：')
    s['sex'] = input('性别：')
    s['score'] = int(input('分数：'))
    s['remark'] = input('备注：')


# 增加
def add():
    print('请输入需要增加的学生信息')
    students = load() #students为一个字典数据
    #print(type(students))
    #print(students)
    s = {
        'id': len(students) + 1,
        'deleted': False,
    }
    input_student(s)
    students.append(s)
    save(students)


# 删除
def delete():
    id = len(input('请输入要删除的学生id：'))
    students = load()
    for s in students:
        if s['id'] == id:
            s['deleted'] = True
            save(students)
            print('删除成功')
            break
    else:
        print('没有找到')


# 查找
def find():
    id = len(input('请输入要查找的学生id：'))
    students = load()
    for s in students:
        if s['id'] == id:
            print_student(s)
            break
    else:
        print('没有找到')


# 更新
def update():
    id = len(input('请输入要更新的学生id：'))
    students = load()
    for s in students:
        if s['id'] == id:
            print('请更新学生的信息')
            input_student(s)
            save(students)
            break
    else:
        print('没有找到')


# 查看所有学生信息
def print_all():
    students = load()
    for s in students:
        if not s['deleted']:
            print_student(s)


d = {
    '增加': add,
    '删除': delete,
    '查找': find,
    '更新': update,
    '查看': print_all,
}


def main():
    while True:
        op = input('请选择要进行的操作：')
        fun = d.get(op, error)
        fun()


if __name__ == '__main__':
    main()
