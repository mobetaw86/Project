Odoo模組開發實戰
# 目錄
 1.	資料表之間的關聯欄位

## 第一章: 資料表之間的關聯欄位

One2one:
一對一關係，格式為:
fields.One2one(關聯物件 Name, 字段顯示名, ... )。
基本上，筆者完全沒有用過，而是用Many2one。

Many2one:
多對一關係，格式為:
fields.Many2one(關聯物件 Name, 字段顯示名, ... )。
可選參數有:
1.ondelete: 可以選擇的值為"cascade"和"null"，預設值為"null"，表示 one 端的 record 被刪除後，
many 端的 record 是否串聯(cascade)刪除。
2. required: True
3. readonly: True
4. select: True - (creates an index on the Foreign Key field) -> 沒用過

One2many:
一對多關係，格式為:
fields.One2many(關聯物件Name(comodel_name), 關聯字段(inverse_name), 字段顯示名, ... ),
例:'address': fields.One2many('res.partner.address', 'partner_id', 'Address')。

many2many:
多對多關係，例如:
'category_id':fields.Many2many('res.partner.category','res_partner_category_rel','partner_id','category_id','Categories')

表示以多對多關係
category_id 所在的資料表會關聯到 res.partner.category,

當定義上述字段時，Odoo 會自動創建關聯表為 'res_partner_category_rel',
它含有關聯字段'partner_id'和'category_id'。

補充:
筆者習慣，程式先寫Ｍany2one，再寫One2many這樣才知道One2many的inverse_name要寫誰。
 
