import PyPDF2


def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    pdf_file_obj.close()
    return (text.replace('˘ ', '').replace('ˆ ', '').replace('ˇ ', '')
            .replace('˙ ', '').replace('˝ ', '').replace(' ¸', '')
            .replace('¸ ', '').replace('', ''));


if __name__ == '__main__':
    print(extract_text_from_pdf('C6_slides_rom.pdf'))