#!/usr/bin/env python3
from db2pq import wrds_update_pq

# Auditors
wrds_update_pq("feed01_auditors", "audit", 
                      col_types={"auditor_key": "int32",
                                   "pcaob_reg_num": "int32",
                                   "pcaob_app_num": "int32",
                                   "aud_loc_key": "int32", 
                                   "auditor_pcaob_reg": "boolean"})

# Auditor Changes
wrds_update_pq("feed02_auditor_changes", "audit", 
                      col_types={"auditor_change_key": "int32",
                                   "dismiss_key": "int32",
                                   "file_accepted": "timestamp",
                                   "engaged_auditor_key": "int32",
                                   "dismissed_gc": "boolean", 
                                   "dismissed_disagree": "boolean", 
                                   "auditor_resigned": "boolean",
                                   "dismiss_pcaob_reg": "boolean",
                                   "merger": "boolean",
                                   "is_benefit_plan": "boolean",
                                   "aud_letter_disagree": "boolean", 
                                   "aud_letter_no_comm": "boolean",
                                   "aud_letter_agree": "boolean",
                                   "aud_co_disagree": "boolean",
                                   "engaged_auditor_pcaob": "boolean"}, 
                      drop="^(match|prior|closest|dismiss_name|" + 
                           "engaged_auditor_name|eventdate_aud_name)")

# Audit Fees
wrds_update_pq("feed03_audit_fees", "audit", 
                      drop="^(match|prior|closest)", 
                      col_types={"eventdate_aud_fkey": "int32",
                                   "file_accepted": "timestamp",
                                   "auditor_fkey": "int32", 
                                   "audit_gig_key": "int32",
                                   "fiscal_year": "int32",
                                   "restatement":"boolean",
                                   "fees_pcaob_reg":"boolean"})
               
# Audit Fees with Restatements
wrds_update_pq("feed04_audit_fees_restated", "audit",
                      drop="^(match|prior|closest)", 
                      col_types={"eventdate_aud_fkey": "int32", 
                                   "file_accepted": "timestamp",
                                   "auditor_fkey": "int32", 
                                   "audit_gig_key": "int32",
                                   "fiscal_year": "int32",
                                   "restatement":"boolean",
                                   "fees_pcaob_reg":"boolean"})

# Audit Opinions
wrds_update_pq("feed05_audit_opinions", "audit",
                      drop="^(match|prior|closest)", 
                      col_types={"audit_op_key": "int32", 
                                   "auditor_fkey": "int32",
                                   "file_accepted": "timestamp",
                                   "auditor_affil_fkey": "int32",
                                   "going_concern": "boolean",
                                   "op_aud_pcaob": "boolean",
                                   "eventdate_aud_fkey": "int32",
                                   "fiscal_year_of_op": "int32"})

wrds_update_pq("feed34_revised_audit_opinions", "audit",
                      drop="^(match|closest|prior)",
                      col_types={"audit_op_key": "int32", 
                                   "eventdate_aud_fkey": "int32",
                                   "integrated_audit": "boolean",
                                   "auditor_fkey": "int32",
                                   "auditor_affil_fkey": "int32",
                                   "is_nth_add_op": "int32",
                                   "going_concern": "boolean",
                                   "op_aud_pcaob": "boolean",
                                   "file_accepted": "timestamp",
                                   "eventdate_aud_fkey": "int32",
                                   "fiscal_year_of_op": "int32"})

wrds_update_pq("feed06_benefit_plan_opinions", "audit", 
                      drop="^(match|closest|prior)",
                      col_types={"benefit_plan_key": "int32", 
                                   "auditor_key": "int32",
                                   "is_nth_opinion": "int32",
                                   "op_aud_pcoab": "boolean",
                                   "going_concern": "boolean",
                                   "eventdate_aud_fkey": "int32"})

wrds_update_pq("feed07_current_auditor", "audit", 
                       col_types={"auditor_key": "int32"}) 

