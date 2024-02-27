import os
import logging
from tkinter import messagebox
from utils import (
    convert_docx_to_pdf_for_windows,
    convert_xlsx_to_pdf_for_windows,
    convert_docx_to_pdf_for_linux,
    convert_xlsx_to_pdf_for_linux,
)


def main(input_file):
    logging.basicConfig(
        filename="ex_1/logs.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    _, file_ext = os.path.splitext(input_file)  # Получили расширение файла
    output_dir = "ex_1/converted_files"

    if file_ext == ".docx":
        convert_docx_to_pdf_for_windows(input_file, output_dir)
    elif file_ext == ".xlsx":
        convert_xlsx_to_pdf_for_windows(input_file, output_dir)
    else:
        messagebox.showerror("Error", "Unsupported file format")


if __name__ == "__main__":
    input_file_path = input("Enter the path to the input file: ")
    main(input_file_path)
