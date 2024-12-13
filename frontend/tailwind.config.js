/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#00585c",
        secondary: "#21b1ab",
        accent: "#d97a27",
        neutral: "rgb(24 25 25)",
        white: "#ffffff",
        black: "#000000",
        disabled: "#F2F1F2",
        disabled_text: "#D9D9D9",
        footer : "rgb(116 123 123)",
        section : "#363738",
        button : "rgb(48 103 32)"
      },
      fontFamily : { arial : ['Arial']}
    },
  },
  plugins: [],
};
