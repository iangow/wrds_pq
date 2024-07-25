#!/usr/bin/env python3
from db2pq import wrds_update_pq

# Auditor Changes
wrds_update_pq("feed55_auditor_ratification", "audit", 
               drop="^(match|prior|closest)",
               col_types={"auditor_ratification_fkey": "int32",
                                 "share_class_fkey": "int32",
                                 "auditor_fkey": "int32",
                                 "pcaob_registration_number": "int32"})


wrds_update_pq("feed56_accounting_estimates_chan", "audit", 
               drop="^(match|prior|closest)",
               col_types={"accounting_estimates_cha_fke": "int32"})

wrds_update_pq("feed65_impairments", "audit",
               drop="^(match|prior|closest)",
               col_types={"mtrl_imprmnt_fct_key": "int32",
                          "mtrl_imprmnt_key": "int32",
                          "quantitative_taxonomy_fkey": "int32",
                          "eventdate_aud_fkey": "int32",
                          "is_range": "boolean",
                          "is_final": "boolean"})

wrds_update_pq("feed74_aqrm", "audit",
               drop="^(match|prior|closest)",
               col_types={"flag_year": "int32",
                          "fye_of_opinion": "int32",
                          "ideal_fye_of_opinion": "int32"})

wrds_update_pq("feed78_critical_audit_matters", "audit", 
               col_types={"audit_opinion_fkey": "int32",
                          "auditor_fkey": "int32",
                          "critical_audit_matter_key": "int32",
                          "critical_audit_matter_topic_fkey": "int32"})

wrds_update_pq("feed85_cybersecurity", "audit", 
               col_types={"cybersecurity_breach_key": "int32",
                          "number_of_records_lost": "int64"},
               drop="^(match|prior|closest)")


wrds_update_pq("feed86_audit_firm_events", "audit",
               drop="^(match|prior|closest)")

wrds_update_pq("feed89_pcaob_report", "audit",
               col_types={"auditor_report_key": "int32",
                          "auditor_affiliate_fkey": "int32",
                          "inspection_year": "int32",
                          "auditor_fkey": "int32",
                          "has_firm_signed": "boolean",
                          "has_written_response": "boolean",
                          "is_clean_report": "boolean"})

wrds_update_pq("feed91_aaer", "audit",
               col_types={"aaer_event_key": "int32",
                          "first_release_fkey": "int32",
                          "most_recent_release_fkey": "boolean"})
