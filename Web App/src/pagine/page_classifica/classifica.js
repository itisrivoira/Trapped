import React from "react";
import {useState, useEffect} from "react";
import {Outlet, Link} from "react-router-dom";
import "./style_classifica.css";
import {BtnTornaIndietro} from "../componenti/buttons/button";
import Table from "../componenti/table/table";

export const Classifica = () => {
  
  const [dataTable, setDataTable] = useState([]);

  useEffect(() => {
    fetch('http://localhost:4000/classifica', {
      method: 'GET'
    })
    .then(response => response.json())
    .then(res => setDataTable(res))
  }, []);

  const column = [
    { heading: 'Nome', value: 'nome' },
    { heading: 'N. vite', value: 'vite' },
    { heading: 'N. aiuti', value: 'aiuti' },
    { heading: 'Punti', value: 'punti' },
  ]

  return(
    <div className="contenitore_class">
       <div className="row_class">
        <div className="titolo_class">
          Classifica
        </div>
      </div>
      <Table data={dataTable} column={column}/>
      <div className="row_class">
        <div className="button_class">
          <Link to="/">
            <BtnTornaIndietro/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  )
};