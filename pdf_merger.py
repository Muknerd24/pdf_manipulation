import os
from PyPDF2 import PdfWriter

# Specify the directory containing the PDF files
path = "/Users/mohammadullah/pdf_files"

# Create a PdfWriter object
merger = PdfWriter()

try:
    # Loop through each file in the directory
    for file_name in os.listdir(path):
        # Construct the full file path
        full_path = os.path.join(path, file_name)

        # Check if the file is a PDF
        if file_name.lower().endswith('.pdf'):
            print(f"Adding {file_name} to the merger.")
            merger.append(full_path)

    # Save the merged PDF to a new file
    output_file = os.path.join(path, "merged_output.pdf")
    merger.write(output_file)
    print(f"Merged PDF saved as {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    merger.close()
