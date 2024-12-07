import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useSearchParams, Navigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
axios.defaults.withCredentials = true;


const Home = () => {

  const { auth } = useAuth();

  async function handleSubmit(e) {

    // take user to spotify auth page 
    const response = await axios.get('http://localhost:5001/get-client');
    if (response.status === 200 && response.data !== null) {
      
      // build spotify auth url for spotify login
      const base_url = response.data?.spotify_auth_url ?? null;
      if (base_url !== null) {
        const data = {
          client_id: response.data.client_id,
          response_type: "code",
          redirect_uri: "http://localhost:5173/callback",
          state: "shashi",
          scope: response.data.scope,
          show_dialog: true
        };
        const query_params = new URLSearchParams(data);
        const spotify_auth_url = `${base_url}?${query_params.toString()}`

        // go to the url
        window.location.href = spotify_auth_url;

      }
    }
  }


  if (auth?.isAuthenticated) return <Navigate to = "/app" />;

  return (
    <section className="text-primary w-full flex justify-center">
      <div className="w-[80%] bg-white rounded-xl h-fit overflow-hidden flex flex-col lg:flex-row px-4 md:px-8 py-6">

        <div className="text-sm md:text-base font-semibold my-4 text-gray-600">
          <h2>
            Spotify playlists come to life! Log in with your Spotify account to unlock powerful playlist analysis
            powered by advanced language models. Discover trends, gain insights, and enhance your listening experience like never before.
            Ready to explore the music behind the numbers? Log in now and start analyzing!"
            <br />
            <br />
          </h2>
          <br />

          <button
            className="rounded-full px-10 py-2 bg-secondary text-white hover:bg-primary/80 duration-100"
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
