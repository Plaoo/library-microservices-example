import os
import httpx

BOOK_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/books'

def is_book_present(book_id:int):
    url = os.environ.get('BOOK_SERVICE_HOST_URL') or BOOK_SERVICE_HOST_URL
    r = httpx.get(f'{url}{book_id}')
    return True if r.statuscode == 200 else False
