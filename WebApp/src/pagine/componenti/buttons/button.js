import React from "react";
import {Outlet, Link} from "react-router-dom";
import {useState, useEffect} from "react";
import "../../page_impostazioni/style_impostazioni.css"

import imgTornaIndietro from "./img/img_tornaIndietro.png"

import img_impostazioni from "./img/img_impostazioni.png";
import img_impostazioni_on from "./img/img_impostazioni_on.png";

import img_gioca from "./img/img_gioca.png";
import img_gioca_on from "./img/img_gioca_on.png";

import img_classifica from "./img/img_classifica.png";
import img_classifica_on from "./img/img_classifica_on.png";

import img_acceso from  "./img/img_acceso.png";
import img_acceso_on from  "./img/img_acceso_on.png";

import img_spento from  "./img/img_spento.png";
import img_spento_on from  "./img/img_spento_on.png";

//import musica from "../../sound/sound.mp3";
//import {useAudio} from "../../sound/useAudio";

import img_sceltaS from "./img/img_scelta_s.png";
import img_sceltaD from "./img/img_scelta_d.png";
import img_uomo from "../photos/uomo/uomo_davanti_1.png"
import img_donna from "../photos/donna/donna_davanti_1.png"

import img_inizia from "./img/img_inizia.png";
import img_inizia_on from "./img/img_inizia_on.png";

export const BtnImpstazioni = () => {
  const [img, setImage] = useState(img_impostazioni);

	const on_img = () => {
    setImage(img_impostazioni_on);
  };

  const out_img = () => {
    setImage(img_impostazioni);
  }

  return(
    <>
      <Link to="/impostazioni">
        <img 
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnGioca = () => {
  const [img, setImage] = useState(img_gioca);

	const on_img = () => {
    setImage(img_gioca_on);
  };

  const out_img = () => {
    setImage(img_gioca);
  }

  return(
    <>
      <Link to="/confingpartita">
        <img 
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnClassifica = () => {
  const [img, setImage] = useState(img_classifica);

	const on_img = () => {
    setImage(img_classifica_on);
  };

  const out_img = () => {
    setImage(img_classifica);
  }

  return(
    <>
      <Link to="/classifica">
        <img 
          src={img}
          alt=""
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
        <div style={{position: "absolute", width: "95%", left: "0px", paddingLeft: "30px"}}>
          <img
            src={imgTornaIndietro}
            alt=""
          />
        </div>
      </Link>
      <Outlet />
    </>
  )
};

export const BtnMusica = () => {
  const [imgS, setImgS] = useState(img_acceso);
  const [imgD, setImgD] = useState(img_spento_on);

  const premiOn = () => {
    setImgS(img_acceso_on);
    setImgD(img_spento);
  };

  const premiOff = () => {
    setImgS(img_acceso);
    setImgD(img_spento_on);
  };

  return(
    <>
      <img
        className="button_impo"
        src={imgS}
        alt=""
        onClick={premiOn}
      />
      <img
        className="button_impo"
        src={imgD}
        alt=""
        onClick={premiOff}
      />
    </>
  )
};

export const BtnSuoni = () => {
  const [imgS, setImgS] = useState(img_acceso);
  const [imgD, setImgD] = useState(img_spento_on);
  
  const premiOn = () => {
    setImgS(img_acceso_on);
    setImgD(img_spento);
  };

  const premiOff = () => {
    setImgS(img_acceso);
    setImgD(img_spento_on);
  };

  return(
    <>
      <img
        className="button_impo"
        src={imgS}
        alt=""
        onClick={premiOn}
      />
      <img
        className="button_impo"
        src={imgD}
        alt=""
        onClick={premiOff}
      />
    </>
  )
};

export const BtnSceltaP = () => {
  const [state, setState] = useState(false);
  const [personaggio, setPersonaggio] = useState(img_uomo);

  const cambia = () => {
    if (state==false){
      setPersonaggio(img_uomo);
      setState(true);
    }
    else{
      setPersonaggio(img_donna);
      setState(false);
    }
  };

  return(
    <>
      <div>
        <div className="col_confP">
          <img src={img_sceltaS} onClick={cambia} />
        </div>
        <div className="col_confP">
          <img src={personaggio} />
        </div>
        <div className="col_confP">
          <img src={img_sceltaD} onClick={cambia} />
        </div>
      </div>
    </>
  )
};

export const BtnInizia = () => {
  const [img, setImage] = useState(img_inizia);

	const on_img = () => {
    setImage(img_inizia_on);
  };

  const out_img = () => {
    setImage(img_inizia);
  }

  return(
    <>
      <Link to="/partita">
        <img 
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
        />
      </Link>
      <Outlet />
    </>
  )
};