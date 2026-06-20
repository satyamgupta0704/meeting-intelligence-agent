from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

scheduler = BlockingScheduler()

scheduler.add_job(
    lambda: subprocess.run(
        ["python", "sync.py"]
    ),
    trigger="interval",
    minutes=5
)

scheduler.start()