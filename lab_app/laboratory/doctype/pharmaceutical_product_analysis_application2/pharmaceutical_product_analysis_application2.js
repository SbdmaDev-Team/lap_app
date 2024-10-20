// Copyright (c) 2024, eng ezzaldeen alwali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pharmaceutical Product Analysis Application2', {
	 onload: function(frm) {
            if (!frm.doc.ref_name) return;  // Exit if the field is empty
		    frm.set_value('service_cataloge','تحليل صنف جديد');
            frappe.call({
                method: 'lab_app.laboratory.doctype.pharmaceutical_product_analysis_application.pharmaceutical_product_analysis_application.get_preivios_app_data', 
                // method: 'lab_app.laboratory.doctype.attachment_service.attachment_service.get_child_records', 
                 // Path to your server-side method
                // method: 'lab_app.Laboratory.doctype.Initial Pharmaceutical Product Application.get_item_data',  // Path to your server-side method
                args: {
                    name: frm.doc.ref_name  // Passing the field value as an argument
                },
                callback: function(r) {
                    if (r.message) {
                        // Set values to fields based on the returned data
                        frm.set_value('company', r.message.company);
                        frm.set_value('importer', r.message.importer);
                        frm.set_value('item', r.message.item);
                        frm.set_value('trade_aname', r.message.trade_aname);
                        frm.set_value('generic_name', r.message.generic_name);
                        frm.set_value('primary_container', r.message.primary_container);
                        frm.set_value('strength', r.message.strength);
                        // ... add more fields as necessary
                    }
				}});
			
   
            

        },

        after_save: function(frm) {
            // Add a custom button on the form
            // if (frm.doc.attachment !== null ) return;
            // else{ 

                frappe.call({
                    method: 'lab_app.laboratory.doctype.pharmaceutical_product_analysis_application.pharmaceutical_product_analysis_application.add_app_attach', 
                    // method: 'lab_app.laboratory.doctype.attachment_service.attachment_service.get_child_records', 
                     // Path to your server-side method
                    // method: 'lab_app.Laboratory.doctype.Initial Pharmaceutical Product Application.get_item_data',  // Path to your server-side method
                    args: {
                        name: frm.doc.name,
                        service_name: frm.doc.service_cataloge
                         // Passing the field value as an argument
                    },
                    callback: function(r) {
                        if (r.message) {
                            // Set values to fields based on the returned data
                           // frappe.printmsg('hjghjgj');
                           frm.refresh_field('attachment');
                            // ... add more fields as necessary
                        }
                  
         }});}
    // }
			
});