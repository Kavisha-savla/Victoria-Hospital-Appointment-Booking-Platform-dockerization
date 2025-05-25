const express = require('express');
const path = require('path'); // THIS WAS MISSING
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
router.get('/dashboard', isAdmin, (req, res) => {
  res.sendFile(path.join(__dirname, '../views/adminLogin.html'));
});
module.exports = router;
