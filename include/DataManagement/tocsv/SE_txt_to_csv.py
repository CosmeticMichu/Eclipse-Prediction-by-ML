import csv
# Nombre del archivo de texto de entrada
input_file = "data/solar-eclipses.txt"
# Nombre del archivo CSV de salida
output_file = "solar-eclipses.csv"

# Nombres de las columnas
column_names = ["Date", "GrEclTime", "DeltaT", "LunaNum", "SarosNum", "Type", "QLE", "Gamma", "EclMag", "Lat", "Long", "SunAlt", "PathWidth", "CentralDur"]

# Abre el archivo de texto de entrada en modo lectura
with open(input_file, "r") as text_file:
    lines = text_file.readlines()

# Filtra las líneas que comienzan con "0" (asumiendo que son las líneas de datos)
data_lines = [line.strip() for line in lines if line.startswith("0")]

# Procesa las líneas de datos y formatea la fecha como "YY-MM-DD"
formatted_data = []
for line in data_lines:
    parts = line.split()
    year = parts[1]
    month = parts[2]
    day = parts[3]
    formatted_date = f"{year}/{month.zfill(2)}/{day.zfill(2)}"
    formatted_data.append([formatted_date] + parts[4:])  # Combina la fecha formateada con el resto de los datos

# Escribe las líneas de datos en el archivo CSV de salida con los nombres de columna
with open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(column_names)  # Escribe la primera fila con los nombres de columna
    writer.writerows(formatted_data)