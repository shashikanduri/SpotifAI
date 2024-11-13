import { Navigate } from "react-router-dom";
import MainContainer from "../components/MainContainer";
import { useAuth } from "../contexts/AuthContext";
import styles from "./AppLayout.module.css";

function AppLayout() {
const { auth } = useAuth();

  if (!auth.isAuthenticated){
    return <Navigate to = "/" />
  }

  return (
    <>
      <MainContainer />
    </>
  );
}

export default AppLayout;
