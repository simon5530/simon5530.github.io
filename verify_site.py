"""Check the public-only static site contract with Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
PAGES = ("index.html", "privacy/index.html", "terms/index.html")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in {"script", "iframe", "form", "input"}, tag
        if tag == "h1":
            self.h1_count += 1
        assert not any(key.startswith("on") for key in attrs), "inline handler"
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


for name in PAGES:
    text = (ROOT / name).read_text()
    assert 'lang="zh-Hant"' in text and "TanSan-gog(Personal)" in text
    assert '<meta name="viewport"' in text
    page = Page()
    page.feed(text)
    assert page.h1_count == 1, name
    for link in page.links:
        parsed = urlsplit(link)
        assert parsed.scheme in ("", "https"), link
        if parsed.scheme:
            assert not parsed.username and not parsed.password
            continue
        target = ROOT / parsed.path.lstrip("/")
        if target.is_dir():
            target = target / "index.html"
        assert target.is_file(), (name, link)
    print(f"PASS {name}: title structure, no active collection, local links")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    assert path.suffix.lower() not in {".json", ".pem", ".key", ".p12"}, path
    assert "client_secret_" not in path.name, path
print("PASS public tree has no credential-file artifacts")
