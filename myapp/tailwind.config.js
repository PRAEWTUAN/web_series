/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "media",
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        angsana: ["angsana"],
        Sriracha: ["Sriracha"],
        KoHo: ["KoHo"],
        sarabun: ["Sarabun", "sans-serif"],
        mitr: ["Mitr", "sans-serif"],
        prompt: ["Prompt", "sans-serif"],
        Oswald: ["Oswald"]
      }
    }
  },
  plugins: []
}
