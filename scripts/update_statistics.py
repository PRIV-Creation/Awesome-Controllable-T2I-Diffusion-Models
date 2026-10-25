"""Regenerate the README chart and auditable statistics from the catalog.

Run: python scripts/update_statistics.py --as-of YYYY-MM-DD
Requires matplotlib==3.9.4. Bibliographic dates are retained in data/paper_dates.json.
"""

import argparse
from collections import Counter
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from catalog import read_catalog


ROOT = Path(__file__).resolve().parents[1]


def build(as_of: str, check: bool = False):
    cutoff = date.fromisoformat(as_of)
    papers, entry_count = read_catalog(ROOT / "README.md")
    dates = json.loads((ROOT / "data/paper_dates.json").read_text())
    rows = []
    for key, paper in sorted(papers.items()):
        if key not in dates:
            raise ValueError(f"Missing release-date evidence: {key} {paper.title}")
        evidence = dates[key]
        year = int(evidence["date"][:4])
        if year > cutoff.year or (len(evidence["date"]) == 10 and date.fromisoformat(evidence["date"]) > cutoff):
            raise ValueError(f"Future-dated paper: {key}")
        rows.append({"identifier": key, "title": paper.title, "year": year,
                     "date": evidence["date"], "date_basis": evidence["basis"],
                     "date_source": evidence["source"],
                     "categories": " | ".join(sorted(paper.categories)), "paper_url": paper.url})
    years = Counter(row["year"] for row in rows)
    categories = Counter(category for paper in papers.values() for category in paper.categories)
    summary = {"as_of": as_of, "unique_papers": len(papers), "category_entries": entry_count,
               "cross_listed_entries": entry_count - len(papers),
               "by_year": {str(y): years[y] for y in range(min(years), cutoff.year + 1)},
               "by_category": dict(sorted(categories.items())),
               "date_basis": dict(sorted(Counter(row["date_basis"] for row in rows).items())),
               "readme_sha256": hashlib.sha256((ROOT / "README.md").read_bytes()).hexdigest()}
    assert sum(summary["by_year"].values()) == len(papers)
    assert sum(categories.values()) == entry_count
    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    outputs = {ROOT / "data/paper-statistics.json": json.dumps(summary, indent=2) + "\n",
               ROOT / "data/paper-statistics.csv": csv_buffer.getvalue()}
    if check:
        for path, expected in outputs.items():
            if not path.exists() or path.read_text() != expected:
                raise ValueError(f"Stale generated statistics: {path.relative_to(ROOT)}")
        print(f"Statistics current: {len(papers)} papers / {entry_count} category entries")
        return
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                         "text.color": "#252b35", "axes.labelcolor": "#515b6a"})
    fig, ax = plt.subplots(figsize=(12, 6.1), dpi=180)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.73, bottom=0.23)
    labels = list(summary["by_year"])
    values = list(summary["by_year"].values())
    bars = ax.bar(labels, values, width=0.64, color="#4974ad", zorder=3)
    ax.set_ylim(0, max(values) * 1.2)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
    ax.grid(axis="y", color="#e6eaf0", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    ax.set_ylabel("Unique papers", labelpad=12)
    ax.tick_params(axis="both", length=0, pad=10, labelcolor="#515b6a")
    for name, spine in ax.spines.items():
        spine.set_visible(name == "bottom")
        spine.set_color("#bec6d1")
    ax.bar_label(bars, labels=[str(v) for v in values], padding=7, fontsize=15, fontweight="medium")
    fig.text(0.08, 0.92, "Papers in the collection", fontsize=25, fontweight="bold")
    fig.text(0.08, 0.84, f"{len(papers):,} unique papers", fontsize=18, color="#4974ad")
    fig.text(0.97, 0.85, f"Updated {as_of}", fontsize=12, color="#657184", ha="right")
    fig.text(0.08, 0.12, "Year of first arXiv submission; publication year for papers without arXiv.", fontsize=11, color="#657184")
    fig.text(0.08, 0.07, f"Cross-listed papers count once. {cutoff.year} includes records through {as_of}.", fontsize=11, color="#657184")
    fig.savefig(ROOT / "assets/count.png", facecolor="white", metadata={"Software": "scripts/update_statistics.py"})
    plt.close(fig)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build(args.as_of, args.check)
