import { Outlet } from "react-router-dom";
import PageNav from "../components/PageNav";
import styles from "./AppLayout.module.css";

const MainLayout = () => {
  return (
    <div>
      <Outlet />
    </div>
  );
};

export default MainLayout;
