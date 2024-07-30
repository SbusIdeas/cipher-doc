import PyPDF2
import os

def split_pdf(input_pdf, output_folder):
    """
    Splits a large PDF file into smaller PDF files, each containing two pages.
    
    Args:
        input_pdf (str): The path to the input PDF file.
        output_folder (str): The folder where the output PDFs will be saved.
    """

    # Check if the output folder exists, if not, create it
    if os.path.exists(output_folder): 
        os.mkdir(output_folder)

    # Open the PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page_count = 0
        # Iterate through each page
        for i in range(len(reader.pages)):
            if page_count == 0:
                writer = PyPDF2.PdfWriter()
            page_count += 1

            # Extract and read member ID number on the first page
            if page_count == 1:
                lines = reader.pages[i].extract_text().splitlines()
                for line in lines:
                    if "ID Number:" in line:
                        id_no = line.split()[-1]
                        filename = id_no

            # Add the current page to the writer
            writer.add_page(reader.pages[i])
            
            if page_count != 2:
                continue

            # Reset page count for the next PDF file
            page_count = 0

            # Output file name
            output_pdf = f'{output_folder}/{filename}.pdf'
            
            # Write the pages to a new PDF file
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

# Define the input PDF file and the output folder
pdf_file = 'payslips.pdf'
output_folder = 'output_pages'

# Call the function to split the PDF
input_pdf = pdf_file
split_pdf(input_pdf, output_folder)
