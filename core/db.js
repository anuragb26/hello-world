var mysql = require("promise-mysql");
var settings = require("../settings");

module.exports.executeQuery = function(queryString,callback)
{
    mysql.createConnection(settings.dbConfig).then(function(conn)
    {
        conn.query(queryString).
        then(function(data)
        {
            callback(data);
        }).catch(function(err)
        {
            console.log(err);
            callback(null,err);
        });
    }).catch(function(err)
    {
        console.log(err);
        callback(null,err);
    })
};

