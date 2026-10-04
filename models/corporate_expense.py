from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class CorporateExpense(models.Model):
    _name = 'corporate.expense'
    _description = 'Corporate Expense'

    name = fields.Char(
                    string='Vendor Invoice', 
                    required=True
                    )
    amount = fields.Float(string='Amount')
    company_id = fields.Many2one(
                    comodel_name='res.company', 
                    string='Company', 
                    required=True, 
                    default=lambda self: self.env.company
                    )
    state = fields.Selection(
                    [
                        ('draft','Draft'),
                        ('approved','Approved'),
                    ], 
                    string='State', 
                    default='draft'
                    )

    def action_generate_global_expense_audit_logs(self):
        companies = self.env['res.company'].search([])

        for company in companies:
            aggregated_data = self.env['corporate.expense'].with_company(company).read_group(
                domain=[('company_id','=',company.id),('state','=','approved')],
                fields=['amount:sum'],
                groupby=['company_id']
            )

            if aggregated_data:
                for data in aggregated_data:
                    calculated_sum_value = data.get('amount',0.0)
                    _logger.info(
                        "Audit Lock: Entity %s registers total approved expenditure balance of %s.",
                        company.name,
                        calculated_sum_value
                    )

            else:
                _logger.info(f"Audit Lock: Entity {company.name} registers total approved expenditure balance of {aggregated_data}")
        
        return True