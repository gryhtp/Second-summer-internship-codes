const express = require('express')
const {InfluxDB} = require('@influxdata/influxdb-client')
const app = express()
const port = 1
const token = ''
const org = ''
const client = new InfluxDB({url: '', token: token})
const queryApi = client.getQueryApi(org)

app.use(express.static('public'))
app.set('port', port);
app.listen(app.get('port'), () => {
    console.log(`Listening on ${app.get('port')}.`);
  });

app.get('/api/cpu_total_user', (req, res) => {
    let csv = []
    const query = 
    `from(bucket: "Telemetry")
    |> range(start: -5m)
    |> filter(fn: (r) => r["_measurement"] == "cpu")
    |> filter(fn: (r) => r["_field"] == "usage_user")
    |> filter(fn: (r) => r["cpu"] == "cpu-total")
    |> yield(name: "mean")`

    queryApi.queryRows(query, {
        next(row, tableMeta) {
          o = tableMeta.toObject(row)
          csv.push(o)
          // console.log(`${o._time} ${o._measurement}: ${o._field}=${o._value}`)
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

app.get('/api/ram_total_usage_percent', (req, res) => {
  let csv = []
  const query = 
  `from(bucket: "Telemetry")
  |> range(start: -5m)
  |> filter(fn: (r) => r["_measurement"] == "mem")
  |> filter(fn: (r) => r["_field"] == "used_percent")
  |> yield(name: "mean")`

  queryApi.queryRows(query, {
      next(row, tableMeta) {
        o = tableMeta.toObject(row)
        csv.push(o)
        // console.log(`${o._time} ${o._measurement}: ${o._field}=${o._value}`)
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

app.get('/api/processes', (req, res) => {
  let csv = []
  const query = 
  `from(bucket: "Telemetry")
  |> range(start: -5m)
  |> filter(fn: (r) => r._measurement == "processes")
  |> filter(fn: (r) => r._field == "running" or r._field == "blocked" or r._field == "idle" or r._field == "unknown")
  |> yield(name: "max")`

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

