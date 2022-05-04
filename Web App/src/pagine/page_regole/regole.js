import React from "react";
import {Outlet, Link} from "react-router-dom";
import {Carousel} from 'react-bootstrap';
import {BtnTornaIndietro} from "../componenti/buttons/button";
import "./style_regole.css";

export const Regole = () => {
  return(
    <div className="contenitore_impo">
      <div className="row_impo">
        <div className="titolo_impo">
          Regole del gioco
        </div>
      </div>
      <div className="row_impo">
        <div className="regole">
          <Carousel>
            
            <Carousel.Item>
              <div className="a">
                <Carousel.Caption>
                  <h3 className="h3">1.</h3>
                  <p className="p">Per completare il gioco devi rispondere correttamente correttamente a tutte le domande nel tempo prestabilito.</p>
                </Carousel.Caption>
              </div>
            </Carousel.Item>

            <Carousel.Item>
              <div className="a">
                <Carousel.Caption>
                  <h3 className="h3">2.</h3>
                  <p className="p">Hai a disposizione 3 vite, in caso di risposta sbagliata perdi una vita. Se esaurisci tutte le vite, perdi la partita.</p>
                </Carousel.Caption>
              </div>
            </Carousel.Item>

            <Carousel.Item>
              <div className="a">
                <Carousel.Caption>
                  <h3 className="h3">3.</h3>
                  <p className="p">Hai a disposizione 3 suggerimenti, in caso di utilizzo eliminano una risposta sbagliata tra le quattro presenti.</p>
                </Carousel.Caption>
              </div>
            </Carousel.Item>
            
          </Carousel>
        </div>
      </div>
      <div className="row_impo">
        <div className="button_regole">
          <Link to="/gioco">
            <BtnTornaIndietro/>
          </Link>
          <Outlet />
        </div>
      </div>
    </div>
  )
};