---
permalink: /get/mathematics-geometry_trigonometry-books/
title: "Geometry and trigonometry books"
layout: single
toc: false
author_profile: false
classes: wide
share: true
sidebar:
  nav: "get"
---

<!-- HTML Table -->
<table id="myTable" class="display" style="width:100% !important;">
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
            <th>Column 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
            <td>Row 1, Col 3</td>
        </tr>
        <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
            <td>Row 1, Col 3</td>
        </tr>
        <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
            <td>Row 1, Col 3</td>
        </tr>
        <tfoot>
            <tr>
              <th>Column 1</th>
              <th>Column 2</th>
              <th>Column 3</th>
            </tr>
        </tfoot>
    </tbody>
</table>

<!-- DataTables Initialization Script -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) { // Check if jQuery is loaded
        jQuery('#myTable').DataTable({
            "language": {
                "lengthMenu": "Display entries: _MENU_"
            },
            "initComplete": function () {
                this.api().columns().every(function () {
                    var column = this;

                    // Create select element and add class
                    var select = document.createElement('select');
                    select.classList.add("dataTables_length", "select"); // Add classes here
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
</script>



