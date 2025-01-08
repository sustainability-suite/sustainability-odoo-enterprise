{
    "name": "Sustainability: Carbon for assets ",
    "summary": "Make Sustainability module compatible with account_asset from Odoo",
    "version": "16.0.1.0.0",
    "author": "MCO2, Open Net Sàrl",
    "maintainers": ["jguenat", "bonnetadam", "jacopobacci"],
    "development_status": "Production/Stable",
    "category": "Accounting/Sustainability",
    "website": "https://github.com/sustainability-suite/sustainability-odoo-enterprise",
    "depends": ["account_asset", "sustainability"],
    "data": [
        "views/account_asset.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "LGPL-3",
}
