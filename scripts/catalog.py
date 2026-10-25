"""Read and deduplicate the paper entries maintained in README.md."""

from dataclasses import dataclass, field
from pathlib import Path
import re
import unicodedata


ENTRY = re.compile(
    r"\*\*(.*?)\*\*<br>\s*\n\*(.*?)\*<br>\s*\n([^\n]+)", re.S
)
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d+)")
LINK = re.compile(r"\[\[([^\]]+)\]\((https://[^\s)]+)\)\]")


def normalize_title(title: str) -> str:
    text = unicodedata.normalize("NFKD", title).casefold()
    return "".join(c for c in text if c.isalnum())


@dataclass
class Paper:
    identifier: str
    title: str
    authors: str
    publication: str
    url: str
    categories: set = field(default_factory=set)
    arxiv_id: str = ""


def read_catalog(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.count("<!-- start -->") != 1 or text.count("<!-- end -->") != 1:
        raise ValueError("README must contain exactly one catalog start/end pair")
    body = text.split("<!-- start -->")[1].split("<!-- end -->")[0]
    remainder = ENTRY.sub("", body)
    for line in remainder.splitlines():
        if line.strip() and not line.startswith(("#", '<a id="')):
            raise ValueError(f"Unparsed catalog content: {line!r}")
    papers = {}
    title_ids = {}
    memberships = set()
    entry_count = 0
    for match in ENTRY.finditer(body):
        title, authors, publication = match.groups()
        headings = re.findall(r"^#{2,4} (.+)$", body[: match.start()], re.M)
        if not headings:
            raise ValueError(f"Paper without a category: {title}")
        category = re.sub(r"^[^A-Za-z]+", "", headings[-1]).strip()
        links = LINK.findall(publication)
        if not links or not any(label in ("Paper", "arXiv", "DOI") for label, _ in links):
            raise ValueError(f"Paper without a bibliography link: {title}")
        arxiv = ARXIV.search(publication)
        doi = next((url.split("doi.org/", 1)[1].lower() for _, url in links if "doi.org/" in url), "")
        identifier = "arxiv:" + arxiv[1] if arxiv else "doi:" + doi if doi else links[0][1]
        normalized = normalize_title(title)
        if normalized in title_ids and title_ids[normalized] != identifier:
            raise ValueError(f"Potential duplicate with different identifiers: {title}")
        title_ids[normalized] = identifier
        if (identifier, category) in memberships:
            raise ValueError(f"Duplicate within category {category}: {title}")
        memberships.add((identifier, category))
        entry_count += 1
        if identifier not in papers:
            papers[identifier] = Paper(identifier, title.rstrip("."), authors, publication,
                                       links[0][1], arxiv_id=arxiv[1] if arxiv else "")
        papers[identifier].categories.add(category)
    if not papers:
        raise ValueError("The catalog is empty")
    return papers, entry_count
