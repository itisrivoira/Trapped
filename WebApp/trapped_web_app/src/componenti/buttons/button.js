import React from "react";
import {useState} from "react";

import img_impostazioni from './img/img_impostazioni.png';
import img_impostazioni_on from './img/img_impostazioni_on.png';

import img_gioca from './img/img_gioca.png';
import img_gioca_on from './img/img_gioca_on.png';

import img_classifica from './img/img_classifica.png';
import img_classifica_on from './img/img_classifica_on.png';

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
    <img 
      src={img}
      onMouseEnter={on_img}
      onMouseLeave={out_img}
    />
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
    <img 
      src={img}  
      onClick={() => alert('Il gioco inizierà da qui')}
      onMouseEnter={on_img}
      onMouseLeave={out_img}
    />
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
    <img 
      src={img}
      onMouseEnter={on_img}
      onMouseLeave={out_img}
    />
  )
};