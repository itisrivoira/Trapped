import React from "react";
import {Outlet, Link} from "react-router-dom";
import {BtnTornaIndietro} from "../componenti/buttons/button";
import "../page_impostazioni/style_impostazioni.css";

export const Regole = () => {
  return(
    <div className="contenitore_impo">
      <div className="row_impo">
        <div className="titolo_impo">
          Regole del gioco
        </div>
      </div>
      <div className="row_impo">
        <div className="col_impo">
          regole
        </div>
      </div>
      <div className="row_impo">
        <div className="button_impo">
          <Link to="/partita">
            <BtnTornaIndietro/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  )
};