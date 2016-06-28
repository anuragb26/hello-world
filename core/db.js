var mysql = require("promise-mysql");
var settings = require("../settings");

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
    var conn = mysql.createConnection(settings.dbConfig);

    conn.connect().
        then(function()
        {
            conn.query(queryString).
                then(function()
                {
                    callback(data);
                }).catch(function(err)
                {
                    console.log(err);
                    callback(null,err);
                });
        }).
        catch(function(err)
        {
            console.log(err);
            callback(null,err);
        });
};

