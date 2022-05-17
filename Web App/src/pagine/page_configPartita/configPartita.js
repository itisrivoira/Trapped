import React from "react";
import {Outlet, Link} from "react-router-dom";
import './style_configPartita.css';
import {useContext} from "react";
import {Nickname} from "../../GlobalProvider";
import {BtnSceltaP, BtnInizia, BtnTornaIndietro} from '../componenti/buttons/button';

export const ConfigPartita = () => {
  const {nickname, setNickname} = useContext(Nickname);

  const change = (event) => {
    setNickname(event.target.value);
  }

  return(
    <div className="contenitore_configP">
      <div className="row_configP">
        <div className="titolo_configP">
          Scegli personaggio
        </div>
      </div>
      <div className="row_configP">
        <BtnSceltaP />
      </div>
      <div className="row_configPInput">
        <input className="inputName" type="text" placeholder="Nickname" onChange={change}></input>
      </div>
      <div className="row_configPB">
        <BtnInizia />
      </div>
      <div className="row_configP">
        <Link to="/">
          <BtnTornaIndietro/>
        </Link>
        <Outlet />
      </div>
    </div>
  )
};