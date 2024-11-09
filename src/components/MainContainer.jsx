import CityList from "./CityList";
import Logo from "./Logo";
import styles from "./MainContainer.module.css";

function MainContainer() {
  return (
    <div className={styles.sidebar}>
      <Logo />

      <CityList />

      <footer className={styles.footer}>
        <p className={styles.copyright}>
          &copy; Copyright {new Date().getFullYear()} by WorldWise Inc.
        </p>
      </footer>
    </div>
  );
}

export default MainContainer;
