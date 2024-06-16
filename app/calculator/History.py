from calculator.calculation import Calculation as calc

class Calculator_History:
    log: list[calc] = []

    @classmethod
    def addCalculation(cls, Calc):
        return cls.log.append(Calc)
    
    @classmethod
    def getLastCalculation(cls):
        return cls.log[len(cls.log)-1]
