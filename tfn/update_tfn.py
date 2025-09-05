#!/usr/bin/env python3
from db2pq import wrds_update_pq

updated = wrds_update_pq("amend", "tfn")
updated = wrds_update_pq("avgreturns", "tfn", 
                         col_types = {"buycount": "float8"})
updated = wrds_update_pq("company", "tfn")
updated = wrds_update_pq("form144", "tfn")
updated = wrds_update_pq("header", "tfn")
updated = wrds_update_pq("idfhist", "tfn")
updated = wrds_update_pq("idfnames", "tfn")
updated = wrds_update_pq("rule10b5", "tfn")
updated = wrds_update_pq("table1", "tfn")
updated = wrds_update_pq("table2", "tfn")
updated = wrds_update_pq("s12type1", "tfn")
updated = wrds_update_pq("s12type2", "tfn")
updated = wrds_update_pq("s34", "tfn")
updated = wrds_update_pq("s34type1", "tfn")
updated = wrds_update_pq("s34type2", "tfn")
