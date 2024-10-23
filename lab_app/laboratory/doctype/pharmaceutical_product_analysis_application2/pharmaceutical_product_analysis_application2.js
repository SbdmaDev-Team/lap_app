// Copyright (c) 2024, eng ezzaldeen alwali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pharmaceutical Product Analysis Application2', {


	 onload: function(frm) {

            if (!frm.doc.ref_name) return;  // Exit if the field is empty
		    frm.set_value('service_cataloge','طلب تحليل منتج دوائي مسجل');

          
                // Initial filter setup
            
                
            

            // if (frm.doc.has_date === 1) {  // Change the condition as per your requirement
            //     frm.set_df_property('start_date', 'hidden', false);  // Show this field
            //     frm.set_df_property('end_date', 'hidden', false);   // Hide this field
            // } else {
            //     frm.set_df_property('end_date', 'hidden', true);
            //     frm.set_df_property('end_date', 'hidden', true);
            // }
            
            frappe.call({
                method: 'lab_app.laboratory.doctype.pharmaceutical_product_analysis_application2.pharmaceutical_product_analysis_application2.get_preivios_app_data', 
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
                        frm.set_value('batch', r.message.batch);
                        // ... add more fields as necessary
                    }
				}});
			
   
            

        },
        service_cataloge: function(frm) {
            frm.set_value('attachment', []);

            if (frm.doc.service_cataloge && !frm.__islocal){
                frappe.call({
                    method: 'frappe.client.get',
                    args: {
                    doctype: 'Service Catalog',
                    name: frm.doc.service_cataloge
            },
            callback: function(response) {
            var r = response.message;
            $.each(r.attachments, function(i, row) {
            var child = frm.add_child('attachment',{
                "attachment_type": row.attachment_type,
                "mandatory": row.mandatory,
                "description": row.description,
                "has_date": row.has_date});
            });  
        frm.refresh_field('attachment');
        }
       });}

    



},

workflow_state: function(frm) {

    // frappe.msgprint(frm.doc[workflow_state_fieldname]+'hgjg');
    //  if (frm.doc.workflow_state == 'sent' ){


     frm.set_value('verification', []);

    if (frm.doc.service_cataloge && !frm.__islocal){
        frappe.call({
            method: 'frappe.client.get',
            args: {
            doctype: 'Service Catalog',
            name: frm.doc.service_cataloge  },
            
    callback: function(response) {
    var r2 = response.message;
    $.each(r2.verification, function(i, row2) {
    var child = frm.add_child('verification', {
        "verification_type": row2.verification_type,
        "status": row2.status,
        "note": row2.note
        });
    });  
// frm.refresh_field('verification');
    
}
   });}}
// }

    

//     refresh: function(frm) 
//     {
//         // Add a custom button on the form
//         // if (frm.doc.attachment !== null ) return;
//         // else{ 
//             // if (frm.is_new()) {
                
//                 frappe.printmsg('ffff');
//         if (frm.doc.workflow_state ==='Sent' || frm.doc.workflow_state ==='Verified'){

//                 frappe.printmsg('ffff');
//             frappe.call({
//                 method: 'lab_app.laboratory.doctype.pharmaceutical_product_analysis_application2.pharmaceutical_product_analysis_application2.add_app_verification', 
//                  args: {
//                     name: frm.doc.name,
//                     service_name: frm.doc.service_cataloge,
//                     status: frm.doc.workflow_state
//                     },
//                 callback: function(r) {
//                     if (r.message) {
//                         // Set values to fields based on the returned data
//                        frappe.printmsg('hjghjgj');
                      
//                     //    frm.refersh();
//                     //    frm.refresh_field('attachment');
//                     //    frm.refresh_field('verification');
//                         // ... add more fields as necessary
//                     }
                   
//                     // else{frappe.printmsg('خطأ في الخدمة'); }
                    
              
//                 }});
//             }
// },
        // service_cataloge: function(frm) {
        //     // Add a custom button on the form
        //     // if (frm.doc.attachment !== null ) return;
        //     // else{ 
        //         // if (frm.is_new()) {
        //     frappe.call({
        //         method: 'lab_app.laboratory.doctype.pharmaceutical_product_analysis_application2.pharmaceutical_product_analysis_application2.add_app_service', 
        //             args: {
        //             name: frm.doc.name,
        //             service_name: frm.doc.service_cataloge,
        //             status: frm.doc.workflow_state
        //             },
        //         callback: function(r) {
        //             if (r.message) {
        //                 frm.reload_doc();
        //                 // Set values to fields based on the returned data
        //                 // frappe.printmsg('hjghjgj');
        //                 frm.refresh_field('attachment');
        //                 frm.refresh_field('verification');
        //                 // ... add more fields as necessary
        //             }
                    
        //             // else{frappe.printmsg('خطأ في الخدمة'); }
        //         }});
                        
            
       
        // },

        
       


			
});
