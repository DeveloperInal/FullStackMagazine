/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        customBlue: "0e294a",
      },
    },
  },
  plugins: [],
  corePlugins: {
    preflight: false // <== disable this!
  },
}