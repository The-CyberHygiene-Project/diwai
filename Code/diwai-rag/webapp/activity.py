"""Activity log: one row per add/remove job, in SQLite so it survives restarts."""
import sqlite3
import threading
from datetime import datetime

ACTIVE = ("waiting", "working")


class ActivityLog:
    def __init__(self, path):
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        with self._lock, self._db:
            self._db.execute(
                "CREATE TABLE IF NOT EXISTS jobs ("
                " id INTEGER PRIMARY KEY AUTOINCREMENT, created TEXT, filename TEXT,"
                " kind TEXT, state TEXT, outcome TEXT, message TEXT, detail TEXT,"
                " progress INTEGER, payload TEXT)")

    def add(self, filename, kind, payload="", state="waiting", outcome="waiting",
            message="⏳ Waiting", detail=""):
        with self._lock, self._db:
            cur = self._db.execute(
                "INSERT INTO jobs (created, filename, kind, state, outcome, message,"
                " detail, progress, payload) VALUES (?,?,?,?,?,?,?,0,?)",
                (datetime.now().isoformat(timespec="seconds"), filename, kind, state,
                 outcome, message, detail, payload))
            return cur.lastrowid

    def update(self, job_id, **fields):
        cols = ", ".join(f"{k} = ?" for k in fields)
        with self._lock, self._db:
            self._db.execute(f"UPDATE jobs SET {cols} WHERE id = ?", (*fields.values(), job_id))

    def get(self, job_id):
        with self._lock:
            row = self._db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        return dict(row) if row else None

    def recent(self, limit=200):
        with self._lock:
            rows = self._db.execute("SELECT * FROM jobs ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]

    def active_count(self):
        with self._lock:
            return self._db.execute(
                "SELECT COUNT(*) FROM jobs WHERE state IN (?, ?)", ACTIVE).fetchone()[0]

    def mark_interrupted(self):
        """Jobs left waiting/working by a previous run can't resume: the upload
        is gone from memory. Say so plainly."""
        with self._lock, self._db:
            self._db.execute(
                "UPDATE jobs SET state = 'done', outcome = 'interrupted',"
                " message = '❌ Interrupted, drop the file again' WHERE state IN (?, ?)", ACTIVE)
