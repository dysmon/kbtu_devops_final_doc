# Logs redirection

## Task description

Task 0.3

- Create simple API
- Create a directory /home/logs and redirect all logs to log files in that folder while your application is running. Limit the number of files to 3 (delete others) and set a log size limit of 1MB. Save the execution time of your log rotations to /home/log_rotates.log

Note: You can't do anything with your application; make changes ONLY at the infrastructure level

## First task

Created simple API on FastAPI(Python)

```Python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Response": "Hello world!"}

@app.get("/devopsina")
def get_devopsina():
    return {"Response": "You get devopsina(rare loot)"}
```
