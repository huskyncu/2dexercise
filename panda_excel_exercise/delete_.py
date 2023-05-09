def delete_():
    import pandas as pd
    name=input('請輸入要刪除的名字')
    df = pd.read_excel('data.xlsx')
    df = df.drop(df[df['名字'] == name].index)
    df.to_excel('data.xlsx',index=False)
delete_()