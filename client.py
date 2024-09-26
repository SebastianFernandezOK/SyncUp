import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Cambia la dirección y el puerto si es necesario

# Enviar la ruta del archivo al servidor
file_path = "D:\\User\\Desktop\\code\\compu 2\\proyect\\files\\archivo.docx"  # Cambia esto a la ruta que necesites
client_socket.sendall(file_path.encode())

# Recibir la respuesta del servidor
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
