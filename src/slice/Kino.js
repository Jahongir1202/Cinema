import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  kinoList: null,
};

const KinoSlice = createSlice({
  name: "kino",
  initialState,
  reducers: {},
});

export const {} = KinoSlice.actions;
export default KinoSlice.reducer;
