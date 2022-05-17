const nodemailer = require('nodemailer');
let express = require("express");
let bodyParser = require('body-parser');

let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));


app.post("/", (req, res) => {

	let mailsor = res.body.sorgente
	let corpomail = res.body.corpomail

	let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: "mei.chang@denina.it",
            pass: "PASSWORD"
        }
	});
  
	let message = {
		from: mailsor,
		to: "mei.chang@denina.it",
		subject: "contacts",
		html: corpomail
	}
	
	transporter.sendMail(message, function(err, info) {
	if (err) {
		console.log(err);
	} else {
		console.log(info);
	}
	})




});
  


app.listen(4000, () => {
	console.log("SERVER ATTIVO");
});