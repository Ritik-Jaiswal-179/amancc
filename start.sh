gunicorn -w 4 -k uvicorn.workers.UvicornWorker code:app
