import React from "react";
import "./style_impostazioni.css";
import {BtnMusica,BtnSuoni, BtnTornaIndietro} from "../componenti/buttons/button";

export const Impostazioni = () => {
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
          <BtnTornaIndietro/>
        </div>
      </div>
    </div>
  )
};