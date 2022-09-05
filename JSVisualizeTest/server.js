const express = require("express")
const app = express();

app.get("/data", (req, res) => {
    res.json({name: "kyle", food: "Rice"})
});

app.listen(3000);