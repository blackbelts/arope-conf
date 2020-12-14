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

        if data['lob']:
            ids = self.env['insurance.line.business'].search([]).ids
            if ids:
                lob_exist = True
            else:
                p_ids = self.self.env['insurance.line.business'].create(data['lob'])
        if data['product']:
            ids=self.env['insurance.product'].search([]).ids
            if ids:
                product_exist=True
            else:
                p_ids=self.self.env['insurance.product'].create(data['product'])


        if data['customer']:
            persons=self.env['persons'].create(data['customer'])
            search_ids=self.env['persons'].search([('type','=','customer'),('create_date','<',insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            c_write=True
        if data['broker']:
            persons = self.env['persons'].create(data['broker'])
            search_ids = self.env['persons'].search(
                [('type', '=', 'broker'), ('create_date', '<', insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            b_write=True
        if data['policy']:
            persons = self.env['policy.arope'].create(data['policy'])
            search_ids = self.env['policy.arope'].search(
                [('create_date', '<', insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            p_write=True
        if data['risk']:
            persons = self.env['policy.risk'].create(data['risk'])
            search_ids = self.env['policy.risk'].search(
                [('create_date', '<', insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            risk_write=True
        if data['claim']:
            # persons = self.env['claim.arope'].create(data['claim'])
            c_ids=self.env['claim.arope'].search([])
            return len(c_ids.ids)
            # if ids:
            #     return "Claim Exist"
            # else:
            #     return "no Claims"
            # search_ids = self.env['claim.arope'].search(
            #     [('create_date', '<', insert_date)]).unlink()
            claim_write=True
        if data['coll']:
            persons = self.env['collection.arope'].create(data['coll'])

            # search_ids = self.env['collection.arope'].search(
            #     [('create_date', '<', insert_date)]).unlink()
            coll_write=True
        self.env['arope.log'].create({'broker':b_write,
                                      'customer':c_write,'policy':p_write,'claim':claim_write,
                                      'collection':coll_write,
                                      'risk':risk_write})
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


