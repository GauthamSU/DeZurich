from pyscript import window, when, display
import js
from js import document

heading_1 = document.getElementById('section-1').getElementsByTagName('h1')[0]
heading_2 = document.getElementById('section-2').getElementsByTagName('h1')[0]
heading_3 = document.getElementById('section-3').getElementsByTagName('h1')[0]
heading_4 = document.getElementById('section-4').getElementsByTagName('h1')[0]

if js.localStorage.getItem('color-theme'):
    if not js.localStorage.getItem('color-theme') == 'dark':
        heading_1.classList.add('border-image')
        heading_2.classList.add('border-image1')
        heading_3.classList.add('border-image')
        heading_4.classList.add('border-image')
else:
    if not window.matchMedia('(prefers-color-scheme: dark)').matches:
        heading_1.classList.add('border-image')
        heading_2.classList.add('border-image1')
        heading_3.classList.add('border-image')
        heading_4.classList.add('border-image')


@when('click', '#theme-toggle')
def toggle_border():
    if js.localStorage.getItem('color-theme'):
        if not js.localStorage.getItem('color-theme') == 'light':
            if heading_1.classList.contains('border-image'):
                heading_1.classList.remove('border-image')
            if heading_2.classList.contains('border-image1'):
                heading_2.classList.remove('border-image1')
            if heading_3.classList.contains('border-image'):
                heading_3.classList.remove('border-image')
            if heading_4.classList.contains('border-image'):
                heading_4.classList.remove('border-image')
            
        else:
            if not heading_1.classList.contains('border-image'):
                heading_1.classList.add('border-image')
            if not heading_2.classList.contains('border-image1'):
                heading_2.classList.add('border-image1')
            if not heading_3.classList.contains('border-image'):
                heading_3.classList.add('border-image')
            if not heading_4.classList.contains('border-image'):
                heading_4.classList.add('border-image')
    else:
        if not document.documentElement.classList.contains('dark'):
            if not heading_1.classList.contains('border-image'):
                heading_1.classList.add('border-image')
            if not heading_2.classList.contains('border-image1'):
                heading_2.classList.add('border-image1')
            if not heading_3.classList.contains('border-image'):
                heading_3.classList.add('border-image')
            if not heading_4.classList.contains('border-image'):
                heading_4.classList.add('border-image')
        else:
            if heading_1.classList.contains('border-image'):
                heading_1.classList.remove('border-image')
            if heading_2.classList.contains('border-image1'):
                heading_2.classList.remove('border-image1')
            if heading_3.classList.contains('border-image'):
                heading_3.classList.remove('border-image')
            if heading_4.classList.contains('border-image'):
                heading_4.classList.remove('border-image')