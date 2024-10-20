# Copyright (c) 2024, eng ezzaldeen alwali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AttachmentService(Document):
	pass
@frappe.whitelist()
def get_child_records(parent):
    # Fetch records from the child doctype
    child_records = frappe.get_all('Attachment Service', filters={'parent':parent}, fields=['attachment_type', 'mandatory','description'])
    return child_records
