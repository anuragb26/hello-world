var net = require('net');


var pad  = function(n)
{
    return (n<10)?'0'+n:n;
}

var server = net.createServer(function (socket)
{
    var date = new Date()
    var timeStamp = date.getFullYear()+"-"+pad(String(parseInt(date.getMonth()) +1))+"-"+pad(date.getDate())+" "+pad(date.getHours())+ ":"+pad(date.getMinutes()) + "\n";
    socket.write(timeStamp);
    socket.end();

});


server.listen(process.argv[2]);