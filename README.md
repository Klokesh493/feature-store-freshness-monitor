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

## Business problem

A model can keep serving requests with stale features. Operators need to flag feature groups whose age exceeds their contract.

## Project walkthrough

```mermaid
flowchart LR
    A["Feature age and maximum allowed age"]
    B["Compare each feature group to its freshness limit"]
    C{"Age exceeds limit?"}
    D["Emit stale feature group"]
    E["Omit fresh group"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 freshness_monitor.py sample_features.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
