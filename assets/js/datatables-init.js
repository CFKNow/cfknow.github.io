document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
        // Initialize DataTables and store the instance
        var dataTableInstance = jQuery('table.display').DataTable({
            "language": {
                "lengthMenu": "Display entries: _MENU_"
            },
            "columnDefs": [
                {
                    "targets": [3, 5, 8, 9], // Indices of 'Authors', 'Audience', 'Last checked', and 'License' columns
                    "visible": false
                }
            ],
            "initComplete": function () {
                //console.log("DataTable initialized.");
                this.api().columns().every(function () {
                    var column = this;
                    var columnName = jQuery(column.header()).text().trim();

                    // Define the column names to exclude from the dropdown filter
                    var excludedColumns = ["Title", "Subjects", "Audience", "Authors", "URLs", "Reviews", "License"];
                    if (excludedColumns.includes(columnName)) {
                        //console.log("Column excluded from dropdown filter:", columnName);
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
                    column.data().unique().sort().each(function (d) {
                        select.add(new Option(d));
                    });
                });
            }
        });

        // Additional code for setting column styles
        jQuery('table.display td').css({
            'white-space': 'pre-wrap',
            'word-wrap': 'break-word'
        });

        // Inject CSS to limit the width of the first column
        // var style = document.createElement('style');
        // style.type = 'text/css';
        // style.innerHTML = '.display th:first-child, .display td:first-child { max-width: 15%; }';
        // document.head.appendChild(style);

        // Setup column visibility toggle
        jQuery(document).on('click', 'a.toggle-vis', function(e) {
            e.preventDefault();
        
            // Log that the link was clicked
            // console.log("Toggle link clicked.");
        
            let columnIdx = jQuery(this).data('column');
            // console.log("Toggling visibility for column:", columnIdx);
            let column = dataTableInstance.column(columnIdx);
        
            // Check if the column was found before toggling visibility
            if (column) {
                // Toggle the visibility
                column.visible(!column.visible());
            } else {
                console.error("Column not found:", columnIdx);
            }
        });

    } else {
        console.error("jQuery is not loaded");
    }
});
