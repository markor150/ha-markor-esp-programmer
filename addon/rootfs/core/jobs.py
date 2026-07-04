from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
import uuid

@dataclass
class Job:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    status: str = "queued"

    action: str = ""

    result: dict | None = None


class JobManager:

    def __init__(self):

        self.lock = Lock()

        self.jobs = {}

    def create(self, action):

        job = Job(action=action)

        self.jobs[job.id] = job

        return job

    def get(self, job_id):

        return self.jobs.get(job_id)

    def list(self):

        return list(self.jobs.values())


manager = JobManager()
