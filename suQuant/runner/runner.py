# Copyright 2018 sukki-quant. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import datetime

class Runner(object):
    """
    TODO 執行訓練的物件

    基本上目的是把 Runner 和 Server 分開來，也就是 Runner 在最外層
    是對整個 RL 訓練 + 交易回測的一個控制面板
    目的是讓整個 Trading Logic 能盡量不依賴執行環境
    未來如果要把 Trading Logic 移植到其他交易平台也比較沒有問題
    """

    def __init__(self):
        """
        TODO 初始化

        這邊的初始化主要是仿照我們有一個回測或是訓練的控制面板
        透過這個面板能對交易回測或 RL 做一些基礎設定

        TODO 未來可以透過讀取 config 來設置好這些東西

        """
        self.backward_start = []                           # 回測開始時間
        self.backward_end   = []                           # 回測結束時間
        self.forward_start  = []                           # 前測開始時間，可以從回測結束時間往後一個算
        self.forward_end    = []                           # 前測結束時間
        # self.execution    = 1MOHLC                       # 回測 TICK 尺度，先預設 1MOHLC
        self.deposit        = 100000                       # 回測總資金
        self.time_frame     = 0 #M15                          # 回測尺度
        self.market         = ["EURUSD","EURJPY","EURGBP"] # 回測需要使用到的市場資料
        self.server         = 0 #server                       # Server 物件，主要模擬基本的券商伺服器
        self.trader         = 0 #trader                       # Trader 物件，主要模擬高階抽象的策略邏輯，包含 RL Algo + Report

    def loadData(self,start,end):
        pass

    def run_backward(self):
        """
        TODO 執行回測

        其實回測和前測邏輯基本一樣
        只是回測會有訓練 + 最佳化問題，前測就是單純的測試

        """
        pass
        # TODO 準備回測資料
        # self.prepare(backwrad_start,backward_end)

        # TODO 執行回測初始化
        # self.backward_init()

        # TODO 開始對每個 TICK 進行回測
        #for tick in backward_period:
        #
        #    TODO 準備該 TICK 的資料
        #    這個目的是為了把價格和系統做隔離
        #    每個 TICK 都只能從 Runner 取得該 TICK 資料
        #    self.price_move()
        #
        #    TODO 執行回測中在該 TICK 要做的事情
        #    self.backward_tick()

        # TODO 結束回測（存檔案或是紀錄資料）
        # self.backward_deinit()

    def run_forward(self):
        """
        TODO 執行前測

        基本上和執行回測應該是差不多，只是不需要訓練或最佳化

        """
        pass
        # TODO 準備前測資料
        # self.prepare(forward_start,forward_end)

        # 前測初始化
        # self.forward_init(forward_start)

        # TODO 前測每個 TICK
        # for tick in forward_period:
        #
        #    TODO 價格移動
        #    self.price_move()
        #
        #    TODO 前測每個 TICK
        #    self.forward_tick()
        # TODO 前測結束
        #self.forward_deinit()

    def prepare(self,start,end):
        """
        TODO 設定好 runner 此次 run 的資料

        由於 market 資料可能沒有對齊，所以這邊就要給他對齊
        同時要準備好 price_move 的時候設定好該 tick 的 ask, bid

        """
        pass


    def price_move(tick):
        """
        TODO 價格移動

        HACK 當價格移動的時候，就把最新的價格直接複製一份到各 class 中
        我不知道 python 能不能做 lexical binding....
        先這樣吧！

        """
        pass
        # TODO 取得現在價格
        # now_price = get_price(tick)

        # TODO 把價格 pass 給 server
        # server.set_price(now_price)

        # TODO 把價格 pass 給 trader
        # trader.set_price(now_price)

        # TODO 把價格 pass 給 report
        # report.set_price(now_price)

        # THINK 或許可以不用這樣 pass....

    def on_init(self):
        """
        TODO 初始化

        還沒想 backward_init 和 forward_init

        """

    def on_tick(self):
        """
        TODO 每個 TICK 要做的事情

        還沒想 backward_tick 以及 forward_tick 要做的事情
        先統一當 on_tick 好了

        """
        pass

        # TODO Sever 要確認新的 TICK 資料對 server 的影響
        # 例如新的資料近來碰到 Take Profit 或是 Stop Loss
        # server.new_tick_check();

        # TODO Report 要每個月進行資料紀錄
        # report.log_monthly();

        # TODO 如果進入新的 BAR ( 畢竟策略還是 RUN 在一個時間尺度上面 )
        # if new_open_bar :
        #
        #     TODO 執行該 BAR 要做的事情
        #     on_bar();

        # TODO Sever 開始做各種確認
        # THINK 可能會包在一個函數裡面，不暴露在 runner 中

        # TODO Sever 確認是否該 BAR 新的掛單有立即成交
        # server.check_entry()

        # THINK 以下可能整併到 check_entry 裡面
        # ----------------------------------------------------------------------
        # TODO Sever 確認是否有 add position 伴隨主單掛單
        # server.check_add_position()

        # TODO Sever 確認是否有 parital close 伴隨主單掛單
        # server.check_partial_close()


        # THINK 以下可能整併到 check_modfiy 裡面
        # ----------------------------------------------------------------------
        # TODO Sever 確認是否有 trailing stop 被觸發需要 modify order 的 SL
        # server.traling_stop_update()

        # TODO Sever 確認是否有 breakeven stop 被觸發需要 modify order 的 SL
        # server.breakeven_stop_update()


        # TODO Sever 確認是否有 Order Close 因為碰到 SL/TP 而 Close
        # pending order 不需要在 server side 去 check 不會有這問題
        # server.check_close_by_sltp()

        # TODO 以下可能整併到 check_reentry 裡面
        # ----------------------------------------------------------------------

        # TODO 確認是否有 re_entry
        # server.market_re_entry()

        # TODO 以下可能整併到 check_close 裡面
        # ----------------------------------------------------------------------
        # TODO 先更新還存在的 Order 的 Profit
        # server.update_profit()

        # TODO 確認是否有 Order 碰到 Take Profit
        # server.check_takeprofit()

        # TODO 確認是否有 Order 碰到 Stop Loss
        # server.check_stoploss()

        # TODO 以下可能整併到 check_delete 裡面
        # 因為伴隨主單消失，可能 pending 也需要刪除
        # ----------------------------------------------------------------------
        # TODO 確認 add position 是否要 exit
        # server.check_add_position_exit()

        # TODO 確認 partial close 是否要 exit
        # server.check_partial_close_exit()

        # TODO 最終全部都弄完之後，就要更新 log 的資訊
        # report.update

    def on_bar(self):
        """

        執行在每個 BAR 也就是 Trder 可以思考的時候
        基本上 RL 也是執行在這個 level

        """
        pass
        # TODO report 可能每個 bar 需要 update
        # report.new_bar_update()

        # ======================================================================
        # TODO RL 基本上包含在這裡，Traing 和 get_signal 都在這邊
        # get signal 基本上就是 get action
        trader.train_and_get_signal()
        # ======================================================================

        # TODO report 的 signal 要更新
        # report.signal_update()

        # TODO trader 根據 signal 決定是否要 entry
        # trader.entry_check()

        # TODO report 更新 entry 資訊
        # report.entry_bar_update()

        # TODO trader 根據 signal 決定是否要 exit
        # trader.exit_check()

        # TODO report 根據 exit 的資訊
        # report.exit_bar_update()

        # TODO 因為 exit 之後可能 reentry 所以這邊在決定是否要 reentry
        # 例如反向單, 多單變空單就要 long exit + short entry
        # trader.re_entry_check()

        # TODO 再一次更新 report 的資訊
        # report.entry_bar_update()

        # TODO 每個 bar 的所有事情都做完，對整個 bar 最後資訊做更新
        # report.every_bar_update()

        # TODO 每個 bar 裡面可能有主動關掉(exit)的交易
        # 對主動關掉的交易進行紀錄，這和 SL/TP 不同
        # report.closed_trade_update();

    def on_deinit(self):
        """
        TODO 反初始化

        deinit 基本上應該會分 backward_deinit 和 forward_deinit
        預計就是把 report 紀錄的東西 log 出來

        """
        pass
