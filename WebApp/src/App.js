import React from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom";
import {Home} from "./pagine/page_home/home";
import {Impostazioni} from "./pagine/page_impostazioni/impostazioni";
import {ConfigPartita} from "./pagine/page_configPartita/configPartita";
import {Classifica} from "./pagine/page_classifica/classifica";

const App = () => {
	return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/" element={<Home />}>
        </Route>
        <Route
          path="/impostazioni" element={<Impostazioni />}>
        </Route>
        <Route
          path="/confingpartita" element={<ConfigPartita />}>
        </Route>
        <Route
          path="/classifica" element={<Classifica />}>
        </Route>
        <Route
          path="/partita" element={<Partita />}>
        </Route>
      </Routes>
    </BrowserRouter>
	);
}

export default App;