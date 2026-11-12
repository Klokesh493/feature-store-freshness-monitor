# Feature Store Freshness Monitor walkthrough

## Business problem

A model can keep serving requests with stale features. Operators need to flag feature groups whose age exceeds their contract.

## Reproduce the workflow

Run `python3 freshness_monitor.py sample_features.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
payment_risk
```

The sample supplies these fields. `feature_group`, `age_minutes`, `max_age_minutes`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
