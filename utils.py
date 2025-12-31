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

import re

def clean_schedule(text):
    if not text:
      return ""

    text = text.lower()

    # eliminar palabras irrelevantes
    text = re.sub(
      r'(hs?|tm|turno.*|a confirmar|mañana|tarde)',
      '',
      text
    )

    # buscar rangos horarios (ej: 8 a 12 / 8.30 a 12.30)
    rangos = re.findall(
      r'(\d{1,2}(?:[.:]\d{2})?\s*a\s*\d{1,2}(?:[.:]\d{2})?)',
      text
    )

    if rangos:
        return rangos[-1].strip()  # último rango
    else:
        return text.strip()

