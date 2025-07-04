## Additional SQL Insights

1.  Which day of the week has the highest frequency of late deliveries?

Identifying if specific days consistently have more late deliveries helps the Operations team optimize staffing and fleet distribution accordingly.

This analysis could reveals whether delivery performance is uneven across the week. 
For example, if Fridays and Sundays show more late deliveries, it may be due to peak demand with insufficient staff coverage or traffic congestion.

SELECT
  DAYNAME(order_placed_at) AS day_of_week,
  COUNT(*) AS total_orders,
  SUM(delivery_time_min > 60) AS late_deliveries,
  ROUND(AVG(delivery_time_min), 1) AS avg_time
FROM deliveries
GROUP BY day_of_week
ORDER BY late_deliveries DESC;

2. What time of day have the most delivery delays?

Identifying peak hours for delays allows the Ops team to reinforce courier availability in those hours and adjust real-time estimates during those windows.
This would help figure if delays are concentrated in specific time ranges. Which often align with urban congestion or high kitchen load.

SELECT
  HOUR(order_placed_at) AS hour_of_day,
  COUNT(*) AS total_deliveries,
  AVG(delivery_time_min) AS avg_delivery_time
FROM deliveries
WHERE order_placed_at >= NOW() - INTERVAL 30 DAY
GROUP BY hour_of_day
ORDER BY avg_delivery_time DESC;

3. Which restaurants act as bottlenecks in the delivery chain?

Restaurants with excessive handoff times can delay even short-distance deliveries. Identifying these early allows the platform to trigger operational interventions.
The query compares each restaurant’s average preparation time with the average total delivery time for their orders. A large gap may indicate that delays are occurring after the food is ready—potentially in handoff coordination or pickup queuing.

SELECT
  r.name,
  r.area,
  r.avg_preparation_time_min,
  AVG(d.delivery_time_min) AS delivery_avg_time,
  AVG(d.delivery_time_min) - r.avg_preparation_time_min AS delay_over_prep
FROM orders o
JOIN deliveries d ON o.delivery_id = d.delivery_id
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_id
HAVING COUNT(*) >= 30
ORDER BY delay_over_prep DESC
LIMIT 10;

4. Which traffic levels cause the greatest delay per kilometer?

Measuring how much time is added per kilometer under different traffic conditions helps the Ops team recalibrate ETA formulas, and define which traffic levels require surge pricing or dynamic routes.

WITH traffic_efficiency AS (
  SELECT
    traffic_condition,
    SUM(delivery_time_min) AS total_time,
    SUM(delivery_distance_km) AS total_km
  FROM deliveries
  WHERE delivery_distance_km > 0
  GROUP BY traffic_condition
)
SELECT
  traffic_condition,
  ROUND(total_time / total_km, 2) AS minutes_per_km
FROM traffic_efficiency
ORDER BY minutes_per_km DESC;