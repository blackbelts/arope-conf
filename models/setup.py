from odoo import models, tools, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime


class MedicalPriceTable(models.Model):
    _name = 'medical.price'
    _description = 'Set up Price tables'
    _rec_name = 'product_name'
    package = fields.Selection([('individual', 'Individual'),
                             ('sme', 'SME'),],
                            'Package For',
                            default='individual')

    product_name = fields.Char(string='Product Name')
    sort = fields.Integer('Sort')


    price_lines = fields.One2many('medical.price.line','price_id',string='Prices')
    cover_lines = fields.One2many('medical.cover','cover_id',string='Covers')
    # internal_lines = fields.One2many('medical.internal.hospital.treatment', 'internal_id', string='Internal Hospital Treatment')
    # outpatient_lines = fields.One2many('medical.outpatient.services', 'outpatient_id', string='Outpatient Services')

    # @api.multi
    def price(self):
        self.env['medical.api'].get_price({'type':'individual','dob':['1999-5-4'], 'lang':'en'})

class MedicalPriceTableLines(models.Model):
    _name = 'medical.price.line'

    from_age = fields.Float('From Age')
    to_age = fields.Float('To Age')
    price = fields.Float('Price')
    price_id = fields.Many2one('medical.price', ondelete='cascade')

class MedicalCoversType(models.Model):
    _name = 'medical.covers.type'
    _rec_name = 'type'

    type = fields.Char('Type')
    ar_type = fields.Char('Arabic Type')

class MedicalCovers(models.Model):
      _name = 'medical.cover'

      benefit = fields.Text(string='Benefit')
      value = fields.Text(string='Value')
      en_benefit = fields.Text(string='English Benefit')
      en_value = fields.Text(string='English Value')
      type = fields.Many2one('medical.covers.type', 'Type')
      sort = fields.Integer('Sort')
      cover_id = fields.Many2one('medical.price', ondelete='cascade')



class Notes(models.Model):
    _name = 'medical.notes'
    _rec_name = 'note'

    note = fields.Text('Note')
    ar_note = fields.Text('Arabic Note')
    package = fields.Selection([('individual', 'Individual'),
                                ('sme', 'SME'), ('all', 'All')],
                               'Note For',
                               default='individual')
    sort = fields.Integer('Sort')