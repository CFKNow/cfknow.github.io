import pandas as pd
import os

# Function to capitalize the first letter and replace certain characters
def format_title(input, key):
    if len(input) > len(key) + 1:
        input = input[2 * (len(key) + 1):]
        title = input.replace('-', ' ').replace('_', ' and ')
    else:
        title = input
    return title[0].capitalize() + title[1:]

# Function to create Markdown files from Excel sheets with specific replacements
def create_markdown_from_excel_with_replacements(excel_file):
    xls = pd.ExcelFile(excel_file)
    rows_count_dict = {}
    subjects_count = {}  # Initialize a dictionary to store the count of each subject

    for sheet_name in xls.sheet_names:
        sheet_data = pd.read_excel(xls, sheet_name, header=None)
        first_row = sheet_data.iloc[0, 0] if not sheet_data.empty else sheet_name

        if not pd.isna(first_row) and isinstance(first_row, str):
            key = first_row.split('/')[0] if '/' in first_row else ''
            md_filename = './out/' + first_row.split('/', 1)[1] + '.md' if '/' in first_row else f'./out/{sheet_name}.md'
            title = format_title(first_row, key)

            with open(md_filename, 'w') as file:
                file.write(f'---\npermalink: /{first_row}/\n')
                file.write(f'title: "{title}"\nlayout: single\ntoc: false\n')
                file.write(f'author_profile: false\nclasses: wide\nshare: true\nsidebar:\n  nav: {key}\n---\n\n')

                if len(sheet_data) > 1:
                    df = pd.read_excel(xls, sheet_name, header=1)

                    if key in rows_count_dict:
                        rows_count_dict[key] += len(df)
                    else:
                        rows_count_dict[key] = len(df)

                    num_empty_reviews = df['Reviews'].isna().sum()
                    num_non_empty_reviews = len(df) - num_empty_reviews

                    file.write(f'Number of "orphaned rows": {num_empty_reviews}. Can you write a review to help other learners?\n\n')
                    file.write(f'Number of rows with non-empty reviews: {num_non_empty_reviews}\n\n')

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
                            # Existing cell value processing code goes here...
                            file.write(f"    <td>{cell_value}</td>\n")
                        file.write("</tr>\n")

                    file.write("<tfoot>\n<tr>\n")
                    for _ in df.columns:
                        file.write("    <td></td>\n")
                    file.write("</tr>\n</tfoot>\n")

                    # Process the Subjects column to count occurrences of each subject
                    if 'Subjects' in df.columns:
                        for subjects in df['Subjects'].dropna():
                            for subject in subjects.split('<br>'):
                                subject = subject.strip()  # Removing leading/trailing whitespaces
                                if subject in subjects_count:
                                    subjects_count[subject] += 1
                                else:
                                    subjects_count[subject] = 1

                else:
                    file.write("No content available")

    return rows_count_dict, subjects_count

rows_count_dict, subjects_count = create_markdown_from_excel_with_replacements('cfk.xlsx')
print(rows_count_dict)
print(sum(rows_count_dict.values()))
print(subjects_count)  # Print the count of each unique subject
