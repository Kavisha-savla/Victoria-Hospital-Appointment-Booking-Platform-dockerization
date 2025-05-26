const express = require('express');
const path = require('path');
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
router.get('/dashboard', isAdmin, (req, res) => {
  console.log('Admin dashboard accessed by:', req.session.user);
  res.sendFile(path.join(__dirname, '../views/adminDashboard.html'));
});
module.exports = router;
