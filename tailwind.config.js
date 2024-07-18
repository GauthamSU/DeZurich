/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
    './static/pyscript/*.py',
    './**/**/templates/*.html',
    './**/**/templates/**/*.html',
  ],
  theme: {
    extend: {
      keyframes: {
        appear: {
          '0%': { transform: 'translateX(300px)' },
          '100%': { transform: 'translateX(0)' },
                },
        translateTop: {
          'from': { transform: 'translateY(300px)' },
          'to': { transform: 'translateY(0)' },
              },
        opacity: {
          'from': { opacity: '0'},
          'to': {opacity: '1'}
              }
              },
      animation: {
        'appear': 'appear 1s ease-in-out forwards',
        'translateTop': 'translateTop 1s ease-in-out forwards',
        'opacity': 'opacity 1s ease-in-out forwards'
                }
            },
      fontFamily: {
        caveat: ['"Caveat"', 'cursive'],
        graduate: ['"Graduate"', 'serif'],
        marko: ['"Marko One"', 'serif'],
        roboto: ['"Roboto"', 'sans-serif'],
        josefin: ['"Josefin Sans"', 'sans-serif'],
        maamli: ['"Ga Maamli"', 'sans-serif']
      },
  },
  plugins: [
    require('flowbite/plugin')
],
} 

