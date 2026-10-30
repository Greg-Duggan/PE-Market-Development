"""Rebuild everything: generate the data, run the analysis, write the outputs.

    python run_all.py
"""
from src import analysis, generate_data

if __name__ == "__main__":
    companies, contacts, log = generate_data.generate()
    results = analysis.run_analysis(companies, contacts, log)
    analysis.write_outputs(results)
    print("Done. See outputs/ for the ranked targets, next actions, charts, and the one-page summary.")
