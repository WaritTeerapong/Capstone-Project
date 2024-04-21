const colors = require('tailwindcss/colors');
import Image from "next/image";
import Link from 'next/link';





export default function () {
  
  return (
    <div className="bg-background w-[1920px] h-[1080px] text-white justify-center relative">
      <div className="bg-white w-[960px] h-[1080px] ml-[960px]  ">
      <p className="ml-[230px] absolute top-[325px] text-loginco font-Inter font-bold text-[48px]">Login</p>
      <p className="ml-[230px] absolute top-[395px] text-loginco font-Inter font-normal text-[16px]"> Welcome! Please fill username and password to <br />sign in into your account.</p>
      
      
      <div className="md:flex md:items-center mb-6 pb-[100px]  ">
        
      <div className="mt-[500px] w-[500px] h-[70px]   ">
      <input
        className="appearance-none  rounded w-full py-2 px-4 text-gray-700 leading-tight ml-[234px]  "
        type="text"
        placeholder="Username"
      />
       <div className="md:flex md:items-center mb-6  ">
            <div className="md:w-1/3 ">
              
            </div>
            <div className=" mt-[50px] w-[500px] h-[70px] ">
              <input
                className="ppearance-none  rounded w-full py-2 px-4 text-gray-700 leading-tight ml-[110px]  ] "
                type="password" placeholder="Password"
              />
            </div>
          </div>
          
    </div>

   
    
    </div>
    <label className="flex items-center gap-2 text-black ml-[234px]">
      <input type="checkbox" className="accent-black scale-125 "/> Remember Password
     
    </label>
    
    <button className="bg-Rectangle2 hover:bg-blue-700 text-white font-semibold w-[500px] h-[70px] ml-[234px] mt-[60px]  rounded-[10px] text-[24px]">Login</button>
    
   
<h1 className="text-loginco mt-[51px] ml-[320px] ">Don’t have an account? <Link href="/signuppage" className="text-background font-normal text-[16px]   ]">Create an Account</Link> </h1>
                    


      
      
      
      
      
      
      
      
      
      
      
      </div>
      <div className="bg-Rectangle2 absolute top-0 w-[300px] h-[120px]"></div>
      <div className="bg-Rectangle2 absolute top-[90px] w-[300px] h-[120px] left-[-90px] rotate-90 "></div>
      <div className="bg-Rectangle2 absolute top-[120px] w-[90px] h-[90px] left-[120px]   "></div>

      
      <div className="bg-Rectangle2 absolute top-[960px] w-[300px] h-[120px] left-[660px]   "></div>
      <div className="bg-Rectangle2 absolute top-[870px] w-[300px] h-[120px] left-[750px] rotate-90   "></div>
      <div className="bg-Rectangle2 absolute top-[870px] w-[90px] h-[90px] left-[750px]   "></div>


      
      <Image
        className="ml-[403px] absolute top-[267px]"
        src="/ph_detective-duotone.svg"
        alt="Image description"
        width={154}
        height={154}
      />
      <p className="ml-[385px] absolute top-[426px] text-white font-Inter font-light text-[36px]">Welcome To</p>
      <p className="ml-[310px] absolute top-[494px] text-white font-Inter font-bold text-[128px]">Finder</p>
      <p className="ml-[188px] text-center font-light absolute top-[629px] text-white font-Inter  text-[24px] mt-[38.4px]">If you've lost something, worry not. We're here to help <br /> you
          locate it quickly and easily. Let's get started on <br />finding what
          you've lost!</p>
           
          
    </div>
  );
}
