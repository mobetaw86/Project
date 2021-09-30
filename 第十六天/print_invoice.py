from odoo import api, models, fields
from odoo.exceptions import UserError

class PrintInvoice(models.TransientModel):
    _name = 'print.invoice'

    def generateReport(self):
        active_ids = self.env.context.get('active_ids')
        invoice_ids = self.env['alltop_freezer.alltop_invoice'].browse(active_ids).ids
        datas = {
            'ids': invoice_ids
        }
        return self.env.ref('alltop_freezer.freezer_invoice_report').report_action(self, data=datas)
