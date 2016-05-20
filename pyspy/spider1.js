var superagent = require('superagent')
    // var cheerio = require("cheerio")

const phoneurl = 'http://www.ncu.edu.cn/zydt/xyhy.htm'
var doSomething = function(err, res) {
    const phonePattern = /<tr>\s+?(<td>.+?<\/td>\s+?){4}<\/tr>/g
    const infoPattern = /<td>.+?<\/td>/g

        // console.log(res.text)
    var phoneDict = res.text.match(phonePattern)
    console.log(phoneDict[0].match(infoPattern))
        // for (var x=0; x<phoneDict.length; x++){
        //     phoneList = {
        //         'office': infoPattern.exec(x)[1],
        //         'detail': infoPattern.exec(x)[1],
        //         'quhao': infoPattern.exec(x)[1],
        //         'number': infoPattern.exec(x)[1]
        //     }
        //     console.log(phoneList)
        // }

}

// superagent.get(phoneurl).end(doSomething)


// var http = require('http');
// http.get(phoneurl, function(res) {
//     var size = 0;
//     var chunks = [];
//   res.on('data', function(chunk){
//       size += chunk.length;
//       chunks.push(chunk);
//   });
//   res.on('end', function(){
//       var data = Buffer.concat(chunks, size);
//       console.log(data.toString())
//   });
// }).on('error', function(e) {
//   console.log("Got error: " + e.message);
// });
