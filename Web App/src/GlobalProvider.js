import { createContext, useState } from "react";
import musica from "./pagine/sound/sound.mp3";

export const Music = createContext();

export const GlobalProvider = ({children}) => {
	const [music, setMusic] = useState(false);

	return(
		<Music.Provider value={{music, setMusic}}>
        {children}
		</Music.Provider>
	)
};