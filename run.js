var ps = require('path');
var fs = require('fs');
var Beetle = require('beetle')
var path = process.argv[2];

var re = [];
var OUTPUT_VALID = "***beetle***";
formatFile(path);

function formatFile(path){
  if(!path) return;
  try{
    var fileStr = fs.readFileSync(path, 'utf8');
    var beetle = new Beetle(fileStr);
    fileStr = beetle.formatRequires().getFileString();
    re.push(200);
    re.push(fileStr);
  }catch(err){
    re.push(500);
    re.push(JSON.stringify(err));
  }
  console.log(re.join(OUTPUT_VALID));
}

