# Catalog statistics

`README.md` contains the maintained paper entries. `paper-statistics.csv` has one row per unique paper, including its bibliography link, date source, and all categories. `paper-statistics.json` contains the counts and a SHA-256 of the README used to calculate them.

Identity uses the version-independent arXiv ID, then DOI, then the normalized title. This preserves distinct accepted papers that share a conference-program URL. A paper listed in several categories contributes one paper to the total and one membership to each relevant category. The parser rejects repeated entries within a category and identical normalized titles with conflicting identifiers so maintainers can resolve possible duplicates.

The chart groups papers by the year of their first arXiv submission. `paper_dates.json` records those dates from the arXiv API's `published` field, which is distinct from the latest revision date. For a paper without an identified arXiv record, the chart uses its verified publication or announced conference year. Accepted papers carry an explicit status in the catalog. The last year is partial through the displayed update date. The figure describes this collection's coverage.

After adding or correcting entries, add the corresponding date evidence and regenerate:

```sh
uv run --with matplotlib==3.9.4 python scripts/update_statistics.py --as-of YYYY-MM-DD
uv run --with matplotlib==3.9.4 python scripts/update_statistics.py --as-of YYYY-MM-DD --check
```

Python with matplotlib 3.9.4 installed can run the same script directly. Generation uses the checked-in README and date evidence without network access. The check also verifies the source and data hashes embedded in the PNG. Review the CSV, annual totals, and rendered `assets/count.png` together before committing.
