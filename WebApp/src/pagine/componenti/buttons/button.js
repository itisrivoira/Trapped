import React from "react";
import {Outlet, Link} from "react-router-dom";
import {useState} from "react";

import img_impostazioni from "./img/img_impostazioni.png";
import img_impostazioni_on from "./img/img_impostazioni_on.png";

import img_gioca from "./img/img_gioca.png";
import img_gioca_on from "./img/img_gioca_on.png";

import img_classifica from "./img/img_classifica.png";
import img_classifica_on from "./img/img_classifica_on.png";

export const BtnImpstazioni = () => {
  const [state, setState] = useState(false);
  const [img, setImage] = useState(img_impostazioni);

	const on_img = () => {
    setState(true);
    setImage(img_impostazioni_on);
  };

  const out_img = () => {
    setState(false);
    setImage(img_impostazioni);
  }

  return(
    <>
      <Link to="/impostazioni">
        <img 
          src={img}
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnGioca = () => {
  const [state, setState] = useState(false);
  const [img, setImage] = useState(img_gioca);

	const on_img = () => {
    setState(true);
    setImage(img_gioca_on);
  };

  const out_img = () => {
    setState(false);
    setImage(img_gioca);
  }

  return(
    <>
      <Link to="/confingpartita">
        <img 
          src={img}  
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};


export const BtnClassifica = () => {
  const [state, setState] = useState(false);
  const [img, setImage] = useState(img_classifica);

	const on_img = () => {
    setState(true);
    setImage(img_classifica_on);
  };

  const out_img = () => {
    setState(false);
    setImage(img_classifica);
  }

  return(
    <>
      <Link to="/classifica">
        <img 
          src={img}
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnTornaIndietro = () => {
 
  return(
    <>
      <Link to="/">
        <input type="button" value="TORNA INDIETRO" />
      </Link>
      <Outlet />
    </>
  )
};