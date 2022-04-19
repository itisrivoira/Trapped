import React from "react";
import './style_partita.css';
import {useState, useEffect, useContext} from "react";
import TypeWriter from "react-typewriter";
import {Stanza} from "../componenti/photos/photo";
import {BtnVita, BtnAiuto, BtnMenu} from "../componenti/buttons/button";
import {stockDomande} from "../../domandeGioco";
import {Cont} from "../../GlobalProvider";

export const Partita = () => {
  const {cont, setCont} = useContext(Cont);
  const [domanda, setDomanda] = useState([]);
  const [riA, setRiA] = useState([]);
  const [riB, setRiB] = useState([]);
  const [riC, setRiC] = useState([]);
  const [riD, setRiD] = useState([]);
  const [corr, setCorr] = useState([]);


  useEffect(() => {
    stockDomande.map((data) => {
      setDomanda(previous => [...previous, data.domanda]);
      setRiA(previous => [...previous, data.A])
      setRiB(previous => [...previous, data.B])
      setRiC(previous => [...previous, data.C])
      setRiD(previous => [...previous, data.D])
      setCorr(previous => [...previous, data.corretta])
    });
  }, []);
  
  const rispondi = () => {
    var buttons = document.getElementsByClassName("btnRisp");

    for (var j = 0; j < buttons.length; j++){
      buttons[j].addEventListener("click", function(e){
        var lettera = this.getAttribute("name");
        if (corr[cont] == lettera){
          alert("Coretta, " + this.value);
        }
      });
    }
  };

  const avanti = () => {
    setCont(previous => (previous + 1));
  };

  return(
    <div className="partita">
      <div className="contenitore">
        <div className="sinistra">
          <div className="menu">
            <BtnMenu />
          </div>
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
              <BtnAiuto />
            </div>
            <div className="btnCuori">
              <BtnAiuto />
            </div>
            <div className="btnCuori">
              <BtnAiuto />
            </div>
          </div>
          <div className="button">
            <input type="button" value={riA[cont]} name="A" onClick={rispondi} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riB[cont]} name="B" onClick={rispondi} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riC[cont]} name="C" onClick={rispondi} className="btnRisp" />
          </div>
          <div className="button">
            <input type="button" value={riD[cont]} name="D" onClick={rispondi} className="btnRisp" />
          </div>          
        </div>
      </div>
      <div className="contDomanda">
        <div className="domanda">
            <div className="interlocutore">

            </div>
            <div className="testoDomanda" id="domandaTesto">
              <TypeWriter
                options={{
                  autoStart: true,
                  loop: true,
                  delay: 100,
                  cursor: '|',
                }}
                typing={1}>
                  {domanda[cont]}
              </TypeWriter>
            </div>
            <div className="contAvanti">
              <input type="button" value="AVANTI" className="avanti" onClick={avanti}/>
            </div>
        </div>
      </div>
    </div>
  )
};