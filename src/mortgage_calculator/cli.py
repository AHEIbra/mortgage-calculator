import click

from mortgage_calculator.calculator import MortgageCalculator


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


def main():
    return cli()
