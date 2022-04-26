import React from "react";
import './style_partita.css';
import {useState, useEffect, useContext} from "react";
import TypeWriter from "react-typewriter";

import {Stanza} from "../componenti/photos/photo";
import {TitStanza} from "../componenti/testo/testo";
import {BtnMenu, BtnRegole, BtnEsci} from "../componenti/buttons/button";
import {stockDomande} from "../../domandeGioco";
import {Cont, Pers, Aiuti, Vite, Giuste} from "../../GlobalProvider";
import {MyTimer} from "../componenti/cronometro/cronometro";

import img_cuore from "../componenti/buttons/img/cuore.png";
import img_c_u from "../componenti/buttons/img/cuore_usato.png";

import img_chiav from "../componenti/buttons/img/chiavetta.png";
import img_chiav_u from "../componenti/buttons/img/chiavetta_usata.png";

export const Partita = () => {
  const {pers, setPers} = useContext(Pers);
  const {cont, setCont} = useContext(Cont);
  const {vite, setVite} = useContext(Vite);
  const {aiuti, setAiuti} = useContext(Aiuti);
  const {giuste, setgiuste} = useContext(Giuste);

  const [c1, setC1] = useState(img_cuore);
  const [c2, setC2] = useState(img_cuore);
  const [c3, setC3] = useState(img_cuore);

  const [a1, setA1] = useState(img_chiav);
  const [a2, setA2] = useState(img_chiav);
  const [a3, setA3] = useState(img_chiav);

  const [domanda, setDomanda] = useState([]);
  const [riA, setRiA] = useState([]);
  const [riB, setRiB] = useState([]);
  const [riC, setRiC] = useState([]);
  const [riD, setRiD] = useState([]);
  const [corr, setCorr] = useState([]);
  const [sel, setSel] = useState("");

  const time = new Date();
  time.setSeconds(time.getSeconds() + 299);

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
  
  const rispondi = (e) => {
    let risp = e.target.id;
    setSel(risp);
  };

  const avanti = () => {
    if (sel == ""){
      alert("Non hai selezioanto nulla!\nScegli una risposta.")
    }
    else{
      if (sel == corr[cont]){
        alert(sel + " corretta");
        setCont(previous => (previous + 1));
      }
      else{
        alert(sel + " sbagliata")
        setVite(previous => (previous - 1));
      }
    }
    document.getElementsByName("risposta").checked = false;
  };

  useEffect(() => {
    if (vite == 2){
      setC1(img_c_u);
    }
    else if (vite ==1){
      setC1(img_c_u);
      setC2(img_c_u);
    }
    else if (vite <= 0){
      setC1(img_c_u);
      setC2(img_c_u);
      setC3(img_c_u);
      alert("GAME OVER")
    }
   }, [vite]);

  const chiediAiuto = () => {
    setAiuti(previous => (previous - 1));
  };

  useEffect(() => {
    if (aiuti == 2){
      setA1(img_chiav_u);
    }
    else if (vite ==1){
      setA1(img_chiav_u);
      setA2(img_chiav_u);
    }
    else if (vite <= 0){
      setA1(img_chiav_u);
      setA2(img_chiav_u);
      setA3(img_chiav_u);
    }
   }, [aiuti]);

  return(
    <div className="partita">
      <div className="contenitore">
        <div className="menu">
          <div className="cron">
            <MyTimer expiryTimestamp={time} />
          </div>
          <div className="btn">
            <BtnMenu />
          </div>
          <div className="btn">
            <BtnRegole />
          </div>
          <div className="btn">
            <BtnEsci />
          </div>
        </div>
        <div className="sinistra">
          <div className="titolo">
            <TitStanza />
          </div>
          <div className="mappa">
            <Stanza />
          </div>
        </div>
        <div className="destra">
          <div className="cuori">
            <div className="contCuori">
              <img className="cuore" src={c1} />
              <img className="cuore" src={c2} />
              <img className="cuore" src={c3} />
            </div>
          </div>
          <div className="aiuti">
            <div className="contAiuti">
              <img className="aiuto" src={a1} onClick={chiediAiuto} />
              <img className="aiuto" src={a2} onClick={chiediAiuto} />
              <img className="aiuto" src={a3} onClick={chiediAiuto} />
            </div>
          </div>
          <div className="button">
            <input type="radio" name="risposta" id="A" onClick={rispondi} />
            <label for="A">{riA[cont]}</label>
          </div>
          <div className="button">
            <input type="radio" name="risposta" id="B" onClick={rispondi} />
            <label for="B">{riB[cont]}</label>
          </div>
          <div className="button">
            <input type="radio" name="risposta" id="C" onClick={rispondi} />
            <label for="C">{riC[cont]}</label>
          </div>
          <div className="button">
            <input type="radio" name="risposta" id="D" onClick={rispondi} />
            <label for="D">{riD[cont]}</label>
          </div>          
        </div>
      </div>
      <div className="contDomanda">
        <div className="domanda">
            <div className="interlocutore">
              <img className="per" src={pers} />
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