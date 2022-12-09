import os

from notebuild.core.core import command_line_parser
from notebuild.manage import BaseServer, ServerManage


# lsof -t -i:8102
# sudo kill -9 `sudo lsof -t -i:8102`


class WorkerServer(BaseServer):
    def __init__(self):
        path = os.path.abspath(os.path.dirname(__file__))
        super(WorkerServer, self).__init__('noteworker_server', path)

    def init(self):
        manage = ServerManage()
        try:
            manage.init()
        except Exception as e:
            print(e)

        manage.add_job(server_name='noteworker_server',
                       directory=self.current_path,
                       command=f"celery -A pyflower flower --port=8102",
                       user='bingtao',
                       stdout_logfile="/notechats/logs/noteworker/strategy.log")
        manage.start()


def notecoin():
    args = command_line_parser()
    package = WorkerServer()
    if args.command == 'init':
        package.init()
    elif args.command == 'stop':
        package.stop()
    elif args.command == 'start':
        package.start()
    elif args.command == 'restart':
        package.restart()
    elif args.command == 'help':
        info = """
    init
    stop
    start
    restart
        """
        print(info)
