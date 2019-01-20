// Copyright (c) 2019, Beshoy Atef and contributors
// For license information, please see license.txt

frappe.ui.form.on('ESR',"amount",
	function(frm,cdt,cdn) {
														 


								var salry                 = frm.doc.salary ;
								var end_of_service_reason = frm.doc.end_of_service_reason ;
								var years                 = frm.doc.employment_period ;
								var months                = frm.doc.month ;
								var days                = frm.doc.days ;
								if(salry ,end_of_service_reason , years,months) {
							 	frappe.call({
								 		"method":"esr.esr.doctype.esr.esr.getsalry",
								 		args:{
								 			salry                 : salry,
								 			leave                 : end_of_service_reason,
								 			years                 : years,
								 			months                : months,
								 			days                  : days, 
								 		},

                                callback: function(data){
                                	frappe.model.set_value(cdt,cdn,"esr_amount",data.message);
                                	frappe.msgprint("esr amount = "+data.message+ "");

                                }


												 	})}
							 	else{
							 		frappe.msgprint("plesae complete the form ")
							 	


							  
				

      						 
                                       };   





	}
);
