# Copyright (c) 2013, indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
from frappe.utils import cstr

class PrimaryProcessRFQ(Document):
	pass

@frappe.whitelist()
def get_csv():
	args = frappe.local.form_dict
	w = UnicodeWriter()
	w = add_header(w,args)
	w = add_data(w,args)
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Primary Process RFQ"

def add_header(w,args):
	w.writerow(["Quotation No", "Part No", "Drawing No", "Mat Spec & Type", "Qty","Primary Process","Unit Cost"])
	return w

def add_data(w,args):
	cl=frappe.get_doc("Primary Process RFQ",args['doc']).primary_process_rfq_details
	for c in cl:
		row = [
			c.quotation_no or "",
			c.part_no or "",
			c.drawing_no or "",
			c.mat_spec__type or "",
			c.qty or "",
			c.primary_process or "",
			c.unit_cost or ""
		]
		w.writerow(row)
	return w