from noteworker.worker import get_default_app

app = get_default_app()


@app.task
def flower_log(msg):
    return msg
