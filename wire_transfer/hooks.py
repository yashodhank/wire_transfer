# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wire_transfer"
app_title = "Wire Transfer"
app_publisher = "Libermatic"
app_description = "Manage wire transfer"
app_icon = "fa fa-money"
app_color = "green"
app_email = "info@libermatic.com"
app_license = "MIT"
fixtures = [{
        'doctype': 'Custom Field',
        'filters': [
                { 'dt': 'Customer' },
                [
                    'fieldname',
                    'in',
                    (
                        'id_information',
                        'id_type',
                        'id_no',
                    )]
            ]
    }]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wire_transfer/css/wire_transfer.css"
# app_include_js = "/assets/wire_transfer/js/wire_transfer.js"

# include js, css files in header of web template
# web_include_css = "/assets/wire_transfer/css/wire_transfer.css"
# web_include_js = "/assets/wire_transfer/js/wire_transfer.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = { 'Customer' : 'public/js/custom_script/customer.js' }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wire_transfer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "wire_transfer.install.before_install"
after_install = "wire_transfer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wire_transfer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wire_transfer.tasks.all"
# 	],
# 	"daily": [
# 		"wire_transfer.tasks.daily"
# 	],
# 	"hourly": [
# 		"wire_transfer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wire_transfer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wire_transfer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wire_transfer.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wire_transfer.event.get_events"
# }
