import { useEffect, useState } from "react";
import axios from "axios";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function App() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/logs").then((res) => {
      setLogs(res.data);
    });
  }, []);

  return (
    <div style={{ background: "#111", minHeight: "100vh", padding: 40 }}>
      <h2 style={{ color: "white" }}>Network Speed Logger</h2>
      <p style={{ color: "white" }}>
Latest Download: {logs[0]?.download} Mbps |
 Upload: {logs[0]?.upload} Mbps |
 Ping: {logs[0]?.ping} ms
</p>

      
     

      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={logs}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="download" />
          <Line type="monotone" dataKey="upload" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

