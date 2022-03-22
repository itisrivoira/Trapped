import React from 'react';
import './App.css';
import {BtnImpstazioni, BtnGioca, BtnClassifica} from './componenti/home_page/buttons/button';

const App = () => {


	return (
		<>
      <div className="contenitore">
        <div className="button">
          <BtnImpstazioni />
        </div>
        <div className="button">
          <BtnGioca />
        </div>
        <div className="button">
          <BtnClassifica />
        </div>
      </div>
		</>
	);
}

export default App;