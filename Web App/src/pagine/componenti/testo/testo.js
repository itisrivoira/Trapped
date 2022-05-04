import React from "react";
import "../../page_partita/style_partita.css";
import {useState, useEffect, useContext} from "react";
import {Cont} from "../../../GlobalProvider";

export const TitStanza = () => {
  const {cont, setCount} = useContext(Cont);
  const [testo, setTesto] = useState("Classe 5c");

  useEffect(() => {
    if (cont >= 2 && cont < 4){
      setTesto("Bagno");
    }
    else if (cont >= 4 && cont < 6){
      setTesto("Giardino");
    }
    else if (cont >= 6 && cont < 8){
      setTesto("Laboratorio Info");
    }
    else if (cont >= 8 && cont < 10){
      setTesto("Presidenza");
    }
  }, [cont]);

  return(
    <h1>{testo}</h1>
  )
};