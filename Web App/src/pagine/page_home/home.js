import React from "react";
import './style_home.css';
import {BtnImpstazioni, BtnGioca, BtnClassifica} from '../componenti/buttons/button';

export const Home = () => {
  return(
    <div className="contenitore_home">
      <div className="row_home">
        <div className="col_home">
          <div className="titolo_home">
            Trapped
          </div>
          <div className="button_sopra">
            <BtnGioca />
          </div>
          <div className="button_sotto">
            <div className="button_in1">
              <BtnImpstazioni />
            </div>
            <div className="button_in2">
              <BtnClassifica />
            </div>
          </div>
        </div>
        <div className="col_home">

        </div>
      </div>
    </div>
  )
};