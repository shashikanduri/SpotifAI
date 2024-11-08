 import { Outlet } from "react-router-dom";
import AppNav from "./AppNav";
import Logo from "./Logo";
import styles from "./MainContainer.module.css";

function MainContainer() {
  return (
    <div className={styles.sidebar}>
      <Logo />
      <AppNav />

      <Outlet />

      <footer className={styles.footer}>
        <p className={styles.copyright}>
          &copy; Copyright {new Date().getFullYear()} by WorldWise Inc.
        </p>
      </footer>
    </div>
  );
}

export default MainContainer;
