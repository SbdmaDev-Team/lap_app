// Copyright (c) 2024, eng ezzaldeen alwali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Initial Pharmaceutical Product Application', {
	onload: function(frm) {
        // Set query to filter the Customer field
        frm.set_query('importer', function() {
            return {
                filters: {
                    'establishment_type': 'IMPORTER'  // Filter customers by country
                }
            };
        });
		frm.set_query('company', function() {
            return {
                filters: {
                    'establishment_type': 'EXTERNAL COMPANY'  // Filter customers by country
                }
            };
        });
        
    },
        // item: function(frm) {
        //     if (!frm.doc.item) return;  // Exit if the field is empty
    
        //     frappe.call({
        //         method: 'lab_app.laboratory.doctype.initial_pharmaceutical_product_application.initial_pharmaceutical_product_application.get_item_data', 
        //          // Path to your server-side method
        //         // method: 'lab_app.Laboratory.doctype.Initial Pharmaceutical Product Application.get_item_data',  // Path to your server-side method
        //         args: {
        //             name: frm.doc.item  // Passing the field value as an argument
        //         },
        //         callback: function(r) {
        //             if (r.message) {
        //                 // Set values to fields based on helpthe returned data
        //                 frm.set_value('trade_aname', r.message.trade_aname);
        //                 frm.set_value('generic_name', r.message.generic_name);
        //                 frm.set_value('primary_container', r.message.primary_container);
        //                 frm.set_value('strength', r.message.strength);
        //                 // ... add more fields as necessary
        //             }
        //         }
        //     });

            

        // },
    // Custom buttons
        refresh: function(frm) {
            // Add a custom button on the form
            frm.add_custom_button(__('طلب تحليل صنف'), function() {
                // Action to perform when the button is clicked
            var new_application = frappe.model.get_new_doc('Pharmaceutical Product Analysis Application2');          
            new_application.ref_name = frm.doc.name;
            
            frappe.set_route('Form', 'Pharmaceutical Product Analysis Application2',new_application.name);
         // frappe.set_route('Form', 'pharmaceutical-product-analysis-application',{ref_name:frm.doc.name});
        }, __('أضافة')); // Group under "Utilities"
        }

    
//    refersh: function(frm) {
//    frm.add_custom_button('Open Customer', function() {
//     // Open the Customer doctype's form
//     frappe.set_route('Form', 'Pharmaceutical Product Analysis Application');
//  },'Openustomer')
// frm.add_custom_button('Open Reference form', () => {
//     frappe.set_route('Form', 'Pharmaceutical Product Analysis Application');}),
//             frm.add_custom_button('طلب تحليل  ', () => {
//         frm.doc.status = 'Closed'
//     });
// }


}
);
