const { fontFamily } = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    preflight: false,
    container: false,
  },
  darkMode: ["class", '[data-theme="dark"]'],
  content: ["./src/**/*.{jsx,tsx,html}"],
  theme: {
    extend: {
      aspectRatio: {
        '4/3': '4 / 3',
      },
      spacing: {


      },
      // fontFamily: {
      //   sans: ['"Inter"', ...fontFamily.sans],
      //   jakarta: ['"Plus Jakarta Sans"', ...fontFamily.sans],
      //   mono: ['"Fira Code"', ...fontFamily.mono],
      // },
      // borderRadius: {
      //   sm: "4px",
      // },
      // screens: {
      //    sm: "0px",
      //    lg: "997px",
      // },
    },
  },
  plugins: [],
};