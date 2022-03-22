import React from "react";
import {BtnTornaIndietro} from "../componenti/buttons/button";

export const Classifica = () => {
  return(
    <div className="contenitore">
       <div className="row">
        <div className="titolo">
          classifica
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