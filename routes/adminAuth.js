const express = require('express');
const path = require('path');
const router = express.Router();
router.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, '../views/adminLogin.html'));
});
router.post('/login', (req, res) => {
  const { email, password } = req.body;
  if (email === 'admin@example.com' && password === 'admin123') {
    req.session.user = { email, role: 'admin' };
    return res.redirect('/admin/dashboard');
  }

  return res.send('Invalid credentials');
});
module.exports = router;
