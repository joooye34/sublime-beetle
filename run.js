
var path = process.argv[2] || "";
var re = 'hello world!';
console.log(re +':'+ path);

// var ps = require('path');
// var fs = require('fs');
// var Beetle = require('../lib/beetle')
// var path = process.argv[2];

// function formatFile(path){
//   if(!path) return;
//   try{
//     var fileStr = fs.readFileSync(path, 'utf8');
//     var beetle = new Beetle(fileStr);
//     fileStr = beetle.formatRequires().getFileString();
//     fs.writeFileSync(path, fileStr, 'utf8');
//   }catch(err){
//     console.log(JSON.stringify(err));
//   }
// }
