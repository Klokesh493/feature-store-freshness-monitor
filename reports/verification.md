# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 freshness_monitor.py sample_features.csv
payment_risk
test_flags_stale_feature_group (test_freshness_monitor.FreshnessMonitorTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
