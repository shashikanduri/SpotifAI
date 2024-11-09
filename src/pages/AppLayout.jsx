import MainContainer from "../components/MainContainer";
import User from "../components/User";
import ProtectedRoute  from "../pages/ProtectedRoute";

import styles from "./AppLayout.module.css";

function AppLayout() {
  return (
    <ProtectedRoute>
      <div className={styles.app}>
        <MainContainer />
        <User />
      </div>
    </ProtectedRoute>
  );
}

export default AppLayout;
