import re

_progress = {}

WRITE_RE = re.compile(r"\((\d+)\s?%\)")

def update(job_id: str, line: str):
    m = WRITE_RE.search(line)
    if m:
        _progress[job_id] = {
            "percent": int(m.group(1)),
            "line": line,
        }

def get(job_id: str):
    return _progress.get(job_id, {
        "percent": 0,
        "line": "",
    })

def finish(job_id: str):
    _progress[job_id] = {
        "percent": 100,
        "line": "Finished",
    }
