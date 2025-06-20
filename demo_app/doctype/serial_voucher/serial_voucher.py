import frappe
import random
import string

def generate_serials(doc, method):
    doc.serial_numbers = []

    if doc.generate_type == "Auto Generate":
        for i in range(doc.quantity):
            serial = "SR-" + ''.join(random.choices(string.digits, k=8))
            row = doc.append("serial_numbers", {})
            row.serial_number = serial
            row.item = doc.item

    elif doc.generate_type == "Use Existing":
        frappe.msgprint("Please manually select existing serials.")

    elif doc.generate_type == "Based on Raw Material":
        raw_items = get_raw_materials(doc.work_order)
        for item in raw_items:
            serial = f"{item.item_code}-" + ''.join(random.choices(string.digits, k=6))
            row = doc.append("serial_numbers", {})
            row.serial_number = serial
            row.item = item.item_code

def get_raw_materials(work_order):
    return frappe.get_all("Work Order Item", filters={"parent": work_order}, fields=["item_code"])

