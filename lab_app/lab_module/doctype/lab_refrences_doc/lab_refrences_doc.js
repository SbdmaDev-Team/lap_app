// Copyright (c) 2024, eng ezzaldeen alwali and contributors
// For license information, please see license.txt

frappe.ui.form.on('lab_refrences_doc', {
	// refresh: function(frm) {

	// }

	validate: function(frm){
		frm.set_value('reg_date',frappe.ui.now_datetime())
	}

});
