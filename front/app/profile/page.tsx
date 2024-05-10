const colors = require('tailwindcss/colors');
import Image from "next/image";
import Link from 'next/link';




export default function Home() {
  
  
    return (
  <div className="w-[1920px] h-[1392px] ">
   <div className="w-[1920px] h-[100px] flex">
   <Image
        className="ml-[104px] absolute top-[12.5px] "
        src="/logoblue.svg"
        alt="Image description"
        width={80}
        height={55}
        />


    <Image
        className="ml-[610px] absolute top-[27px]  "
        src="/Vector.svg"
        alt="Image description"
        width={30}
        height={30}
    />

    <Image
        className="ml-[1300px] absolute top-[4px] w-[25px] h-[25px] mt-[25px]   "
        src="/f7_camera-fill.svg"
        alt="Image description"
        width={80}
        height={55}
      />
    <h1 className= "ml-[214px] font-inter font-bold text-[40px] text-background mt-[15px]">Finder</h1>
    <input
      type="text"
      className=" p-2 pl-[70px]  w-[777px] h-[55px]  bg-gray-50 ml-[250px] mt-[15px] border-[#2D3648] border-[1px] rounded-[10px] text-[#2D3648] opacity-50 "
      placeholder="Find what you're looking for right here....."
                
    />

<Link href="/profile" className="text-background font-normal font-inter text-[24px] text-center  ml-[200px] mt-[25px] ]">Alex Logitima</Link> 
<Image
        className="ml-[1740px] absolute top-[4px] w-[54px] h-[54px] mt-[12.5px]   "
        src="/img user.svg"
        alt="Image description"
        width={54}
        height={54}
      />

  </div>

<div className="border-b-2 border-[#2D3648] w-[1920px] h-[1px] opacity-50 "></div>
<h1 className="text-background ml-[960px] text-[64px] mt-[190px] font-bold font-inter">Profile</h1>
<Image
        className="ml-[500px] absolute top-[450px] "
        src="/Ellipse 1.svg"
        alt="Image description"
        width={325}
        height={325}
      />
    <div className="w-[660px] h-[320px] ml-[1100px] mt-[80px]  rounded-[10px]  drop-shadow-2xl bg-white pt-[20px] ">
        <Image
        className="w-[32px] h-[32px]  ml-[600px] "
        src="/tabler_edit.svg"
        alt="Image description"
        width={32}
        height={32}
        />
      
        <div className="flex  ">
          <input
          className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[80px] w-[245px] h-[70px]  ] "
          type="text" placeholder="Alex Logitama"
          
          />
          
          
          <input
          className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight  w-[245px] h-[70px] ml-5  ] "
          type="tel" placeholder="086-555-4600"
          />

        </div>
        <div className="w-[245px] h-[1px] bg-[#2d3648] ml-[80px]"></div>
        <div className="w-[245px] h-[1px] bg-[#2d3648] ml-[345px]"></div>

        <div className="mt-[10px]">
        <input
          className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[80px] w-[505px] h-[70px]  ] "
          type="Email" placeholder="vuhaithuongnute@gmail.com"
          
          />
          <div className="w-[505px] h-[1px] bg-[#2d3648] ml-[80px]"></div>
        </div>

        <div className="mt-[10px]">
        <input
          className="appearance-none  rounded  py-2 px-4 text-gray-700 leading-tight ml-[80px] w-[245px] h-[70px]  ] "
          type="Password" placeholder="Password"
          
          />
          <div className="w-[245px] h-[1px] bg-[#2d3648] ml-[80px]"></div>
        </div>


        </div>

    <div className="w-[1500px] h-[720px] ml-[300px] mt-[80px]  rounded-[10px]  drop-shadow-2xl bg-white pt-[20px] flex "> 
    <div className="w-[1500px] h-[1px] bg-[#2d3648]  mt-[60px]  ">
      <div className="flex gap-[120px] -mt-[55px] text-[#2d3648] font-semibold text-[18px] ">
      <h1 className="ml-[140px]">Photo</h1>
      <h1>Name</h1>
      <h1>Category</h1>
      <h1>Sub Category</h1>
      <h1>Location</h1>
      <h1>Date Request</h1>
      <h1>Status</h1>
      </div>

    
    <div className="flex mt-[80px] gap-[75px] ">
    <Image
        className="w-[54px] h-[54px]  ml-[140px] "
        src="/img user (1).svg"
        alt="Image description"
        width={54}
        height={54}
        />
        <div className="flex gap-[60px]  text-[#2d3648] font-semibold text-[18px] ">
      
      <h1 className="-ml-[10px]" >Head Phone G435</h1>
      <h1>Headphone</h1>
      <h1 className="ml-[60px]">Logitech</h1>
      <h1 className="ml-[60px]">Science Connect</h1>
      <h1 className="ml-[20px]">2024-03-10</h1>
      <div className="border-[1px] border-[#1400FF] w-[150px] h-[30px] ">
      <h1 className="ml-[40px] text-[#1400FF]  ">In progress</h1>
      </div>

      </div>

    </div>

    <div className="flex mt-[80px] gap-[75px] ">
    <Image
        className="w-[54px] h-[54px]  ml-[140px] "
        src="/img user (2).svg"
        alt="Image description"
        width={54}
        height={54}
        />
        <div className="flex gap-[60px]  text-[#2d3648] font-semibold text-[18px] ">
      
      <h1 className="-ml-[10px]" >Canon EOS T3i</h1>
      <h1>Camera</h1>
      <h1 className="ml-[60px]">Canon</h1>
      <h1 className="ml-[60px]">Science Connect</h1>
      <h1 className="ml-[20px]">2024-02-26</h1>
      <div className="border-[1px] border-[#C70E27] w-[150px] h-[30px] ">
      <h1 className="ml-[40px] text-[#C70E27]  ">Rejected</h1>
      </div>

      </div>

    </div>

    <div className="flex mt-[80px] gap-[75px] ">
    <Image
        className="w-[54px] h-[54px]  ml-[140px] "
        src="/img user (5).svg"
        alt="Image description"
        width={54}
        height={54}
        />
        <div className="flex gap-[60px]  text-[#2d3648] font-semibold text-[18px] ">
      
      <h1 className="-ml-[10px]" >Canon EOS 80D</h1>
      <h1>Camera</h1>
      <h1 className="ml-[60px]">Canon</h1>
      <h1 className="ml-[60px]">Science Connect</h1>
      <h1 className="ml-[20px]">2024-02-23</h1>
      <div className="border-[1px] border-[#55CE63] w-[150px] h-[30px] ">
      <h1 className="ml-[40px] text-[#55CE63]  ">Returned</h1>
      </div>

      </div>

    </div>

    <div className="flex mt-[80px] gap-[75px] ">
    <Image
        className="w-[54px] h-[54px]  ml-[140px] "
        src="/img user (3).svg"
        alt="Image description"
        width={54}
        height={54}
        />
        <div className="flex gap-[60px]  text-[#2d3648] font-semibold text-[18px] ">
      
      <h1 className="-ml-[10px]" >iPhone X White</h1>
      <h1>Phone</h1>
      <h1 className="ml-[60px]">iPhone</h1>
      <h1 className="ml-[60px]">Science Connect</h1>
      <h1 className="ml-[20px]">2024-02-18</h1>
      <div className="border-[1px] border-[#7D10FF] w-[150px] h-[30px] ">
      <h1 className="ml-[40px] text-[#7D10FF]  ">In progress</h1>
      </div>

      </div>

    </div>



    </div>


    </div>
        
</div>

  

             
           




      
   
    );
}