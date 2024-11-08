import { createContext, useContext, useReducer } from "react";

const isUserLoggedIn = () => {
  const session = sessionStorage.getItem("isLoggedIn");
  const isAuthenticated = session ? session : false;
  const user = session ? JSON.parse(sessionStorage.getItem("user")) : null;
  return {user, isAuthenticated};
};


const initialContext = isUserLoggedIn();
console.log(initialContext);
const AuthContext = createContext(initialContext);


function reducer(state, action) {
  switch (action.type) {
    case "login":
      sessionStorage.setItem("isLoggedIn", true);
      return { ...state, user: action.payload, isAuthenticated: true };
    case "logout":
      return { ...state, user: null, isAuthenticated: false };
    default:
      throw new Error("Unknown action");
  }
}

const FAKE_USER = {
  name: "Jack",
  email: "jack@example.com",
  password: "qwerty",
  avatar: "https://i.pravatar.cc/100?u=zz",
};

function AuthProvider({ children }) {

  const [{ user, isAuthenticated }, dispatch] = useReducer(
    reducer,
    initialContext
  );

  function login(email, password) {
    if (email === FAKE_USER.email && password === FAKE_USER.password)
      sessionStorage.setItem("user", JSON.stringify(FAKE_USER));
      dispatch({ type: "login", payload: FAKE_USER });
  }

  function logout() {
    dispatch({ type: "logout" });
  }

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined)
    throw new Error("AuthContext was used outside AuthProvider");
  return context;
}

export { AuthProvider, useAuth };
