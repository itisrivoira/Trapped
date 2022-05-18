const nodemailer = require('nodemailer');
let express = require("express");
let bodyParser = require('body-parser');
const { sendFile } = require('express/lib/response');

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
            user: "trapped5c@gmail.com",
            pass: "trapped123"
        },
		tls:{
			rejectUnauthorized: false,
		},
	});
	
  
	let message = {
		from: mailsor,
		to: "trapped5c@gmail.com",
		subject: mailsor,
		html: corpomail
	}
	
	transporter.sendMail(message, function(err, info) {
	if (err) {
		console.log(err);
	} else {
		console.log(info);
		console.log(mailsor);
		console.log(corpomail);
	}
	})

	

});
  


app.listen(4000, () => {
	console.log("SERVER ATTIVO");
});