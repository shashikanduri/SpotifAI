import { NavLink } from "react-router-dom";
import Logo from "./Logo";
import styles from "./PageNav.module.css";
import { useAuth } from "../contexts/AuthContext";

function PageNav() {

  const { auth, logout } = useAuth();

  return (
    <nav className={styles.nav}>
      {
        auth.isAuthenticated && 
        <ul>
          <li>
            <NavLink to="/" onClick={logout} className={styles.ctaLink}>
              Logout
            </NavLink>
          </li>
        </ul>
      }

    </nav>
  );


}

export default PageNav;
