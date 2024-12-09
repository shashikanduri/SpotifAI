
import SpinnerFullPage from "../components/SpinnerFullPage";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useState, useEffect } from "react";
import axios from "axios";

function Callback(){

    const { auth, login } = useAuth();
    
    const [params] = useSearchParams();
    const navigate = useNavigate();
    const [accessToken, setAccessToken] = useState(false);
    const headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
    }

    useEffect(
        () => {
          
          // define an async function for signin after receiving the code from spotify
          async function signin(){
            
            if (!auth.isAuthenticated) {
              const code = params.get("code");
            
              // only signin once when access token process is done
              if (code && !accessToken) {
                const response = await axios.post(`${import.meta.env.VITE_APP_API_URI}/login`, { code : code }, { headers : headers });
                if (response.status === 200){
                  login(response.data.data.user_name);
                  setAccessToken(true);
                  navigate("/app");
                }
              }
              else{
                navigate("/");
              }
            }
            else {
              navigate("/app");
            }
          }
    
          // call the above function
          signin();
    
        },
        []
      );

    
    return <SpinnerFullPage />;
}

export default Callback;