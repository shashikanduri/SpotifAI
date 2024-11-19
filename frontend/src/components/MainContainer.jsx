
function MainContainer() {
  console.log(document.cookie);

  return (
    <section className="text-primary w-full flex justify-center">

      <div className="w-[80%] bg-white rounded-xl h-fit overflow-hidden flex flex-col px-4 md:px-8 py-6">
        <h1 className = "font-bold text-xl"> Your Playlists </h1>
        <div className="text-sm md:text-base font-semibold my-4 text-gray-600">
          <h2>
            Spotify playlists come to life! Log in with your Spotify account to unlock powerful playlist analysis
            powered by advanced language models. Discover trends, gain insights, and enhance your listening experience like never before.
            Ready to explore the music behind the numbers? Log in now and start analyzing!"
            <br />
            <br />
          </h2>
          <br />
        </div>
      </div>
    </section>
  );
}

export default MainContainer;
