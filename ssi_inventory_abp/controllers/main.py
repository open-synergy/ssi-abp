# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main


class AbpApiPublicApiController(main.RestController):
    _root_path = "/abp_api/public/"
    #TODO:
    _collection_name = "ssi.inventory.abp.public.services"
    _default_auth = "public"
