import React from "react";
import {Outlet, Link} from "react-router-dom";
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
          <Link to="/">
            <BtnTornaIndietro/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  )
};