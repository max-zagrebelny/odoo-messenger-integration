{
    "name": """WhatsApp Integration""",
    "summary": """WhatsApp integration powered by Sync Studio and Twilio""",
    "category": "Marketing",
    "images": ["images/sync_whatsapp.jpg"],
    "version": "15.0.2.0.0",
    "application": False,
    "author": "IT Projects Labs, Eugene Molotov",
    "support": "help@itpp.dev",
    "depends": ["sync", "multi_livechat"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/sync_project_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sync_whatsapp/static/src/models/discuss/discuss.js",
            "sync_whatsapp/static/src/models/discuss_sidebar_category/discuss_sidebar_category.js",
        ],
    },
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
