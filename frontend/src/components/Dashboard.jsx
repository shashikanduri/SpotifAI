import { useEffect, useState } from "react";
import Playlists from "./Playlists";
import TopArtists from "./TopArtists";
import TopTracks from "./TopTracks";
import { useAuth } from "../contexts/AuthContext";
import axios from "axios";


function Dashboard() {

    const { setAuth } = useAuth();

    const [playlists, setPlaylists] = useState([]);
    const [topArtists, setTopArtists] = useState([]);
    const [topTracks, setTopTracks] = useState([]);
    
    useEffect(() => {
        async function getData(){
            const response = await axios.get('http://localhost:5001/dashboard');
            setPlaylists(response.playlists);
            setTopTracks(response.top_tracks);
            setTopArtists(response.top_artists);
            setAuth((prev) => ({ ...prev, user : response.user_info}));
        }
        getData();
    })

    return (
        <>
            <Playlists playlists = {playlists}/>
            <TopArtists topArtists = {topArtists}/>
            <TopTracks topTracks = {topTracks}/>
        </>
    );
}

export default Dashboard;
