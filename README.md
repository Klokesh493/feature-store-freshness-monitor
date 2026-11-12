# Feature Store Freshness Monitor

A model can keep serving requests with stale features. Operators need to flag feature groups whose age exceeds their contract.

## What I built

I built a feature-contract check that compares each group's observed age in minutes to its own maximum age. The output lists groups strictly above their limit for operator review.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [freshness_monitor.py](freshness_monitor.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 freshness_monitor.py sample_features.csv
```

The sample flags payment_risk as stale. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 freshness_monitor.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The ages are supplied by the caller. The CLI does not fetch timestamps or monitor a live feature store.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
