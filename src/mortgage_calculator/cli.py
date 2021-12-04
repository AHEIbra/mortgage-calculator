import click

from mortgage_calculator.calculator import (
    MortgageCalculator,
    MortgageHelpToBuyCalculator,
)


@click.group()
def cli():
    """ Calculate mortgage payments """
    pass


@cli.command('monthly_payments', short_help='Calculate monthly mortgage payments')
@click.option(
    '--property_price', default=500000, help='The total price of the property'
)
@click.option(
    '--deposit', default=0.1, help='Deposit as a percentage e.g. 0.2 for a 20% deposit'
)
@click.option(
    '--interest',
    default=0.01,
    help='Mortgage interest rate as a percentage e.g. 0.01 for a 1% interest',
)
@click.option('--mortgage_duration', default=25, help='Mortgage duration in years')
@click.option(
    '--cpi',
    default=0.03,
    help='Consumer price index, i.e. inflation in percentage e.g. 0.02 for a 2% inflation rate',
)
def monthly_payments(property_price, deposit, interest, mortgage_duration, cpi):
    """Calculate monthly mortgage payments"""
    mc = MortgageCalculator(property_price, deposit, interest, mortgage_duration, cpi)
    monthly_mortgage_payment = mc.calculate_monthly_mortgage()
    click.echo(f'Your monthly mortgage is {monthly_mortgage_payment}')


@cli.command('summarise', short_help='Summarise mortgage')
@click.option(
    '--property_price', default=500000, help='The total price of the property'
)
@click.option(
    '--deposit', default=0.1, help='Deposit as a percentage e.g. 0.2 for a 20% deposit'
)
@click.option(
    '--interest',
    default=0.01,
    help='Mortgage interest rate as a percentage e.g. 0.01 for a 1% interest',
)
@click.option('--mortgage_duration', default=25, help='Mortgage duration in years')
@click.option(
    '--available_cash',
    default=52000,
    help="Available cash for mortgage fees, deposit and SDLT",
)
@click.option(
    '--mortgage_fees',
    default=2200,
    help="Mortgage fees including conveyancor and legal fees etc",
)
@click.option(
    '--help_to_buy_equity', default=0.0, help="Add help to buy equity if required"
)
def summarise_mortgage(
    property_price,
    deposit,
    interest,
    mortgage_duration,
    available_cash,
    mortgage_fees,
    help_to_buy_equity,
):
    """Summarise mortgage"""
    if help_to_buy_equity > 0:
        mc = MortgageHelpToBuyCalculator(
            property_price=property_price,
            deposit=deposit,
            interest=interest,
            mortgage_duration=mortgage_duration,
            help_to_buy_equity=help_to_buy_equity,
            available_cash=available_cash,
            mortgage_fees=mortgage_fees,
        )
        click.echo(mc.summarise())
    else:
        mc = MortgageCalculator(
            property_price,
            deposit,
            interest,
            mortgage_duration,
            available_cash=available_cash,
            mortgage_fees=mortgage_fees,
        )
        click.echo(mc.summarise())


def main():
    return cli()
