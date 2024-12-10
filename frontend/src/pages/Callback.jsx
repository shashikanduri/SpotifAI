
import SpinnerFullPage from "../components/SpinnerFullPage";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";

function Callback(){

    const { login } = useAuth();
    
    const [params] = useSearchParams();
    const navigate = useNavigate();

    // callback page for getting auth status from backend and setting context
    useEffect(() => {
      const status = params.get("status");
      const name = params.get("display_name");
      if (status === "ok"){
        login(name);
        navigate('/app');
      }
      else{
        navigate('/');
      }
    },
      []
    );

    
    return <SpinnerFullPage />;
}

export default Callback;