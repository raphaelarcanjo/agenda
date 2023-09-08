window.onload = () =>
    document.querySelectorAll('input:not([type=submit],[type=checkbox],[type=radio])').forEach(field =>
        field.classList.add('form-control')
    )