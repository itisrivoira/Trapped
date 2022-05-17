import React from "react";
import {Outlet, Link} from "react-router-dom";
import {BtnMusica,BtnSuoni, BtnTornaIndietro} from "../componenti/buttons/button";
import "../page_impostazioni/style_impostazioni.css";

export const Menu = () => {
  return(
    <div className="contenitore_impo">
      <div className="row_impo">
        <div className="titolo_impo">
          Impostazioni
        </div>
      </div>
      <div className="row_impo">
        <div className="col_impo">
          Musica
        </div>
        <div className="col_impo">
          <BtnMusica />
        </div>
      </div>
      <div className="row_impo">
        <div className="col_impo">
          Suoni
        </div>
        <div className="col_impo">
          <BtnSuoni />
        </div>
      </div>
      <div className="row_impo">
        <div className="button_impo">
          <Link to="/gioco">
            <BtnTornaIndietro/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  )
};
      