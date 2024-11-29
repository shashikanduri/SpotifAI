import { useEffect, useState } from "react";
import Playlists from "./Playlists";
import TopArtists from "./TopArtists";
import TopTracks from "./TopTracks";
import { useAuth } from "../contexts/AuthContext";
import axios from "axios";
axios.defaults.withCredentials = true;

function Dashboard() {

    const [playlists, setPlaylists] = useState([]);
    
    useEffect(() => {
        async function getData(){
            const response = await axios.get('http://localhost:5001/dashboard');
            setPlaylists(response.data.data.playlists.items);
        }
        getData();
    }, [])

    return (
        <>
            <Playlists playlists = {playlists}/>
        </>
    );
}

export default Dashboard;
