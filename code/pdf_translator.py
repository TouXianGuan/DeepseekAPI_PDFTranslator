import sys
import openai
from PyPDF2 import PdfReader

class PDFTranslator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.total_time = 0

    def translate_text(self, text):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates English to Chinese."},
                {"role": "user", "content": text},
            ],
            stream=False
        )
        return response.choices[0].message.content

    def read_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def save_txt(self, file_path, text):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

    def translate_pdf(self, input_path, output_path):
        text = self.read_pdf(input_path)
        print(f"The length of your pdf is {len(text)}.")
        translated_text = ""
        start = 0
        call_count = 0

        while start < len(text):
            end = start + 20000
            while end < len(text) and text[end] != '.':
                end += 1
            if end < len(text):
                end += 1
            chunk = text[start:end]
            translated_chunk = self.translate_text(chunk)
            translated_text += translated_chunk
            start = end
            call_count += 1
            print(f"Deepseek-v2 API has been called {call_count} times.")
    
        self.save_txt(output_path, translated_text)
        print(f"Translation saved to {output_path}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python translate_pdf.py <input_pdf_path> <output_txt_path> <deepseek_api_key>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    api_key = sys.argv[3]

    translator = PDFTranslator(api_key)
    translator.translate_pdf(input_path, output_path)

if __name__ == "__main__":
    main()