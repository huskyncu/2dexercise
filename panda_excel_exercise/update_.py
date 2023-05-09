def update_():
    import pandas as pd
    df = pd.read_excel('data.xlsx')
    ele = ['危險因子','年紀','性別','藥物','劑量','部位']
    name = input('請輸入名字:')
    while True:
        try:
            if list(df[df['名字']==name]['名字'])[0]==name:
                break
            else:
                print('請重輸')
        except:
            break
    for i in ele:
        answer = input('請輸入'+i+'，不輸即不修改:')
        if answer!="":
            df.loc[df['名字'] ==name, i] = answer
    df.to_excel('data.xlsx',index=False)
update_()