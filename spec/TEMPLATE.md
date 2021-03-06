# 設計規格範例 - 此處填寫規格名稱
- 標題內容請寫到提交訊息 (commit message) 的主題行 (subject line)

| 作者         | 諮詢小組 | 狀態   | 　上次更新 | 規格版本 |
| ------       | ------   | ------ | ------     | ----     |
| fatfingererr | None     | 待審   | 2018.2.6   | 0.1      |

- 請在標題後插入上方表格，並留意：
    - **作者** 以 GitHub 帳號表示，或是個人暱稱、全名
    - **諮詢小組** 若規格提交事先有和本專案的其他貢獻者諮詢過，請列於此
    - **狀態** 初次提交可空白或寫 `待審`，經過評審後狀態可能變更為 `通過` 或 `拒絕`
    - **上次更新** 以規格提交日期為準，格式為 `YYYY.m.d`
    - **規格版本** 以兩位數字表示，初次提交為 `0.1`
        - 只有狀態改變才會動到第一位主版本號，否則都是迭代增加次版本號

## 摘要

- 這個實作完畢後能做什麼？本段落務必寫成能讓協作者看懂的說明
- 摘要內容請作為提交訊息的本文

有幾件事情在寫規格之前請留意：

- 不是所有的實作都要寫成規格，請考慮實作的粒度

- 通常要為了規格特別寫文件時，需要寫入的內容須滿足下列條件：
    - 條件一：為了描述我們現在要解決的問題，這件事協作者有必要知道
    - 條件二：如果協作者廣泛接受解決方法，有利於後續彼此的開發
    - 條件三：不需要對確切的設定檔變更、或資料庫配置變更建立規格
        - 但仍然需要在原本規格中說明對未來版本的影響

- 在開始開發之前，請務必盡量完善規格
   - 在規格通過評審後，你可以自由地使用任何技巧實作
   - 然而你的規格可能經過討論後修改，最終採用的解決方案可能和你所想的不同

- API 的變更始終受到最嚴格的評審，會更動到 API 的規格請主動提供更多實作細節

關於使用本規格模板 =TEMPLATE= 請留意：

- 你的規格需要以 =markdown= 模式撰寫，如同本模板 =TEMPLATE.md=
- 請在第 79 個半形字符處換行
- 規格檔名和所在目錄，請對應可能的實作位置，若對應多個檔案，則以目錄位置為準
- 請不要刪除模板中跳過的段落，請至少補上一個 =無= 或 =None=
- 如果你打算在文檔中插入圖片，請將圖片放到 =spec/image= 目錄底下並引用
- 如果你的規格會對 API 造成影響，請在標題開頭加上 =[APIImpact]=

在你撰寫完畢 **摘要** 之後，請接著如下的段落撰寫

## 問題描述

- 詳細描述你的問題，以及對這個問題你提出的實作方面的解決方案

- 如果是對於一個全新的功能進行初步實作，也請簡要描述實作方向

### 使用情況

- 什麼樣的使用情況會造成你提的問題，請詳細將情境與使用情況做說明

- 尤其是對什麼對象造成問題，例如對開發人員、使用者等

## 解決方案

- 在這裡請仔細提出你的實作方案，盡可能地將實作方案詳細說明

- 如果這個段落非常的長，請務必在結尾做個簡要的小結

- 如果你沒有明確的實作方案，只是想對問題作詳細的描述並得到回饋：
    - 可以不完成本段落並提交，等待其他人的討論

### 其他作法

- 如果你認為還有其他可行也不差的解決方案，也可以在此說明

- 你不需要對其他可行方案做詳細的考究，可以只把想法表示出來

- 目的只是幫助大家去思考你的實作方案相對其他方法的優缺點

### 資料庫

- 使用者會在乎你的解決方法如果對資料庫造成的影響，因為資料庫中有他們的東西

- 因此在此請詳細說明你的實作方案可能對資料庫造成的變更

### API 變更

- 累了... 先把標題補完

### 安全性

- 是否有一些關鍵資料或安全性問題

### 使用者

- 對使用者的影響

### 效能

- 對效能的影響

### 佈署與測試

- 對佈署及測試的影響

### 開發人員

- 對想要在本專案上進行客製化的開發人員，或是本專案的其他貢獻者的影響

## 實作細節

### 指派

這裡列出這個規格的指派對象，可能規格你寫完發現你不是最適合開發這個功能的人

#### 主要指派

這裡請列出主要指派的對象，通常是一個人並請標註他的 GitHub ID 例如

| Ricky | [fatfingererr](https://github.com/fatfingererr) |

#### 其他貢獻者

這裡你可以列出你認為這個規格有誰能幫主要指派對象的忙，在評審後將會被通知

### 任務列表

這裡請 **條列式** 列出完成這個規格需要的相關任務

具有先後順序的任務請列於一個群組任務下，以方便大家平行進行，例如：

- [ ] 任務 1
- [ ] 任務 2
- [ ] 任務 3
    - [ ] 群組任務 1
    - [ ] 群組任務 2
- [ ] 任務 4


## 依賴

這裡請詳細列出完成這個規格內容的實作，可能依賴的第三方套件、外部工具

## 測試

- 這裡請詳細列出對於實作內容你打算如何規劃完整的測試內容

- 這裡的測試除了單元測試外，更重要是對整合測試的描述

- 一樣列點，請分以下主題分別列出

### 單元測試


### 整合測試


## 文件

- 這裡請說明這些功能實做完了之後，目前現有的開發文件有哪些地方需要更改

- 以及方法完成之後，你會有哪些文件需要撰寫，也請在此列點


## 參考資料

- 對於你撰寫這份規格中所使用到的專業或關鍵資訊，請列出引用來源

- 除此之外，本規格在撰寫完成之前，曾經在哪裡討論過（例如 GitHub Issue, mailing list ）也請列出

- 或是本專案實作有參考理論學術資訊，也請列出

- 其他你覺得會幫助大家理解本規格的參考資料

## 修訂紀錄

這裡列出規格的修訂紀錄，例如對於規格中的某些設計做了修改

參考格式如下

|     日期 | 修改簡要描述 |
| 2018.2.5 | 初稿         |
| 2018.3.1 | 測試部分添加更詳細的單元測試規劃 |
