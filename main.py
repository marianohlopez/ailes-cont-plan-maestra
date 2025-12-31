from db import connect_db
from extract import extract_master, extract_activate
from transform import export_excel, send_mail
from utils import get_fech_range

def main():

  conn = connect_db()
  cursor = conn.cursor()

  start_date, end_date = get_fech_range()
  activates = extract_activate(cursor, start_date, end_date)

  if activates:
    data_master = extract_master(cursor)
    file = export_excel(data_master)
    send_mail(activates, file)
  else:
    print("No hubo activaciones en el período evaluado.")

if __name__ == "__main__":
  main()