from src.calc.mortgage_calculator import MortgageCalculator


if __name__ == '__main__':
    calc = MortgageCalculator(property_price=500000,
                              deposit=0.10,
                              interest=0.01,
                              mortgage_duration=25)

    print("Mortgage deposit", calc.deposit_amount)
    print("Mortgage amount", calc.mortgage_amount)
    print("Mortgage monthly payment", calc.calculate_monthly_mortgage())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
