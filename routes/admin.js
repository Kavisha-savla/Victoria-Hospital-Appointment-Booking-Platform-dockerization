const express = require('express');
const path = require('path');
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
const Appointment = require('../models/Appointment');
router.get('/dashboard', isAdmin, (req, res) => {
  console.log('Admin dashboard accessed by:', req.session.user);
  res.sendFile(path.join(__dirname, '../views/adminDashboard.html'));
});
router.get('/api/appointments', isAdmin, async (req, res) => {
  try {
    const appointments = await Appointment.find();
    res.json(appointments);
  } catch (err) {
    console.error('Error fetching appointments:', err);
    res.status(500).json({ error: 'Failed to fetch appointments' });
  }
});
module.exports = router;