# Non-reliance restatements
wrds_update_pq("feed09_nonreliance_restatements", "audit", 
                        drop="^(match|closest|prior)",
                        col_types={"res_accounting": "boolean",
                                     "res_fraud": "boolean", 
                                     "res_cler_err": "boolean",
                                     "res_adverse": "boolean", 
                                     "res_improves": "boolean", 
                                     "res_other": "boolean",
                                     "res_sec_invest": "boolean",
                                     "res_begin_aud_fkey": "int32", 
                                     "res_notif_key": "int32", 
                                     "current_aud_fkey": "int32", 
                                     "res_begin_aud_fkey": "int32", 
                                     "res_end_aud_fkey": "int32",
                                     "file_accepted": "timestamp",
                                     "file_date_aud_fkey": "int32"})
 
# SOX 302 Disclosure Controls
wrds_update_pq("feed10_sox_302_disclosure_contro", "audit",
            drop="^(prior|match|closest)",
            col_types={"ic_dc_key": "int32", 
                       "is_effective": "int32",
                       "material_weakness": "boolean",
                       "sig_deficiency": "boolean",
                       "noteff_acc_rule": "int32",
                       "noteff_fin_fraud": "int32",
                       "notefferrors": "int32",
                       "noteff_other": "int32",
                       "eventdate_aud_fkey": "int32"})
                     
# SOX 404 Internal Controls
wrds_update_pq("feed11_sox_404_internal_controls", "audit",
                      drop="^(prior|match|closest)",
                        col_types={"ic_op_fkey": "int32",
                                     "auditor_fkey": "int32", 
                                     "eventdate_aud_fkey": "int32"})

# Accelerated Filer
wrds_update_pq("feed16_accelerated_filer", "audit",
                      drop="^(match|closest|prior)",
                      col_types={"accel_filer_key": "int32",
                                   "hst_season_issuer": "int32",   
                                   "hst_is_shell_co": "int32",                      
                                   "hst_is_accel_filer": "int32",     
                                   "hst_is_large_accel": "int32", 
                                   "hst_is_voluntary_filer": "int32", 
                                   "hst_is_small_report": "int32",   
                                   "did_not_disc": 'boolean',
                                   "file_accepted": "timestamp",
                                   "eventdate_aud_fkey": "int32"})

# Director and officer changes
wrds_update_pq("feed17_director_and_officer_chan", "audit",
                        drop="^(match|closest|prior|do_change_text)",
                        col_types={"do_off_pers_key": "int32",
                                     "do_change_key": "int32",
                                     "eventdate_aud_fkey": "int32",
                                     "file_accepted": "timestamp",
                                     "interim": 'boolean',
                                     "do_off_remains": 'boolean',
                                     "retain_other_pos": 'boolean',
                                     "eff_date_unspec": 'boolean', 
                                     "eff_date_next_meet": 'boolean',
                                     'is_c_level': 'boolean', 
                                     'is_bdmem_pers': 'boolean', 
                                     'is_legal': 'boolean', 
                                     'is_scitech_pers': 'boolean', 
                                     'is_admin_pers': 'boolean', 
                                     'is_fin_pers': 'boolean', 
                                     'is_op_pers': 'boolean', 
                                     'is_cont': 'boolean', 
                                     'is_chair': 'boolean', 
                                     'is_chair_other': 'boolean', 
                                     'is_secretary': 'boolean', 
                                     'is_coo': 'boolean', 
                                     'is_president': 'boolean', 
                                     'is_ceo': 'boolean', 
                                     'is_cfo': 'boolean', 
                                     'is_exec_vp': 'boolean'})
                                     
# Director and officer changes
wrds_update_pq("feed17_director_and_officer_chan", "audit",
                        keep="^(do_off_pers_key|do_change_text)$",
                        col_types={"do_off_pers_key": "int32"},
                        alt_table_name="feed17_do_change_text")

# Non-timely Filer Information And Analysis
wrds_update_pq("feed20_nt", "audit",
                      drop="^(match|closest|prior)",
                      col_types={"nt_notify_key": "int32",
                                 "ac_file_accepted": "timestamp",
                                 "eventdate_aud_fkey": "int32",
                                 "aud_at_file_date": "int32",
                                 "part2_c_check": "boolean", 
                                 "part2_b_check": "boolean",
                                 "part2_a_check": "boolean",
                                 "part4_3_check": "boolean",
                                 "file_accepted": "timestamp",
                                 "ten_k_trans_report": "boolean"})
