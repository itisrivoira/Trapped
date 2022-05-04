import React from 'react';
import {BtnEsciGameOver} from "../componenti/buttons/button";
import {Outlet, Link} from "react-router-dom";
import "./style_GameOver.css";

export const GameOver = () => {
  
  return (
    <div className="contGameOver">
      <div className="contTitGameOver">
        <h1 className="titoloGameO">GAME</h1>
        <h1 className="titoloGameO">OVER</h1>
        <div className="btnEsciGameOver">
          <Link to="/">
              <BtnEsciGameOver/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  );
}