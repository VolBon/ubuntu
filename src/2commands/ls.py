from commands import Command


class Ls(Command):
    cmd_name = 'ls'
    cmd_description = 'list current directory'

    def execute(self):
        self._run(['ls'])

