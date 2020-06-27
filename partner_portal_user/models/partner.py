from odoo import api, models


class Partner(models.Model):
	_inherit = 'res.partner'

	@api.multi
	def act_create_user_portal(self):
		Users = self.env['res.users']
		portal_group = self.env.ref('base.group_portal').id
		for rec in self:
			if rec.user_ids:
				rec.user_ids.write({'groups_id': [(4, portal_group)]})
				continue
			if not rec.email:
				continue
			user = Users.create({'partner_id': rec.id, 'name': rec.name, 'login': rec.email, 'groups_id': [(4, portal_group)]})
			user.action_reset_password()
			
