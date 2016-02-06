from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Add Wing",
					"description": _("Wing Info."),
				},
				{
					"type": "doctype",
					"name": "Add House Type",
					"description": _("House Type Info.")
				},
				{
					"type": "doctype",
					"name": "Add Owner",
					"description": _("Owner Database."),
				},
				{
					"type": "doctype",
					"name": "Add Tenent",
					"description": _("Tenent Database."),
				},
				{
					"type": "doctype",
					"name": "Add Property",
					"description": _("Property Database."),
				},
				{
					"type": "doctype",
					"name": "Add Shop",
					"description": _("Shop Database."),
				},
				{
					"type": "doctype",
					"name": "Body Member",
					"description": _("Body Member Database."),
				},
				{
					"type": "doctype",
					"name": "Meetings",
					"description": _("Meeting Information."),
				},
				{
					"type": "doctype",
					"name": "Notice",
					"description": _("Notice List."),
				},
				{
					"type": "doctype",
					"name": "Society",
					"description": _("Society Information."),
				},
				{
					"type": "doctype",
					"name": "Maintenance Type",
					"description": _("List of Maintenance Types."),
				},
				{
					"type": "doctype",
					"name": "Collection Type",
					"description": _("List of Collection Types."),
				},
				#{
				#	"type": "doctype",
				#	"name": "Dues",
				#	"description": _("Apply Dues."),
				#},
				
			]
		},
	]
