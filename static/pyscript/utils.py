from pyscript import window, when, display
import js
from js import document

dark_icon = document.getElementById('theme-toggle-dark-icon')
light_icon = document.getElementById('theme-toggle-light-icon')

if js.localStorage.getItem('color-theme'):
    if js.localStorage.getItem('color-theme') == 'dark':
        light_icon.classList.remove('hidden')
    else:
        dark_icon.classList.remove('hidden')
else:
    if window.matchMedia('(prefers-color-scheme: dark)').matches:
        light_icon.classList.remove('hidden')
    else:
        dark_icon.classList.remove('hidden')


@when('click', '#theme-toggle')
def toggle_theme():
    dark_icon.classList.toggle('hidden')
    light_icon.classList.toggle('hidden')
    if js.localStorage.getItem('color-theme'):
        if js.localStorage.getItem('color-theme') == 'light':
            document.documentElement.classList.add('dark')
            js.localStorage.setItem('color-theme', 'dark')
        else:
            document.documentElement.classList.remove('dark')
            js.localStorage.setItem('color-theme', 'light')
    else:
        if document.documentElement.classList.contains('dark'):
            document.documentElement.classList.remove('dark')
            js.localStorage.setItem('color-theme', 'light')
        else:
            document.documentElement.classList.add('dark')
            js.localStorage.setItem('color-theme', 'dark')
            


