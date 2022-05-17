import React from 'react';
import {useContext} from "react";
import {GameOver} from "../page_gameOver/gameOver";
import {Partita} from "../page_partita/partita";
import {Vittoria} from "../page_vittoria/vittoria";
import {StatoPage} from "../../GlobalProvider";

export const Gioco = () => {
  const {statoPage, setStatoPage} = useContext(StatoPage);

  return (
    <div>
      { 
        statoPage === "partita" && (<Partita />)
      }
      {
        statoPage === "gameOver" && (<GameOver />)
      }
      {
        statoPage === "vittoria" && (<Vittoria />)
      }
    </div>
  );
}