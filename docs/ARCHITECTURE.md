# Feature Store Freshness Monitor architecture

Checks ML feature freshness and flags stale feature groups before serving incidents.

```mermaid
flowchart LR
    N0["sample_features.csv"]
    N1["freshness_monitor.py"]
    N2["stale / stale groups"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
