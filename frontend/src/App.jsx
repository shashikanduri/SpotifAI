
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import AppLayout from "./pages/AppLayout";
import PageNotFound from "./pages/PageNotFound";
import MainLayout from "./pages/MainLayout";
import Home from "./pages/Home";



function App() {

  const router = createBrowserRouter(
    [
      {
        path: "/",
        element: <MainLayout />,
        children: [
          { index: true, element: <Home /> },
          { path: "app", element: <AppLayout /> }
        ]
      },
      { path: '*', element: <PageNotFound /> }
    ]
  );

  return <RouterProvider router={router} />;

}

export default App;