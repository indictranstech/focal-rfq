# Copyright (c) 2013, indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
from frappe.utils import cstr

class MaterialRFQ(Document):
	pass

@frappe.whitelist()
def get_csv():
	args = frappe.local.form_dict
	w = UnicodeWriter()
	w = add_header(w,args)
	w = add_data(w,args)
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Material RFQ"

def add_header(w,args):
	w.writerow(["Quotation No", "Part No", "Drawing No", "Mat Spec & Type", "Qty",
		"OD", "ID", "LG","Cost/Inch\nSCD","Cost/Inch\nUSD","Cost/PC\nSCD","Cost/PC\nSCD"])
	return w

def add_data(w,args):
	cl=frappe.get_doc("Material RFQ",args['doc']).material_rfq_details
	for c in cl:
		row = [
			c.quotation_no or "",
			c.part_no or "",
			c.drawing_no or "",
			c.mat_spec_type or "",
			c.qty or "",
			c.od or "",
			c.id or "",
			c.lg or "",
			c.Cost_per_inch_scd or "",
			c.Cost_per_inch_d or "",
			c.cost_per_pc_scd or "",
			c.cost_per_pc_d or ""
		]
		w.writerow(row)
	return w

	
		
