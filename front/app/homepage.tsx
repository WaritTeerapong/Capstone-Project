const colors = require('tailwindcss/colors');
import Image from "next/image";
import Link from 'next/link';
import { useRouter } from 'next/router'
export default function Home() {
    return (
      <div className="flex flex-col items-center justify-center w-[1920px] h-[1080px] py-2">
        <h1 className="text-4xl font-bold text-center mb-2">Login</h1>
        <h1 className="text-4xl font-normal text-center mb-4 text-[16px] ">Welcome! Please fill username and password to <br/> sign in into your account.</h1>
        <form className="w-full max-w-sm">
          <div className="md:flex md:items-center mb-6">
            <div className="md:w-1/3">
              <label className="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                Username
              </label>
            </div>
            <div className="md:w-2/3">
              <input
                className="appearance-none border-2 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
                type="text"
              />
            </div>
          </div>
          <div className="md:flex md:items-center mb-6">
            <div className="md:w-1/3">
              <label className="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                Password
              </label>
            </div>
            <div className="md:w-2/3">
              <input
                className="appearance-none border-2 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
                type="password"
              />
            </div>
          </div>
          <div className="md:flex md:items-center">
            <div className="md:w-1/3"></div>
            <div className="md:w-2/3">
              <button
                className="shadow bg-purple-500 hover:bg-purple-400 focus:shadow-outline-purple focus:outline-none text-white font-bold py-2 px-4 rounded"
                type="submit"
              >
                Login
              </button>
            </div>
          </div>
        </form>
        <div className="text-center mt-6">
          <a
            href="/signup"
            className="inline-block text-sm text-purple-500 align-baseline hover:text-purple-800"
          >
            Don't have an account? Create an account
          </a>
        </div>
      </div>
      
    );
  }