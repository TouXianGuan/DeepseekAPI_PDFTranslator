# DeepseekAPI_PDFTranslator

## Introduction
DeepseekAPI_PDFTranslator is a Python-based tool that leverages the DeepSeek-V2 model to translate PDF documents from English to Chinese. The Deepseek model is a powerful AI model designed for natural language processing tasks, including translation.  

## DeepSeek V2 Model
To learn more about the DeepSeek V2 model and its capabilities, you can visit the official website:

[DeepSeek Official Website](https://www.deepseek.com)  

## API Key
Sign in [deepseek platform](https://platform.deepseek.com/) and achieve the API Key.


## Usage
To use this tool, follow these steps:

1. **Download the Source Code**: Clone or download this repository to your local machine.

2. **Install Dependencies**: Ensure you have Python installed on your system. Then, install the required dependencies by running:  
```sh
pip install openai PyPDF2
```

3. **Run the Script**: Open your command line interface and navigate to the directory where the source code is located. Use the following command to translate a PDF file:  
```sh
python translate_pdf.py <input_pdf_path> <output_txt_path> <deepseek_api_key>
```
- <input_pdf_path>: The path to the input PDF file you want to translate.

- <output_txt_path>: The path where the translated text will be saved as a text file.

- <deepseek_api_key>: Your API key for accessing the Deepseek API.

## Example
Here is an example of how to use the script:

```sh
python translate_pdf.py ./documents/sample.pdf ./translated/sample_translated.txt YOUR_API_KEY
```

## Dependencies
- openai: For interacting with the Deepseek API.

- PyPDF2: For reading text from PDF files.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or support, please contact [touxianguan@outlook.com].

Thank you for using DeepseekAPI_PDFTranslator! We hope this tool simplifies your document translation needs.

