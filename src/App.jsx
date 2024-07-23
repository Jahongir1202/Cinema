
import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from "./layout/Root";
import Home from "./components/Home";
import Detail from "./components/Detail";
import Jangari from "./components/Jangari";
import CinemaId from "./components/CinimaId"; // Ism to'g'irlandi
import CinemaRoot from "./layout/CinemaRoot";
import Cinema from "./components/Cinema";
import MutfilmRoot from "./layout/MutfilmRoot";
import MutfilmId from "./components/MutfilmId";
import SerialId from "./components/SerialId";
import SerialRoot from "./layout/SerialRoot";
import Comedia from "./components/Comedia";
import Drama from "./components/Drama";
import Ujas from "./components/Ujas";
import Romance from "./components/Romance";
import Fantastik from "./components/Fantastik";
import Hayotiy from "./components/Hayotiy";
import Serialar from "./components/Serialar";
import Mutfim from "./components/Mutfim";

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
          element: <Detail />,
        },
        {
          path: "jangari",
          element: <Jangari />,
        },
        {
          path: 'cinema',
          element: <CinemaRoot />,
          children: [
            {
              path: ":id",
              element: <CinemaId />, // Ism to'g'irlandi
            },
          ],
        },
        {
          path:'multifilm',
          element:<MutfilmRoot/>,
          children:[
            {
              path:":id",
              element:<MutfilmId/>
            }
          ]
        },
        {
          path:'serial',
          element:<SerialRoot/>,
          children:[
            {
              path:":id",
              element:<SerialId/>
            }
          ]
        },
        {
          path:"comedia",
          element:<Comedia/>
        },
        {
          path:"drama",
          element:<Drama/>
        },
        {
          path:"ujas",
          element:<Ujas/>
        },
        {
          path:"romance",
          element:<Romance/>
        },
        {
          path:"fantastik",
          element:<Fantastik/>
        },
        {
          path:"hayotiy",
          element:<Hayotiy/>
        },
        {
          path:"hamma_serialar",
          element:<Serialar/>
        },
        {
          path:"hamma_kinolar",
          element:<Cinema/>
        },
        {
          path:"hamma_multifilmlar",
          element:<Mutfim/>
        }
      ],
    },
  ]);

  return <RouterProvider router={routes} />;
}

export default App;
