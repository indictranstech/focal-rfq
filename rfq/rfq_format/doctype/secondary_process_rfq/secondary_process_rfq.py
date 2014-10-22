# Copyright (c) 2013, indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
from frappe.utils import cstr

class SecondaryProcessRFQ(Document):
	pass

@frappe.whitelist()
def get_csv():
	args = frappe.local.form_dict
	w = UnicodeWriter()
	w = add_header(w,args)
	w = add_data(w,args)
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Secondary Process RFQ"

def add_header(w,args):
	w.writerow(["Quotation No", "Part No", "Drawing No", "Mat Spec & Type", "Qty","Secondary Process","Unit Cost"])
	return w

def add_data(w,args):
	cl=frappe.get_doc("Secondary Process RFQ",args['doc']).secondary_process_rfq_details
	for c in cl:
		row = [
			c.quotation_no or "",
			c.part_no or "",
			c.drawing_no or "",
			c.mat_spec__type or "",
			c.qty or "",
			c.secondary_process or "",
			c.unit_cost or ""
		]
		w.writerow(row)
	return w