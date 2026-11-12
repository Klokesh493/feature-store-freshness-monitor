# Feature Store Freshness Monitor

Checks ML feature freshness and flags stale feature groups before serving incidents.

Focus: AI/ML platform reliability.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 freshness_monitor.py sample_features.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.
