const express = require('express');
const { verifyManufacturer } = require('../controllers/manufacturerController');
const router = express.Router();

router.post('/verify', verifyManufacturer);

module.exports = router;
