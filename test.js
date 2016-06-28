var _ = require('underscore');
var mysql = require("mysql");

_.each([1,2,3],function(arrayElement)
{
	console.log(arrayElement*2);
});

var con = mysql.createConnection
	({
		host: "127.0.0.1",
		user:"root",
		password:"",
		database:"vt_service"
	});

con.connect(function(err)
	{
		if(err)
		{
			console.log("Error connecting to Db");
			return ;
		}
		console.log("Connection Established");
	});

//var queryString = "SELECT `id`, `name`, `image`, `description`, `branding`, `rating`, `setup_fee`, `transaction_fees`, `how_to_url`, `currencies` FROM `vt_services`";
var queryString = "SELECT * from  `vt_services`";

con.query(queryString,
		function(err,rows)
{
	if(err)
	{
		console.log("received error");
	}
		console.log(rows);

});

/*
con.query(queryString).then(
		function(record)
		{
			console.log(record);
		}).catch(function(err)
		{
			console.log(err);
		});
*/
con.end(function(err)
	{

	})


