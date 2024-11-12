/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './eb/templates/**/*.html',
    './**/*.html',
    './easybuy/**/*.js',    // JavaScript files in app
    './eb/**/*.jsx',   // If I React in Django
    './static/**/*.js',  
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        ivory: '#F9FAFB',
        'slate-gray': '#334155',
        'sage-green': '#6D9886',
        'mustard-yellow': '#EAB308',
      },
      fontFamily: {
        'playball': ['Playball', 'cursive'],
      },
    },
  },  
  plugins: [],
}

