from odoo import api, fields, models

class CurrencyWizard(models.TransientModel):
    _name = 'curr.wizard'

    currency_id = fields.Many2one('res.currency',string='Currency Rate')
    rate = fields.float('Rate',digit=(12,12))
    date = fields.Date('Date',default=lambda self:fields.datetime.today())


    def update_currency(self):
        # context = self.env.context
        # record = self.env[context['active_model']].browse(
        #     context['active_id'])
        # if context['active_model'] == 'persons':
        #     person = record

        user=self.env['res.currency.rate'].create(
            {'date': self.date, 'rate':self.rate, 'currency_id':self.currency_id.id})