from datetime import date, timedelta

def get_fech_range():
  today = date.today()
  day_week = today.weekday()

  if day_week == 0:  # lunes
    # viernes anterior
    start_date = today - timedelta(days=3)
    end_date = today - timedelta(days=1)
  else:
    # cualquier otro día: solo ayer
    start_date = today - timedelta(days=1)
    end_date = today - timedelta(days=1)

  return start_date, end_date
