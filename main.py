from mortgage_calculator.calculator import (
    MortgageCalculator,
    MortgageHelpToBuyCalculator,
)

if __name__ == '__main__':
    calc = MortgageCalculator(
        property_price=500000, deposit=0.10, interest=0.01, mortgage_duration=25
    )

    print('Mortgage deposit', calc.deposit_amount)
    print('Mortgage amount', calc.mortgage_amount)
    print('Mortgage monthly payment', calc.calculate_monthly_mortgage())

    htb_calc = MortgageHelpToBuyCalculator(
        property_price=519000,
        deposit=0.07,
        interest=0.08,
        mortgage_duration=25,
        help_to_buy_equity=0.05,
    )

    print('Mortgage HTB amount', htb_calc.mortgage_amount)
    print('HTB equity', htb_calc.help_to_buy_equity_amount)
    print('HTB sdlt', htb_calc.sdlt)
