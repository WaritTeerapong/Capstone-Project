const colors = require('tailwindcss/colors');
import Image from "next/image";
import Link from 'next/link';




export default function Home() {
  
  return (
    <div className="bg-background w-[1920px] h-[1080px] text-white justify-center relative">
      <div className="bg-white w-[960px] h-[1080px] ml-[960px]  ">
      <p className="ml-[230px] absolute top-[325px] text-loginco font-Inter font-bold text-[48px]">Create an account</p>
      <p className="ml-[230px] absolute top-[395px] text-loginco font-Inter font-normal text-[16px]">Find lost items easily with our Lost and Found service.<br /> Get started now! </p>
      
      
      <div className="md:flex md:items-center mb-6   ">
        
        
      <div className="mt-[500px]    ">
      <input
        className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[230px] w-[500px] h-[70px]  "
        type="Email"
        placeholder="Email"
      />
      
       <div className="md:flex md:items-center mb-6 md:w-1/3  ">
            
            <div className=" mt-2  flex space-x-4  ">
              <input
                className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[230px] w-[245px] h-[70px]  ] "
                type="text" placeholder="Username"
              />
              <input
                className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[485px] w-[245px] h-[70px]   ] "
                type="tel" placeholder="Phone"
              />
            </div>
    </div>     


<div className="md:flex md:items-center mb-6  md:w-1/3">
           
            <div className="  flex space-x-4  ">
              <input
                className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[230px] w-[245px] h-[70px]  ] "
                type="Password" placeholder="Confirm Password"
              />
              <input
                className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[230px] w-[245px] h-[70px]  ] "
                type="Password" placeholder="Password"
              />
            </div>
          </div>


      </div>
      


   
    
    </div>
   
    
    <button className="bg-Rectangle2 hover:bg-blue-700 text-white font-semibold w-[500px] h-[70px] ml-[234px]  rounded-[10px] text-[24px]">Sign Up </button>
    
   
<h1 className="text-loginco mt-[20px] ml-[387px] ">Have an account?<Link href="front\app\signuppage.tsx" className="text-background font-normal text-[16px]   ]"> Login</Link> </h1>
                    


      
      
      
      
      
      
      
      
      
      
      
      </div>
      <div className="bg-Rectangle2 absolute top-0 w-[300px] h-[120px]"></div>
      <div className="bg-Rectangle2 absolute top-[90px] w-[300px] h-[120px] left-[-90px] rotate-90 "></div>
      <div className="bg-Rectangle2 absolute top-[120px] w-[90px] h-[90px] left-[120px]   "></div>

      
      <div className="bg-Rectangle2 absolute top-[960px] w-[300px] h-[120px] left-[660px]   "></div>
      <div className="bg-Rectangle2 absolute top-[870px] w-[300px] h-[120px] left-[750px] rotate-90   "></div>
      <div className="bg-Rectangle2 absolute top-[870px] w-[90px] h-[90px] left-[750px]   "></div>


      
      <Image
        className="ml-[300px] absolute top-[267px]"
        src="/ph_detective-duotone.svg"
        alt="Image description"
        width={354}
        height={354}
      />
      <p className="ml-[300px] absolute top-[657px] text-white font-Inter font-bold text-[128px] w-[810px] h-[120px]">Finder</p>
     
           
          
    </div>
  );
}
