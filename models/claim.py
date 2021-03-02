from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropeClaim(models.Model):
    _name="claim.arope"
    _rec_name='claimNo'
    policy_no = fields.Integer(string="Policy Number", copy=True,)
    policy_number = fields.Char(string="Policy Number",compute='get_policy_numbers', store=True)
    # line_of_bussines = fields.Char(string='Line of business')
    product = fields.Char(string="Product", copy=True,)
    lob = fields.Char(string="Line of business", copy=True, )
    sub_journal = fields.Char('Sub-Journal', copy=True)
    claim_year = fields.Char(string="Claim Year", copy=True, )
    claimNo = fields.Integer(string="ClaimNo", copy=True, )
    claim_serNo = fields.Integer(string="Claimserno", copy=True, )
    date_declared= fields.Date(string="Date Declared", copy=True,)
    date_occured= fields.Date(string="Date Occured", copy=True,)
    claim_status= fields.Char(string="Claim Status", copy=True,)
    policy_serno = fields.Integer(string="policy SerNo.")

    curr = fields.Char("Currency", copy=True)
    pin=fields.Integer(string='PIN')
    claim_eval=fields.Float(string='Claim eval')
    fees_eval=fields.Float(string='Fees eval')
    recoveryamt_eval=fields.Float(string='Recovery Amt')
    claim_paid=fields.Float(string='Claim Paid')
    agent_code=fields.Char(string='Agent_code')

    @api.constrains('product', 'policy_no')
    def get_policy_numbers(self):
        for record in self:
            if record.policy_no and record.product:
                record.policy_number = record.product + '/' + str(record.policy_no)














