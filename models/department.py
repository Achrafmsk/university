from odoo import models, fields, api, _


class UniversityDepartment(models.Model):
    _name = 'university.department'
    _description = 'department of university management'
    _inherit = ['mail.thread', 'mail.activity.mixin', ]
    name = fields.Char('Name', tracking=True)
    code = fields.Char('Code', tracking=True)
    director = fields.Char('Director', tracking=True)
    discipline = fields.Char('Discipline', tracking=True)
    date = fields.Date('Date of creation')
    department_id = fields.Many2one(comodel_name='university.teacher', string='departments')


    reference = fields.Char(string='department reference', required=True, copy=False, readonly=True,
                        default=lambda self: _('New'))


@api.model
def create(self, vals):
    if vals.get('reference', _('New')) == _('New'):
        vals['reference'] = self.env['ir.sequence'].next_by_code('university.department.seq') or _('New')
    result = super(UniversityDepartment, self).create(vals)
    return result
