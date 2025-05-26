const express = require('express');
const path = require('path');
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
const Appointment = require('../models/Appointment');
router.get('/dashboard', isAdmin, (req, res) => {
  console.log('Admin dashboard accessed by:', req.session.user);
  res.sendFile(path.join(__dirname, '../views/adminDashboard.html'));
});
router.get('/api/appointments', async (req, res) => {
  try {
    const { status, department } = req.query;
    const query = {};

    if (status) query.status = status;
    if (department) query.department = department;

    console.log('Incoming query:', req.query);
    console.log('MongoDB query:', query);

    const appointments = await Appointment.find(query);
    res.json(appointments);
  } catch (err) {
    console.error('Error fetching appointments:', err);
    res.status(500).json({ error: 'Server error' });
  }
});

module.exports = router;
