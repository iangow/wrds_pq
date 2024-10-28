#!/usr/bin/env python3
from db2pq import wrds_update_pq 

wrds_update_pq("idsum", "ibes")
wrds_update_pq("statsum_epsus", "ibes",
col_types = {'acttims_act': 'string', 
             'anntims_act': 'string'})
wrds_update_pq("statsumu_epsus", "ibes")

wrds_update_pq("act_xepsus", "ibes", 
               col_types = {"acttims": "string", "anntims": "string"})
wrds_update_pq("act_epsus", "ibes",
               col_types = {"acttims": "string", "anntims": "string"})
wrds_update_pq("actpsum_epsus", "ibes")
