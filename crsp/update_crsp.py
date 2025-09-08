#!/usr/bin/env python3
from db2pq import wrds_update_pq

# Update Treasury yield table crsp.tfz_ft
# From WRDS:
# The error is correct, the table "tfz_ft," does not exist. Behind the scenes this web
# query form is joining two tables on the fly. The tables this query is joining are
# "crsp.tfz_idx" and either "crsp.tfz_dly_ft" or "crsp.tfz_mth_ft" (depending on if
# you want daily or monthly data) by the variable "kytreasnox."

# Here are some links to the information about these tables:
# https://wrds-web.wharton.upenn.edu/wrds/tools/variable.cfm?library_id=137&file_id=77140
# https://wrds-web.wharton.upenn.edu/wrds/tools/variable.cfm?library_id=137&file_id=77137
# https://wrds-web.wharton.upenn.edu/wrds/tools/variable.cfm?library_id=137&file_id=77147
wrds_update_pq("tfz_idx", "crsp")
wrds_update_pq("tfz_dly_ft", "crsp")

wrds_update_pq("mse", "crsp")

# Update monthly data
wrds_update_pq("msf", "crsp", 
            col_types = {'permno':'int32', 'permco':'int32'})

wrds_update_pq("msi", "crsp")

wrds_update_pq("msedelist", "crsp")

wrds_update_pq("ermport1", "crsp", 
            col_types = {'permno':'int32', 'capn':'int32'})

# Update daily data
wrds_update_pq("dsf", "crsp", 
               col_types = {'permno':'int32', 'permco': 'int32'})

wrds_update_pq("dsi", "crsp")

wrds_update_pq("dsedelist", "crsp",
               col_types = {'permno':'int32', 'permco': 'int32'})

wrds_update_pq("erdport1", "crsp",
               col_types = {'permno':'int32', 'capn': 'int32'})

wrds_update_pq("ccmxpf_linktable", "crsp",
                                col_types = {'lpermno':'int32', 
                                             'lpermco': 'int32',
                                             'usedflag': 'int32'})
    
wrds_update_pq("ccmxpf_lnkhist", "crsp", 
               col_types = {'lpermno':'int32', 
                            'lpermco': 'int32'})

wrds_update_pq("dsedist", "crsp",
                      col_types = {'permno':'int32',
                                   'permco':'int32'})
wrds_update_pq("dse", "crsp",
                      col_types = {'permno':'int32',
                                   'permco':'int32'})

wrds_update_pq("stocknames", "crsp",
                          col_types = {'permno':'int32', 
                                       'permco': 'int32'})
                                            
wrds_update_pq("dseexchdates", "crsp",
                           col_types = {'permno':'int32', 
                                        'permco': 'int32'})

# Update other data sets
wrds_update_pq("msp500list", "crsp")
wrds_update_pq("ccmxpf_lnkused", "crsp")

wrds_update_pq("dsp500", "crsp")
wrds_update_pq("dsp500p", "crsp")
wrds_update_pq("msp500", "crsp")
wrds_update_pq("msp500p", "crsp")
wrds_update_pq("mcti", "crsp")
wrds_update_pq("mcti_corr", "crsp")
wrds_update_pq("msedist", "crsp")
wrds_update_pq("mseshares", "crsp")
wrds_update_pq("comphist", "crsp")
