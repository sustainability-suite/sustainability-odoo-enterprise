# © 2025 Open Net Sarl
# License LGPL-3 or later (https://www.gnu.org/licenses/agpl).

import copy

from lxml import etree

from odoo import _, api, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        """
        The module l10n_ch_hr_payroll_elm_transmission erases the classic notebook inside the employee form.
        This override is used to add a new page to the employee form.
        """
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type == "form":
            for commuting_page in arch.xpath("//page[@name='commuting_settings']"):
                # Copy the Commuting page
                new_page = copy.deepcopy(commuting_page)
                new_page.set("name", "commuting_settings_l10n_ch")
                new_page.set("string", _("Sustainability"))

                # Add a group around the carbon_commuting_ids field
                new_page.append(
                    etree.Element(
                        "group",
                        attrib={
                            "string": _("Commuting"),
                            "name": "sustainability_commuting",
                        },
                    )
                )
                new_page.xpath("//group[@name='sustainability_commuting']")[0].append(
                    new_page.xpath("//field[@name='carbon_commuting_ids']")[0]
                )
                new_page.xpath("//field[@name='carbon_commuting_ids']")[0].set(
                    "nolabel", "1"
                )

                # Add Remote Work group
                if group_remote_work := arch.xpath(
                    "//field[@name='monday_location_id']/.."
                ):
                    new_page.append(group_remote_work[0])

                arch.xpath("//notebook")[0].append(new_page)
        return arch, view
