const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

let notFoundPage = (req, res) => {
    res.render('error_page/404');
};

let internalError = (req, res) => {
    res.render('error_page/500');
};

exports.notFoundPage = notFoundPage;
exports.internalError = internalError;
