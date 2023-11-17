
document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
        jQuery('table.dataTable').DataTable({
            "language": {
                "lengthMenu": "Display entries: _MENU_"
            },
            "initComplete": function () {
                this.api().columns().every(function (index) {
                    var column = this;

                    // Exclude specific columns by index
                    var excludedColumns = [1, 2];
                    if (excludedColumns.includes(index)) {
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
            }
        }); 
    } else {
        console.error("jQuery is not loaded");
    }
});

