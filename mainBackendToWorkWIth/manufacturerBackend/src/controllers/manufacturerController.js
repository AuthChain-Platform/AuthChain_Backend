const manufacturers = require('../data/dummyManufacturers');

exports.verifyManufacturer = async (req, res) => {
    const { brandName, registration_no } = req.body;

    try {
        const manufacturer = manufacturers.find(
            (m) =>
                m.brandName.toLowerCase() === brandName.toLowerCase() &&
                m.registration_no === registration_no
        );

        if (!manufacturer) {
            return res.status(404).json({ error: "Manufacturer is not found" });
        }

        if (!manufacturer.verified) {
            return res.status(400).json({ error: "Manufacturer verification failed" });
        }

        res.status(200).json({
            message: "Manufacturer verified successfully",
            verified: true,
            details: manufacturer,
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Internal Server Error" });
    }
};
