import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors:{
        background:"#1C2F93",
        Rectangle2:"#1f2f85",
        loginco:"#2D3648",
        bordergrey:"#2D364880" 
        
      }
    },
  },
 
  plugins: [],
};
export default config;
