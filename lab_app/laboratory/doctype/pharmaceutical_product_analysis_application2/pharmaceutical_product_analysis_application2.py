# Copyright (c) 2024, eng ezzaldeen alwali and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document

class PharmaceuticalProductAnalysisApplication2(Document):

    pass
    # def after_save(self):
    # # if self.__islocal:
    # # self.add_app_attach()
    # # self.add_app_verification()
    # frappe.msgprint("Items from Sales Order") 
    # if not self.attachment:
    #     frappe.msgprint("Items from Sales Order")
    #     # Get the Delivery Note document where you want to append the items
    #     service_attach = frappe.get_doc('Service Catalog', self.service_name)

    #     # Loop through each item in the Sales Order Item child table
    #     for attch in service_attach.attachments:
    #         # Append each item to the Delivery Note Item child table
    #         analiysis_doc.append('attachment', {
    #             "attachment_type": attch.attachment_type,
    #             "mandatory": attch.mandatory,
    #             "description": attch.description,
    #             "has_date": attch.has_date
    #         })
    # self.save()
    # frappe.db.commit()

    @frappe.whitelist()
    def add_app_service(name,service_cataloge,status):
        add_app_attach(name,service_cataloge)
        # add_app_verification(name,service_cataloge,status)

    def add_app_attach(name,service_cataloge):
        analiysis_doc = frappe.get_doc('Pharmaceutical Product Analysis Application2', name)
        frappe.msgprint("Items from Sales Order")
        if not analiysis_doc.attachment:
            
            frappe.msgprint("Items from Sales Order")
            # Get the Delivery Note document where you want to append the items
            service_attach = frappe.get_doc('Service Catalog', service_cataloge)
        
            # Loop through each item in the Sales Order Item child table
            for attch in service_attach.attachments:
                # Append each item to the Delivery Note Item child table
                analiysis_doc.append('attachment', {
                    "attachment_type": attch.attachment_type,
                    "mandatory": attch.mandatory,
                    "description": attch.description,
                    "has_date": attch.has_date
                })
            analiysis_doc.save()
            frappe.db.commit()

    def add_app_verification(self):
        analiysis_doc = frappe.get_doc('Pharmaceutical Product Analysis Application2', self.name)
        service_attach = frappe.get_doc('Service Catalog', self.service_name)
        # for ch in self.verification:
            # if not ch.status == status:
            #     return
        # Loop through each item in the Sales Order Item child table
        for attch in service_attach.verification:
            if attch.status == status:
                # Append each item to the Delivery Note Item child table
                analiysis_doc.append('verification', {
                    "verification_type": attch.verification_type,
                    "status": attch.status,
                    "note": attch.note
                    })
        
                # Save the Delivery Note with the new items
        analiysis_doc.save()
        # Optionally commit if this is outside a transaction (Frappe generally handles transactions)
        frappe.db.commit()
        # frappe.msgprint(f"Items from Sales Order {name} have been copied to Delivery Note {service_name}")






# on load : Fetch Data
@frappe.whitelist()
def get_preivios_app_data(name):
    data = {}
    # Fetch data from another doctype
    appdata = frappe.get_doc('Initial Pharmaceutical Product Application', name)  # Replace 'Customer' with your source doctype
    if appdata:
        data['importer'] = appdata.importer
        data['company'] = appdata.company
        data['item'] = appdata.item
        data['primary_container'] = appdata.primary_container
        data['strength'] = appdata.strength
        data['generic_name'] = appdata.generic_name
        data['trade_aname'] = appdata.trade_aname
        data['batch'] = appdata.batch
        # ... add more fields as necessary
    return data


@frappe.whitelist()
def add_app_service(name, service_name,status):
    add_app_attach(name, service_name)
    add_app_verification(name, service_name,status)




@frappe.whitelist()
def add_app_attach(name, service_name):
    # frappe.msgprint("Items from Sales Order")
    # Get the Sales Order document with its items (source child doctype)
    analiysis_doc = frappe.get_doc('Pharmaceutical Product Analysis Application2', name)
    if not analiysis_doc.attachment:

        # Get the Delivery Note document where you want to append the items
        service_attach = frappe.get_doc('Service Catalog', service_name)
    
        # Loop through each item in the Sales Order Item child table
        for attch in service_attach.attachments:
            # Append each item to the Delivery Note Item child table
            analiysis_doc.append('attachment', {
                "attachment_type": attch.attachment_type,
                "mandatory": attch.mandatory,
                "description": attch.description,
                "has_date": attch.has_date
             })
    
        # Save the Delivery Note with the new items
        analiysis_doc.save()


        # Optionally commit if this is outside a transaction (Frappe generally handles transactions)
        frappe.db.commit()
        
        # analiysis_doc.reload()

        # frappe.msgprint(f"Items from Sales Order {name} have been copied to Delivery Note {service_name}")


# @frappe.whitelist()
# def add_app_verification(name, service_name,status):
#     # frappe.msgprint("Items from Sales Order")
#     # Get the Sales Order document with its items (source child doctype)
#     analiysis_doc = frappe.get_doc('Pharmaceutical Product Analysis Application2', name)
#     if not analiysis_doc.verification:

#         # Get the Delivery Note document where you want to append the items
#         service_attach = frappe.get_doc('Service Catalog', service_name)
    
#         # Loop through each item in the Sales Order Item child table
#         for attch in service_attach.verification:
#             if attch.status == status:
#                 # Append each item to the Delivery Note Item child table
#                 analiysis_doc.append('verification', {
#                     "verification_type": attch.verification_type,
#                     "status": attch.status,
#                     "note": attch.note
#                 })
    
#             # Save the Delivery Note with the new items
#         analiysis_doc.save()

#         # Optionally commit if this is outside a transaction (Frappe generally handles transactions)
#         frappe.db.commit()


@frappe.whitelist()
def add_app_verification(name, service_name,status):
    # frappe.msgprint("Items from Sales Order")
    # Get the Sales Order document with its items (source child doctype)
    analiysis_doc = frappe.get_doc('Pharmaceutical Product Analysis Application2', name)
    service_attach = frappe.get_doc('Service Catalog', service_name)
    for ch in analiysis_doc.verification:
        if not ch.status == status:
            return
    # Loop through each item in the Sales Order Item child table
    for attch in service_attach.verification:
        if attch.status == status:
            # Append each item to the Delivery Note Item child table
            analiysis_doc.append('verification', {
                "verification_type": attch.verification_type,
                "status": attch.status,
                "note": attch.note
                })
    
            # Save the Delivery Note with the new items
    analiysis_doc.save()
    # Optionally commit if this is outside a transaction (Frappe generally handles transactions)
    frappe.db.commit()
    # frappe.msgprint(f"Items from Sales Order {name} have been copied to Delivery Note {service_name}")

