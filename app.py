from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from werkzeug.utils import secure_filename
from pdf2docx import Converter as PDFToWordConverter
from docx2pdf import convert as word_to_pdf_convert
from PIL import Image
import os
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'jpg', 'jpeg', 'png'}

class UploadForm(FlaskForm):
    file = FileField('Select File', validators=[
        FileRequired(),
        FileAllowed(ALLOWED_EXTENSIONS, 'Invalid file type!')
    ])
    submit = SubmitField('Convert')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        conversion_type = request.form.get('conversion_type')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            output_path = convert_file(file_path, conversion_type)
            
            if output_path:
                return send_file(output_path, as_attachment=True)
            else:
                flash('Conversion failed. Please try again.', 'error')
                return redirect(url_for('upload_file'))
        
    return render_template('upload.html', form=form)

def convert_file(file_path, conversion_type):
    output_path = os.path.splitext(file_path)[0]
    
    try:
        if conversion_type == 'pdf-to-word':
            output_path += '.docx'
            cv = PDFToWordConverter(file_path)
            cv.convert(output_path)
            cv.close()
        elif conversion_type == 'word-to-pdf':
            output_path += '.pdf'
            word_to_pdf_convert(file_path, output_path)
        elif conversion_type == 'image-to-pdf':
            output_path += '.pdf'
            image = Image.open(file_path)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            image.save(output_path, 'PDF', resolution=100.0)
        else:
            return None
        
        return output_path
    except Exception as e:
        print(f"Conversion error: {str(e)}")
        return None

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)