import { configureStore } from "@reduxjs/toolkit";
import Kino from "./slice/Kino";

export const store = configureStore({
  reducer: {
    kinos: Kino,
  },
});
