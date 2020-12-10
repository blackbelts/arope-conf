from odoo import models, tools, fields, api,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime,date

class AropeIMS(models.Model):
    _name="arope.api"

    @api.model
    def update_arope_data(self,data):
        if data['customer']:
            search_ids=self.env['persons'].search([('type','=','customer')]).unlink
            # self.env['persons'].unlink(search_ids)
            self.env['persons'].create(data['customer'])


