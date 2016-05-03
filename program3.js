var fs = require('fs');

var fileContent=fs.readFileSync(process.argv[2]).toString();

var contentByLine=fileContent.split("\n");

var noOfLines = contentByLine.length - 1;

console.log(noOfLines);