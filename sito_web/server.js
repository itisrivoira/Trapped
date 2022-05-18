const nodemailer = require('nodemailer');
let express = require("express");
let bodyParser = require('body-parser');

let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));


app.post("/arrivamail", (req, res) => {

	console.log("server mail");

	let mailsor = req.body.sorgente
	let corpomail = req.body.corpomail

	let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: "1448218569m@gmail.com",
            pass: "asd"
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