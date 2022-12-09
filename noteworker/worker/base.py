from notesecret import read_secret

from .app import WorkApp

global app
app = None


def get_default_app():
    """
    get_default_app
    """
    global app
    if app is not None:
        return app

    app= WorkApp(
        "noteWorker",
        broker=read_secret(cate1="noteworker", cate2="workApp", cate3='broker') or "redis://localhost:6379/0",
        backend=read_secret(cate1="noteworker", cate2="workApp", cate3='backend') or "redis://localhost:6379/0"
    )
    return app
