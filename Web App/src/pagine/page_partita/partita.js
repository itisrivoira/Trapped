import React from "react";
import './style_partita.css';
import {useState, useEffect, useContext} from "react";
import TypeWriter from "react-typewriter";

import {Stanza} from "../componenti/photos/photo";
import {TitStanza} from "../componenti/testo/testo";
import {BtnMenu, BtnRegole, BtnEsci} from "../componenti/buttons/button";
import {Cont, Pers, Aiuti, Vite, StatoPage, Nickname} from "../../GlobalProvider";
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
  const {statoPage, setStatoPage} = useContext(StatoPage);
  const {nickname, setNickname} = useContext(Nickname);

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
  time.setSeconds(time.getSeconds() + 180);

  const [tot_punti, setTot_punti] = useState(100);

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:4000/partita', {
      method: 'GET'
    })
    .then(response => response.json())
    .then(function(res){
      setData(res);
    });

    data.map((value) => {
      setDomanda(previous => [...previous, value.domanda]);
      setRiA(previous => [...previous, value.risp_A])
      setRiB(previous => [...previous, value.risp_B])
      setRiC(previous => [...previous, value.risp_C])
      setRiD(previous => [...previous, value.risp_D])
      setCorr(previous => [...previous, value.risp_Corr])
    });
  }, []);

  useEffect(() => {
    data.map((value) => {
      setDomanda(previous => [...previous, value.domanda]);
      setRiA(previous => [...previous, value.risp_A])
      setRiB(previous => [...previous, value.risp_B])
      setRiC(previous => [...previous, value.risp_C])
      setRiD(previous => [...previous, value.risp_D])
      setCorr(previous => [...previous, value.risp_Corr])
    });
  }, [data]);
  
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
        alert("corretta");
        setCont(previous => (previous + 1));
      }
      else{
        alert("sbagliata")
        setVite(previous => (previous - 1));
      }
    }
    setSel("");
    let ogg = document.getElementsByName('risposta');
    for (let i=0; i<=3; i++){
      ogg[i].checked = false;
      ogg[i].disabled = false;
    }
  };

  useEffect(() => {
    if (cont == 10){
      setStatoPage("vittoria");
      let record={
        nome_U: nickname,
        vite_U: vite,
        aiuti_U: aiuti,
        punti_U: tot_punti,
      }
      fetch('http://localhost:4000/invioDati', {
        method: 'POST',
        headers: {'Content-Type':'application/json;charset=utf-8'},
        body:JSON.stringify(record)
      })
    }
   }, [cont]);

  useEffect(() => {
    if (vite == 2){
      setC1(img_c_u);
      setTot_punti(previous => (previous - 20));
    }
    else if (vite ==1){
      setC1(img_c_u);
      setC2(img_c_u);
      setTot_punti(previous => (previous - 20));
    }
    else if (vite <= 0){
      setC1(img_c_u);
      setC2(img_c_u);
      setC3(img_c_u);
      setTot_punti(previous => (previous - 20));
      setStatoPage("gameOver");
    }
   }, [vite]);

  const chiediAiuto = () => {
    if (aiuti>0){
      setAiuti(previous => (previous - 1));
      const ogg = document.getElementsByName('risposta');
      let flag = false;
      while (flag==false){
        let rand = Math.floor(Math.random() * 4);
        
        if (corr[cont] != ogg[rand].id){
          if (ogg[rand].disabled != true){
            ogg[rand].disabled = true;
            alert("RISPOSTA "+ogg[rand].id+" è stata tolta")
            flag = true;
          }
        }
      }
    }else{
      alert("HAI TERMIANTO GLI AIUTI!");
    }
  };

  useEffect(() => {
    if (aiuti == 2){
      setA1(img_chiav_u);
      setTot_punti(previous => (previous - 10));
    }
    else if (aiuti ==1){
      setA1(img_chiav_u);
      setA2(img_chiav_u);
      setTot_punti(previous => (previous - 10));
    }
    else if (aiuti <= 0){
      setA1(img_chiav_u);
      setA2(img_chiav_u);
      setA3(img_chiav_u);
      setTot_punti(previous => (previous - 10));
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