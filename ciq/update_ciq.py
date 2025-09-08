#!/usr/bin/env python3
from db2pq import wrds_update_pq

# wrds_update_pq("wrds_gvkey", "ciq")
# wrds_update_pq("wrds_cusip", "ciq")
# wrds_update_pq("wrds_cik", "ciq")
wrds_update_pq("ciqfininstance", "ciq",
               col_types = {"financialinstanceid": "int32",
                            "financialperiodid": "int32",
                            "documentid": "int32"})
wrds_update_pq("ciqfincollection", "ciq",
               col_types = {"financialinstanceid": "int32",
                            "financialcollectionid": "int32"})                            
                            
wrds_update_pq("ciqfinperiod", "ciq")
wrds_update_pq("ciqgvkeyiid", "ciq")
wrds_update_pq("ciqfininstancetocollection", "ciq",
               col_types = {"financialinstanceid": "int32",
                            "financialcollectionid": "int32"})
