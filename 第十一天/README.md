Odoo模組開發實戰
# 目錄
 1.	Action 
    <br/>
    1.1 URL Actions (ir.actions.act_url)
    <br/>   
    
## 第一章 Action

 1. URL Actions (ir.actions.act_url)
      <br/>
      
         1.1 用途: 用於打開網頁
         1.2 屬性: 
 
|  屬性 | 內容 | 
| --------  | -------- | 
| name   | 名稱 |  
| target |  若值為 new ，則跳轉到新窗口，若值為self 則當前窗口跳轉 |
| url    | 跳轉的連接 |
     
         1.3 範例       
![image](https://user-images.githubusercontent.com/90267374/133021095-441a1591-b9ae-46f9-9594-27de58cbe697.png)
![image](https://user-images.githubusercontent.com/90267374/133040030-2a0ce9bb-b47c-4130-9855-b2c6ef3e7895.png)

| VIEW      | ACTION   | 
| --------  | -------- | 
|  ![image](https://user-images.githubusercontent.com/90267374/133020824-5bb7d0a1-48ce-4653-9e3e-775d3b663448.png) | ![image](https://user-images.githubusercontent.com/90267374/133020711-fdb70845-af8f-43c9-ab0c-c360742ca84f.png) |
