app.get('/api/ram_total_usage_percent', (req, res) => {
  let csv = []
  const query = 
  `from(bucket: "Telemetry")
  |> range(start: -10s)
  |> filter(fn: (r) => r["_measurement"] == "mem")
  |> filter(fn: (r) => r["_field"] == "used_percent")
  |> yield(name: "mean")`

  queryApi.queryRows(query, {
      next(row, tableMeta) {
        o = tableMeta.toObject(row)
        csv.push(o)
        console.log(`${o._time} ${o._measurement}: ${o._field}=${o._value}`)
      },
      error(error) {
        console.error(error)
        res.end()
      },
      complete() {
        res.json(csv)
      },
    })
})
