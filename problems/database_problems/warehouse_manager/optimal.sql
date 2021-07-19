SELECT name AS warehouse_name, SUM(units*Width*Length*Height) AS volume
FROM
Warehouse -- Warehouse_name | product_id | units | product_id | product_name | Width | Length | Height
    LEFT JOIN Products ON Warehouse.product_id = Products.product_id
GROUP BY warehouse_name