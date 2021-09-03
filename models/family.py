from odoo import _, api, fields, models


class familiy(models.Model):
    _name = 'static.familiy'
    
    name = fields.Char(string='father name', required=True)
    fam_count = fields.Integer(string='Family count')
    location = fields.Char(string='Location')
    cell_phone = fields.Char(string='cell phone')
    tel_phone = fields.Char(string='tel phone')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')])
