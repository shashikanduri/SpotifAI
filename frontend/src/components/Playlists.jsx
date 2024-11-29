import Playlist from "./Playlist";


function Playlists({playlists}) {

  return (
    <section className="text-primary w-full flex justify-center">

      <div className="w-[70%] bg-white rounded-xl h-fit overflow-hidden flex flex-col px-4 md:px-8 py-6">
        <h1 className = "font-bold text-xl"> Your Playlists </h1>
        <div className="text-sm md:text-base font-semibold my-4 text-gray-600">
          {
            playlists?.map((playlist) => playlist ? <Playlist key = {playlist.id} playlist = {playlist} /> : null)
          }
          <br />
        </div>
      </div>
    </section>
  );
}

export default Playlists;
