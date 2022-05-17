import {Outlet, Link} from "react-router-dom";
import {useState, useEffect, useContext} from "react";
import {Music, SoundBtn, Cont, Pers, Aiuti, Vite, StatoPage, Nickname} from "../../../GlobalProvider";
import {useAudio} from "../audio/useAudio";
import clickBtn from "../../sound/clickButton.wav";
import "../../page_impostazioni/style_impostazioni.css"
import "../../page_partita/style_partita.css"

import imgTornaIndietro from "./img/img_tornaIndietro.png"

import img_impostazioni from "./img/img_impostazioni.png";
import img_impostazioni_on from "./img/img_impostazioni_on.png";

import img_regole from "./img/img_regole.png";
import img_regole_on from "./img/img_regole_on.png";

import img_esci from "./img/img_esci.png";
import img_esci_on from "./img/img_esci_on.png";

import img_gioca from "./img/img_gioca.png";
import img_gioca_on from "./img/img_gioca_on.png";

import img_classifica from "./img/img_classifica.png";
import img_classifica_on from "./img/img_classifica_on.png";

import img_acceso from  "./img/img_acceso.png";
import img_acceso_on from  "./img/img_acceso_on.png";

import img_spento from  "./img/img_spento.png";
import img_spento_on from  "./img/img_spento_on.png";

import img_sceltaS from "./img/img_scelta_s.png";
import img_sceltaD from "./img/img_scelta_d.png";
import img_uomo from "../photos/uomo/uomo_davanti_1.png"
import img_donna from "../photos/donna/donna_davanti_1.png"

import img_inizia from "./img/img_inizia.png";
import img_inizia_on from "./img/img_inizia_on.png";

import img_esciGameOver from "./img/img_esciGameOver.png";
import img_esciGameOver_on from "./img/img_esciGameOver_on.png";

