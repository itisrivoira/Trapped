import React from "react";
import "./style_classifica.css";
import {BtnTornaIndietro} from "../componenti/buttons/button";

export const Classifica = () => {
  return(
    <div className="contenitore_class">
       <div className="row_class">
        <div className="titolo_class">
          Classifica
        </div>
      </div>
      <div className="row_class">
        <div className="button_class">
          <BtnTornaIndietro/>
        </div>
      </div>
    </div>
  )
};