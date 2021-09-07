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
# 目錄
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
    ● Odoo的核心開發語言
    ● 這裡使用3.7，可使用3.6+的版本
    ![image](https://user-images.githubusercontent.com/90267374/132377939-d28c5c7b-7e20-4363-8832-97e3475c5982.png)
 
2 PostgreSQL
    ●	初始版本： 1996年7月8日
    ●	免費、開源
    ●	關聯式資料庫
    ●	Odoo 的御用資料庫 (此次使用官網 10.14 版本，可使用10+之版本)
    ●	知名客戶： Skype、美國勞工部
 
3 Odoo
    ●	Odoo（先前曾名為OpenERP，更早之前則為TinyERP）
    ●	是一套企業資源規劃（ERP）及客戶關係管理（CRM）系統。
    ●	以Python語言開發，資料庫採用開源的PostgreSQL。
    ●	免費、開源ERP系統
    ●	功能模組化
    ●	針對存在模組開發額外功能強大
    ●	MVC架構
 
4 PyCharm
    ●	免費(Community)
    ●	多平台安裝簡易
    ●	優點: 整合版控、Terminal、Python Console...等
    (若為Pro版也包含資料庫連線工具，直接對應程式碼使用之SQL檢查)
    ●	缺點: 消耗記憶體較高，對於大量變更檔案時會很慢，專業版需要收費

 
## 第二章 開發環境建置(Windows 10)
Python 3.7.X
    ●	https://www.python.org/ 
    ●	點選進3.7.X後，往下拉到最底找到Files，


    ●	記得將python 加到環境變數(記得使用管理員權限安裝)
    ●	因自動安裝會預設裝到奇怪的地方，因此選擇自訂安裝
    ●	若Python為64位元版本，在一開始的畫面會有64-bit的字樣

    ●	請把路徑放到C:/底下，
    資料夾名稱皆可(e.g py37, Python37 … etc.)
    ●	上方選項可預設選取，也可全選

    ●	https://www.postgresql.org/download/


    ●	請右鍵點選使用系統管理員執行
 
設定server listen port
 
 
若不需安裝則取消勾選
 
3 Odoo
 
3 Odoo
在C:/ 建立odoo資料夾，並將剛剛下載的odoo壓縮檔解壓至C:/odoo/ 
    ●	https://wkhtmltopdf.org/downloads.html



    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數

    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數

    將 C:\Program Files\wkhtmltopdf\bin\ 加入環境變數


    ●	https://www.jetbrains.com/toolbox-app/download 
    ●	https://www.jetbrains.com/toolbox-app/download

 
 
 
6 安裝Microsoft visual studio C++ 14.0
    ●	https://visualstudio.microsoft.com/zh-hant/downloads/

    6 安裝Microsoft visual studio C++ 14.0
    ● 往下拉找到Desktop & Mobile 分類裡面有個Desktop development with C++打勾，接下來按下 install後等待安裝完成

    7 設定odoo專用的postgreSQL的登入帳號
    ● 在開始直接搜尋pgAdmin4，進去後輸入剛剛設定的密碼postgres

    7 設定odoo專用的postgreSQL的登入帳號
    ●	右鍵點擊Login/Group Roles -> create -> Login/Group Roles

 
請重新開機讓Python跟wkhtmltopdf的環境變數載入
 
重新開機後使用cmd執行下面指令，
觀察是否有被正確抓到程式 python --version wkhtmltopdf -V
    ●	執行PyCharm，開啟C:/odoo
    ●	Pycharm將會抓取python程式位置，並且對開啟資料夾裡的所有檔案進行索引，這會花費一點時間要稍微等待一下

    ●	建立 python 虛擬環境

    ●	將路徑設定在C:\odoo\venv_odoo13(無此名稱會建立一個資料夾) 注意，這一定得是空資料夾才可建立環境
    ●	只勾選 Make available to all projects (讓所有專案可使用此環境) 不勾選 Inherit global site-packages 
    (繼承python主要已擁有套件[此設定會把所有套件複製一份])
 
●	建立一個執行環境，名稱odoo13(自己喜歡都行) script path選擇C:\odoo\odoo-13.0\odoo-bin
    Parameters 輸入 -c odoo.conf
 
●	畫面下方開啟terminal，安裝odoo所需套件輸入並執行下面指令
 
●	增加自訂模組資料夾
    對odoo跟目錄右鍵 -> new -> Directory，輸入addons (也可以取自己
 
●	增加odoo伺服器設定，檔案命名為odoo.conf
 
●	輸入以下內容
    [options] db_host=localhost db_port=5432 db_user=odoo db_password=odoo
    addons_path=addons, odoo/addons, ../addons xmlrpc=8069
 
●	執行odoo伺服器
●	到瀏覽器的網址列輸入 127.0.0.1:8069，能看到Odoo的建立資料庫畫面就完成了
 
 
