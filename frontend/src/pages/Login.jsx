import { useEffect } from "react";
import axios from "axios";
import { Navigate, useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import styles from './Login.module.css';
import PageNav from "../components/PageNav";

export default function Login() {

  const [params] = useSearchParams();
  const { auth, updateSpotifyAuth } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();

    // take user to spotify auth page 
    const response = await axios.get('http://127.0.0.1:5000/get-client');
    if (response.status === 200 && response.data !== null) {

      // build spotify auth url for spotify login
      const base_url = response.data?.spotify_auth_url ?? null;
      if (base_url !== null) {
        const data = {
          client_id: response.data.client_id,
          response_type: "code",
          redirect_uri: "http://localhost:5173",
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

  useEffect(
    () => function () {
      if (!auth.isAuthenticated) {
        const code = params.get("code");
        if (code) {
          updateSpotifyAuth("shashi");
          navigate("/app");
        }
      }
      else {
        navigate("/app");
      }
    },
    []
  );

  if (auth.isAuthenticated) return <Navigate to = "/app" />

  return (
    <main className={styles.homepage}>
      <PageNav />
      <section>
        <h1>
          SpotifAI
          <br />
        </h1>
        <h2>
          Analyze you spotify music collection with LLMs.
        </h2>
        <button onClick={handleSubmit} className="cta">
          Login with Spotify
        </button>
      </section>
    </main>
  );
}
