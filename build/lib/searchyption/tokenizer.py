import PyPDF2

class Tokenizer:
    # def __init__(self):
    #     pass
    

    @staticmethod
    def pdf_to_text(file_path):
        pdf_reader = PyPDF2.PdfFileReader(file_path)
        texts = ""
        for page_number in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_number)
            texts = texts + page.extractText()
        return texts

    @staticmethod
    def tokenize(text):
        tokens = word_tokenize(text)
        return tokens


# token = Tokenizer.pdf_to_text("2.pdf")
print(Tokenizer.tokenize("this is test for the nltk tokenizer"))
