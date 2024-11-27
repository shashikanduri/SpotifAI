import { createContext, useContext, useState } from "react";

const isUserLoggedIn = () => {
  const spotify_auth_status = localStorage.getItem("isAuthenticated");
  const isAuthenticated = spotify_auth_status ? spotify_auth_status : false;
  const user = isAuthenticated ? localStorage.getItem("user") : null;

  return {user, isAuthenticated};
};


const initialContext = isUserLoggedIn();
const AuthContext = createContext(initialContext);

function AuthProvider({ children }) {

  const [auth, setAuth] = useState(isUserLoggedIn());

  function logout() {
    localStorage.removeItem("isAuthenticated");
    setAuth((prev) => ({ ...prev, user: null, isAuthenticated : false}));
  }

  return (
    <AuthContext.Provider value = {{ auth, logout, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  const context = useContext(AuthContext);
  return context;
}

export { AuthProvider, useAuth };
