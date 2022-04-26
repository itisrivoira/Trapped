import React from "react";
import "../../page_partita/style_partita.css";
import {useState, useEffect, useContext} from "react";
import {Cont} from "../../../GlobalProvider";

import classe from "./img/classe.png";
import bagno from "./img/bagno.png";
import giardino from "./img/giardino.png";
import laboratorio from "./img/laboratorio.png";

export const Stanza = () => {
  const {cont, setCount} = useContext(Cont);
  const [img, setImg] = useState(classe);

  useEffect(() => {
    if (cont >= 2 && cont < 4){
      setImg(bagno);
    }
    else if (cont >= 4 && cont < 6){
      setImg(giardino);
    }
    else if (cont >= 6 && cont < 8){
      setImg(laboratorio);
    }
  }, [cont]);

  return(
    <img
      className="img"
      src={img}
    />
  )
};