"""gunicorn WSGI server configuration."""
import os
from multiprocessing import cpu_count


def max_workers():
    return 2 * cpu_count()


accesslog = "/code/logs/gunicorn_access.log"
errorlog = "/code/logs/gunicorn_error.log"
access_log_format = (
    " Address: %(h)s - User: %(u)s - Date: %(t)s - Time: %(T)s - QueryStrings: %(q)s - "
    "Status: %(s)s - Length: %(b)s - Referer: %(f)s - UserAgent: %(a)s - Info: %(r)s "
)
max_requests = 1000
max_requests_jitter = 50
workers = max_workers()
bind = [f"0.0.0.0:{os.getenv('SERVER_PORT', 8000)}"]
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 1000
