import pandas as pd
import os

# Function to capitalize the first letter and replace certain characters
def format_title(title):
    title = title.replace('-', ' ').replace('_', ' and ')
    return title.capitalize()

# Function to create Markdown files from Excel sheets with specific replacements
def create_markdown_from_excel_with_replacements(excel_file):
    # Load the Excel file
    xls = pd.ExcelFile(excel_file)

    # Iterate over each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        first_row = pd.read_excel(xls, sheet_name, nrows=1, header=None).iloc[0, 0]
        if not pd.isna(first_row) and isinstance(first_row, str):
            md_filename = "./out/" + first_row + ".md"
            title = format_title(first_row)

            with open(md_filename, 'w') as file:
                # Write the header to the Markdown file
                file.write(f'---\npermalink: /get/{first_row}/\n')
                file.write(f'title: "{title}"\nlayout: single\ntoc: false\n')
                file.write('author_profile: false\nclasses: wide\nshare: true\nsidebar:\n  nav: get\n---\n\n')

                if len(pd.read_excel(xls, sheet_name, header=None)) > 1:
                    df = pd.read_excel(xls, sheet_name, header=1)
                    # class="table_cols_toggles"
                    file.write('<div>\nToggle column: <a class="toggle-vis" data-column="3">Authors</a> - <a class="toggle-vis" data-column="8">Last checked</a> - <a class="toggle-vis" data-column="9">License</a>\n</div>')
                    file.write('<table class="display">\n<thead>\n<tr>\n')
                    for col in df.columns:
                        file.write(f'    <th>{col}</th>\n')
                    file.write('</tr>\n</thead>\n<tbody>\n')

                    for i in df.index:
                        row = df.loc[i]
                        file.write("<tr>\n")
                        for j, cell in enumerate(row):
                            cell_value = '' if pd.isna(cell) else cell
                            if df.columns[j] == "URLs" and isinstance(cell_value, str):
                                cell_value = cell_value.replace('>PDF', ' class="btn btn--primary">PDF')
                                cell_value = cell_value.replace('>HTML', ' class="btn btn--primary">HTML')
                                cell_value = cell_value.replace('>Res</a>', ' class="btn btn--primary">Res</a>')
                                cell_value = cell_value.replace('>Errata</a>', ' class="btn btn--primary">Errata</a>')
                                cell_value = cell_value.replace('>Site</a>', ' class="btn btn--info">Site</a>')
                            elif df.columns[j] == "Reviews" and isinstance(cell_value, str):
                                cell_value = cell_value.replace('<a ', '<a class="btn btn--danger" ')
                            file.write(f"    <td>{cell_value}</td>\n")
                        file.write("</tr>\n")

                    file.write("<tfoot>\n<tr>\n")
                    for _ in df.columns:
                        file.write("    <td></td>\n")
                    file.write("</tr>\n</tfoot>\n")

                    file.write("</table>\n")


create_markdown_from_excel_with_replacements('cfk.xlsx')
