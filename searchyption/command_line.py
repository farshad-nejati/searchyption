from searchyption import About
from searchyption.tokenizer import Tokenizer
from .iomanager import IOManager
import sys
import os

def main():
    # print(os.path.abspath())
    if len(sys.argv) > 1:
        if sys.argv[1] == "tokenize":
            if len(sys.argv) > 2:
                file = sys.argv[2]
                file_path = os.path._getfullpathname(file)
                file_path = os.path._getfullpathname(file)
                filename, file_extension = IOManager.file_and_extension(file)
                file_extension = file_extension[1:]
                print(file)
                if os.path.isfile(file):
                    print(file_path)
                else:
                    print("Error: No such file or directory: ", file)
                    sys.exit()
                if not filename:
                    print("Error: Command Not Found!")
                    sys.exit()
                else:
                    print(filename)
                    print(file_extension)
                    if file_extension == "pdf":
                        pdf_text = Tokenizer.pdf_to_text(file_path)
                        print(Tokenizer.tokenize(pdf_text))
                    elif (file_extension == "doc") or (file_extension == "docx"):
                        doc_text = Tokenizer.word_to_text(file_path)
                        print(Tokenizer.tokenize(doc_text))
                    elif file_extension == "txt":
                        text = Tokenizer.read_text(file_path)
                        print(Tokenizer.tokenize(text))
                    else:
                        print(os.path.abspath(file))
                        print("Searchyption only support \".pdf\" , \".doc\" , \".docx\" , \".txt\" file formats")
            else:
                print("Error: argument 2 is not set!")

        elif sys.argv[1] == "--help":
            print("\nusage: searchyption tokenize [filename]\n")
            print("[filename] : text file, document, pdf")
        else:
            print("Error: Command Not Found!")
            print("use \"searchyption --help\" for  help\n")
    else:
        print(About.about())
        print("use \"searchyption --help\" for  help\n")
    