from odoo import models, tools, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime


class Aropelinebusiness(models.Model):
    _name = "insurance.line.business"
    _rec_name = 'line_of_business'
    line_of_business = fields.Char(string='Line of Business', required=True)
    object = fields.Selection([('person', 'Person'),
                               ('vehicle', 'Vehicle'),
                               ('cargo', 'Cargo'),
                               ('location', 'Location'),
                               ('Project', 'Project')],
                              'Insured Type', track_visibility='onchange', )
    desc = fields.Char(string='Description')
    image = fields.Binary(string='Image')
    icon = fields.Char('Icon')


    product_ids=fields.One2many('insurance.product','line_of_bus',string='Products')


class Product(models.Model):
    _name = 'insurance.product'
    _rec_name = 'arabic_desc'

    product_name = fields.Char('Product Name', required=True)
    line_of_bus = fields.Many2one('insurance.line.business', 'Line of Business',required=True)
    _sql_constraints = [
        ('product_unique', 'unique(product_name,line_of_bus)', 'Product already exists!')]

    questionnaire_file = fields.Many2many('ir.attachment', string="Upload File")
    file_name = fields.Char("File Name")
    arabic_desc = fields.Char("Arabic Desc")
    prod_desc = fields.Char("Desc")
    questionnaire_ids = fields.One2many('questionnaire.lines.setup', 'product_id')
    # survey_ids = fields.One2many('survey.line.setup', 'product_id')
    # final_application_ids = fields.One2many('final.application.setup', 'product_id')
    # offer_setup_ids = fields.One2many('offer.setup', 'product_id')
    # state_id = fields.Many2one('state.setup', ondelete='cascade')


class Notification(models.Model):
    _name = 'system.notify'
    _rec_name = 'type'

    type = fields.Selection([('Collection', 'Collection'),
                               ('Renewal', 'Renewal')],
                              'Type', required=True)
    color = fields.Selection([
        ('Orange', 'Orange'),
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Black', 'Black')
    ],'Color',required=True)
    no_days = fields.Integer('Number of days', required=True)

    _sql_constraints = [
        ('type_unique', 'unique(type,color,no_days)', 'Rule Exist!')]

class Notification(models.Model):
    _name = 'commission.table'
    # _rec_name = 'type'
    lob = fields.Many2many('insurance.line.business',string='Line of business')
    product = fields.Many2many('insurance.product',string='Products')
    broker = fields.Many2many('persons',string='Broker')
    basic = fields.Float('Basic')
    comp_comm = fields.Float('Complementary Commission')
    trans_comm = fields.Float('Transportation Commission')

    other_comm = fields.Float('Other Commission')

class QuestionnaireLineSetup(models.Model):
    _name = 'questionnaire.lines.setup'
    _rec_name = 'question'
    question = fields.Char('Question')
    # options = fields.Many2many('selection.options', sting="Selections")
    desc = fields.Char('Description')
    question_type = fields.Selection([('text', 'Text'), ('numerical', 'Numerical')],
                                     'Question Type', default='text')

    product_id = fields.Many2one('insurance.product', ondelele='cascade', index=True)
    # sub_questionnaire_id = fields.Many2one('sub.questionnaire', ondelele='cascade', index=True)






