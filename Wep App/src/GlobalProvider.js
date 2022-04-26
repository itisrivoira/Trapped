import { createContext, useState } from "react";
import {useAudio} from "./pagine/componenti/audio/useAudio";

import musica from "./pagine/sound/sound.mp3";

export const Music = createContext();
export const SoundBtn = createContext();
export const Pers = createContext();
export const Cont = createContext(0);
export const Vite = createContext(3);
export const Aiuti = createContext(3);
export const Giuste = createContext(0);

export const GlobalProvider = ({children}) => {
	const [music, setMusic] = useAudio(musica, true);
  const [soundBtn, setSoundBtn] = useState(false);
  const [pers, setPers] = useState();
  const [cont, setCont] = useState(0);
  const [vite, setVite] = useState(3);
  const [aiuti, setAiuti] = useState(3);
  const [giuste, setGiuste] = useState(0);


	return(
		<Music.Provider value={{music, setMusic}}>
      <SoundBtn.Provider value={{soundBtn, setSoundBtn}}>
        <Pers.Provider value={{pers, setPers}}>
          <Cont.Provider value={{cont, setCont}}>
            <Vite.Provider value={{vite, setVite}}>
              <Aiuti.Provider value={{aiuti, setAiuti}}>
                <Giuste.Provider value={{giuste, setGiuste}}>
                  {children}
                </Giuste.Provider>
              </Aiuti.Provider>
            </Vite.Provider>
          </Cont.Provider>
        </Pers.Provider>        
      </SoundBtn.Provider>
		</Music.Provider>
	)
};