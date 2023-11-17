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
        <!-- Add more rows as needed -->
    </tbody>
</table>

<!-- DataTables Initialization Script -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) { // Check if jQuery is loaded
        jQuery('#myTable').DataTable(); // Initialize DataTables using jQuery
        "lengthChange": false;
    } else {
        console.error("jQuery is not loaded");
    }
});
</script>
