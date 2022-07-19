/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/*"],
  theme: {
    extend: {
      gridTemplateRows: {
        '3': 'repeat(3, minmax(80px, 80px))'
      },
      gridTemplateColumns: {
        '3' : 'repeat(3, mimax(80px,80px))'
      }
    },
  },
  plugins: [],
}
