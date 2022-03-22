import React from "react";
import './style_home.css';
import {Titolo} from '../componenti/photos/photo';
import {BtnImpstazioni, BtnGioca, BtnClassifica} from '../componenti/buttons/button';

export const Home = () => {
  return(
    <div className="contenitore">
      <div className="row">
        <div className="titolo">
          <Titolo/>
        </div>
      </div>
      <div className="row">
        <div className="button">
          <BtnImpstazioni />
        </div>
        <div className="button">
          <BtnGioca />
        </div>
        <div className="button">
          <BtnClassifica />
        </div>
      </div>
    </div>
  )
};