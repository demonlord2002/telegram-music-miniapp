import React, { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Room from "./pages/Room";
import WebApp from "@twa-dev/sdk";

export default function App() {
  useEffect(() => {
    WebApp.expand();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Room />} />
      </Routes>
    </BrowserRouter>
  );
}
