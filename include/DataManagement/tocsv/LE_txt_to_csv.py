import csv

# Nombre del archivo de texto de entrada
input_file = "data/lunar-eclipses.txt"
# Nombre del archivo CSV de salida
output_file = "lunar-eclipses.csv"

# Nombres de las columnas
column_names = ["CatNum", "Date", "GrEclTime", "DeltaT", "LunaNum", "SarosNum", "Type", "QSE", "Gamma", "PenMag", "UmMag", "PenM", "ParM", "TotalM", "Lat", "Long"]

# Abre el archivo de texto de entrada en modo lectura
with open(input_file, "r") as text_file:
    lines = text_file.readlines()

# Filtra las líneas que comienzan con "0" (asumiendo que son las líneas de datos)
data_lines = [line.strip() for line in lines if line.startswith("0")]

# Escribe las líneas de datos en el archivo CSV de salida con los nombres de columna
with open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(column_names)  # Escribe la primera fila con los nombres de columna
    writer.writerows([line.split() for line in data_lines])