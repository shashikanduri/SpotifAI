import { useEffect, useState } from "react";
import axios from "axios";
import { Navigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
axios.defaults.withCredentials = true;


const Home = () => {

  const { auth } = useAuth();
  
  async function handleSubmit(e) {

    // take user to spotify auth page 
    const response = await axios.get(`${import.meta.env.VITE_APP_API_URI}/authorize`);
    if (response.status !== 200 ){
      console.log(response);
    }
    else{
      window.location = response.data?.url;
    }
  }


  if (auth?.isAuthenticated) return <Navigate to = "/app" />;

  return (
    <section className="text-white w-full flex justify-center">
      <div className="w-[80%] bg-section rounded-xl h-fit overflow-hidden flex flex-col lg:flex-row px-4 md:px-8 py-6">

        <div className="text-sm md:text-base font-semibold my-4">
          <h2>
            Spotify playlists come to life! Log in with your Spotify account to unlock powerful playlist analysis
            powered by advanced language models. Discover trends, gain insights, and enhance your listening experience like never before.
            Ready to explore the music behind the numbers? Log in now and start analyzing!
            <br />
            <br />
          </h2>
          <br />

          <button
            className="rounded-full px-10 py-2 bg-button text-white hover:bg-primary/80 duration-100"
            onClick = {handleSubmit}
          >
            Login with Spotify
          </button>

          <br />
        </div>
      </div>
    </section>
  );
};

export default Home;
