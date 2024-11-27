import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

function AppLayout() {
  const { auth } = useAuth();
  console.log(auth);

  if (!auth.isAuthenticated){
    return <Navigate to = "/" />
  }

  return (
    <>
      <Outlet />
    </>
  );
}

export default AppLayout;
