# Copyright (c) 2024, eng ezzaldeen alwali and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class InitialPharmaceuticalProductApplication(Document):
    pass
    # def before_insert(self):
    #     doc = frappe.get_doc('Sbdma Items', self.item)
    #     # frappe.msgprint(_(doc.trade_aname))
    #     self.primary_container: doc.primary_container
    #     self.strength: doc.strength
    #     self.generic_name: doc.generic_name
    #     self.trade_aname: doc.trade_aname
# @frappe.whitelist()
# def get_item_data(name):
#     data = {}
#     # Fetch data from another doctype
#     item = frappe.get_doc('Sbdma Item', name)  # Replace 'Customer' with your source doctype
#     if item:
#         data['primary_container'] = item.primary_container
#         data['strength'] = item.strength
#         data['generic_name'] = item.primary_container
#         data['trade_aname'] = item.strength
#         # ... add more fields as necessary
#     return data



