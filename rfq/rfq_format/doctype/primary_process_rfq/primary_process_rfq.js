frappe.provide("rfq.rfq_format");
rfq.rfq_format.PrimaryProcessRFQ = frappe.ui.form.Controller.extend({
	
	refresh: function() {
		this.frm.dashboard.reset();
		cur_frm.add_custom_button(__('Export RFQ'), cur_frm.cscript.export_data, "icon-download", true);
	},
	export_data:function(doc,cdt,cdn){
		window.location.href = repl(frappe.request.url +
			'?cmd=%(cmd)s&doc=%(doc)s', {
			cmd: "rfq.rfq_format.doctype.primary_process_rfq.primary_process_rfq.get_csv",
			doc: cur_frm.docname,
		
		});
	}

});
$.extend(cur_frm.cscript, new rfq.rfq_format.PrimaryProcessRFQ({frm: cur_frm}));
