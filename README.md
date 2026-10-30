# Market Development Toolkit

**Thesis-driven market mapping, target screening, and outreach analytics for a private equity sourcing team, built with SQL and Python on fictional data.**

> **All companies, people, and numbers in this repository are randomly generated.** The investment thesis is an illustration, not any firm's criteria. The project demonstrates a workflow, not market facts.

## What it does

A market development analyst typically answers three questions. This project answers each one with reproducible code.

| Question | How it is answered |
|---|---|
| **Where should we look?** | A SQL market map of six software subverticals: size, growth, margins, sponsor penetration, concentration, and addressable targets |
| **Who should we call first?** | A hard thesis screen, then a 0-100 fit score with tiers, plus a sensitivity analysis showing how stable the shortlist is when the weights change |
| **How is outreach going?** | Funnel conversion, channel and owner performance with confidence intervals, and a rule-based next action for every best-fit target |

Start with the executed notebook, which GitHub renders with its charts: [`notebooks/01_market_map_and_target_screen.ipynb`](notebooks/01_market_map_and_target_screen.ipynb). A one-page summary is in [`outputs/summary_one_pager.md`](outputs/summary_one_pager.md).

## Results on the fictional data (seed 42)

- **The screen.** 400 companies; 101 (25%) pass every criterion (revenue band, growth, recurring revenue, EBITDA margin, ownership).
- **The map.** *Construction project software* has the most addressable targets (43), 23.8% median growth, and only 9% PE-backed companies. *Dental & specialty practice* is the most crowded at 53% PE-backed.
- **The shortlist.** 31 tier A companies out of 283 actionable (founder-owned or VC-backed). Under four alternative weightings, 17 to 21 of the top 25 stay the same (rank correlation 0.86 to 0.97).
- **The funnel.** 158 companies contacted, 52 replied (33%), 28 interested, 16 intro calls, 6 management meetings, 2 NDAs.
- **What works.** Warm intros replied 44% of the time (n=16, 95% interval 23% to 67%) versus LinkedIn at 7% (n=76, 3% to 14%). Those intervals do not overlap. Differences between team members do overlap, so they are not read as performance.
- **Wasted effort.** 25 of 158 contacted companies (16%) already have a PE sponsor or a strategic parent.
- **Coverage gaps.** 22 of the 31 tier A companies need action now (find a contact, start outreach, or re-engage a stale thread).

![Market map](outputs/charts/02_market_map.png)

| | |
|---|---|
| ![Screen funnel](outputs/charts/01_screen_funnel.png) | ![Outreach funnel](outputs/charts/05_outreach_funnel.png) |

## Repository structure

```
data/                 companies.csv, contacts.csv, outreach_log.csv (generated, seed 42)
sql/                  01_thesis_screen, 02_market_map, 03_pipeline_funnel,
                      04_channel_and_owner_performance, 05_coverage_gaps
src/
  generate_data.py    fictional dataset (companies, contacts, dated outreach events) with integrity checks
  scoring.py          fit score, tiers, and weight sensitivity
  db.py               loads the data into SQLite and runs the .sql files
  analysis.py         runs everything, writes outputs, 95% Wilson intervals
  charts.py           matplotlib charts
notebooks/            executed analysis notebook
outputs/              ranked_targets.csv, next_actions.csv, weight_sensitivity.csv, charts/, summary_one_pager.md
tests/                scoring rules, data integrity, and SQL-vs-pandas cross-checks
run_all.py            regenerates the data and every output
```

## How to run

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_all.py                                       # rebuild data and outputs
jupyter notebook notebooks/01_market_map_and_target_screen.ipynb
pytest                                                  # 24 tests
```

## Method in brief

- **Data.** 400 fictional software companies in six subverticals, 553 contacts, and a dated outreach log. Subverticals differ in growth, margins, and sponsor penetration, so the analysis has something to find. Each row has a data-confidence flag, as estimates would in real life.
- **Screen.** Sequential criteria in SQL (revenue band, growth, recurring revenue, EBITDA margin, ownership) so you can see which one removes the most companies.
- **Score.** Six criteria worth 100 points (size 20, growth 25, recurring 15, profitability 15, ownership 15, market 10). Tiers: A at 85, B at 72, C at 58. Sponsor-backed and strategic-owned companies are scored for context but not ranked.
- **Sensitivity.** The weights are judgment calls, so the shortlist is re-computed under four alternative weightings and compared with the base case.
- **Outreach.** Each company's furthest stage comes from the event log. Channel and owner rates carry Wilson intervals because the samples are small.
- **Next actions.** Explicit rules assign each best-fit company one action: find a contact, start outreach, follow up, re-engage, park, or in progress.

## Skills demonstrated

SQL (CTEs, window functions, conditional aggregation, joins, a median without `MEDIAN()`), Python (pandas, matplotlib), testing (pytest, including checks that the SQL agrees with an independent pandas calculation), statistics (confidence intervals on small samples, sensitivity analysis), and communication (an executed notebook and a one-page summary).

## Limitations and next steps

- The data is synthetic. Real sourcing data would be messier: missing values, stale records, and conflicting estimates.
- Reply rates come from small samples, and the scoring weights are judgment calls.
- Next steps: a time dimension to track quarter-over-quarter movement, a text-based screen that classifies companies from website descriptions, and a CRM export connection.

## License

MIT. See [LICENSE](LICENSE).
