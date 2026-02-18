def extract_master(cursor):

  query = """ 
    SELECT 
      UPPER(p.alumno_apellido), p.alumno_nombre, p.alumno_dni, p.prestipo_nombre_corto, 
      DATE_FORMAT(a.alumno_fec_nac, '%d/%m/%Y') AS alumno_fec_nac, 
      p.prestacion_escuela_anio, p.prestacion_escuela_turno, o.os_nombre, 
      o.os_campo1 AS asist, p.prestacion_os_nro_afiliado_alumno AS num_afil, 
      e.escuela_nombre, p.prestacion_carga_horaria AS esc_horario, 
      e.escuela_direccion, l.localidad_nombre, 
      par.partido_nombre, a.alumno_diagnostico
    FROM v_prestaciones p 
    JOIN v_alumnos a
      ON p.prestacion_alumno = a.alumno_id
    LEFT JOIN v_os o
      ON p.prestacion_os = o.os_id
    LEFT JOIN v_escuelas e
      ON p.prestacion_escuela = e.escuela_id
    LEFT JOIN v_localidades l
      ON e.escuela_localidad = l.localidad_id
    LEFT JOIN v_partidos par
      ON l.localidad_partido = par.partido_id
    WHERE p.prestacion_estado = 1
      AND p.prestipo_nombre_corto != "TERAPIAS"
      AND p.prestacion_alumno != 522
   """
  cursor.execute(query)

  return cursor.fetchall()

def extract_activate(cursor, start_date, end_date):

  cursor.execute("SET lc_time_names = 'es_ES';")

  query = """
    SELECT 
      p.alumno_apellido, 
      p.alumno_nombre,
      p.prestipo_nombre_corto, 
      o.os_nombre, 
      o.os_campo1 AS asis,
      MONTHNAME(p.prestacion_fec_aut_OS_desde) AS mes_aut
    FROM v_prestaciones p 
    LEFT JOIN v_os o
      ON p.prestacion_os = o.os_id
    WHERE p.prestacion_estado = 1
      AND p.prestipo_nombre_corto != 'TERAPIAS'
      AND p.prestacion_alumno != 522
      AND DATE(p.prestacion_fec_pase_activo) BETWEEN %s AND %s
    """
  cursor.execute(query, (start_date, end_date))
  return cursor.fetchall()
