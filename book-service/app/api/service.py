import os
import httpx

AUTHOR_SERVICE_HOST_URL = "http://localhost:8002/api/v1/authors"


def is_author_present(book_id: int):
    url = os.environ.get("AUTHOR_SERVICE_HOST_URL") or AUTHOR_SERVICE_HOST_URL
    r = httpx.get(f"{url}{authors_id}")
    return True if r.statuscode == 200 else False
