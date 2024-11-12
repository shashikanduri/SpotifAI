import Logo from "./Logo";
import styles from "./PageNav.module.css";

function PageNav() {
  return (
    <nav className={styles.nav}>
      <Logo />
    </nav>
  );
}

export default PageNav;
