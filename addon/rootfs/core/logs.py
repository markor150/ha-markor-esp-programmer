from collections import defaultdict

_logs = defaultdict(list)

def add(job_id, line):
    _logs[job_id].append(line)

def get(job_id):
    return _logs.get(job_id, [])

def clear(job_id):
    _logs.pop(job_id, None)
