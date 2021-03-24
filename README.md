# YahooAutoBuy(Yahoo商城下單程式)
#### 前言
此程式透過Python selenium下單購買商品，目前功能單一並有部分侷限，使用前請閱讀本說明。

#### Python版本
  - [x] 3.7.3

#### 操作說明
1. 編輯「Config.ini」。
```config
[Section_Info]
loginEmail = yahoo帳號
password = yahoo密碼
commodityUrl = yahoo購買商品頁面https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid=8378928
buyCount = 購買數量
```
2. 預先至Yahoo商城設定「快速結帳」，預先調整好預設值。
3. 執行「YahooAutoBuy.exe」。

#### 注意事項
* chromedriver.exe需與YahooAutoBuy.exe位於同一目錄。
* 若執行程式出現`chrome version must be >= xx.x.xxxx.x
 (Driver info: chromedriver=x.xx.xxxxxx`之類錯誤訊息，請至[ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)下載符合本機Chrome版本或最新版本chromedriver，並覆蓋既有exe檔案。
* 本程式需事先設定好結帳畫面數值(透過Yahoo商城快速結帳功能)，若未完成前述設定，程式將於執行到結帳畫面時結束程式，轉為手動完成後續步驟。
* Config.ini中buyCount(購買數量)，會受限於商品本身限制，部分商品有購買上/下限，例如某商品最多購買3件，此時若設定6，依然只會購買3件。此外此功能目前是基於系統預設購買數量向上增加數量，因此若基數為2，您設定buyCount=3時，最終購買數量將會是4件(程式是假定基數為1，尚未撰寫檢查Code)。
* 本程式選購商品後，會直接利用購物車選擇確認購買，故使用程式前請先清空購物車。

#### 後記
本程式依舊有許多尚未完善的部分，僅具備基本訂購的功能，若是僅需要掛著程式等待自動訂購商品且無特殊需求者，此程式您可納入參考。不符合以上描述者，目前仍建議使用官方網頁進行訂購或Fork專案進行程式修改。