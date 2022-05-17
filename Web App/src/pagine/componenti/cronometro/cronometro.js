import React from 'react';
import { useTimer } from 'react-timer-hook';
import {useState, useContext} from "react";
import {StatoPage} from "../../../GlobalProvider";

export function MyTimer({ expiryTimestamp }) {
  const {statoPage, setStatoPage} = useContext(StatoPage);

  const {
    seconds,
    minutes,
  } = useTimer({ expiryTimestamp, onExpire: () => 
    {
      setStatoPage("gameOver");
    }
  });

  return (
    <div>
      <span>{minutes}</span>:<span>{seconds}</span>
    </div>
  );
}