export const BtnImpstazioni = () => {
  const [img, setImage] = useState(img_impostazioni);
  const [sbtn, setSbtn] = useAudio(clickBtn, false);
  const {soundBtn} = useContext(SoundBtn);

	const on_img = () => {
    setImage(img_impostazioni_on);
    if (soundBtn == true){
      setSbtn(true);
    }
  };

  const out_img = () => {
    setImage(img_impostazioni);
  };

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
  const [sbtn, setSbtn] = useAudio(clickBtn, false);
  const {soundBtn} = useContext(SoundBtn);

	const on_img = () => {
    setImage(img_gioca_on);
    if (soundBtn == true){
      setSbtn(true);
    }
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
  const [sbtn, setSbtn] = useAudio(clickBtn, false);
  const {soundBtn} = useContext(SoundBtn);

	const on_img = () => {
    setImage(img_classifica_on);
    if (soundBtn == true){
      setSbtn(true);
    }
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
    <div style={{position: "absolute", width: "95%", left: "0px", paddingLeft: "30px"}}>
      <img
        src={imgTornaIndietro}
        alt=""
      />
    </div>
  )
};

export const BtnMusica = () => {
  const [imgS, setImgS] = useState(img_acceso);
  const [imgD, setImgD] = useState(img_spento);

  const {music, setMusic} = useContext(Music);

  const premiOn = () => {
    setImgS(img_acceso_on);
    setImgD(img_spento);
    setMusic();
  };

  const premiOff = () => {
    setImgS(img_acceso);
    setImgD(img_spento_on);
    setMusic();
  };

  useEffect(() => {
   if (music == true){
    setImgS(img_acceso_on);
    setImgD(img_spento);
   }
   else if (music == false){
    setImgS(img_acceso);
    setImgD(img_spento_on);
   }
  }, [music]);

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

  const {soundBtn, setSoundBtn} = useContext(SoundBtn);
  
  const premiOn = () => {
    setImgS(img_acceso_on);
    setImgD(img_spento);
    setSoundBtn(true);
  };

  const premiOff = () => {
    setImgS(img_acceso);
    setImgD(img_spento_on);
    setSoundBtn(false);
  };

  useEffect(() => {
    if (soundBtn == true){
     setImgS(img_acceso_on);
     setImgD(img_spento);
    }
    else if (soundBtn == false){
     setImgS(img_acceso);
     setImgD(img_spento_on);
    }
   }, [soundBtn]);

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
  const {pers, setPers} = useContext(Pers);

  const [state, setState] = useState("uomo");
  const [personaggio, setPersonaggio] = useState(img_uomo);

  

  useEffect(() => {
    if (state == "uomo"){
      setPers(img_uomo);
    }
    else if(state == "donna"){
      setPers(img_donna);
    }
  }, [state]);

  const cambia = () => {
    if (state == "uomo"){
      setPersonaggio(img_donna);
      setState("donna");
    }
    else if (state == "donna"){
      setPersonaggio(img_uomo);
      setState("uomo");
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
  const [sbtn, setSbtn] = useAudio(clickBtn, false);
  const {soundBtn} = useContext(SoundBtn);
  const {nickname, setNickname} = useContext(Nickname);

  let link = "";

	const on_img = () => {
    setImage(img_inizia_on);
    if (soundBtn == true){
      setSbtn(true);
    }
  };

  const out_img = () => {
    setImage(img_inizia);
  }

  const contrInseri = () => {
    if (nickname == ""){
      alert("Non hai inserito il nickname")
    }
  }

  return(
    <>
      <Link to={nickname != "" ? "/gioco" : "/confingpartita"}>
        <img 
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
          onClick={contrInseri}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnMenu = () => {
  const [img, setImage] = useState(img_impostazioni);

	const on_img = () => {
    setImage(img_impostazioni_on);
  };

  const out_img = () => {
    setImage(img_impostazioni);
  }

  return(
    <>
      <Link to="/menu">
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

export const BtnRegole = () => {
  const [img, setImage] = useState(img_regole);

	const on_img = () => {
    setImage(img_regole_on);
  };

  const out_img = () => {
    setImage(img_regole);
  }

  return(
    <>
      <Link to="/regole">
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

export const BtnEsci = () => {
  const [img, setImage] = useState(img_esci);
  
  const {pers, setPers} = useContext(Pers);
  const {cont, setCont} = useContext(Cont);
  const {vite, setVite} = useContext(Vite);
  const {aiuti, setAiuti} = useContext(Aiuti);
  const {statoPage, setStatoPage} = useContext(StatoPage);
  const {nickname, setNickname} = useContext(Nickname);

	const on_img = () => {
    setImage(img_esci_on);
  };

  const out_img = () => {
    setImage(img_esci);
  }
  
  const azzera = () => {
    setStatoPage("partita");
    setPers("");
    setCont(0);
    setVite(3);
    setAiuti(3);
    setNickname("");
   };

  return(
    <>
      <Link to="/">
        <img
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
          onClick={azzera}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnEsciGameOver = () => {
  const [img, setImage] = useState(img_esciGameOver);

  const {pers, setPers} = useContext(Pers);
  const {cont, setCont} = useContext(Cont);
  const {vite, setVite} = useContext(Vite);
  const {aiuti, setAiuti} = useContext(Aiuti);
  const {statoPage, setStatoPage} = useContext(StatoPage);
  const {nickname, setNickname} = useContext(Nickname);

	const on_img = () => {
    setImage(img_esciGameOver_on);
  };

  const out_img = () => {
    setImage(img_esciGameOver);
  };

  useEffect(() => {
    
  }, [statoPage]);

 const azzera = () => {
  setStatoPage("partita");
  setPers("");
  setCont(0);
  setVite(3);
  setAiuti(3);
  setNickname("");
 };

  return(
    <>
      <Link to="/">
        <img
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
          onClick={azzera}
        />
      </Link>
      <Outlet />
    </>
  )
};

export const BtnEsciVittoria = () => {
  const [img, setImage] = useState(img_esciGameOver);

  const {pers, setPers} = useContext(Pers);
  const {cont, setCont} = useContext(Cont);
  const {vite, setVite} = useContext(Vite);
  const {aiuti, setAiuti} = useContext(Aiuti);
  const {statoPage, setStatoPage} = useContext(StatoPage);
  const {nickname, setNickname} = useContext(Nickname);

	const on_img = () => {
    setImage(img_esciGameOver_on);
  };

  const out_img = () => {
    setImage(img_esciGameOver);
  };

  useEffect(() => {
    
  }, [statoPage]);

 const azzera = () => {
  setStatoPage("partita");
  setPers("");
  setCont(0);
  setVite(3);
  setAiuti(3);
  setNickname("");
 };

  return(
    <>
      <Link to="/">
        <img
          src={img}
          alt=""
          onMouseEnter={on_img}
          onMouseLeave={out_img}
          onClick={azzera}
        />
      </Link>
      <Outlet />
    </>
  )
};