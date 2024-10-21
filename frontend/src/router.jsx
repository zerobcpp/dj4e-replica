import React from "react";
import {BrowserRouter, Routes, Route} from 'react-router-dom'; 
import Home from "./core/Home.jsx";


const Router = () => {
  return (
    <BrowserRouter> 
        <Routes>
            <Route path ="/Home" element={<Home/>}/>

          </Routes>
    </BrowserRouter> 
  )
}

export default Router;