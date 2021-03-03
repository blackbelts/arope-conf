from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropeIMS(models.Model):
    _name="arope.api"

    @api.model
    def update_arope_data(self,data,insert_date):
        c_write=False
        b_write = False
        p_write = False
        claim_write = False
        coll_write = False
        lob_exist=False
        product_exist = False
        risk_write = False
        sub_files =False
        log_id=self.env['arope.log'].create({'broker': b_write,
                                      'customer': c_write, 'policy': p_write, 'claim': claim_write,
                                      'collection': coll_write,
                                      'risk': risk_write})
        # if data['lob']:
        #     ids = self.env['insurance.line.business'].search([]).ids
        #     if ids:
        #         lob_exist = True
        #     else:
        #         p_ids = self.self.env['insurance.line.business'].create(data['lob'])
        # if data['product']:
        #     ids=self.env['insurance.product'].search([]).ids
        #     if ids:
        #         product_exist=True
        #     else:
        #         p_ids=self.self.env['insurance.product'].create(data['product'])
        #
        #
        # if data['customer']:
        #     log_id.c_write=True
        #     search_ids=self.env['persons'].search([('type','=','customer')]).unlink()
        #     persons=self.env['persons'].create(data['customer'])
        #     # self.env['persons'].unlink(search_ids)
        #     # c_write=True
        # if data['broker']:
        #     log_id.b_write = True
        #     search_ids = self.env['persons'].search(
        #         [('type', '=', 'broker')]).unlink()
        #     persons = self.env['persons'].create(data['broker'])
        #
        #     # self.env['persons'].unlink(search_ids)
        #     # b_write=True
        # if data['policy']:
        #     log_id.p_write=True

            # search_ids = self.env['policy.arope'].search([]).unlink()
            # persons = self.env['policy.arope'].create(data['policy'])

            # self.env['persons'].unlink(search_ids)
            # p_write=True
        # if data['subs']:
        #     search_ids = self.env['sub.files'].search([]).unlink()
        #     persons = self.env['sub.files'].create(data['subs'])
        #     # self.env['persons'].unlink(search_ids)
        #     sub_files = True
        # if data['risk']:
        #     persons = self.env['policy.risk'].create(data['risk'])
        #     search_ids = self.env['policy.risk'].search(
        #         [('create_date', '<', insert_date)]).unlink()
        #     # self.env['persons'].unlink(search_ids)
        #     risk_write=True
        if data['claim']:
            search_ids = self.env['claim.arope'].search([]).unlink()
            persons = self.env['claim.arope'].create(data['claim'])
            claim_write=True
        # if data['coll']:
        #     search_ids = self.env['collection.arope'].search([]).unlink()
        #     persons = self.env['collection.arope'].create(data['coll'])
        #     coll_write=True
        # self.env['arope.log'].create({'broker':b_write,
        #                               'customer':c_write,'policy':p_write,'claim':claim_write,
        #                               'collection':coll_write,
        #                               'risk':risk_write})
        return [product_exist,lob_exist]


class AropeIMSLOG(models.Model):
    _name="arope.log"
    batch_date=fields.Date('Recieved Date')
    broker = fields.Boolean('Broker')
    customer = fields.Boolean('Customer')
    policy = fields.Boolean('Policy')
    collection = fields.Boolean('Collection')
    claim = fields.Boolean('Claim')
    risk = fields.Boolean('Motor Risks')


