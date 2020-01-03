from odoo import fields, models, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.model
    def create(self, values_list):
        res = super(MrpWorkorder, self).create(values_list)

        final_lot = self.env['stock.production.lot'].create({
            'name': self.env['ir.sequence'].next_by_code('mrp.workorder'),
            'product_id': res.product_id.id
        })

        res.final_lot_id = final_lot.id

        return res

    def open_tablet_view(self):

        counter = 0
        while self.curren_quality_check_id:
            counter += 1

            if self.curren_quality_check_id.component_is_byproduct:
                if not self.curren_quality_check_id.lot_id:
                    lot_tmp = self.env['stock.production.lot'].create({
                        'name': self.env['ir.sequence'].next_by_code('mrp.workorder'),
                        'product_id': self.curren_quality_check_id.component_id.id
                    })
                    self.curren_quality_check_id.lot_id = lot_tmp.id
                    if self.curren_quality_check_id.quality_state == 'none':
                        self.action_next()
            else:
                if not self.curren_quality_check_id.component_id.categ_id.is_canning:
                    self.curren_quality_check_id.qty_done = 0
                self.action_skip()

            if counter > 20:
                raise models.ValidationError('20')

        # for check in self.finished_product_check_ids:
        #
        #     if check.component_is_byproduct:
        #         if not check.lot_id:
        #             lot_tmp = self.env['stock.production.lot'].create({
        #                 'name': self.env['ir.sequence'].next_by_code('mrp.workorder'),
        #                 'product_id': check.component_id.id
        #             })
        #             check.lot_id = lot_tmp.id
        #         if check.quality_state == 'none':
        #             if self.component_tracking != 'none' and not self.lot_id:
        #                 raise models.ValidationError('{} {}'.format(
        #                     check.qty_done,
        #                     self.current_quality_check_id.qty_done,
        #
        #                 ))
        #             self.action_next()
        #
        #     else:
        #         if not check.component_id.categ_id.is_canning:
        #             check.qty_done = 0
        #         self.action_skip()

        self.action_first_skipped_step()

        return super(MrpWorkorder, self).open_tablet_view()

    def action_next(self):
        res = super(MrpWorkorder, self).action_next()
        self.qty_done = 0

    def on_barcode_scanned(self, barcode):

        qty_done = self.qty_done
        custom_serial = self.env['stock.production.lot.serial'].search([('serial_number', '=', barcode)])
        if custom_serial:
            barcode = custom_serial.stock_production_lot_id.name
        super(MrpWorkorder, self).on_barcode_scanned(barcode)
        self.qty_done = qty_done + custom_serial.display_weight

    def open_out_form_view(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mrp.workorder',
            'views': [[self.env.ref('dimabe_manufacturing.mrp_workorder_out_form_view').id, 'form']],
            'res_id': self.id,
            'target': 'fullscreen'
        }

