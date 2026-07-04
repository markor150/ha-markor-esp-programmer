from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Job:
    id: str
    action: str
    status: str = "queued"
    created: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    result: dict | None = None


class JobManager:

    def __init__(self):
        self.jobs = {}

    def create(self, action):
        job = Job(
            id=str(uuid4()),
            action=action,
        )
        self.jobs[job.id] = job
        return job

    def get(self, job_id):
        return self.jobs.get(job_id)

    def list(self):
        return list(self.jobs.values())

    def finish(self, job_id, result):
        if job_id in self.jobs:
            self.jobs[job_id].status = "finished"
            self.jobs[job_id].result = result

    def fail(self, job_id, result):
        if job_id in self.jobs:
            self.jobs[job_id].status = "failed"
            self.jobs[job_id].result = result


manager = JobManager()
