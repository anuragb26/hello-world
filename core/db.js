var mysql = require("promise-mysql");
var settings = require("../settings");
var connection;

/*

module.exports.executeQuery = function(queryString,callback)
{
    var conn = mysql.createConnection(settings.dbConfig);

    conn.connect(function(err)
    {
        if(err)
        {
            console.log(err);
            callback(null,err);
        }
        else
        {
            conn.query(queryString,function(err,data)
            {
                if(err)
                {
                    console.log(err);
                    callback(null,err);
                }
                else
                {
                    callback(data);
                }
            });
        }
    })
};

*/

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

