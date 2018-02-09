def priceLoad(price_file_path):
    '''
    TODO 讀取 price 資料並轉換成本專案的格式

    目前考慮應該是讀取 1MOHLC
    所以也就是格式如下

           datetime          Open    High   Low   Close   Spread
    (YYYY-mm-dd HH:MM:SS)
    --------------------    ------   -----  ----  ------  -------

    每個 Symbol 都可以有一個檔案, 例如 EURUSD.txt USDJPY.txt
    它會自動對齊 data 的時間.. 應該會用 panda ...

    price 要不要自己一個物件呢...
    覺得還是要, 因為 spread 的問題, 我希望能 custom spread

    也就是說 EURUSD 的資料可以有變動的 spread 也可以不給
    但是我們可以調用 price 自訂 spread

    調用的時候可能例如
    price.const_spread = 0.2

    然後只能設定一次, 設定第二次就會爆掉
    其實我想要的是類似 C++ const 的功能

    然後 price.ask 和 price.bid 會以當 tick 的 open 來算
    open = bid 而 ask = open + spread

    也就是在買的時候收 spread
    '''
    pass
