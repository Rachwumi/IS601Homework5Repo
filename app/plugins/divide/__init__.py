from decimal import Decimal
from app.commands import Command
from app.calculator import Calculator

class DivideCommand(Command):
    def execute(self, i1, i2):
        try:
            result = Calculator.subtract( Decimal(i1), Decimal(i2) , 'divide')
            print(f"The value of", i1, "/",i2, "is equal to",result)
        except Exception:
            print('Please type in Decimal or Integer format: 2.0, 1.5, 18 and your second decimal can not be 0.0')