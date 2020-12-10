from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropeIMS(models.Model):
    _name="arope.api"

    @api.model
    def update_arope_data(self,data,insert_date):
        if data['customer']:
            persons=self.env['persons'].create(data['customer'])
            search_ids=self.env['persons'].search([('type','=','customer'),('create_date','<',insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            return True
        if data['broker']:
            persons = self.env['persons'].create(data['broker'])
            search_ids = self.env['persons'].search(
                [('type', '=', 'broker'), ('create_date', '<', insert_date)]).unlink()
            # self.env['persons'].unlink(search_ids)
            return True


