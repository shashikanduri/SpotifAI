import CityList from "./CityList";
import styles from '../pages/Login.module.css';;
import PageNav from "./PageNav";

function MainContainer() {
  return (
    <main className={styles.homepage}>
      <PageNav />
      <section>
        <CityList />
      </section>
    </main>
  );
}

export default MainContainer;
