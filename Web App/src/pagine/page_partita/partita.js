import React from "react";
import './style_partita.css';
import {useState, useEffect} from "react";

import {Stanza} from "../componenti/photos/photo";
import {BtnVita} from "../componenti/buttons/button";
import {stockDomande} from "../../domandeGioco";

export const Partita = () => {
  const [i, setI] = useState(0);
  const [domanda, setDomanda] = useState();
  const [riA, setRiA] = useState();
  const [riB, setRiB] = useState();
  const [riC, setRiC] = useState();
  const [riD, setRiD] = useState();

  var cont = 0;
  var dom = [];
  var rispA = [];
  var rispB = [];
  var rispC = [];
  var rispD = [];
  var corr = [];

  useEffect(() => {
    stockDomande.map((data) => {
      dom[cont] = data.domanda;
      rispA[cont] = data.A;
      rispB[cont] = data.B;
      rispC[cont] = data.C;
      rispD[cont] = data.D;
      corr[cont] = data.corretta;
      cont= cont + 1;
    });
    setDomanda(dom[0]);
    setRiA(rispA[0]);
    setRiB(rispB[0]);
    setRiC(rispC[0]);
    setRiD(rispD[0]);
    cont = 1;
   }, []);

   const avanti = () => {
    setDomanda(dom[cont]);
    setRiA(rispA[cont]);
    setRiB(rispB[cont]);
    setRiC(rispC[cont]);
    setRiD(rispD[cont]);
    cont = cont + 1;
   };


  return(
    <div className="partita">
      <div className="contenitore">
        <div className="sinistra">
          <div className="titolo">
            <h1>Classe 5c</h1>
          </div>
          <div className="mappa">
            <Stanza />
          </div>
        </div>
        <div className="destra">
          <div className="btn">
            <div className="btnCuori">
              <BtnVita />
            </div>
            <div className="btnCuori">
              <BtnVita />
            </div>
            <div className="btnCuori">
              <BtnVita />
            </div>
          </div>
          <div className="btn">
            <div className="btnCuori">
              <BtnVita />
            </div>
            <div className="btnCuori">
              <BtnVita />
            </div>
            <div className="btnCuori">
              <BtnVita />
            </div>
          </div>
          <div className="button">
            <input type="button" value={riA} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riB} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riC} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riD} className="btnRisp" />
          </div>          
        </div>
      </div>
      <div className="contDomanda">
        <div className="domanda">
            <div className="testoDomanda">
              {domanda}
            </div>
            <div className="contAvanti">
              <input type="button" value="AVANTI" className="avanti" onClick={avanti}/>
            </div>
        </div>
      </div>
    </div>
  )
};