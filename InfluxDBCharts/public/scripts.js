const loadData = () => {
  let ramTrace;
  let cpuTrace;
  let processTrace;

  const cpuPlot = (cpuTrace) => {
    const layout = {
      title: "Local CPU Usage",
    };
    return Plotly.newPlot(
      "graphs-container",
      [cpuTrace],
      layout
    );
  };

  const ramPlot = (ramTrace) => {
    const layout = {
      title: "Local Ram Usage Percent",
    };
    return Plotly.newPlot(
      "ram-graph",
      [ramTrace],
      layout
    );
  };

  const processPlot = (processTrace) => {
    const layout = {
      title: "Local Processes",
    };
    return Plotly.newPlot(
      "process-graph",
      [processTrace],
      layout
    );
  };

  const fetchRamData = () => {
    ramTrace = fetch("/api/ram_total_usage_percent")
      .then((response) => response.json())
      .then((data) => {
        const unpackData = (arr, key) => {
          return arr.map((obj) => obj[key]);
        };
        const traceData = {
          type: "scatter",
          mode: "lines",
          name: "Ram total Usage",
          x: unpackData(data, "_time"),
          y: unpackData(data, "_value"),
          line: { color: "#17BECF" },
        };
        return traceData;
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    return [ramTrace];
  };

  [ramTrace] = fetchRamData();

  Promise.all([ramTrace]).then((values) => {
    ramPlot(values[0], values[1]);
  });

  function printRam() {
    [ramTrace] = fetchRamData();

    Promise.all([ramTrace]).then((values) => {
      ramPlot(values[0], values[1]);
    });
  }

  const fetchData = () => {
    cpuTrace = fetch("/api/cpu_total_user")
      .then((response) => response.json())
      .then((data) => {
        const unpackData = (arr, key) => {
          return arr.map((obj) => obj[key]);
        };
        const traceData = {
          type: "scatter",
          mode: "lines",
          name: "CPU total Usage for User",
          x: unpackData(data, "_time"),
          y: unpackData(data, "_value"),
          line: { color: "#17BECF" },
        };
        return traceData;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    return [cpuTrace];
  };

  [cpuTrace] = fetchData();

  Promise.all([cpuTrace]).then((values) => {
    cpuPlot(values[0], values[1]);
  });

  function printCpu() {
    [cpuTrace] = fetchData();

    Promise.all([cpuTrace]).then((values) => {
      cpuPlot(values[0], values[1]);
    });
  }

  const fetchProcessData = () => {
    processTrace = fetch("/api/processes")
      .then((response) => response.json())
      .then((data) => {
        const unpackData = (arr, key) => {
          return arr.map((obj) => obj[key]);
        };
        const traceData = {
          type: "scatter",
          mode: "lines",
          name: "Processes",
          x: unpackData(data, "_time"),
          y: unpackData(data, "_value"),
          line: { color: "#17BECF" },
        };
        return traceData;
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    return [processTrace];
  };

  [processTrace] = fetchProcessData();

  Promise.all([processTrace]).then((values) => {
    processPlot(values[0], values[1]);
  });

  function printProcesses() {
    [processTrace] = fetchProcessData();

    Promise.all([processTrace]).then((values) => {
      processPlot(values[0], values[1]);
    });
  }
  
  function callGraphs(){
    printCpu();
    printRam();
    printProcesses();
  }

  setInterval(callGraphs, 3000);

};

$(window).on("load", loadData);

