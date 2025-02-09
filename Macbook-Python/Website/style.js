document.addEventListener("DOMContentLoaded", function() {
    fetch("navbar.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("navbar").innerHTML = data;
        });

    fetch("footer.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("footer").innerHTML = data;
        });

    mermaid.initialize({
        startOnLoad: true
    });
});

$(document).ready(function() {
    $('.dropdown-toggle').dropdown();
    $('.dropdown-submenu a').on("click", function(e) {
        var submenu = $(this).next('ul');
        $('.dropdown-menu').not(submenu).removeClass('show');
        submenu.toggleClass('show');
        e.stopPropagation();
        e.preventDefault();
    });
});

// Load the navbar.html content into the placeholder
fetch('navbar.html')
    .then(response => response.text())
    .then(data => {
        document.getElementById('navbar-placeholder').innerHTML = data;
    });