document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
        // Initialize DataTables and store the instance
        var dataTableInstance = jQuery('table.display').DataTable({
            "language": {
                "lengthMenu": "Display entries: _MENU_"
            },
            "columnDefs": [
                { 
                    "targets": ["Authors", "Last checked", "License"],
                    "visible": false,
                    "searchable": false
                }
            ],
            "initComplete": function () {
                this.api().columns().every(function (index) {
                    var column = this;
                    var columnName = jQuery(column.header()).text().trim();

                    // Define the column names to exclude from the dropdown filter
                    var excludedColumns = ["Title", "Subjects", "Audience", "URLs", "Reviews"];
                    if (excludedColumns.includes(columnName)) {
                        return; // Skip this iteration
                    }

                    // Create select element and add class
                    var select = document.createElement('select');
                    select.classList.add("dataTables_length", "select");
                    select.style.backgroundColor = "transparent"; 
                    select.add(new Option(''));

                    column.footer().replaceChildren(select);

                    // Apply listener for user change in value
                    select.addEventListener('change', function () {
                        var val = jQuery.fn.dataTable.util.escapeRegex(select.value);

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                    // Add list of options
                    column.data().unique().sort().each(function (d, j) {
                        select.add(new Option(d));
                    });
                });

                // Apply specific styles to the table
                jQuery('table.display').css({
                    'margin': '0',
                    'clear': 'both',
                    'width': '100%',
                    'table-layout': 'fixed'
                });
            }
        });

        // Additional code for setting column styles
        jQuery('table.display td').css({
            'white-space': 'pre-wrap',
            'word-wrap': 'break-word'
        });

        // Inject CSS to limit the width of the first column
        var style = document.createElement('style');
        style.type = 'text/css';
        style.innerHTML = '.display th:first-child, .display td:first-child { max-width: 15%; }';
        document.head.appendChild(style);

        // Setup column visibility toggle
        document.querySelectorAll('a.toggle-vis').forEach((el) => {
            el.addEventListener('click', function (e) {
                e.preventDefault();

                let columnIdx = this.getAttribute('data-column');
                let column = dataTableInstance.column(columnIdx);

                // Toggle the visibility
                column.visible(!column.visible());
            });
        });
    } else {
        console.error("jQuery is not loaded");
    }
});
