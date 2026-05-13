import docx
from docx.enum.style import WD_STYLE_TYPE

def list_styles(filepath):
    doc = docx.Document(filepath)
    print("Available Table Styles:")
    for style in doc.styles:
        if style.type == WD_STYLE_TYPE.TABLE:
            print(f" - {style.name}")

if __name__ == '__main__':
    list_styles('FYP_Final_Report_AI_Interview_System.docx')
