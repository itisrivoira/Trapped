import React from "react";
import './style_home.css';
import {BtnImpstazioni, BtnGioca, BtnClassifica} from '../componenti/buttons/button';

export const Home = () => {
  return(
    <div className="contenitore_home">
      <div className="row_home">
        <div className="titolo_home">
          Trapped
        </div>
      </div>
      <div className="row_home">
        <div className="button_home">
          <BtnImpstazioni />
        </div>
        <div className="button_home">
          <BtnGioca />
        </div>
        <div className="button_home">
          <BtnClassifica />
        </div>
      </div>
    </div>
  )
};