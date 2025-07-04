-- 1. Top 5 customer areas with highest average delivery time in the last 30 days.
SELECT
    customer_area,
    AVG(delivery_time_min) AS avg_delivery_time
FROM deliveries
WHERE order_placed_at >= NOW() - INTERVAL 30 DAY
GROUP BY customer_area
ORDER BY avg_delivery_time DESC
LIMIT 5;

-- 2. Average delivery time per traffic condition, by restaurant area and cuisine type.
SELECT
    R.area AS restaurant_area,
    R.cuisine_type,
    D.traffic_condition,
    AVG(D.delivery_time_min) AS avg_delivery_time
FROM orders O
JOIN restaurants R ON O.restaurant_id = R.restaurant_id
JOIN deliveries D ON O.delivery_id = D.delivery_id
GROUP BY R.area, R.cuisine_type, D.traffic_condition
ORDER BY avg_delivery_time DESC;

-- 3. Top 10 delivery people with the fastest average delivery time,
--    considering only those with at least 50 deliveries and who are still active.
SELECT
    d.delivery_person_id,
    dp.name AS delivery_person_name,
    COUNT(*) AS total_deliveries,
    AVG(d.delivery_time_min) AS avg_delivery_time
FROM deliveries d
JOIN delivery_persons dp ON d.delivery_person_id = dp.delivery_person_id
WHERE dp.is_active
GROUP BY d.delivery_person_id, dp.name
HAVING total_deliveries >= 50
ORDER BY avg_delivery_time ASC
LIMIT 10;

-- 4. The most profitable restaurant area in the last 3 months,
--    defined as the area with the highest total order value.
SELECT
    r.area AS restaurant_area,
    SUM(o.order_value) AS total_order_value
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
JOIN deliveries d ON o.delivery_id = d.delivery_id
WHERE d.order_placed_at >= NOW() - INTERVAL 3 MONTH
GROUP BY r.area
ORDER BY total_order_value DESC
LIMIT 1;

-- 5. Identify delivery people who show an increasing trend (≥2 rises) in average delivery time.
WITH month_avg AS (
    SELECT
        delivery_person_id,
        DATE_FORMAT(order_placed_at, '%Y-%m') AS ym,
        AVG(delivery_time_min) AS avg_time,
        LAG(AVG(delivery_time_min)) OVER (
            PARTITION BY delivery_person_id
            ORDER BY DATE_FORMAT(order_placed_at, '%Y-%m')
        ) AS prev_time
    FROM deliveries
    GROUP BY delivery_person_id, DATE_FORMAT(order_placed_at, '%Y-%m')
),
inc_counter AS (
    SELECT
        delivery_person_id,
        SUM(avg_time > prev_time) AS inc_months,
        COUNT(*) AS n_months
    FROM month_avg
    WHERE prev_time IS NOT NULL
    GROUP BY delivery_person_id
)
SELECT delivery_person_id, inc_months
FROM inc_counter
WHERE inc_months >= 2
ORDER BY inc_months DESC;