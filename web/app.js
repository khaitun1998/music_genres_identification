const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const http = require('http');
const middleware = require('./Http/middleware/middleware.js');
const routes = require('./route/routes.js');

require('dotenv').config();

app.set('port', process.env.PORT || 3000);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs');

/**
 * Route
 */
app.use('/', routes);

/**
 * Middleware handle errors
 */
app.use(middleware.notFoundPage);
app.use(middleware.internalError);

const httpServ = http.createServer(app);
httpServ.listen(app.get('port'));