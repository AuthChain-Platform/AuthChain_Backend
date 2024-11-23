const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const manufacturerRoutes = require('./routes/manufacturer');

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.use('/api/manufacturers', manufacturerRoutes);

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
