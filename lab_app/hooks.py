# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lab_app"
app_title = "Lab App"
app_publisher = "eng ezzaldeen alwali"
app_description = "Lab_App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ezwalialwali@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lab_app/css/lab_app.css"
# app_include_js = "/assets/lab_app/js/lab_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/lab_app/css/lab_app.css"
# web_include_js = "/assets/lab_app/js/lab_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lab_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lab_app.install.before_install"
# after_install = "lab_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lab_app.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"lab_app.tasks.all"
# 	],
# 	"daily": [
# 		"lab_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"lab_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lab_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lab_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lab_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lab_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lab_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
fixtures = [
    {
        "dt": "Workflow",
        "filters":{
            "name":"Laboratory Workflow"
        }

    },
      {
        "dt": "Workflow State",
        "filters":[
            [
            "name","in",("Sent","Verified","Distribute","analysis","Initial Verified","Incomplate","Closed","Receive","Initial Review","Review","Final Review")
            ]
        ]        

    }

]
