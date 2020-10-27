from datetime import timedelta, datetime
import base64
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo import api, fields, models

class AgentUsersWizard(models.TransientModel):
    _name = 'person.user.wizard'

    name = fields.Char('Name')
    username = fields.Char('User Name')
    password = fields.Char('Password')
    # agent_code = fields.Char(string='Person Code')
    card_id = fields.Char(string='National ID')
    user_type = fields.Selection([('agency', 'agency'),
                                ('person', 'person'), ],default='person')
    is_broker=fields.Boolean('Broker')
    is_customer=fields.Boolean('Customer')
    is_surveyor=fields.Boolean('Surveyor')
    def update_surv_data(self):
        form = self.env.ref('arope-conf.person_form_view')
        return {
            'name': ('Partner'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'persons',
            # 'view_id': [(self.env.ref('smart_claim.tree_insurance_claim').id), 'tree'],
            'views': [(form.id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'default_name': self.name,'default_user_password': self.password,
                        'default_card_id': self.card_id, }

        }


    def generate_broker_users(self):
        # context = self.env.context
        user_dict={}
        # record = self.env[context['active_model']].browse(
        #     context['active_id'])
        # if context['active_model'] == 'persons':
        #     person = record
        if self.is_broker:
           user_dict=  {'name': self.name, 'login':self.card_id, 'password':self.password,
             'card_id': self.card_id,
              'groups_id': [
                self.env['res.groups'].search([('name', '=', 'Broker')]).id]}
        elif self.is_customer:
            user_dict = {'name': self.name, 'login': self.card_id , 'password': self.password,
                         'card_id': self.card_id,
                         'groups_id': [
                             self.env['res.groups'].search([('name', '=', 'Client')]).id]}
        # elif self.is_surveyor:
        #     user_dict = {'name': self.name, 'login': self.card_id , 'password': self.password,
        #                  'card_id': self.card_id,
        #                  'groups_id': [
        #                      self.env['res.groups'].search([('name', '=', 'Surveyor')]).id]}
        #
        user=self.env['res.users'].create(user_dict)
        self.env['persons'].search([('card_id','=',user.card_id)],limit=1).is_user=True


            # user_dict = {'name': self.name, 'login': self.card_id, 'password': self.password,
            #              'agent_code': self.agent_code,
            #              'card_id': self.card_id, 'related_person': person.id,
            #              'groups_id': [
            #                  self.env['res.groups'].search([('name', '=', 'Broker')]).id}


