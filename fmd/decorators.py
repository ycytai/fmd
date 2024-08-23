from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from typing_extensions import Literal


def default_data_range(
    freq: Literal['daily', 'monthly', 'quarterly', 'yearly'],
    years: int | None = None,
    quarters: int | None = None,
    months: int | None = None,
    days: int | None = None,
):
    """Set default data range when retrieving data from API."""

    def dec(func):
        def wrapper(self, *args, **kwargs):
            match freq:
                case 'daily':
                    if not kwargs.get('start_date') and not kwargs.get('end_date'):
                        end_date = datetime.today().date()
                        start_date = end_date - timedelta(days=days)
                        kwargs['start_date'] = start_date
                        kwargs['end_date'] = end_date

                case 'monthly':
                    if (
                        not kwargs.get('start_year')
                        and not kwargs.get('start_month')
                        and not kwargs.get('end_year')
                        and not kwargs.get('end_month')
                    ):
                        today = datetime.today()
                        end_year = today.year
                        end_month = today.month

                        start_dt = today - relativedelta(months=months)
                        start_year = start_dt.year
                        start_month = start_dt.month

                        kwargs['start_year'] = start_year
                        kwargs['start_month'] = start_month
                        kwargs['end_year'] = end_year
                        kwargs['end_month'] = end_month

                case 'quarterly':
                    if (
                        not kwargs.get('start_year')
                        and not kwargs.get('start_quarter')
                        and not kwargs.get('end_year')
                        and not kwargs.get('end_quarter')
                    ):
                        today = datetime.today()
                        end_year = today.year
                        end_quarter = (today.month - 1) // 3 + 1

                        total_quarters = end_quarter - quarters
                        start_year = today.year + (total_quarters - 1) // 4
                        start_quarter = (total_quarters - 1) % 4 + 1

                        kwargs['start_year'] = start_year
                        kwargs['start_quarter'] = start_quarter
                        kwargs['end_year'] = end_year
                        kwargs['end_quarter'] = end_quarter

                case 'yearly':
                    if not kwargs.get('start_year') and not kwargs.get('end_year'):
                        end_year = datetime.today().year
                        start_year = end_year - years
                        kwargs['start_year'] = start_year
                        kwargs['end_year'] = end_year

            return func(self, *args, **kwargs)

        return wrapper

    return dec
