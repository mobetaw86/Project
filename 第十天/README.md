Odoo模組開發實戰
# 目錄
 1.	Action 
    <br/>
    1.1 Window Actions (ir.actions.act_window）
    <br/>   
    
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


