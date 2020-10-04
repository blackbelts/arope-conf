from odoo import api, fields, models


class Brands(models.Model):
      _name = 'car.brands'
      _rec_name = 'brand'

      brand = fields.Char('Brand')


class Covers(models.Model):
      _name = 'cover.benfeits'

      cover_name = fields.Char('Cover')
      ar_cover = fields.Char('Arabic Cover')
      amount = fields.Float('Amount')
      product_id = fields.Many2one('product.covers', string="product_id", ondelete='cascade')


class ProductCovers(models.Model):
      _name = 'product.covers'
      _rec_name = 'product_name'

      product_name = fields.Char('Product Name')
      ar_product_name = fields.Char('Arabic Product Name')
      cover_ids = fields.One2many('cover.benfeits', 'product_id', string="Category Benefit")
      motor_rating_ids = fields.One2many('motor.rating.table', 'product_id', string="Rates")

      # @api.multi
      def price(self):
            self.env['motor.api'].get_price(
                  {'brand': 'chinese cars & east asia', 'lang': 'en', 'price': 500000})


class MotorRating(models.Model):
      _name = 'motor.rating.table'
      brand = fields.Selection([('all brands', 'All Brands (except Chinese & East Asia)'),
                                ('chinese cars & east asia', 'Chinese Cars & East Asia'), ('all models', 'All Models')],
                               'Brand')
      deductible = fields.Char('Deductible')
      # fields.Selection([('250 EGP', '250 EGP'),
      #                     ('4 Per Thousand', '4 Per Thousand')],
      #                    'Deductible')

      sum_insured_from = fields.Float('From Sum Insured')
      sum_insure_to = fields.Float('To Sum Insured')
      product_id = fields.Many2one('product.covers', ondelete='cascade')
      # product = fields.Char(related='product_id.product_name', string='product', store=True)

      rate = fields.Float('Rate', digits=(12, 4))



