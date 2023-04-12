import csv
import init
# 一維陣列轉二維陣列
# 分割


def to_list(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    return lines

# 二維陣列轉換成字典


def list_to_dict(lines):
    # 轉換成字典
    dicts = {}
    for line in lines:
        dicts[line[0]] = {'factor': line[1], 'age': line[2], 'gender': line[3],
                          'medicine': line[4], 'use': line[5], 'part': line[6]}
    return dicts


def store_kind(dicts):
    # 先儲存資料種類
    factor_list = []
    med_list = []
    part_list = []
    for key, line in dicts.items():
        if line['factor'] not in factor_list:
            factor_list.append(line['factor'])
        if line['medicine'] not in med_list:
            med_list.append(line['medicine'])
        if line['part'] not in part_list:
            part_list.append(line['part'])
    return factor_list, med_list, part_list
# 查詢病患資料


def query(dicts):
    has = False
    name = input("請輸入名字：")
    if name.isalpha():
        name = name.capitalize()
    for name_key, data in dicts.items():
        if name == name_key:
            has = True
            print(
                f"名字：{name}\n年紀：{data['age']}\n性別：{data['gender']}\n危險因子：{data['factor']}\n使用藥物：{data['medicine']}")
            if len(data['use']) > 1:
                single, per = data['use'].split('*')
                print(f'服用劑量：{single} mg ', end='')
                if per == '1':
                    print('once a day')
                elif per == '2':
                    print('twice a day')
                else:
                    print(per+" times a day")
            else:
                print("服用劑量：Not taste")
            print(f"部位: {data['part']}")
            break
    if has == False:
        print("查無此人")
# 篩選資料，根據篩選要求挑選資料


def select(dicts, factor_list, med_list, part_list):
    # 釐清要求
    # 危險因子選擇
    print("危險因子有以下選擇：", end='')
    for i in range(len(factor_list)):
        if i != 0:
            print(' ', end='')
        print("("+str(i+1)+")"+factor_list[i], end='')
    factor = input('請輸入1~'+str(len(factor_list))+'，可複選: ')
    f = [0]*5
    for i in factor:
        f[int(i)-1] = 1
    # 年齡範圍
    age_com = input('請輸入篩選年齡與範圍,格式：Y~O ,Y,O 均為數字: Y要比O小；若不以此標準篩選則輸入all: ')
    if age_com == 'all':
        age_min = 0
        age_max = 10000
    else:
        age_min, age_max = map(int, age_com.split('~'))
    # 藥物選擇
    print("使用藥物有以下選擇：", end='')
    for i in range(len(med_list)):
        if i != 0:
            print(' ', end='')
        print("("+str(i+1)+")"+med_list[i], end='')
    med = input('請輸入1~'+str(len(med_list))+'，可複選: ')
    m = [0]*5
    for ee in med:
        m[int(ee)-1] = 1
    # 性別選擇
    gender = input("請輸入篩選性別：(1)男 (2)女: ")
    g = [0]*2
    for e3 in gender:
        g[int(e3)-1] = 1
    # 使用劑量範圍
    use_com = input('請輸入篩選使用劑量與範圍,格式：L~M ,L,M 均為數字且L比M小: ；若不以此標準篩選則輸入all: ')
    if use_com == 'all':
        use_min = 0
        use_max = 10000
    else:
        use_min, use_max = map(int, use_com.split('~'))
    # 部位
    print("部位有以下選擇：", end='')
    for i in range(len(part_list)):
        if i != 0:
            print(' ', end='')
        print("("+str(i+1)+")"+part_list[i], end='')
    part = input('請輸入1~'+str(len(part_list))+'，可複選: ')
    p = [0]*6
    for e4 in part:
        p[int(e4)-1] = 1
    # 挑選資料
    has = False
    sort_list = []
    for key, line in dicts.items():
        age = int(line['age'])
        if line['gender'] == '男':
            gender = 0
        else:
            gender = 1
        med = line['medicine']
        total = eval(line['use'])
        part = line['part']
        if f[factor_list.index(line['factor'])] and total >= use_min and total <= use_max and age >= age_min and age <= age_max and m[med_list.index(med)] and g[gender] and p[part_list.index(part)]:
            has = True
            sort_list.append([key, line])
    if has == False:
        print("not found")
    else:
        sort_(sort_list)

# 排序資料


def sort_(sort_list):
    command1 = int(input('(1)依年紀排序(2)依使用量排序'))
    command2 = int(input('(1)由小到大排序(2)依大到小排序'))
    if command1 == 1 and command2 == 1:
        sort_list.sort(key=lambda x: (int(x[1]['age'])))
    elif command1 == 1 and command2 == 2:
        sort_list.sort(key=lambda x: (-int(x[1]['age'])))
    elif command1 == 2 and command2 == 1:
        sort_list.sort(key=lambda x: (eval(x[1]['use'])))
    elif command1 == 2 and command2 == 2:
        sort_list.sort(key=lambda x: (-eval(x[1]['use'])))
    output_list=[]
    a=''
    for people in sort_list:
        s_l=[people[0]]
        for i in list(people[1].values()):
            s_l.append(i)
        output_list.append(s_l )
    name = input('輸入匯出資料表檔名：')
    write_csv(name,output_list)


# 以下是回答問題的函式。
def problem1(dicts, factor_list):
    # todo
    print("problem 1:", end='')
    l = [0 for i in range(len(factor_list))]
    n = [0 for i in range(len(factor_list))]
    for key, line in dicts.items():
        l[factor_list.index(line['factor'])] += int(line['age'])
        n[factor_list.index(line['factor'])] += 1
    for i in range(len(factor_list)):
        l[i] = l[i]/n[i]
    print(factor_list[l.index(min(l))])


def problem2(dicts, med_list):
    # todo
    print("problem 2:", end='')
    l = [0 for i in range(len(med_list))]
    for key, line in dicts.items():
        l[med_list.index(line['medicine'])] += 1
    print(med_list[l.index(max(l))])


def problem3(dicts, part_list):
    # todo
    print("problem 3:", end='')
    l = [0 for i in range(len(part_list))]
    for key, line in dicts.items():
        l[part_list.index(line['part'])] += 1
    print(str(round(l[part_list.index('阿基里斯腱')]/sum(l)*100, 2))+"%")


def problem4(dicts, factor_list):
    # todo
    print("problem 4:", end='')
    l = [0 for i in range(len(factor_list))]
    n = [0 for i in range(len(factor_list))]
    for key, line in dicts.items():
        l[factor_list.index(line['factor'])] += eval(line['use'])
        n[factor_list.index(line['factor'])] += 1
    for i in range(len(factor_list)):
        l[i] = l[i]/n[i]
    print(factor_list[l.index(max(l))])


# 開檔讀檔
def open_file():
    with open('text.txt', mode='r', encoding='UTF-8') as f:
        lines = f.readlines()
    return lines

# 開檔寫檔


def write_file(s):
    with open('text.txt', mode='w', encoding='UTF-8') as f:
        f.write(s)


# 新增資料
def insert_(lists):
    name = input('請輸入名字：')
    fact = input('請輸入危險因子：')
    gender = input('請輸入性別：')
    age = input('請輸入年齡：')
    medicine = input('請輸入藥物：')
    part = input('請輸入部位：')
    use = input('請輸入使用量，格式：單一使用量*一天使用次數 或0：')
    # name,fact,gender,age,medicine,part,use='Ank','1','男','30','Ciprofloxacin','阿基里斯腱','500*2'
    if fact in lists:
        lists[name] = {'factor': fact, 'age': age, 'gender': gender,
                       'medicine': medicine, 'use': use, 'part': part}
    else:
        lists.setdefault(name, {'factor': fact, 'age': age, 'gender': gender,
                         'medicine': medicine, 'use': use, 'part': part})
    # 加入字串
    string = ""
    for k, v in lists.items():
        string += name+" "
        for index, data in v:
            if index == "part":
                string += data+"\n"
            else:
                string += data+" "
    write_file(string)
    write_csv('myfile', to_list(open_file()))
    return lists

# 讀寫csv


def read_csv():
    with open('myfile.csv', newline='', encoding='UTF-8-Sig') as csvfile:
        rows = csv.reader(csvfile)
        return list(rows)[1:]
       


def write_csv(name, lines):
    with open(name+'.csv', 'w', newline='', encoding='UTF-8-Sig') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerow(['名字','危險因子','年紀','性別','藥物','劑量','部位'])
        mywriter.writerows(lines)

# 初始化


def init_():
    init.write_file(init.initial())
    init.write_csv(to_list(init.initial()))


# 以下是主函式
while True:
    c0 = ""
    c = input("(1) query (2)select (3)insert (4)analysis (5)exit：")
    if c == '5':
        print('exit')
        break
    elif (c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == 'i') == False:
        print('invalid command')
        continue
    while (c0 == '1' or c0 == '2') == False:
        c0 = input('read from (1) csv/(2)txt：')
        if c0 == '1':
            lists = list_to_dict(read_csv())
        elif c0 == '2':
            lines = list_to_dict(to_list(open_file()))
        else:
            print('invalid command')
    factor_list, med_list, part_list = store_kind(lists)
    if c == '1':
        query(lists)
    elif c == '2':
        select(lists, factor_list, med_list, part_list)
    elif c == '3':
        lists = insert_(lists)
    elif c == '4':
        problem1(lists, factor_list)
        problem2(lists, med_list)
        problem3(lists, part_list)
        problem4(lists, factor_list)
    elif c == 'i':
        init_()
    else:
        print('invalid command')
