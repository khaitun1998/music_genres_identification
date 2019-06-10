const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const formidable = require('formidable');
const fs = require('fs');
const path = require('path');
const model = require('../model/musicGenresModel.js');

let index = (req, res) => {
    res.render('index');
};

let getGenres = (req, res) => {
    let form = new formidable.IncomingForm();

    form.parse(req);

    form.on('fileBegin', function (name, file){
        file.path = __dirname + '/speech/uploads/' + file.name;
    });

    let filename = "";

    form.on('file', function (name, file){
        filename = file.name;
        if(path.extname(filename) != ".mp3"){
            fs.unlink(path.join(__dirname + '/speech/uploads/' + filename), err => {
                if(err){
                    res.json({
                        success: false,
                        message: err
                    })
                }
                else{
                    res.json({
                        success: false,
                        message: "Mp3 file only!!"
                    })
                }
            })
        }
        else{
            model.getGenres(filename).then(r => {
                fs.unlink(path.join(__dirname + '/speech/uploads/' + filename), err => {
                    if (err) {
                        console.log(err);
                        res.json({success: false, message: err});
                    }
                    else {
                        res.json({
                            success: true,
                            message: r
                        })
                    }
                })
            }).catch(e => {
                res.json({
                    success: false,
                    message: e
                })
            })
        }
    });
};

exports.getGenres = getGenres;
exports.index = index;
