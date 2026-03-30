import fitz  # PyMuPDF
from pptx import Presentation
from pptx.util import Inches
import os
import io

def generate_pptx_from_pdf(pdf_path, pptx_path):
    print(f"Opening {pdf_path}...")
    # Open the PDF document
    doc = fitz.open(pdf_path)
    
    # Create a new presentation
    prs = Presentation()
    
    # Set presentation slide size to 16:9 aspect ratio standard
    # Width: 13.333 inches, Height: 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # 6 is the layout for a blank slide
    blank_slide_layout = prs.slide_layouts[6]
    
    print(f"Found {len(doc)} pages. Generating slides...")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Render the page to a pixmap (image)
        # Using a higher scale for better resolution (DPI ~ 144)
        zoom_x = 2.0  # horizontal zoom
        zoom_y = 2.0  # vertical zoom
        mat = fitz.Matrix(zoom_x, zoom_y)
        
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        # We can extract the image bytes directly without writing to disk
        image_bytes = pix.tobytes("png")
        image_stream = io.BytesIO(image_bytes)
        
        # Add a blank slide
        slide = prs.slides.add_slide(blank_slide_layout)
        
        # Calculate sizing to fit exactly or adjust based on 16:9
        # In most PDF-based presentations, the aspect is already 16:9 or 4:3
        # We stretch the image to cover the entire slide
        slide.shapes.add_picture(image_stream, 0, 0, width=prs.slide_width, height=prs.slide_height)
        
        if (page_num + 1) % 5 == 0:
            print(f"Processed {page_num + 1} slides...")

    # Save the presentation
    prs.save(pptx_path)
    print(f"Successfully saved {pptx_path} with {len(doc)} slides.")

if __name__ == "__main__":
    pdf_file = "The_AI_Progress_Blueprint.pdf"
    pptx_file = "The_AI_Progress_Blueprint.pptx"
    
    if not os.path.exists(pdf_file):
        print(f"Error: {pdf_file} not found in the current directory.")
    else:
        generate_pptx_from_pdf(pdf_file, pptx_file)
