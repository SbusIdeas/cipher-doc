import PyPDF2
import os

def encrypt_pdf(input_pdf, output_pdf, password):
    """
    Encrypts a PDF file with a specified password.

    Args:
        input_pdf (str): The path to the input PDF file.
        output_pdf (str): The name of the output encrypted PDF file.
        password (str): The password to encrypt the PDF with.
    """
    # Open the PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Create a writer
        writer = PyPDF2.PdfWriter()
        
        # Copy pages to writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
            
        # Encrypt the PDF
        writer.encrypt(user_password=password, owner_pwd=None, use_128bit=True)
        
        # Write encrypted PDF to output file
        with open(f"encrypted_pages/{output_pdf}", 'wb') as output_file:
            writer.write(output_file)
            print(f'PDF encrypted and saved as {output_pdf}')


def run():
    """
    Encrypts all PDF files in the 'output_pages' directory
    and saves them to the 'encrypted_pages' directory.
    """
    # Ensure the output directory exists
    os.makedirs("encrypted_pages", exist_ok=True)

    # Iterate over all files in the 'output_pages' directory
    for file in os.listdir("output_pages"):
        member_id = file.split(".")[0]
        
        # Encrypt the PDF file
        encrypt_pdf(f"output_pages/{file}", f"{member_id}-payslip.pdf", file[:6])

if __name__ == "__main__":
    run()
