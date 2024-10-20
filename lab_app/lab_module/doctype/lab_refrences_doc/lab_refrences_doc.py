# -*- coding: utf-8 -*-
# Copyright (c) 2024, eng ezzaldeen alwali and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class lab_refrences_doc(Document):

	def before_insert(self):
		self.reg_date = frappe.utils.now_datetime()
	