# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class MooncardCard(models.Model):
    _inherit = 'mooncard.card'

    journal_id = fields.Many2one(
        'account.journal', string='Mooncard Bank Journal',
        domain=[('type', '=', 'bank')])
    mapping_ids = fields.One2many(
        'mooncard.account.mapping', 'card_id', string='Mapping')


class MooncardAccountMapping(models.Model):
    _name = 'mooncard.account.mapping'

    card_id = fields.Many2one('mooncard.card', string='Moon Card')
    company_id = fields.Many2one(
        related='card_id.company_id', readonly=True, store=True)
    expense_account_id = fields.Many2one(
        'account.account',
        domain=[('type', 'not in', ('view', 'closed', 'consolidation'))],
        string='Expense Account', required=True)
    force_expense_account_id = fields.Many2one(
        'account.account', 'Override Expense Account', ondelete='restrict',
        domain=[('type', 'not in', ('view', 'closed', 'consolidation'))],
        required=True)
