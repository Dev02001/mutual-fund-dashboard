from decimal import Decimal,ROUND_HALF_UP
from datetime import datetime

def validate_nav_data(latest_nav, nav_date):

    if latest_nav is None:
        raise ValueError("Nav is None")
    if nav_date is None:
        raise ValueError("Nav date is None")

    validated_nav = Decimal(latest_nav).quantize(Decimal('0.0001'),rounding=ROUND_HALF_UP)
    validated_nav_date = datetime.strptime(nav_date, "%m/%d/%Y").date()

    return validated_nav, validated_nav_date
