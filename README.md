Odoo模組開發實戰
# 目錄
 1.	開發元件與環境介紹
    1.	Python 3.7
    2.	PostgreSQL 10 
    3.	Odoo 13
    4.	Pycharm
 2.	開發環境建置
    1.	安裝 Python 3.7
    2.	安裝 PostgreSQL 10
    3.	安裝 Odoo
    4.	安裝 wkhtmltopdf
    5.	安裝 Pycharm community
    6.	安裝Microsoft visual studio C++ 14.0
    7.	設定odoo專用的postgreSQL的登入帳號
    8.	odoo伺服器細部設定
 
 3. 模組開發實戰
    1.	情境模擬
    2.	系統規劃
    3.	模組架構建立
    4.	基礎欄位建構
    5.	關聯式欄位建構
    6.	視圖
    7.	動作
    8.	權限
    9.	wizard
    10.	繼承
    11.	報表

## 第一章 開發環境與元件介紹
1.Python
    ●	簡單、應用廣泛、能快速上手      
    <br/>
    ● Odoo的核心開發語言
    <br/>
    ● 這裡使用3.7，可使用3.6+的版本 
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132378090-e3dbfa23-8aea-4676-9cb6-f9e2156c0760.png) 
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426077-eaf595a3-df2b-4b49-a257-7c3aee82adba.png)

    
2 PostgreSQL
    ●	初始版本： 1996年7月8日
    <br/>
    ●	免費、開源
    <br/>
    ●	關聯式資料庫
    <br/>
    ●	Odoo 的御用資料庫 (此次使用官網 10.14 版本，可使用10+之版本)
    <br/>
    ●	知名客戶： Skype、美國勞工部
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426179-ecd5676e-4a62-4356-9a9a-5796ccb3f0ee.png)
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426244-031b78ba-b483-48b6-a801-c4c491389893.png)

 
3 Odoo
    ●	Odoo（先前曾名為OpenERP，更早之前則為TinyERP）
    <br/>
    ●	是一套企業資源規劃（ERP）及客戶關係管理（CRM）系統。
    <br/>
    ●	以Python語言開發，資料庫採用開源的PostgreSQL。
    <br/>
    ●	免費、開源ERP系統
    <br/>
    ●	功能模組化
     <br/>
    ●	針對存在模組開發額外功能強大
    ●	MVC架構
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426322-355c1607-67e3-49ee-91d4-b295d6907eef.png)

4 PyCharm
    ●	免費(Community)
    <br/>
    ●	多平台安裝簡易
    <br/>
    ●	優點: 整合版控、Terminal、Python Console...等(若為Pro版也包含資料庫連線工具，直接對應程式碼使用之SQL檢查)
    <br/>
    ●	缺點: 消耗記憶體較高，對於大量變更檔案時會很慢，專業版需要收費
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426356-6a4cff07-1e81-4ea3-9b3e-17f5fcb4ea82.png) 

 
## 第二章 開發環境建置(Windows 10)
Python 3.7.X
    ●	https://www.python.org/ 
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426467-749bb1f1-eee0-442c-988f-bf36cbf8b4d5.png)

2-1 安裝
    ●	點選進3.7.X後，往下拉到最底找到Files，
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426549-00ff245d-a2d1-4a7b-8a0b-3997774523ba.png)

2-1 安裝 Python 3.7
    ●	記得將python 加到環境變數(記得使用管理員權限安裝)
    <br/>
    ●	因自動安裝會預設裝到奇怪的地方，因此選擇自訂安裝
    <br/>
    ●	若Python為64位元版本，在一開始的畫面會有64-bit的字樣
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426628-3cf4c4e3-26b5-4d23-b8eb-0612b419fe66.png)
    <br/>
    ●	請把路徑放到C:/底下，資料夾名稱皆可(e.g py37, Python37 … etc.)
    <br/>
    ●	上方選項可預設選取，也可全選
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426667-eb9de1ad-67a9-4c37-abc4-598d621c47de.png)
    <br/>
    ●	https://www.postgresql.org/download/
     <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132426957-580aca85-9cbe-4a2b-a6cb-9ee8c333f729.png) 


2-2 PostgreSQL 10
    ●	請右鍵點選使用系統管理員執行
    ![image](https://user-images.githubusercontent.com/90267374/132427073-46cec859-0ec1-4d35-9199-7ca8e56b09f7.png)
    ![image](https://user-images.githubusercontent.com/90267374/132427084-5640f10b-451f-4bbe-bd4d-4e439438b4cf.png)
    ![image](https://user-images.githubusercontent.com/90267374/132427104-610ccf24-9cae-4854-9c62-a7931259c91b.png)
    ![image](https://user-images.githubusercontent.com/90267374/132427119-ede4ee89-4913-41fb-a5d7-4d960f69e7f3.png)
 
3 Odoo
    在C:/ 建立odoo資料夾，並將剛剛下載的odoo壓縮檔解壓至C:/odoo/ 
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427152-91274c96-899b-4366-86a0-c8f22c3face0.png)        
    <br/>
    ●	https://wkhtmltopdf.org/downloads.html    
    在C:/ 建立odoo資料夾，並將剛剛下載的odoo壓縮檔解壓至C:/odoo/
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427203-d2fd90d5-f8f4-409b-b6c4-0ddd56b86d90.png)    
    <br/>
    ●	https://wkhtmltopdf.org/downloads.html
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427251-abc7c62c-9c0f-42dc-978a-3bfc9434a2aa.png)
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427285-0df4e88c-bb66-492f-beff-ed107ec7a0cb.png)    
    <br/>
    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427311-b0c2182e-c20b-4b32-b46b-a38c3896c86e.png)
    <br/>
    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427339-c2e17b6b-085f-44e3-8c1b-507068819f30.png)
    <br/>
    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427353-3dace1b7-bb94-4136-810b-b252a6ab8b12.png)
    <br/>
 PyCharm
    <br/>
    ●	https://www.jetbrains.com/toolbox-app/download 
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427412-1c290372-2b82-4312-8a3f-231d9a9f1f28.png)
    <br/>
    ●	https://www.jetbrains.com/toolbox-app/download
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427432-b70185a2-f004-4f50-8e8a-e51492d17a85.png)    
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427462-8080fa3c-0f0c-434c-85a4-7ded3828b528.png)
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427481-015af1a1-1887-4820-9bb1-b0ae3e6b9c37.png)
 
