from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import os
from dotenv import load_dotenv
import yagmail
from utils import clean_schedule

load_dotenv()

MAIL_AUTOR = os.getenv("MAIL_AUTOR")
APP_GMAIL_PASS = os.getenv("APP_GMAIL_PASS")
MAIL_DESTINO = os.getenv("MAIL_DESTINO")

def export_excel(data_master):
    
  # Hoja 1 - Resumen general

  wb = Workbook()
  ws = wb.active
  ws.title = "Sheet1"

  headers_master = ["Apellido PAC MAY", "Nombre/s", "DNI", "TIPO", "Fecha Nacimiento", "Curso/Grado", "Turno solicitado", 
                        "Acrónimo OS|PP", "AS", "Nro. de Afiliado", "Nombre de la Institución", "Horario_fx", 
                        "Dirección", "Localidad", "Provincia", "Diagnóstico"]
  
  ws.append(headers_master)

  idx_horario = headers_master.index("Horario_fx")

  for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal='center')

  for row in data_master:
    row = list(row)
    row[idx_horario] = clean_schedule(row[idx_horario])
    ws.append(row)

  nombre_archivo = "Datos - Planilla Maestra.xlsx"
  wb.save(nombre_archivo)
  print(f"Archivo Excel generado: {nombre_archivo}")
  return nombre_archivo

def send_mail(activates, file_name):

  body = f"""Buenos días,

  Se informan las prestaciones activadas recientemente:

  """

  for a in activates:
    lst_name, name, type, os_name, asis = a
    body += f"- {lst_name}, {name} | TIPO: {type} | OS: {os_name} | AS: {asis}\n"

  body += "\nSaludos,\nMariano López - Ailes Inclusión."
  try:
    yag = yagmail.SMTP(MAIL_AUTOR, APP_GMAIL_PASS)
    yag.send(
      to=MAIL_DESTINO,
      subject="Activaciones - Planilla maestra",
      contents= body,
      attachments=file_name
    )
    print("Correo enviado correctamente.")
  except Exception as e:
    print("Error al enviar el correo:", e)