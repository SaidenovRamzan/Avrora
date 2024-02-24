import logging
import subprocess
from docx2pdf import convert
from tkinter import messagebox


def convert_docx_to_pdf_for_linux(docx_file, output_dir):
    try:
        # Создаем pdf фаил
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                output_dir,
                docx_file,
            ]
        )
        logging.info(f"Conversion successful: {docx_file} -> {output_dir}")
    except Exception as e:
        logging.error(f"Error converting {docx_file} to PDF: {str(e)}")
        messagebox.showerror("Error", f"Error converting {docx_file} to PDF: {str(e)}")


def convert_docx_to_pdf_for_windows(docx_file, output_dir):
    try:
        convert(docx_file, output_path=output_dir)
        logging.info(f"Conversion successful: {docx_file} -> {output_dir}")
    except Exception as e:
        logging.error(f"Error converting {docx_file} to PDF: {str(e)}")
        messagebox.showerror("Error", f"Error converting {docx_file} to PDF: {str(e)}")
