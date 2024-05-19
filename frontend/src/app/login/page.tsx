"use client";
import { TextField } from '@mui/material';
import Link from 'next/link';

const Login = () => {

    return (
        <div className="items-center justify-center flex min-h-screen w-full h-full">
            <div className="bg-blue-700 min-h-screen w-1/2 p-8 hidden md:block">
                <div className="p-8 min-h-screen items-center justify-center flex">
                    <div className="max-w-md p-8 text-center">
                        <h2 className="text-2xl text-gray-100 mb-2">
                            Welcome to
                        </h2>
                        <h1 className="text-8xl text-white font-bold mb-3">
                            Finder
                        </h1>
                        <h3 className="text-sm text-gray-200  mb-2">
                            If you've lost something, worry not. We're here to help you locate it quickly and easily.
                            Let's get started on finding what you've lost!
                        </h3>
                    </div>
                </div>
            </div>
            <div className="bg-white w-full md:w-1/2 p-8 min-h-screen flex items-center justify-center ">
                <div className="max-w-md bg-white p-8 w-full flex flex-col justify-center">
                    <h2 className="text-2xl font-bold mb-2">
                        Login
                    </h2>
                    <h3 className="text-sm text-gray-600 mb-4">
                        Welcome! Please fill email and password to login into your account.
                    </h3>
                    <form >
                        {/* Email */}
                        <div className="mb-4">
                            <TextField
                                className="w-full px-3 pl-0 text-sm border rounded-lg "
                                label="Email"
                                type="email"
                                id="email"
                                name="email"
                                placeholder="Enter your email"
                            // onChange={handleChange}
                            // required
                            />
                        </div>
                        {/* Password */}
                        <div className="mb-4">
                            <TextField
                                className='w-full px-3 pl-0 text-sm border rounded-lg'
                                label="Password"
                                type="password"
                                id="password"
                                name="password"
                            // onChange={handleChange}
                            // required
                            />
                        </div>
                        <button className="w-full bg-blue-700 text-white py-2 rounded-lg hover:bg-blue-700">
                            Login
                        </button>
                    </form>
                    <p className="mt-4 text-center text-sm">
                        Don’t have an account? &nbsp;
                        <Link href="/register" className="text-blue-700 hover:underline">
                            Create an account
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Login;
