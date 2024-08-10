import xlwings as xw

def get_color_hex(color):
    """Convert a color float to a hexadecimal string."""
    if color is None:
        return None
    try:
        # Convert float color to integer and then to hex
        color_int = int(color)
        # Convert to hex, remove '0x' prefix, pad with zeros if necessary
        return f"{color_int:06X}"
    except ValueError:
        return None

def get_text_format(cell):
    if not cell.value:
        return ""

    text = str(cell.value)
    tags = []

    font = cell.api.Font
    if font.Bold:
        tags.append("strong")
    if font.Italic:
        tags.append("em")
    if font.Underline == 2:  # xlUnderlineStyleSingle
        tags.append("u")

    color = get_color_hex(font.Color)
    if color and color != 'FFFFFF':  # Ignore white color
        tags.append(f'span style="color:#{color}"')

    # Ignore background color section
    # bgcolor = get_color_hex(cell.api.Interior.Color)
    # if bgcolor and bgcolor != 'FFFFFF':  # Ignore white color
    #     tags.append(f'span style="background-color:#{bgcolor}"')

    if tags:
        open_tags = " ".join(f"<{tag}>" for tag in tags)
        close_tags = " ".join(f"</{tag}>" for tag in reversed(tags))
        formatted_text = f"{open_tags}{text}{close_tags}"
    else:
        formatted_text = text

    return formatted_text

# Initialize Excel application
excel = xw.App(visible=False)
workbook = excel.books.open(r'D:\My-Github\pyhton-projects\excel to HTML\test.xlsx')
sheet = workbook.sheets['Sheet1']
cell = sheet.range('A1')

# Extract and format text
html_text = get_text_format(cell)

# Output HTML
html_file = r'D:\My-Github\pyhton-projects\excel to HTML\test.html'
with open(html_file, 'w') as file:
    file.write('<html>\n')
    file.write('<body>\n')
    file.write(f'<p>{html_text}</p>\n')
    file.write('</body>\n')
    file.write('</html>\n')

print("Content printed!")

# Cleanup
workbook.close()
excel.quit()
