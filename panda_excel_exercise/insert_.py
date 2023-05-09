def insert_():
    import pandas as pd  
    df = pd.read_excel('data.xlsx')  
    questions = ['名字','危險因子','年紀','性別','藥物','劑量','部位']
    data = []
    for question in questions:
        if question=='名字':
            while True:
                answer = input('請輸入'+question+":")
                try:
                    if list(df[df['名字']==answer]['名字'])[0]==answer:
                        print('已存在該人資料，請重新輸入')
                except:
                    data.append(answer)
                    break
        else:
            data.append(input(question))
    df2 = pd.DataFrame([data],columns=['名字','危險因子','年紀','性別','藥物','劑量','部位'])
    df= pd.concat([df2,df],ignore_index=True)
    df.to_excel('data.xlsx', index=False)
insert_()