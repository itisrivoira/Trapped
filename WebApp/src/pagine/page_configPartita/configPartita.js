import React from "react";
import {BtnTornaIndietro} from "../componenti/buttons/button";

export const ConfigPartita = () => {
  return(
    <div className="contenitore">
       <div className="row">
        <div className="titolo">
          PARTITA
        </div>
      </div>
      <div className="row">
        <div className="button">
          <BtnTornaIndietro/>
        </div>
      </div>
    </div>
  )
};