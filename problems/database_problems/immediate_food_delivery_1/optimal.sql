
SELECT
ROUND(
    (select count(*) from Delivery where order_date = customer_pref_delivery_date)
    /
    (select count(*) from Delivery) * 100.0,
    2
) AS immediate_percentage;
