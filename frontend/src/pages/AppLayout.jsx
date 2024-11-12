import { Navigate, useNavigate } from "react-router-dom";
import MainContainer from "../components/MainContainer";
import User from "../components/User";
import { useAuth } from "../contexts/AuthContext";

function AppLayout() {
  
  const { auth } = useAuth();

  if (!auth.isAuthenticated){
    return <Navigate to = "/" />
  }

  return (
    <>
      <MainContainer />
      <User />
    </>
  );
}

export default AppLayout;
