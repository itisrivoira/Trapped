import React from "react";
import {Outlet, Link} from "react-router-dom";
import './style_configPartita.css';
import {BtnSceltaP, BtnInizia, BtnTornaIndietro} from '../componenti/buttons/button';

export const ConfigPartita = () => {
  return(
    <div className="contenitore_configP">
      <div className="row_configP">
        <div className="titolo_configP">
          Scegli personaggio
        </div>
      </div>
      <div className="row_configP">
          <BtnSceltaP />
      </div>
      <div className="row_configP">
        <BtnInizia />
      </div>
      <div className="row_configP">
        <Link to="/">
          <BtnTornaIndietro/>
        </Link>
        <Outlet />
      </div>
    </div>
  )
};