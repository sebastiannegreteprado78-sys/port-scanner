import socket
import datetime

target = "scanme.nmap.org"

servicios = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

with open("reporte.txt", "w") as archivo:
    fecha = datetime.datetime.now()
    archivo.write("=== REPORTE DE ESCANEO ===\n")
    archivo.write(f"Fecha: {fecha}\n")
    archivo.write(f"Objetivo: {target}\n\n")
    
    for puerto in range(20, 445):
        conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = conexion.connect_ex((target, puerto))
        if resultado == 0:
            nombre = servicios.get(puerto, "Desconocido")
            print(f"Puerto {puerto} ABIERTO - {nombre}")
            archivo.write(f"Puerto {puerto} ABIERTO - {nombre}\n")
        conexion.close()

print("Reporte guardado en reporte.txt")
