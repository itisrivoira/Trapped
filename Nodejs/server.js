let express = require("express");
let mysql = require("mysql");
let cors = require('cors');
let bodyParser = require('body-parser');

let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));

app.use(cors());

app.get("/partita", (req, res) => {
  var con = mysql.createConnection({
    host : "localhost",
    user : "root",
    password : "",
    database : "Trapped",
  });

  //apro connessione
  con.connect(function(err) {
    if (!err){
      console.log("Connessione db ok!");
    }
  });
  
  //lancio query
  let arrayDomande = new Array();
  let sql = "select * from Domande";
  con.query(sql, function (err, rows,fields) { //callback daa richiamare quando ricevo qualcosa
    if (!err){ //se ce errore esci altrimenti va avanti
      rows.forEach(element => {
        let domande={
          id:"",
          domanda:"",
          risp_A:"",
          risp_B:"",
          risp_C:"",
          risp_D:"",
          risp_Corr: "",
        }
        domande.id = element.id_D;
        domande.domanda = element.domanda;
        domande.risp_A = element.risp_A;
        domande.risp_B = element.risp_B;
        domande.risp_C = element.risp_C;
        domande.risp_D = element.risp_D;
        domande.risp_Corr = element.risp_Corr;
        arrayDomande.push(domande);
        console.log(element.id_D + "\t\t" + element.domanda);
      });
    } 
    res.send(JSON.stringify(arrayDomande));
  })

  //chiudo connessione
  con.end(function(err) {
    if (!err){
      console.log("Connessione db terminata!");
      console.log("---------------------------------------")
    }
  });
});

app.post("/invioDati", (req, res) => {
  var con = mysql.createConnection({
    host : "localhost",
    user : "root",
    password : "",
    database : "Trapped",
  });
  
  var utente = req.body.nome_U;
  var vite = req.body.vite_U;
  var aiuti = req.body.aiuti_U;
  var punti = req.body.punti_U;

  //apro connessione
  con.connect(function(err) {
    if (!err){
      console.log("Connessione db ok!");
    }
  });
  
  //lancio query
  let arrayDomande = new Array();
  let sql = "INSERT INTO Partite (nome_U, vite_U, aiuti_U, punti_U) VALUES('"+utente+"', "+vite+", "+aiuti+", "+punti+")";
  con.query(sql);

  //chiudo connessione
  con.end(function(err) {
    if (!err){
      console.log("Connessione db terminata!");
      console.log("---------------------------------------")
    }
  });
});

app.get("/classifica", (req, res) => {
  var con = mysql.createConnection({
    host : "localhost",
    user : "root",
    password : "",
    database : "Trapped",
  });

  //apro connessione
  con.connect(function(err) {
    if (!err){
      console.log("Connessione db ok!");
    }
  });
  
  //lancio query
  let arrayPartite = new Array();
  let sql = "select nome_U, vite_U, aiuti_U, punti_U from Partite ORDER BY punti_U DESC";
  con.query(sql, function (err, rows,fields) { //callback daa richiamare quando ricevo qualcosa
    if (!err){ //se ce errore esci altrimenti va avanti
      rows.forEach(element => {
        let partite={
          nome:"",
          vite:"",
          aiuti:"",
          punti:"",
        }
        partite.nome = element.nome_U;
        partite.vite = element.vite_U;
        partite.aiuti = element.aiuti_U;
        partite.punti = element.punti_U;
        
        arrayPartite.push(partite);
        console.log(element.nome_U + "\t\t" + element.punti_U);
      });
    } 
    res.send(JSON.stringify(arrayPartite));
  })

  //chiudo connessione
  con.end(function(err) {
    if (!err){
      console.log("Connessione db terminata!");
      console.log("---------------------------------------")
    }
  });
});

app.listen(4000, () => {
  console.log("SERVER ATTIVO");
});