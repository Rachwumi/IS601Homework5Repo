from decimal import Decimal
from app.commands import Command
from app.calculator import Calculator

class SubtractCommand(Command):
    def execute(self):
        try:
            int1 = input("Please type your first decimal >>> ")
            int2 = input("Please type your second decimal >>> ")
            result = Calculator.subtract( Decimal(int1), Decimal(int2) , 'subtract')
            print(f"The value of", int1, "-",int2, "is equal to",result)
        except Exception:
            print('Please type in Decimal format: 2.0, 1.5, 18.0')