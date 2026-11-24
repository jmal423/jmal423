from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "data-date" in attrs and "data-level" in attrs:
            self.days[date.fromisoformat(attrs["data-date"])] = int(attrs["data-level"])


request = Request("https://github.com/users/jmal423/contributions", headers={"User-Agent": "jmal423-profile"})
calendar = Calendar()
with urlopen(request, timeout=30) as response:
    calendar.feed(response.read().decode())
if len(calendar.days) < 350:
    raise ValueError("Incomplete GitHub calendar")

first = min(calendar.days)
offset = (first.weekday() + 1) % 7
colors = ["#283142", "#185c57", "#20897a", "#43bda2", "#84efd1"]
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 776 133"><rect width="776" height="133" rx="10" fill="#101524"/>']
for day, level in sorted(calendar.days.items()):
    week, row = divmod((day - first).days + offset, 7)
    x = 12 + week * 14
    if day.day <= 7 and row == 0 and week < 52:
        parts.append(f'<text x="{x}" y="18" fill="#ccd6df" font-family="sans-serif" font-size="11">{day:%b}</text>')
    parts.append(f'<rect x="{x}" y="{27 + row * 14}" width="11" height="11" rx="2" fill="{colors[level]}"/>')
Path("assets/contributions.svg").write_text("\n".join(parts + ["</svg>"]), encoding="utf-8")
