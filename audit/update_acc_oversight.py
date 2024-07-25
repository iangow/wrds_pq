#!/usr/bin/env python3
from db2pq import wrds_update_pq

# Auditor Changes
wrds_update_pq("feed55_auditor_ratification", "audit", 
               drop="^(match|prior|closest)",
               col_types={"auditor_ratification_fkey": "int32",
                                 "share_class_fkey": "int32",
                                 "auditor_fkey": "int32",
                                 "pcaob_registration_number": "int32"})
