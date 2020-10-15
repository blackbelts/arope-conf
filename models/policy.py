from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropePolicy(models.Model):
    _name = "policy.arope"
    _rec_name='policy_num'
    policy_num = fields.Integer(string="Policy Number", copy=True)
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
    cur_code = fields.Char("Cur-Code", copy=True)
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
    agent_code = fields.Char('Agent Code', copy=True,)
    introdagt = fields.Char('Introdagt', copy=True,)

    def create_end_requset(self):
        form = self.env.ref('arope-conf.request_form_view')
        self.is_user = True
        return {
            'name': ('Request'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'policy.request',
            # 'view_id': [(self.env.ref('smart_claim.tree_insurance_claim').id), 'tree'],
            'views': [(form.id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'current',

            'context': {'default_type':'end'}

        }
    def create_renew_requset(self):
        form = self.env.ref('arope-conf.request_form_view')
        self.is_user = True
        return {
            'name': ('Request'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'policy.request',
            # 'view_id': [(self.env.ref('smart_claim.tree_insurance_claim').id), 'tree'],
            'views': [(form.id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'current',

            'context': {'default_type':'renew'}

        }


class AropePolicyRequests(models.Model):
    _name = "policy.request"
    _rec_name='name'

    @api.model
    def create(self, vals):
        serial_no = self.env['ir.sequence'].next_by_code('req')

        # merge code and serial number
        vals['name'] = vals.get('type') + '/' + str(serial_no)

        return super(AropePolicyRequests, self).create(vals)

    name=fields.Char('Request')
    type =fields.Selection([('end', 'Endorsement'),
                                ('renew', 'Renwal')],string='Request Type')
    end_reason= fields.Text(string='Endorsement Reason')














