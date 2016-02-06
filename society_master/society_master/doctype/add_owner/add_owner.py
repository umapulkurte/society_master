# Copyright (c) 2013, Wayzon Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import sendmail

class AddOwner(Document):
	def on_submit(self):
		email=self.email_id
		def mail_send(email_id,n_password):
			
			#======Send Welcome Mail=============================================================
			receiver = self.email_id
			new_rv=self
			#ath = frappe.get_doc("Add Owner","OW001")
			#receiver = 'umapulkurte@gmail.com'
			if receiver:
				subj = 'Owner Details :- '
				sendmail([receiver], subject=subj, 
				message = 'Welcome to SatyaPuram Society'+'\n'+'\nYour Login Details Are:\n'+'\nEmail Id:'+ email_id +'\n'+'\nPassword:\n' + n_password +'\n'+'\nPlease Find Attachment of your House Details'+'\n'+'\nThanks & Regards,'+'\n'+'\nSatyaPuram Society',
				attachments=[frappe.attach_print(new_rv.doctype, new_rv.name, file_name=new_rv.name, print_format='')])
				frappe.msgprint("Mail Send")
			else:
				frappe.msgprint(_("Email ID not found, hence mail not sent"))
			#====================================================================================
			
		if(self.email_id):
			mail_send(email,'fkljghlsdfghsl')
		else:
			frappe.msgprint("Welcome Mail Not sent")
		

	def validate(self):
		name=self.owner_name
		email=self.email_id
		c=frappe.db.sql("""select email_id from `tabContact` where first_name=%s and email_id=%s""",(name,email))
		if c:
			frappe.msgprint("Entered Name and Email id already exists!")
		else:
			n=frappe.db.sql("""select max(cast(name as int)) from `tabContact`""")[0][0]
			if n:
				num=int(n)+1
			else:
				num=1
			s=frappe.db.sql("""insert into `tabContact` set name=%s,first_name=%s, email_id=%s""",(num,name,email))

@frappe.whitelist()
def check_house(l,w,h):
	q=frappe.db.sql("""select house_no from `tabAdd Owner` where house_no=%s and select_lane=%s and select_htype=%s""",(l,w,h))
	if q:
		frappe.msgprint("Selected house is already allocated")
		return(q)
	else:
		return 0
		#q1=frappe.db.sql("""select house_no from `tabAdd Tenent` where house_no=%s and lane_no=%s and house_type=%s""",(l,w,h))
		#if q1:
		#	frappe.msgprint("Selected house is already allocated")
		#	return (q1)


@frappe.whitelist()
def mail_send():
	#======Send Scheduled Mail=============================================================
	#receiver = email_id = self.email_id
	n_password = '12345'
	new_rv=self
	#ath = frappe.get_doc("Add Owner","OW001")
	receiver = email_id = 'wayzonwitherpnext@gmail.com'
	if receiver:
		subj = 'Owner Details :- '
		sendmail([receiver], subject=subj, 
			message = 'Welcome to SatyaPuram Society'+'\n'+'\nYour Login Details Are:\n'+'\nEmail Id:'+ email_id +'\n'+'\nPassword:\n' + n_password +'\n'+'\nPlease Find Attachment of your House Details'+'\n'+'\nThanks & Regards,'+'\n'+'\nSatyaPuram Society',
			attachments='')
		frappe.msgprint("Mail Send Successfully")
	else:
		frappe.msgprint(_("Email ID not found, hence mail not sent"))

	if(self.email_id):
		mail_send(email,'fkljghlsdfghsl')
	else:
		frappe.msgprint("Mail not sent")
	#====================================================================================