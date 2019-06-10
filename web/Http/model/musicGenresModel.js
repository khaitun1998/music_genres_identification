const spawn = require('child_process').spawn;
const path = require('path');

let getGenres = (filename) => {
    return new Promise((resolve, reject) => {
        let pyProgram = spawn('python3', [path.join(__dirname + '/../controller/speech/predict.py'), filename]);
        pyProgram.stdout.on('data', data => {
            let tmp = new Buffer.from(String.fromCharCode.apply(null, data));
            let tmp2 = tmp.toString();
            resolve(tmp2);
        });

        pyProgram.stderr.on('data', data => {
            let tmp = String.fromCharCode.apply(null, data);
            let tmp2 = tmp.toString();
            reject(tmp2);
        });
    })
};

exports.getGenres = getGenres;