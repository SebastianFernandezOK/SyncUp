import pypandoc

def convert_word_to_pdf(docx_path, pdf_path):
    # Convertir el archivo Word a PDF
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)
    assert output == ""  # Asegúrate de que no haya errores

# Ejemplo de uso
convert_word_to_pdf('archivo.docx', 'archivo.pdf')
