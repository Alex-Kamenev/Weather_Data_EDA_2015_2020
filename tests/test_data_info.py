import unittest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from edapy.datainfo import DataInfo
from edapy import plot


class DataInfoTests(unittest.TestCase):
    def test_midpoint_preserves_observed_temperatures_for_other_station(self):
        df = pd.DataFrame({"DATE": ["2020-01-01"] * 2, "TMIN": [0.0, 20.0], "TMAX": [10.0, 30.0], "TAVG": [None, 23.0]})
        DataInfo(df).half_sum_fill_in_missing("TAVG")
        self.assertEqual(df["TAVG"].tolist(), [5.0, 23.0])

    def test_date_mean_with_no_observation_stays_missing(self):
        df = pd.DataFrame({"DATE": ["2020-01-01"], "TAVG": [float("nan")]})
        DataInfo(df).average_fill_in_missing(["TAVG"])
        self.assertTrue(pd.isna(df.loc[0, "TAVG"]))

    def test_correlation_plot_accepts_station_names_and_dates(self):
        df = pd.DataFrame({"NAME": ["A", "B", "A"], "DATE": ["2020-01-01"] * 3, "TMIN": [0.0, 2.0, 4.0], "TMAX": [10.0, 12.0, 14.0]})
        plot.heat_map(df)
        plt.close("all")


if __name__ == "__main__":
    unittest.main()
