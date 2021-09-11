Odoo模組開發實戰
# 目錄
   1.增加商務邏輯
## 第一章 增加商務邏輯
   1.自動計算
   ![image](https://user-images.githubusercontent.com/90267374/132932903-4c93a9cf-521e-407c-8d62-26029ae2c5b9.png)
   <br/>
   於租金總額欄位設置 compute = _compute_price_total，store設置為True(計算自斷所依賴的數據改變時，會同時更新)
   ![image](https://user-images.githubusercontent.com/90267374/132932941-b7528978-88e6-454e-8080-d1d071d4b5c2.png)
   <br/>
   建立 _compute_price_total 方法
   ![image](https://user-images.githubusercontent.com/90267374/132933175-69e48700-7d16-42ca-a205-e363128af7fa.png)

  
   
  
