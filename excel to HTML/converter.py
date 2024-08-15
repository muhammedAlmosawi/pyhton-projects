import xlwings as xw

def get_text_format(cell):
    if not cell.value:
        return ""

    text = cell.value
    if not text:
        return ""

    html_parts = []
    cell_length = len(text)

    for i in range(1, cell_length + 1):
        char = cell.api.Characters(i, 1)
        word = char.Text

        bold = char.Font.Bold
        italic = char.Font.Italic
        underline = char.Font.Underline

        if bold:
            word = f"<strong>{word}</strong>"
        if italic:
            word = f"<em>{word}</em>"
        if underline:  
            word = f"<u>{word}</u>"

        html_parts.append(word)

    return " ".join(html_parts)

def get_column_text(sheet, column_letter):
    print("..")
    last_row = sheet.range(f'{column_letter}1').end("down").row
    column_range = sheet.range(f'{column_letter}1:{column_letter}{last_row}')
    column_data = []
    for cell in column_range :
        if cell.value == None:
            break
        print(f"Processing cell: {cell.address}, Value: {cell.value}")
        text = get_text_format(cell)
        column_data.append(text)
    return column_data

excel = xw.App(visible=False)
workbook = excel.books.open(r'D:\My-Github\pyhton-projects\excel to HTML\Text Format Samples (2).xlsx')
sheet = workbook.sheets['Sheet1']
column_letter = 'A'

column_text = get_column_text(sheet, column_letter)


html_file = r'D:\My-Github\pyhton-projects\excel to HTML\test.html'
with open(html_file, 'w', encoding="utf-8") as file:
    file.write('<html>\n')
    file.write('<body>\n')
    for text in column_text:
        file.write(f'<p>{text}</p>\n')
    file.write('</body>\n')
    file.write('</html>\n')

print("Content printed!")

workbook.close()
excel.quit()
