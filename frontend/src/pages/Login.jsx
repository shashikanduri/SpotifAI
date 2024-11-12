import { useEffect } from "react";
import PageNav from "../components/PageNav";
import styles from "./Login.module.css";
import Button from "../components/Button";
import axios from "axios";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

export default function Login() {

  const [params] = useSearchParams();
  const { auth, updateSpotifyAuth } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    
    // take user to spotify auth page 
    console.log("shashi");
    const response = await axios.get('http://127.0.0.1:5000/get-client');
    if(response.status === 200 && response.data !== null){

      // build spotify auth url for spotify login
      const base_url = response.data?.spotify_auth_url ?? null;
      if(base_url !== null){
        const data = {
          client_id : response.data.client_id,
          response_type : "code",
          redirect_uri : "http://localhost:5173",
          state : "shashi",
          scope : response.data.scope,
          show_dialog: true
        };
        const query_params = new URLSearchParams(data);
        const spotify_auth_url = `${base_url}?${query_params.toString()}`
        
        // go to the url
        window.location.href = spotify_auth_url;

      }
    }
  }

  useEffect(
    function () {
      if (!auth.isAuthenticated){
        const code = params.get("code");
        if (code !== null){
          updateSpotifyAuth("shashi");
          navigate("/app");
        }
      }
      else{
        navigate("/app");
      }
    },
    [auth.isAuthenticated]
  );

  return (
    <main className={styles.login}>
      <div className = {styles.form}>
        <Button type="primary" onClick={handleSubmit}>Login</Button>
      </div>
    </main>
  );
}
