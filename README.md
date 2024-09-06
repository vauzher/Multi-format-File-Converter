# Multi-format File Converter

A web application built with Flask that allows users to convert files between different formats, including PDF to Word, Word to PDF, and Image to PDF. This application supports multiple languages, including Arabic and Kurdish.

## Features

- **Multiple Conversion Types:**
  - PDF to Word
  - Word to PDF
  - Image (JPG, JPEG, PNG) to PDF

- **User-Friendly Interface:**
  - Responsive design that works on various screen sizes
  - Tabbed interface for easy selection of conversion type
  - File type validation to prevent incorrect uploads

- **Language Support:**
  - Handles various languages, including Arabic

- **Secure File Handling:**
  - Secure filename generation
  - File size limit to prevent large uploads

## Technologies Used

- Python 3.x
- Flask
- Flask-WTF for form handling
- pdf2docx for PDF to Word conversion
- python-docx2pdf for Word to PDF conversion
- Pillow for image processing
- Bootstrap 5 for frontend design

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/multi-format-file-converter.git
   cd multi-format-file-converter
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

1. Select the desired conversion type by clicking on the appropriate tab.
2. Click the "Choose File" button to select the file you want to convert.
3. Click the "Convert" button to start the conversion process.
4. Once the conversion is complete, the converted file will be automatically downloaded.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pdf2docx](https://github.com/dothinking/pdf2docx) for PDF to Word conversion
- [python-docx2pdf](https://github.com/AlJohri/python-docx2pdf) for Word to PDF conversion
- [Pillow](https://python-pillow.org/) for image processing
- [Bootstrap](https://getbootstrap.com/) for frontend design
