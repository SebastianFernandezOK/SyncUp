# Word to PDF Converter

This project is a document converter that allows you to efficiently and scalably transform Word (.docx) files into PDFs. It is designed to handle multiple conversion requests simultaneously using a socket-based architecture.

## Key Features

- **Multiple Connections**: The use of **sockets** allows multiple clients to connect to the server and send conversion requests concurrently, enhancing the efficiency of the process.

- **IPC Mechanisms**: **Inter-Process Communication (IPC)** mechanisms are implemented to facilitate communication between the server and worker processes that perform file conversion.

- **I/O Asynchrony**: The system utilizes **I/O asynchrony** to optimize the management of input and output operations, allowing the server to process several tasks without blocking, which improves user experience.

- **Distributed Task Queue**: The implementation of a **distributed task queue** ensures that conversion requests are handled in an orderly and efficient manner, allowing for organized processing and the potential to scale according to demand.

- **Command-Line Argument Parsing**: The project includes a mechanism for **command-line argument parsing**, enabling users to interact with the system and customize conversion settings from the terminal.

## Requirements

- Python 3.x
- Libraries: `pypandoc`, `flask`, `socket`, `multiprocessing`, among others.

## How to Use

1. **Install Dependencies**: Ensure you have all the necessary libraries installed.
2. **Run the Server**: Start the server and wait for client connections.
3. **Send Requests**: From the client, send the path of the Word file you wish to convert.
