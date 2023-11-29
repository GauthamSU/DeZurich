/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
    './static/pyscript/*.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
],
}

