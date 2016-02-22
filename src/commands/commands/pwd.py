from commands import Command


class Pwd(Command):
    cmd_name = 'pwd'
    cmd_description = 'Get current directory"'

    def execute(self):
        self._run(['pwd'])
