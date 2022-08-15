#!/bin/bash
for file in $(ls ./)
do 
    if [ "${file##*.}" = "sql" ]; then
        sed -i  ''  '1c\ 
insert into j_ds_bill_day_total (settle_date, bill_item_id, bill_object_id, pd_proj_code, ds_id, pd_merchant_cd, pd_prod_code, pd_prod_ver, fee_type, price, fee_quantity, total_price, settle_period_total_quantity, adjust_fee_quantity, adjust_price, adjust_total_price, adjust_settle_period_total_quantity, settle_start_date, create_time) values
' ${file}
    fi
done