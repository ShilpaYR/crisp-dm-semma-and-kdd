# Data Understanding Report (2025-11-02T22:02:41+00:00)

## 1) Summary
- Shape: **421570 rows × 5 cols**
- Date range: **2010-02-05 00:00:00 → 2012-10-26 00:00:00**

## 2) Data Dictionary (saved to artifacts)
- `data_dictionary.csv` includes dtype, missingness, uniques, and stats.

## 3) Data Quality
- Duplicate rows: **0** (0.0000%)
- Invalid Weekly_Sales: **1285** (0.3048%)
- Weekly missing points (overall): **0** / 143 (0.0000)

- Segment-level weekly gaps saved: `segment_weekly_missing.csv`
## 4) Key EDA Artifacts (PNGs)
- `Weekly_Sales_hist.png`
- `Weekly_Sales_timeseries_top_segments.png`
- `Weekly_Sales_by_store_boxplot.png`

## 5) Acceptance Metrics (saved to `acceptance_metrics.csv`)
- overall_completeness_pct: **100.0000**
- per_column_completeness_pct: **{'Store': 100.0, 'Dept': 100.0, 'Date': 100.0, 'Weekly_Sales': 100.0, 'IsHoliday': 100.0}**
- duplicates_pct: **0.0000**
- invalid_Weekly_Sales_pct: **0.3048**
- weekly_missing_overall_ratio: **0.0000**
- iqr_outliers_count: **35521**
- iqr_outliers_pct: **8.4259**