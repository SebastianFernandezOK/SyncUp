import socket
import pypandoc

def convert_word_to_pdf(docx_path, pdf_path):
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)
    return output

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Cambia la dirección y el puerto si es necesario
server_socket.listen(5)
print("Servidor escuchando...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    # Recibir la ruta del archivo del cliente
    file_path = client_socket.recv(1024).decode()  # Asegúrate de que el tamaño sea adecuado
    print(f"Ruta recibida: {file_path}")

    # Procesar el archivo
    pdf_path = file_path.replace('.docx', '.pdf')
    try:
        convert_word_to_pdf(file_path, pdf_path)
        client_socket.sendall(f"Archivo convertido a {pdf_path}".encode())
    except Exception as e:
        client_socket.sendall(f"Error al convertir el archivo: {str(e)}".encode())

    client_socket.close()
