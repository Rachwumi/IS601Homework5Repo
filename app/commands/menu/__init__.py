from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        result = 'Menu: '
        for i in self.commands:
            result += i+','
        print(result[:-1])