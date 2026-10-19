# Exercise 6: Real-Time Operations Monitoring and Alerting

## Objective
Monitor delivery operations using Python, Prometheus, Grafana, and alert rules.

## Components
- delivery_metrics.py: Generates simulated delivery metrics.
- prometheus.yml: Configures Prometheus scraping.
- alert_rules.yml: Defines delivery alert thresholds.
- Grafana: Visualizes delivery metrics through a dashboard.

## Metrics
- Total deliveries
- Pending deliveries
- Deliveries on the way
- Average delivery time

## Alerts
- HighPendingDeliveries: Pending deliveries greater than 10 for 15 seconds.
- HighAverageDeliveryTime: Average delivery time greater than 30 seconds for 15 seconds.

## Verification
The Python metrics endpoint is available on port 8000. Prometheus successfully scrapes the delivery metrics, Grafana displays the four dashboard panels, and Prometheus lists both alert rules.

## Note
The alert rules are loaded but currently inactive because their firing conditions are not necessarily met.

## Conclusion
A delivery monitoring system was configured using Python, Prometheus, Grafana, and Prometheus alert rules.
