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
        customBlack: "#161819"
      },
    },
  },
  plugins: [],
  corePlugins: {
    preflight: false // <== disable this!
  },
}
