# 券商伺服器 server 規格設計

| 作者         | 諮詢小組 | 狀態   | 　上次更新 | 規格版本 |
| ------       | ------   | ------ | ------     | ----     |
| fatfingererr | None     | 待審   | 2018.2.6   | 0.1      |

## 摘要

在本專案中建立一個 server 物件，透過 server 物件來管理各種 order

## 問題描述

無

### 使用情況

無

## 解決方案

Python 中的 OOP 來實現

### 其他做法

無

### 資料庫

有相關的設置，可能也是先寫死在物件初始化的過程中

### API 變更

無

### 安全性

無

### 使用者

無

### 效能

無

### 佈署與測試

無

### 開發人員

無

## 實作細節

- [ ] `__init__` 物件初始化
    - [ ] 設定基礎屬性，應該會包含：
        -

- 快速掛單函數
    - 停損/停利 可能為缺省變數
    - [ ] `open_buy` 開多單
    - [ ] `open_buy_stop` 開觸價多單
    - [ ] `open_buy_limit` 開限價空單
    - [ ] `open_sell` 開空單
    - [ ] `open_sell_stop` 開觸價空單
    - [ ] `open_sell_limit` 開限價空單


- 基礎操作函數
   - [ ] `order_send` 掛單函數
   - [ ] `order_close` 關閉開倉
   - [ ] `order_delete` 刪除 pending order
   - [ ] `order_modfiy` 修正 order 的 sl, tp, pending entry price


- 內部私有函數
   - [ ] `_chk_valid` 確認 send order 是正確的 (sl/tp不能為負)
   - [ ] `_open_to_hist` 部位關閉後移到歷史 order
   - [ ] `_open_shift` 當部位變更後 order_index 要 shift

- 事件驅動函數
   - [ ] `chk_event_entry` 確認是否有 pending order 為 opened
   - [ ] `chk_event_close` 確認是否有部位碰到 sl tp 自動 closed

- [ ] 基本查詢函數
    - [ ] `order_total` 查詢現在有多少 order
    - [ ] `order_open_time` 查詢 index 指定的 order 的 open 時間
    - [ ] `order_size` 查詢 index 指定 order 的 size
    - [ ] `order_magic_number` 查詢 order 的 magic number
    - [ ] `order_open_price` 查詢 order 的 open price
    - [ ] `order_profit` 查詢 order 現在的 profit
    - [ ] `order_stop_loss` 查詢 order 現在的 stop loss
    - [ ] `order_take_profit` 查詢 order 現在的 take profit
    - [ ] `hist_order_total` 查詢歷史 order 有多少
    - [ ] `hist_order_open_time` 查詢 index 指定的歷史 order 的 open 時間
    - [ ] `hist_order_close_time` 查詢 index 指定的歷史 order 的 close 時間
    - [ ] `hist_order_size` 查詢 index 指定的歷史 order 的 size
    - [ ] `hist_order_magic_number` 查詢 order 的歷史 magic number
    - [ ] `hist_order_open_price` 查詢 order 的 open price
    - [ ] `hist_order_close_price` 查詢 order 的 close price
    - [ ] `hist_order_profit` 查詢 order 現在的 profit
    - [ ] `hist_order_stop_loss` 查詢 order 現在的 stop loss
    - [ ] `hist_order_take_profit` 查詢 order 現在的 take profit


## 依賴

- 暫定應該是 =numpy= 的依賴，版本還沒確定

## 測試

無（還沒想好怎麼測試，會用 TDD 摸索一下）

### 單元測試

無

### 整合測試

無

## 文件

無（再補上寫文件的規劃）

### 參考資料

無

## 修訂紀錄

|     日期 | 修訂簡要描述       |
|----------|--------------------|
| 2017.2.6 | 初稿，自己審先開發 |
