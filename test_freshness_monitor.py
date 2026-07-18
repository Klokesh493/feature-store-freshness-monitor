import unittest

from freshness_monitor import stale_groups


class FreshnessMonitorTest(unittest.TestCase):
    def test_flags_stale_feature_group(self):
        rows = [{"feature_group": "risk", "age_minutes": "45", "max_age_minutes": "10"}]
        self.assertEqual(stale_groups(rows), ["risk"])


if __name__ == "__main__":
    unittest.main()
