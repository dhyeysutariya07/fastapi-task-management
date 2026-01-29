from datetime import datetime
from typing import List
from app.schema.task import TaskRetrieve

tasks_db: List[TaskRetrieve] = [
    TaskRetrieve(
        id=1,
        title="Design API endpoints",
        priority="high",
        estimated_hours=5.0,
        actual_hours=None,
        created_at=datetime(2026, 1, 29, 9, 0),
        updated_at=datetime(2026, 1, 29, 9, 0)
    ),
    TaskRetrieve(
        id=2,
        title="Write Pydantic models",
        priority="medium",
        estimated_hours=3.0,
        actual_hours=None,
        created_at=datetime(2026, 1, 29, 10, 0),
        updated_at=datetime(2026, 1, 29, 10, 0)
    ),
    TaskRetrieve(
        id=3,
        title="Setup in-memory DB",
        priority="high",
        estimated_hours=2.0,
        actual_hours=None,
        created_at=datetime(2026, 1, 29, 11, 0),
        updated_at=datetime(2026, 1, 29, 11, 0)
    ),
    TaskRetrieve(
        id=4,
        title="Create async CRUD services",
        priority="medium",
        estimated_hours=4.0,
        actual_hours=None,
        created_at=datetime(2026, 1, 29, 12, 0),
        updated_at=datetime(2026, 1, 29, 12, 0)
    ),
    TaskRetrieve(
        id=5,
        title="Test endpoints with Swagger",
        priority="low",
        estimated_hours=1.5,
        actual_hours=None,
        created_at=datetime(2026, 1, 29, 13, 0),
        updated_at=datetime(2026, 1, 29, 13, 0)
    ),
]

# Next ID for auto-increment
next_id = 6
