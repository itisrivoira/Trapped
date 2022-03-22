import React from "react";
import {BtnTornaIndietro} from "../componenti/buttons/button";

export const Impostazioni = () => {
  return(
    <div className="contenitore">
      <div className="row">
        <div className="titolo">
          impostazioni
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