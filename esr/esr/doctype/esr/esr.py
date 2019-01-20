# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from __future__ import division 
import frappe
from frappe.model.document import Document

class ESR(Document):
	def validate(self):
			if self.month and self.salary and self.end_of_service_reason and self.employment_period :
				self.esr_amount =getsalry(self.salary,
									      self.end_of_service_reason,
									      self.employment_period,
									      self.month)




def cal_esr(salry , years , months,day):
	day_pre   = float(day) / 348
	month_pre = float(months) / float(12)
	total     = float(years) + float(month_pre)+float(day_pre)
	if total < 5:
		esr   = (float(total) * 0.5)*float(salry)
		return total ,esr
	if total > 5 :
		esr   = ((5 * float(salry))/2)+ ((float(total)-5)*float(salry))
		return	total ,esr
	



@frappe.whitelist()
def getsalry(salry=None,leave=None ,
			 years=None,months=None,
			 days=None):	
	try :
		month = int(months)
	except:
		month =0
	try :
		day = int(days)
	except:
		day = 0
	if salry and leave and years:
		if leave==u"استقالة العامل":
			total, leave = cal_esr(salry ,years , month,day)
			if total < 2 :
			      return str(None)
			if total > 2 and total < 5 :
				esr = float(leave)/3
				return str(esr)
			if total >5 and total <10 :
				esr = float(leave)*(2/3)
				return str(esr)
			if total > 10 :
				esr = float(leave)
				return str(esr)
		
		else:
			total , leave = cal_esr(salry ,years , month,day)
			return str(leave)
	else: return str("please complete the form")
	
