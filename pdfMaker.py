import os
from PIL import Image
from reportlab.pdfgen import canvas

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Collect image files from the current directory
image_files = [
    os.path.join(current_directory, f) for f in os.listdir(current_directory)
    if f.lower().endswith(image_extensions)
]

# Sort images based on their filenames
image_files.sort()

# Define the base output PDF file name
base_pdf_file_name = os.path.join(current_directory, 'output.pdf')

# Initialize the output PDF file name
pdf_file_name = base_pdf_file_name

# Check if the PDF file already exists and rename if necessary
counter = 1
while os.path.exists(pdf_file_name):
    pdf_file_name = os.path.join(current_directory, f'output_{counter}.pdf')
    counter += 1

# Create a PDF file
c = canvas.Canvas(pdf_file_name)

# Print the starting message
print(f"Creating PDF: {pdf_file_name}")
print(f"Found {len(image_files)} images. Starting the conversion...")

# Process each image
for index, image_file in enumerate(image_files):
    img = Image.open(image_file)
    img_width, img_height = img.size
    
    # Set the page size to the image size
    c.setPageSize((img_width, img_height))
    
    # Draw the image onto the PDF page
    c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
    
    # End the current page
    c.showPage()

    # Print progress
    print(f"Processed image {index + 1} of {len(image_files)}: {os.path.basename(image_file)}")

# Save the PDF
c.save()

# Print completion message
print(f"PDF created successfully: {pdf_file_name}")
