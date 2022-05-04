let express = require("express");
let mysql = require("mysql");
let cors = require('cors')

let app = express();

app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));

app.use(cors());

var con = mysql.createConnection({
  host : "localhost",
  user : "root",
  password : "",
  database : "Trapped",
});

app.get("/partita", (req, res) => {
  //apro connessione
  con.connect(function(err) {
    if (!err){
      console.log("Connessione ok!");
    }
  });
  
  //lancio query
  let arrayDomande = new Array();
  let sql = "select * from Domande";
  con.query(sql, function (err, rows,fields) { //callback daa richiamare quando ricevo qualcosa
    if (!err){ //se ce errore esci altrimenti va avanti
      rows.forEach(element => {
        let domande={
          "id":"",
          "domanda":"",
          "risp_A":"",
          "risp_B":"",
          "risp_C":"",
          "risp_D":"",
          "risp_Corr": "",
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
      console.log("Connessione terminata!");
    }
  });
});

app.listen(4000, () => {
  console.log("SERVER ATTIVO");
});