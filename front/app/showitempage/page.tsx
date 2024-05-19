const colors = require('tailwindcss/colors');
import Image from "next/image";
import Link from 'next/link';




export default function Home() {


  return (
    <div className="w-[1920px] h-[1080px] ">
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
        <h1 className="ml-[214px] font-inter font-bold text-[40px] text-background mt-[15px]">Finder</h1>
        <input
          type="text"
          className=" p-2 pl-[70px]  w-[777px] h-[55px]  bg-gray-50 ml-[250px] mt-[15px] border-[#2D3648] border-[1px] rounded-[10px] text-[#2D3648] opacity-50 "
          placeholder="Find what you're looking for right here....."

        />

        <Link href="/loginpage" className="text-background font-bold font-inter text-[24px] text-center  ml-[200px] mt-[25px] ]">Login </Link>
        <Link href="/signuppage" className="text-background font-bold font-inter text-[24px] text-center  ml-[100px] mt-[25px] ]">Signup </Link>

      </div>

      <div className="border-b-2 border-[#2D3648] w-[1920px] h-[1px] opacity-50 "></div>

      <div className="w-[960px] h-[1080px] ml-[960px] border-white border-[1px]">
        <h1 className="font-inter font-bold text-[64px] text-[#2D3648] mt-[76px] ml-[135px]">Head Phone G435</h1>

        <div>
          <h2 className="text-[#2D3648] opacity-50 text-[18px] font-normal ml-[135px] mt-[30px] inline-block  ">Headphone</h2>
          <h2 className="text-[#2D3648] opacity-50 text-[18px] font-normal ml-[5px] inline-block  ">|</h2>
          <h2 className="text-[#2D3648] opacity-50 text-[18px] font-normal ml-[5px] inline-block  ">Logitech</h2>
        </div>


        <div className="flex space-x-2">
          <h2 className="font-bold text-[#2D3648] text-[18px] ml-[135px] font-inter inline-block"> Description: </h2>
          <p className="font-normol text-[#2D3648] text-[18px] ml-[0px] font-inter   ">  Logitech G435 headphones, a sleek and lightweight design in vibrant colors. They feature a comfortable headband, plush ear cups, and a foldable design for easy portability. The headphones boast exceptional sound quality with deep bass and crisp highs, perfect for immersive gaming sessions or enjoying your favorite music on the go.</p>

        </div>

        <div className="flex space-x-2">
          <h2 className="font-bold text-[#2D3648] text-[18px] ml-[135px] font-inter inline-block"> Location Lost:  </h2>
          <p className="font-normol text-[#2D3648] text-[18px] ml-[135px] font-inter   ">  Science Connect, KMUTT</p>

        </div>

        <div className="flex space-x-2">
          <h2 className="font-bold text-[#2D3648] text-[18px] ml-[135px] font-inter inline-block"> Date Lost:   </h2>
          <p className="font-normol text-[#2D3648] text-[18px] ml-[135px] font-inter   "> February 20, 2024</p>

        </div>

        <div className="flex space-x-2">
          <h2 className="font-bold text-[#2D3648] text-[18px] ml-[135px] font-inter inline-block"> Status:  </h2>
          <p className="font-normol text-green-500 text-[18px] ml-[135px] font-inter   "> Active </p>

        </div>

        <button className="bg-white hover:bg-blue-700 hover:text-white  text-[#2D3648] font-semibold w-[180px] h-[52px] ml-[135px]  rounded-[10px] text-[16px] border-[#2D3648] border-[1px] mt-[50px]  ] "> Request </button>

      </div>

      <div className="w-[600px] h-[600px] bg-black -mt-[1000px] ml-[240px] rounded-[10px] "></div>
      <Image
        className="ml-[900px] absolute top-[400px] "
        src="/Right.svg"
        alt="Image description"
        width={80}
        height={55}
      />
      <Image
        className="ml-[104px] absolute top-[400px] "
        src="/Arrow.svg"
        alt="Image description"
        width={80}
        height={55}
      />
      <div className="flex space-x-8  ">
        <div className="w-[120px] h-[120px] bg-white ml-[180px] rounded-[10px] mt-[75px] border-[#2D3648] border-[3px] opacity-50 "></div>
        <div className="w-[120px] h-[120px] bg-white ml-[240px] rounded-[10px] mt-[75px] border-[#2D3648] border-[3px] opacity-50"></div>
        <div className="w-[120px] h-[120px] bg-white ml-[240px] rounded-[10px] mt-[75px] border-[#2D3648] border-[3px] opacity-50"></div>
        <div className="w-[120px] h-[120px] bg-white ml-[240px] rounded-[10px] mt-[75px] border-[#2D3648] border-[3px] opacity-50"></div>
        <div className="w-[120px] h-[120px] bg-white ml-[240px] rounded-[10px] mt-[75px] border-[#2D3648] border-[3px] opacity-50"></div>

      </div>









    </div>





  );
}