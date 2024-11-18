import { Outlet } from "react-router-dom";
import Header from "../components/Header.jsx";
import Footer from "../components/Footer.jsx";


const MainLayout = () => {
  return (
    <main className="h-fit min-h-screen w-screen flex flex-col justify-between overflow-x-hidden bg-neutral">
      <Header />
      <div className="main-container flex-grow">
        <div className="content-container py-[2px] px-[10px] sm:px-[50px] md:px-[100px] mb-8">
          <Outlet />
        </div>
      </div>
      <Footer />
    </main>
  );
};

export default MainLayout;
