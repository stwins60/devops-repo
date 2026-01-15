const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validateUserInput = (req, res, next) => {
  const { name, email, age } = req.body;

  // Check required fields for POST requests
  if (req.method === 'POST') {
    if (!name || name.trim().length === 0) {
      return res.status(400).json({
        success: false,
        error: 'Name is required'
      });
    }

    if (!email) {
      return res.status(400).json({
        success: false,
        error: 'Email is required'
      });
    }
  }

  // Validate name if provided
  if (name !== undefined) {
    if (typeof name !== 'string' || name.trim().length === 0) {
      return res.status(400).json({
        success: false,
        error: 'Name must be a non-empty string'
      });
    }

    if (name.length > 100) {
      return res.status(400).json({
        success: false,
        error: 'Name is too long (max 100 characters)'
      });
    }
  }

  // Validate email if provided
  if (email !== undefined) {
    if (!validateEmail(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format'
      });
    }
  }

  // Validate age if provided
  if (age !== undefined && age !== null) {
    const ageNum = Number(age);
    if (isNaN(ageNum) || ageNum < 0 || ageNum > 150) {
      return res.status(400).json({
        success: false,
        error: 'Age must be a number between 0 and 150'
      });
    }
  }

  next();
};

module.exports = { validateUserInput, validateEmail };
