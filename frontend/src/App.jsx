
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import Login from "./pages/Login";
import AppLayout from "./pages/AppLayout";
import PageNotFound from "./pages/PageNotFound";
import MainLayout from "./pages/MainLayout";



function App() {

  const router = createBrowserRouter(
    [
      {
        path : "/",
        element : <MainLayout />,
        children : [
          { index : true, element : <Login /> },
          { path : "app", element : <AppLayout /> }
        ]
      },
      { path : '*', element : <PageNotFound />}
    ]
  );

  return <RouterProvider router={router} />;

}

export default App;
