import Playlist from "./Playlist";


function TopArtists() {

  return (
    <section className="text-primary w-full flex justify-center">

      <div className="w-[70%] bg-white rounded-xl h-fit overflow-hidden flex flex-col px-4 md:px-8 py-6">
        <h1 className = "font-bold text-xl"> Your Top Artists </h1>
        <div className="text-sm md:text-base font-semibold my-4 text-gray-600">
          <Playlist />
          <br />
        </div>
      </div>
    </section>
  );
}

export default TopArtists;
