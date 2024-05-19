
export default function Home() {



  return (
    <>
      {/* <div className="bg-blue-700 h-screen flex items-center justify-center">
        <div className="flex justify-center items-center ">
          <div className="bg-red-600">
            <h1 className="">Finder</h1>
          </div>
          <div className="bg-green-600">
            <form className="">
              <input type="text" placeholder="Search" />
              <button type="submit">Search</button>
            </form>
          </div>
        </div>
      </div> */}

      <div className="bg-blue-700 h-screen flex flex-col items-center justify-center">
      <div className="flex flex-col justify-center items-center">
        <div className="bg-red-600 p-4 rounded">
          <h1 className="text-white text-4xl">Finder</h1>
        </div>
        <div className="bg-green-600 p-4 rounded mt-4 w-full max-w-md">
          <form className="flex" >
            <input
              type="text"
              placeholder="Search"
              className="flex-grow p-2 rounded-l-lg border border-gray-300 focus:outline-none"
              
            />
            <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded-r-lg">Search</button>
          </form>
        </div>
      </div>
    </div>
    </>
  );

};

