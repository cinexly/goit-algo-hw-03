from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date ()
        today = datetime.today().date()
        dif = today - input_date
        return dif.days
    except:
        return None