import React, { StrictMode } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { AuthProvider } from "./contexts/AuthContext";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(

  <StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </StrictMode>

);
