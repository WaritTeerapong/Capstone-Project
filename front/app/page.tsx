import Image from "next/image";
import Link from 'next/link';

const SearchBar = () => {
  return (
    <div className="bg-background w-[1920px] h-[1080px] text-white justify-center relative">
      <h1 className="font-Inter font-bold text-[158px] pt-[383px] pl-[700px]">Finder</h1>
      <div className="bg-white w-[777px] h-[55px]  mt-[109px] ml-[571px] flex items-center rounded-lg border border-gray-300">
      <Image
        className="ml-[20px] absolute top-[745px] "
        src="/Vector.svg"
        alt="Image description"
        width={30}
        height={30}
      />
      <input
                    type="text"
                    className=" p-2 pl-[20px] w-[650px] text-gray-900 bg-gray-50 ml-[60px]  "
                    placeholder="Find what you're looking for right here....."
                    
                />
      
      </div>

      <input
                    type="file"
                    className=" p-2 pl-[20px] w-[200px] text-gray-900 bg-gray-50 ml-[60px]  "
                    placeholder=""
                    src="/Vector.svg"
                    
                />
      
      </div>
      
      
      
      
      
      
    
  );
};

export default SearchBar;
