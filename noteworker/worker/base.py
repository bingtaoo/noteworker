from notesecret import read_secret

from .app import WorkApp

global _app
_app = None


def get_default_app():
    """
    get_default_app
    """
    global _app
    if _app is  None:
        _app= WorkApp(
        "noteWorker",
        broker=read_secret(cate1="noteworker", cate2="workApp", cate3='broker') or "redis://localhost:6379/0",
        backend=read_secret(cate1="noteworker", cate2="workApp", cate3='backend') or "redis://localhost:6379/0"
    )
    return _app

