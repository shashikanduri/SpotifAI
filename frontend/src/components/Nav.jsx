import React, { useState } from "react";
import { FaCircleUser } from "react-icons/fa6";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";


const Nav = () => {

  const [mobileView, setMobileView] = useState(window.innerWidth <= 1022);
  const [showHamburgerMenu, setShowHamburgerMenu] = useState(false);
  const { auth, logout } = useAuth();
  const navigate = useNavigate();
  window.addEventListener("resize", () =>
    setMobileView(window.innerWidth < 1022)
  );

  function handleLogout(){
    logout();
    navigate("/");
  }

  return (
    <>
      <div className = "main-container mt-20 py-[5px] px-[10px] sm:px-[50px] md:px-[100px] flex justify-center">
    
        <nav className = "flex flex-wrap items-center justify-between w-[70%] py-2 md:py-0">
            <div
                className={`${
                showHamburgerMenu ? "" : "hidden"
                } w-full lg:flex-1 lg:flex lg:items-center lg:w-auto`}
                id="menu"
            >
                <ul 
                  className={`w-full pt-4 text-base items-center font-medium text-primary flex ${
                    auth.user ? 'justify-between' : 'justify-end'
                  } lg:pt-0`}
                >

                  { auth.user && <li> <p className = "font-bold">Welcome, {auth.user}</p> </li> }
                  <li>
                      { auth.isAuthenticated && 
                      <button 
                        className = "md:py-4 py-2 flex gap-2 hover:text-secondary"
                        onClick = {handleLogout}
                      >
                          Sign out <FaCircleUser className = "text-xl" />
                      </button>
                      }
                  </li>
                </ul>
            </div>
        </nav>
      </div>
    </>
  );
};

export default Nav;
