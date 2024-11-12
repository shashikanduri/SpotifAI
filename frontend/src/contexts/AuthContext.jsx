import { createContext, useContext, useState } from "react";

const isUserLoggedIn = () => {
  const spotify_auth_status = localStorage.getItem("isAuthenticated");
  const isAuthenticated = spotify_auth_status ? spotify_auth_status : false;
  const user = isAuthenticated ? JSON.parse(localStorage.getItem("user")) : null;

  return {user, isAuthenticated};
};


const initialContext = isUserLoggedIn();
const AuthContext = createContext(initialContext);

function AuthProvider({ children }) {

  const [auth, setAuth] = useState(isUserLoggedIn());

  function updateSpotifyAuth(name){
    setAuth((prev) => ({ ...prev, user: {name : "shashi"}, isAuthenticated : true}));
    localStorage.setItem("isAuthenticated", true);
    localStorage.setItem("user_name", name);
  }

  function logout() {
    localStorage.removeItem("isAuthenticated");
    localStorage.removeItem("user_name");
    setAuth((prev) => ({ ...prev, user: {}, isAuthenticated : false}));
  }

  return (
    <AuthContext.Provider value = {{ auth, setAuth, logout, updateSpotifyAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  const context = useContext(AuthContext);
  return context;
}

export { AuthProvider, useAuth };
