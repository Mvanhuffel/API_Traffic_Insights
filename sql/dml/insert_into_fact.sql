--Fact table
INSERT INTO fact_transactions (customer_id, service_id, time_id, partner_id, status_id, transaction_count, bytes_sent, bytes_received)
SELECT
  dc.customer_id,
  ds.service_id,
  dt.time_id,
  dp.partner_id,
  dst.status_id,
  st.transaction_count,
  st.bytes_sent,
  st.bytes_received
FROM
  staging_traffic_data st
  JOIN dim_customer dc ON dc.customer_name = st.customer AND dc.active_flag = TRUE
  JOIN dim_service ds ON ds.servicename = st.servicename AND ds.active_flag = TRUE
  JOIN dim_time dt ON dt.transaction_date = st.transaction_date AND dt.hour = st.hour AND dt.active_flag = TRUE
  JOIN dim_partner dp ON dp.partner_name = st.partner AND dp.active_flag = TRUE
  JOIN dim_status dst ON dst.status = st.status AND dst.final_status = st.final_status AND dst.active_flag = TRUE;