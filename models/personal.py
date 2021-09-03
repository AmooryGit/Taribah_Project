from odoo import api, fields, models

class person(models.Model):
    _name = 'static.person'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    birth_date = fields.date(string='Birth Date')   
    gender = fields.Selection(
        string='gender',
        selection=[('male', 'male'), ('female', 'female')]
    )
    family_id = fields.Many2one(string='family', comodel_name='static.familiy', ondelete='restrict')
    
    
