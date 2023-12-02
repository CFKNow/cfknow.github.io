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

    # Initialize a dictionary to store the accumulated count of rows for each key
    rows_count_dict = {}

    # Iterate over each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        sheet_data = pd.read_excel(xls, sheet_name, header=None)
        first_row = sheet_data.iloc[0, 0] if not sheet_data.empty else sheet_name  # Default to sheet name if empty

        if not pd.isna(first_row) and isinstance(first_row, str):
            key = first_row.split('/')[0]
            md_filename = "./out/" + first_row.split('/', 1)[1] + ".md" if '/' in first_row else f"./out/{sheet_name}.md"
            title = format_title(first_row.split('/', 1)[1] if '/' in first_row else sheet_name)

            with open(md_filename, 'w') as file:
                # Write the header to the Markdown file
                file.write(f'---\npermalink: /{first_row}/\n')
                file.write(f'title: "{title}"\nlayout: single\ntoc: false\n')
                file.write(f'author_profile: false\nclasses: wide\nshare: true\nsidebar:\n  nav: {key}\n---\n\n')

                # Check if the sheet has more than one row (to include header and data)
                if len(sheet_data) > 1:
                    # Read the DataFrame, starting from the second row as header
                    df = pd.read_excel(xls, sheet_name, header=1)

                    # Accumulate the count of rows for the key
                    if key in rows_count_dict:
                        rows_count_dict[key] += len(df)
                    else:
                        rows_count_dict[key] = len(df)

                    # Count the number of rows where the "Reviews" column is empty
                    num_empty_reviews = df['Reviews'].isna().sum()
                    # Count the number of rows where the "Reviews" column is not empty
                    num_non_empty_reviews = len(df) - num_empty_reviews

                    # Write the counts to the Markdown file
                    file.write(f'Number of "orphaned rows": {num_empty_reviews}. Can you write a review to help other learners?\n\n')
                    file.write(f'Number of rows with non-empty reviews: {num_non_empty_reviews}\n\n')

                    # Writing the DataFrame to the Markdown file
                    file.write('<div class="table_cols_toggles">\nToggle column: <a class="toggle-vis btn btn--danger" data-column="3">Authors</a> <a class="toggle-vis btn btn--danger" data-column="5">Audience</a> <a class="toggle-vis btn btn--danger" data-column="8">Last checked</a> <a class="toggle-vis btn btn--danger" data-column="9">License</a>\n</div>\n')
                    file.write('<table class="display" style="width:100%">\n<thead>\n<tr>\n')
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
                                cell_value = cell_value.replace('>EPUB', ' class="btn btn--primary">EPUB')
                                cell_value = cell_value.replace('>Web', ' class="btn btn--primary">Web')
                                cell_value = cell_value.replace('>Videos', ' class="btn btn--primary">Videos')
                                cell_value = cell_value.replace('>Res</a>', ' class="btn btn--primary">Res</a>')
                                cell_value = cell_value.replace('>Errata</a>', ' class="btn btn--primary">Errata</a>')
                                cell_value = cell_value.replace('>LATEX</a>', ' class="btn btn--primary">LATEX</a>')
                                cell_value = cell_value.replace('>Code</a>', ' class="btn btn--primary">Code</a>')
                                cell_value = cell_value.replace('>Site</a>', ' class="btn btn--info">Site</a>')
                            elif df.columns[j] == "Reviews" and isinstance(cell_value, str):
                                cell_value = cell_value.replace('<a ', '<a class="btn btn--success" ')

                            file.write(f"    <td>{cell_value}</td>\n")
                        file.write("</tr>\n")

                    file.write("<tfoot>\n<tr>\n")
                    for _ in df.columns:
                        file.write("    <td></td>\n")
                    file.write("</tr>\n</tfoot>\n")
                else:
                    # Handle case when there's no table
                    file.write("No content available")

    return rows_count_dict

# Example usage
row_counts = create_markdown_from_excel_with_replacements('cfk.xlsx')
print(row_counts)
