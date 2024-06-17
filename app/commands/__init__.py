from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            if command_name == "menu":
                self.commands[command_name].execute(self.commands)
            elif command_name == "exit":
                self.commands[command_name].execute()
            else:
                int1 = input("Please type your first decimal >>> ")
                int2 = input("Please type your second decimal >>> ")
                self.commands[command_name].execute(int1,int2)
        except KeyError:
            print(f"No such command: {command_name}")