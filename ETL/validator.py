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



    '''Assign a variable nav_date = data[1]
    assign a variable latest_nav = data[0]
    #validate if latest_nav data type is decimal if no convert to decimal
    after conversion update latest_nav = converted latest_nav
    Now convert nav_date from str to date and format it as dd-mm-yyyy update nav_date = converted and formatted nav_date
    Now validate if latest_nav for nav_nav date exist? if yes return true and if no return false
   '''