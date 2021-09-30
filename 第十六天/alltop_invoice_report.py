

from odoo import api, models, _

class InvoiceReport(models.AbstractModel):
    _name = 'report.alltop_freezer.freezer_invoice_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alltop_freezer.alltop_invoice'].browse(docids)
        res_doc, doc = [], []

        for line in docs:
            for row in line.invoice_line_ids:
                lines = {
                    'name': row.product_id.name,
                    'cell_id': row.cell_id.area_id.name
                }
        return {
            'docids': docids
        }
