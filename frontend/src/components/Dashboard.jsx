import { useEffect, useState } from "react";
import Playlists from "./Playlists";
import axios from "axios";
axios.defaults.withCredentials = true;

function Dashboard() {

    const [playlists, setPlaylists] = useState([]);
    
    useEffect(() => {
        async function getData(){
            const response = await axios.get(`${import.meta.env.VITE_APP_API_URI}/dashboard`);
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
