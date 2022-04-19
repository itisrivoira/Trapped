import { createContext, useState } from "react";
import {useAudio} from "./pagine/componenti/audio/useAudio";

import musica from "./pagine/sound/sound.mp3";

export const Music = createContext();
export const SoundBtn = createContext();
export const Cont = createContext();

export const GlobalProvider = ({children}) => {
	const [music, setMusic] = useAudio(musica, true);
  const [soundBtn, setSoundBtn] = useState(false);
  const [cont, setCont] = useState(0);

	return(
		<Music.Provider value={{music, setMusic}}>
      <SoundBtn.Provider value={{soundBtn, setSoundBtn}}>
        <Cont.Provider value={{cont, setCont}}>
          {children}
        </Cont.Provider>
      </SoundBtn.Provider>
		</Music.Provider>
	)
};