import csv


def write_file(s):
    string =""
    for i in s:
        string+=i+"\n"
    with open('text.txt', mode='w', encoding='UTF-8') as f:
        f.write(string)


def to_list(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    return lines
def write_csv(lines):
    with open('myfile.csv', 'w', newline='',encoding='UTF-8-Sig') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerow(['名字','危險因子','年紀','性別','藥物','劑量','部位'])
        mywriter.writerows(lines)

def initial():
    lines = [
        'Mark 腎功能不良 56 男 Norfloxacin 400*2 阿基里斯腱',
        'Alan 腎功能不良 77 男 Ciprofloxacin 250*4 阿基里斯腱',
        'John 腎功能不良 9 男 Ciprofloxacin 500*1 阿基里斯腱',
        'Alison 併用類固醇 40 女 Pefloxacin 400*4 阿基里斯腱',
        'Ray 併用類固醇 67 男 Ofloxacin 400*4 阿基里斯腱',
        'Andy 併用類固醇 67 男 Ciprofloxacin 750*2 阿基里斯腱',
        'Anna 併用類固醇 76 女 Ciprofloxacin 500*1 阿基里斯腱',
        'Eric 併用類固醇 62 男 Ciprofloxacin 250*2 阿基里斯腱',
        'Ken 併用類固醇 67 男 Levofloxacin 500*1 阿基里斯腱', 
        'Kai 運動或活動量大 41 男 Levofloxacin 500*1 阿基里斯腱',
        'Ann 運動或活動量大 76 女 Ciprofloxacin 500*1 阿基里斯腱', 
        'Cindy 運動或活動量大 42 女 Ciprofloxacin 0 手、髕骨、阿肌里斯腱', 
        'Caris 運動或活動量大 91 男 Levofloxacin 500*1 阿基里斯腱', 
        'Akashi 運動或活動量大 37 男 Ciprofloxacin 0 髕骨', 
        'Tairo 運動或活動量大 63 男 Ciprofloxacin 800*1 股直肌',
        'Tex 運動或活動量大 58 男 Levofloxacin 750*1 臀部', 
        'Yades 糖尿病 32 男 Ciprofloxacin 500*2 內收大肌',
        'Annis 糖尿病 50 女 Ciprofloxacin 0 阿基里斯腱',
        'Isabelle 風濕性疾病 81 女 Levofloxacin 0 阿基里斯腱']
    return lines



# 開檔寫檔

