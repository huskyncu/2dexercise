# Panda Project
###### tags: `合太醬`

## 題目：
病患資料查詢器


## 說明：
請你根據以下表格與所學進行資料分析與整理。
* 原始資料來源： 
![](https://i.imgur.com/s7Hekzv.jpg)

* 注意事項：
最後你的程式能夠從excel讀取檔案。
測資最前面一定會依序輸入以下的資料(不用手動輸入)
測資每個字串間隔只會空一格
每個危險因子隔一個空格後會有一個數字，代表有幾個case具備這個危險因子，接著依序輸入資料。(然後最後透過指令break掉)
為方便處理，我已經將劑量算好了，方便字串處理。
    ```
    Mark 腎功能不良 56 男 Norfloxacin 800 阿基里斯腱
    Alan 腎功能不良 77 男 Ciprofloxacin 1000 阿基里斯腱
    John 腎功能不良 9 男 Ciprofloxacin 500 阿基里斯腱
    Alison 併用類固醇 40 女 Pefloxacin 1600 阿基里斯腱
    Ray 併用類固醇 67 男 Ofloxacin 1600 阿基里斯腱 
    Andy 併用類固醇 67 男 Ciprofloxacin 1500 阿基里斯腱
    Anna 併用類固醇 76 女 Ciprofloxacin 500 阿基里斯腱
    Eric 併用類固醇 62 男 Ciprofloxacin 500 阿基里斯腱
    Ken 併用類固醇 67 男 Levofloxacin 500 阿基里斯腱
    Kai 運動或活動量大 41 男 Levofloxacin 500 阿基里斯腱
    Ann 運動或活動量大 76 女 Ciprofloxacin 500 阿基里斯腱
    Cindy 運動或活動量大 42 女 Ciprofloxacin 0 手、髕骨、阿肌里斯腱
    Caris 運動或活動量大 91 男 Levofloxacin 500 阿肌里斯腱
    Akashi 運動或活動量大 37 男 Ciprofloxacin 0 髕骨
    Tairo 運動或活動量大 63 男 Ciprofloxacin 800 股直肌
    Tex 運動或活動量大 58 男 Levofloxacin 750 臀部
    Yades 糖尿病 32 男 Ciprofloxacin 1000 內收大肌
    Annis 糖尿病 50 女 Ciprofloxacin 0 阿基里斯腱
    Isabelle 風濕性疾病 81 女 Levofloxacin 0 阿基里斯腱
    ```
* 你可以透過各種方式，儲存資料，但是必須讓程式能夠無限執行。

## Part0: 顯示DataFrame 15%
擷取資料後，顯示整個資料的DataFrame

## part1: 程式實踐功能：查詢功能 15%
* 查詢名字後，需印出患者資料。
* 以anna來說，那就需印出Anna的DataFrame：
![](https://hackmd.io/_uploads/B13medmE3.png)


## part2: 程式實踐功能：篩選功能 30%
* 你的程式能夠根據：
  * 輸入：特定危險因子
  * 輸入：篩選年齡下限
  * 輸入：篩選年齡上限
  * 輸入：特定藥物
  * 輸入：特定性別
  * 輸入：特定劑量下限
  * 輸入：特定劑量上限
  * 輸入：特定部位

去篩選出你想要的資料用dataframe顯示出來

範例輸出：
    ![](https://hackmd.io/_uploads/ryUsxYXNn.png)


## part3：程式實踐功能：排序功能 20%
請根據前面學到的排序，讓程式可根據以下優先順序排序：
* 請實作排序功能，讓使用者選擇要排序的資料
  *   全部資料
  *   篩選資料
* 依據下列去排序。
  *   年紀
  *   劑量
* 再讓使用者選擇由小到大還由大到小。
## part4: 程式實踐功能：分析功能 20%  
* 可根據你的篩選功能，以程式輸出回答以下問題。
1. 請問哪個危險因子的平均年齡層最低？
2. 請問哪個藥物使用的病患最多？
3. 請問部位的部分，阿基里斯腱佔全部病患多少比例？
4. 想請問哪個危險因子的平均使用劑量最高？

<!-- 程式一開始你可以在input() 的()裡面提示使用者應該輸入哪些指令
比如：
```python=
while True:
    try:
        command = input("請輸入指令,(1)查詢(2)篩選(3)分析(4)結束程式")
        if command=='1':
            name = input("請輸入名字:")
            #to do ....
        .....

    except:
        break
``` -->




## 模板下載區
請嘗試用panda DataFrame完成上述的程式。
在
請去[答案區](https://github.com/huskyncu/Panda-Project/blob/main/Panda_Project.ipynb)下載並上傳到colab上實作



為了減少麻煩，程式能顯示出來就好，不用處理邊界測資。
<!-- ## 函式化(單元五)
同樣也是將以前的那些功能都改成函式來寫。
把所有功能結合在一起。
程式要求：
需有功能選擇，並設計一個指令是退出程式。
本階段請在[colab](https://colab.research.google.com/drive/1rqDxHuhhcJzVT74N4iC2vw8MljLnPYgX?usp=sharing)完成。
舉例來說你可以寫成：
```python=
# 一維陣列轉換成二維陣列
def to_list():
    #todo
# 二維陣列轉換成字典  
def list_to_dict():
    #todo
# 查詢病患資料
def query():
    #todo
# 篩選資料，根據篩選篩出資料
def select():
    # todo
# 排序資料，並印出資料
def sort_():
    # todo

# 以下是回答問題的函式。
def problem1():
    # todo

def problem2():
    # todo
    
def problem3():
    # todo

def problem4():
    # todo
    
# 以下是主函式
while True:
    choice=input()
    if choice=='???':
        problem1()
        problem2()
        problem3()
        problem4()
    elif choice == '???':
        # todo
    #todo

```

## 例外處理(單元六)
要能解決邊界測資與例外狀況。
避免非法指令輸入。

[colab](https://colab.research.google.com/drive/1GaVF1EKzJyHdELKZPa2sw0Tg9-iKkJLN?usp=sharing) -->
    
<!-- ## txt檔案化(單元七)

本階段請在vscode上處理。
請將單元五你做完的字典函式化的程式拿來這裡使用
並加兩個函式功能。
原本給你的line是一維陣列，現在請你改成用檔案處理的方式，把資料從txt的內容read進python檔並轉換成一維陣列。
接著要請你若資料有更動的話，需寫入並更新。

```python=
def insert_():
    # 這個函式是用來新增資料的。
    # 要使用def write_file將新的lists寫進txt裡
def open_flie():
    # 請使用這個函式來開啟檔案。
    # 並把文字轉換成一維陣列，並回傳。
def write_file():
    # 請使用這個函式來寫入檔案。
lines=open_file()
``` -->

<!-- ## csv/excel檔案化(單元八)
本階段請在vscode上處理。
請將單元五你做完的字典函式化的程式拿來這裡使用
並加兩個函式功能。
原本給你的line是一維陣列，現在請你改成用檔案處理的方式，把資料從csv/excel的內容read進python檔並轉換成一維陣列。
若資料有更新，需要連csv/excel也一起更新。

然後篩選過後的資料表也要印出。

需在前面一開始先問說要讀取txt還是csv/excel？
```python=
while True:
    c0=""
    while (c0=='1' or c0=='2') == False:
        # to do 
        c0 = input('read from (1) csv/(2)txt：')
    #todo
```

以下是函式
```python=
def read_csv():
    with open('myfile.csv', newline='',encoding='UTF-8-Sig') as csvfile:
        rows = csv.reader(csvfile)
        return list(rows)
        
def to_csv(lines):
    print(lines)
    with open('myfile.csv', 'w', newline='',encoding='UTF-8-Sig') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(lines)
```

## 模組化(單元五)
請你創立一些py檔，分別將def 移過去
* main_.py
    * 原本的while True迴圈
* table_.py
    * def to_list
    * def list_to_dict
    * def store_kind
* use_txt.py
    * def write_file
    * def open_file
* use_csv.py
    * def wrtie_csv
    * def read_csv
* insert_.py
    * def insert
* select_.py
    * def select
* query_.py
    * def query
* sort_.py
    * def sort_
* analysis_.py
    * def problem1
    * def problem2
    * def problem3
    * def problem4 -->