def sort_():
    import pandas as pd
    from select_ import select_
    df = pd.read_excel('data.xlsx')
    choice=int(input('排序資料選擇：(1)全部資料(2)篩選資料：'))
    choice1=int(input(('第一優先序：(1)年紀(2)劑量：')))
    choice2=int(input('(1)由小到大(2)由大到小：'))

    if choice1==1:
        l=['年紀','劑量']
    else:
        l=['劑量','年紀']
    if choice2==1:
        ace = True
    else:
        ace = False

    if choice==1:
        sorted_df = df.sort_values(by=l,ascending=ace)
    else:
        sorted_df = select_().sort_values(by=l,ascending=ace)
    sorted_df