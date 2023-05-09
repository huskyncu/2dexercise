def query_():
    while True:
        name = input('請輸入名字')
        import pandas as pd
        try:
            df = pd.read_excel('data.xlsx')
            print(df[df['名字']==name])
            break
        except:
            print('None Exist')
query_()