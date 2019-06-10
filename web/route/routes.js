const express = require('express');
const router = express.Router();
const index = require('../Http/controller/musicGenresController.js');

router.get('/', index.index);

router.post('/uploadfile', index.getGenres);

module.exports = router;