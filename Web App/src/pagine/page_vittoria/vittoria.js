import React from 'react';
import {BtnEsciVittoria} from "../componenti/buttons/button";
import {Outlet, Link} from "react-router-dom";
import "./style_vittoria.css";

export const Vittoria = () => {
  
  return (
    <div className="contVittoria">
      <div className="contTitVittoria">
        <h3 className="titoloVittoria">CONGRATULAZIONI</h3>
        <h3 className="titoloVittoria">HAI VINTO!</h3>
        <div className="btnEsciVittoria">
          <Link to="/">
              <BtnEsciVittoria/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  );
}