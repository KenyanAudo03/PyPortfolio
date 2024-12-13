import docx
import PyPDF2

def count_lines_and_words(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        content = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        lines = content.splitlines()
        words = content.split()
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            content = ' '.join([page.extract_text() for page in pdf_reader.pages])
            lines = content.splitlines()
            words = content.split()
    else:
        raise ValueError("Unsupported file format")

    return len(lines), len(words)

if __name__ == "__main__":
    # Replace 'your_file.docx' or 'your_file.pdf' with the path to your document
    file_path = 'chinese.txt'

    try:
        line_count, word_count = count_lines_and_words(file_path)
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
