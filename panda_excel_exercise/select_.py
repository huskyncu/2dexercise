def select_():
    import pandas as pd
    df= pd.read_excel('data.xlsx')
    
    for i in set(df['危險因子']):
      print(i," ",end='')
    print()
    factor = input('請輸入危險因子:')
    if factor=='':
        mask_factor=1
    else:
        mask_factor=(df['危險因子']==factor)
    min_age = int(input('請輸入年齡下限：'))
    max_age = int(input('請輸入年齡上限：'))
    for i in set(df['藥物']):
        print(i," ",end='')
    print()
    medcine = input('請輸入藥物：')
    if factor=='':
        mask_med=1
    else:
        mask_med=(df['藥物']==medcine)
    gender = input('請輸入性別：')
    min_use = int(input('請輸入使用劑量下限：'))
    max_use = int(input('請輸入使用劑量上限：'))
    for i in set(df['部位']):
            print(i," ",end='')
    print()
    part = input('請輸入部位：')
    if factor=='':
        mask_part=1
    else:
        mask_part=(df['部位']==part)
    mask = ( (mask_factor) & 
        (df['年紀']>=min_age) &
        (df['年紀']<=max_age) &
        (mask_part) &
        (df['性別']==gender) &
        (df['劑量']<=max_use) &
        (mask_med)
        )
    return df[mask]