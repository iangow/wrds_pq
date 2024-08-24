#!/usr/bin/env python3
from db2pq import wrds_update_pq
import datetime

now = datetime.datetime.now()
avail_years = range(2000, now.year+1)

wrds_update_pq("rpa_entity_mappings", "ravenpack_common", sas_schema="rpa")

def update_equities(year):
    updated = wrds_update_pq("rpa_djpr_equities_" + str(year), "ravenpack_dj",
                             col_types = {"timestamp_utc": "timestamp",
                                          "rpa_time_utc": "string",
                                          "event_start_date_utc": "timestamp", 
                                          "event_end_date_utc": "timestamp", 
                                          "reporting_start_date_utc": "timestamp",
                                          "reporting_end_date_utc": "timestamp"},
                             sas_schema="rpa")
    return updated

updated = [ update_equities(year) for year in avail_years]
