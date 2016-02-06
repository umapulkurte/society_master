# Copyright (c) 2013, Wayzon Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AddTenent(Document):
	pass
@frappe.whitelist()
def check_house(l,w,h):
	q=frappe.db.sql("""select house_no from `tabAdd Owner` where house_no=%s and select_lane=%s and select_htype=%s""",(l,w,h))
	if q:
		frappe.msgprint("Selected house is already allocated")
		return (q)
	else:
		q1=frappe.db.sql("""select house_no from `tabAdd Tenent` where house_no=%s and lane_no=%s and house_type=%s""",(l,w,h))
		if q1:
			frappe.msgprint("Selected house is already allocated")
			return (q1)