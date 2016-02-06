cur_frm.cscript.mobile_no=function(doc,cdt,cdn)
{
	var n = doc.mobile_no;
	if((n.length)!=10)
	{
		cur_frm.set_value('mobile_no','')
		frappe.throw("Enter 10 digit no.");
	}

}