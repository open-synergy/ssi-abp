# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo.addons.base_rest.components.service import to_int
from odoo.addons.component.core import Component


class ProductionLotService(Component):
    _inherit = "base.rest.service"
    _name = "production.lot.service"
    _usage = "production_lot"
    _collection = "ssi.inventory.abp.public.services"
    _description = """
        Production Lot Services
        Access to the ping services is allowed to everyone
    """

    def get(self, _id):
        """
        Get partner's informations
        """
        return self._to_json(self._get(_id))

    def create(self, number, product_id):
        """
        Create a production lot
        """
        lot = self.env["stock.production.lot"].create({
            "name": number,
            "product_id": product_id,
        })
        return self._to_json(lot)

    def _get(self, _id):
        return self.env["stock.production.lot"].browse(_id)

    def _to_json(self, lot):
        res = {
            "id": lot.id,
            "number": lot.name,
            "product_name": lot.product_id.name
        }
        return res
