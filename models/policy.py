from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropePolicy(models.Model):
    _name = "policy.arope"
    _rec_name='policy_num'
    policy_num = fields.Integer(string="Policy Number", copy=True)
    pol_number = fields.Char(string="Policy Number",compute='get_policy_numberss', store=True)
    issue_date = fields.Date(string="Issue Date", copy=True, default=datetime.today())
    first_inception_date = fields.Date(string="First Inception", copy=True, default=datetime.today())
    inception_date = fields.Date(string="Incetion", copy=True, default=datetime.today())
    expiry_date = fields.Date(string="End To", default=datetime.today(), copy=True)
    net_premium= fields.Float(string="Net Premium", copy=True)
    charges= fields.Float(string="Charges", copy=True)
    policy_cost= fields.Float(string="policy_cost", copy=True)
    fixed_stamps= fields.Float(string="Fixed stamps", copy=True)
    tax = fields.Float(string="Fixed stamps", copy=True)
    totoal_premium= fields.Float(string="Total Premium", copy=True)

    eq_net= fields.Float(string=" EGP Net Premium", copy=True)

    eq_total= fields.Float(string=" EGP Total Premium", copy=True)

    curr = fields.Char("Currency", copy=True)
    pin=fields.Integer(string='PIN')
    rec_type = fields.Char(string='Rec Type' ,copy=False)
    endorsement_no = fields.Integer(string="Endorsement No.")
    # is_endorsement = fields.Boolean(string="", default=False)
    policy_serno = fields.Integer(string="policy SerNo.")
    policy_seq = fields.Integer(string="policy Seq.")
    lob = fields.Char(string="Line of business", copy=True, )
    product = fields.Char(string="Product", copy=True, )
    # endorsement_date = fields.Date(string="Endorsement Date")
    # customer = fields.Char('Customer', copy=True)
    customer_pin = fields.Integer('Insured PIN', copy=True)
    customer_Name = fields.Char('Customer Name',compute='get_customerNames', store=True)
    agent_code = fields.Char('Agent Code', copy=True,)
    agent_Name = fields.Char('Agent Name' ,compute='get_agentNames', store=True)
    introdagt = fields.Char('Introdagt', copy=True,)

    # @api.multi
    # @api.depends('product', 'policy_num')
    def get_policy_number(self):
        for record in self:
            if record.policy_num and record.product:
                record.pol_number = record.product + '/' + str(record.policy_num)

    def get_agentNam(self):
        for record in self:
            if record.agent_code:
                record.agent_Name = self.env['persons'].search([('agent_code', '=', record.agent_code)], limit=1).name

    def get_customerNam(self):
        for record in self:
            if record.customer_pin:
                record.customer_Name = self.env['persons'].search([('pin', '=', record.customer_pin)], limit=1).name

















