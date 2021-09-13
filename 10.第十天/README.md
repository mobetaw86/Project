Odoo模組開發實戰
# 目錄
 1.	Action 
    <br/>
    1.1 Window Actions (ir.actions.act_window）
    <br/>
    1.2 URL Actions (ir.actions.act_url)
    <br/>
    1.3 Server Actions (ir.actions.server)
    <br/>
    1.4 Report Actions (ir.actions.report)
    <br/>
    1.5 Client Actions (ir.actions.client)
    <br/>
    1.6 Automated Actions (ir.cron)
    
## 第一章 Action
<br/>
1.Window Actions (ir.actions.act_window）
      <br/>   
      
        1.1 用途: 最常用的action類型，用於打開模型的各種視圖    
        1.2 屬性: 
 
|  屬性 | 內容 | 
| --------  | -------- | 
| res_model | 數據model |  
| view_type | 視圖類型如：form,tree,gragh...，type參數列表的第一個會被默認用來展示 |
| view_id   | 指定特定的視圖|
     
        1.3 範例
![image](https://user-images.githubusercontent.com/90267374/133017141-03b48765-ae6f-479a-a596-16a18692d332.png)
      
| VIEW      | ACTION   | 
| --------  | -------- | 
|  ![image](https://user-images.githubusercontent.com/90267374/133016606-58fd20a1-baf7-4b38-aed4-d27867b33aeb.png) |  ![image](https://user-images.githubusercontent.com/90267374/133016564-47b5b2d4-92c1-4079-9116-d6593b136593.png) |

 2. URL Actions (ir.actions.act_url)
      <br/>
      
         2.1 用途: 用於打開網頁
         2.2 屬性: 
 
|  屬性 | 內容 | 
| --------  | -------- | 
| name   | 名稱 |  
| target |  若值為 new ，則跳轉到新窗口，若值為self 則當前窗口跳轉 |
| url    | 跳轉的連接 |
     
         2.3 範例       
![image](https://user-images.githubusercontent.com/90267374/133021095-441a1591-b9ae-46f9-9594-27de58cbe697.png)

| VIEW      | ACTION   | 
| --------  | -------- | 
|  ![image](https://user-images.githubusercontent.com/90267374/133020824-5bb7d0a1-48ce-4653-9e3e-775d3b663448.png) | ![image](https://user-images.githubusercontent.com/90267374/133020711-fdb70845-af8f-43c9-ab0c-c360742ca84f.png) |