6 安裝Microsoft visual studio C++ 14.0
    ●	https://visualstudio.microsoft.com/zh-hant/downloads/
    <br/>
    下載後並執行
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427502-4a4f4051-e732-46d0-bdc0-33e407ee95ec.png)
    <br/>
    6 安裝Microsoft visual studio C++ 14.0
    ● 往下拉找到Desktop & Mobile 分類裡面有個Desktop development with C++打勾，接下來按下 install後等待安裝完成
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427537-6d26ca3a-ac6d-4d3e-b750-f56e3e0281d6.png)
    <br/>
    7 設定odoo專用的postgreSQL的登入帳號
    <br/>
    ● 在開始直接搜尋pgAdmin4，進去後輸入剛剛設定的密碼postgres
    <br/>
      點選PostgreSQL10後會再要求輸入一次密碼
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427567-d15ec86b-ad3f-4411-bced-50c4ab5d858b.png)
    <br/>
    7 設定odoo專用的postgreSQL的登入帳號
    ●	右鍵點擊Login/Group Roles -> create -> Login/Group Roles
      ![image](https://user-images.githubusercontent.com/90267374/132427707-43133b25-753c-462d-aaa9-60826ee8b961.png)

請重新開機讓Python跟wkhtmltopdf的環境變數載入
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427730-2423a8fe-26a5-4996-9ec9-a4bd00a101ee.png)
    <br/>
重新開機後使用cmd執行下面指令，
觀察是否有被正確抓到程式 python --version wkhtmltopdf -V

 Odoo伺服器細部設定
     ●	執行PyCharm，開啟C:/odoo
     <br/>
     ●	Pycharm將會抓取python程式位置，並且對開啟資料夾裡的所有檔案進行索引，這會花費一點時間要稍微等待一下
     <br/>
     ![image](https://user-images.githubusercontent.com/90267374/132427820-688c1e9b-f599-441f-92a0-f8309cedd3f0.png)
     <br/>
     ●	建立 python 虛擬環境
     ![image](https://user-images.githubusercontent.com/90267374/132427846-189eceb9-9801-4752-be58-7e4462091983.png)
     <br/>
     ●	將路徑設定在C:\odoo\venv_odoo13(無此名稱會建立一個資料夾) 注意，這一定得是空資料夾才可建立環境
     ●	只勾選 Make available to all projects (讓所有專案可使用此環境) 不勾選 Inherit global site-packages 
     (繼承python主要已擁有套件[此設定會把所有套件複製一份])
     <br/>
     ![image](https://user-images.githubusercontent.com/90267374/132427878-95948a6e-46c5-4bd4-aa38-   e0516133b86c.png) 
  ●	建立一個執行環境，名稱odoo13(自己喜歡都行) script path選擇C:\odoo\odoo-13.0\odoo-bin
      Parameters 輸入 -c odoo.conf
      <br/>
      ![image](https://user-images.githubusercontent.com/90267374/132427935-0663b81c-e3fe-4393-96d8-a3ee8b43d0ef.png)
      <br/>
  ●	畫面下方開啟terminal，安裝odoo所需套件輸入並執行下面指令
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132427991-26dd53bf-807d-433f-8c79-5832ec4fd4b2.png)
    <br/>
  ●	增加自訂模組資料夾
    對odoo跟目錄右鍵 -> new -> Directory，輸入addons (也可以取自己喜歡的名稱)
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132428035-310db03d-a897-442f-bbc7-16a415737409.png)
    <br/>
  ●	增加odoo伺服器設定，檔案命名為odoo.conf
    <br/>
    ![image](https://user-images.githubusercontent.com/90267374/132428064-6fa23606-4bc7-44d8-baa9-cb0c464aac83.png)
    <br/>
  ●	輸入以下內容
      [options] 
      db_host=localhost 
      db_port=5432 
      db_user=odoo 
      db_password=odoo
      addons_path=addons, odoo/addons, ../addons xmlrpc=8069
      <br/>
      ![image](https://user-images.githubusercontent.com/90267374/132428108-3ffedc20-9e13-4ddf-8c29-f93eab6a3a6d.png)
      <br/>
  ●	執行odoo伺服器
  ●	到瀏覽器的網址列輸入 127.0.0.1:8069，能看到Odoo的建立資料庫畫面就完成了
  <br/>
  ![image](https://user-images.githubusercontent.com/90267374/132428120-dc8d8f3b-cbb2-4553-b7bc-7e6241788bb3.png)

 
