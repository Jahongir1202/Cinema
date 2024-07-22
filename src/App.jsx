import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from "./layout/Root";
import Home from "./components/Home";
import Detail from "./components/Detail";
import Jangari from "./components/Jangari";
import CinimaId from "./components/CinimaId";
import RootJangari from "./layout/RootJangari";

function App() {
  const routes = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      children: [
        {
          index: true,
          element: <Home />,
        },
        {
          path: ":id",
          element: <Detail/>,
        },
        {
          path:"jangari",
          element:<RootJangari/>,
          children:[
            {
              index:true,
              element:<Jangari/>
            },
            {
              path:":id",
              element:<CinimaId/>
            }
          ]
        },
        {
          path:"cinema_id",
          element:<CinimaId/>
        }
      ],
    },
  ]);

  return <RouterProvider router={routes} />;
}

export default App;
