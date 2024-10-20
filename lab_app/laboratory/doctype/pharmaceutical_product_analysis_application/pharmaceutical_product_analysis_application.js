// Copyright (c) 2024, eng ezzaldeen alwali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pharmaceutical Product Analysis Application', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
        frm.add_custom_button('Add Items', () => {
            frappe.new_doc('Pharmaceutical Product Analysis Application Items', {
                application_name: frm.doc.name
            })
        })},
});
