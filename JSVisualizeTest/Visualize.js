
// let dataArray = [
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
//     { width: 25, height: Math.random() * 30 },
// ];

let dataArray = [0, 1];
let integer = 1;

async function a() {

    await axios.get("https://cors-anywhere.herokuapp.com/https://api.btcturk.com/api/v2/ticker").then(response => {
        console.log(response.data.data[0].last);
        dataArray[1] = (response.data.data[0].last);
        console.log(dataArray);

        svg.append("line")
            .data(dataArray)
            .transition()
            .duration(2000)
            .attr('x1', (data, index) => { return 50 })
            .attr('y1', (data, index) => { return 600 })
            .attr("x2", (data, index) => { return integer * 50 })
            .attr("y2", (data, index) => { return 50 })
            .attr("stroke", "black");

        integer++;
    });
}

setInterval(a, 2000);

console.log(dataArray);

const canva = d3.select(".canva");

const svg = canva.append("svg")
    .attr('width', "1500")
    .attr('height', "800")
    .style("overflow-x", "scroll")
    .style("flex", "auto");

svg.append("line")
    .attr("x1", 50)
    .attr("y1", 0)
    .attr("x2", 50)
    .attr("y2", 600)
    .attr("stroke", "black");

svg.append("line")
    .attr("x1", 50)
    .attr("y1", 600)
    .attr("x2", 1000)
    .attr("y2", 600)
    .attr("stroke", "black");

svg.append("text")
    .attr("x", 0)
    .attr("y", 15)
    .text("%100")

svg.append("text")
    .attr("x", 5)
    .attr("y", 600)
    .text("%0")

svg.append("text")
    .attr("x", 5)
    .attr("y", 300)
    .text("%50")

// canva.append("p").text("Red > 25").style("color", "red");
// canva.append("p").text("Orange < 25 and > 20").style("color", "orange");
// canva.append("p").text("Yellow < 20 and > 10").style("color", "yellow");
// canva.append("p").text("Blue < 10").style("color", "blue");

const rectangle = svg.selectAll("rect");