# 🚦 Static Routing using SDN Controller

<p align="center">
  <b>Software Defined Networking Project using POX + Mininet + Open vSwitch</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Emulator-Mininet-2C3E50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Controller-POX-16A085?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Protocol-OpenFlow-blue?style=for-the-badge" />
</p>

---

# 📌 Project Overview

This project demonstrates **Static Routing in Software Defined Networking (SDN)** using the **POX Controller**, **Mininet**, and **Open vSwitch**.

The SDN controller installs predefined flow rules into switches so that packets always follow a fixed route chosen by the controller.

Unlike traditional dynamic routing, where paths may change automatically, this project ensures that traffic follows a manually configured static path.

---

# 🎯 Problem Statement

Implement static routing paths using controller-installed flow rules.

### Required Tasks

* Define routing paths
* Install flow rules manually
* Validate packet delivery
* Document routing behavior
* Perform regression testing after rule reinstallation

---

# 🛠️ Tools & Technologies Used

| Component    | Description             |
| ------------ | ----------------------- |
| Ubuntu       | Operating System        |
| Python       | Programming Language    |
| Mininet      | Network Emulator        |
| POX          | SDN Controller          |
| Open vSwitch | OpenFlow Virtual Switch |
| GitHub       | Source Code Hosting     |

---

# 🧱 Network Topology

```text
h1 ---- s1 ---- s2 ---- s3 ---- h2
```

### Components

* **Hosts:** h1, h2
* **Switches:** s1, s2, s3
* **Controller:** POX

---

# 📁 Repository Structure

```text
SDN_static_routing/
│── README.md
│
├── src/
│   ├── static_routing.py
│   └── mytopo.py
│
├── screenshots/
│   ├── controller running.png
│   ├── topology running.png
│   ├── regression test2.png
│   ├── flow tables.png
│   └── regression test1.png
│
└── docs/
    └── report.pdf 
```

---

# 📄 Source Code Files

| File                    | Purpose                                       |
| ----------------------- | --------------------------------------------- |
| `src/static_routing.py` | Controller logic to install static flow rules |
| `src/mytopo.py`         | Custom Mininet topology                       |
| `README.md`             | Project documentation                         |

---

# ⚙️ Controller Logic (`static_routing.py`)

```python
from pox.core import core
import pox.openflow.libopenflow_01 as of

def rule(con, inp, outp):
    msg = of.ofp_flow_mod()
    msg.match.in_port = inp
    msg.actions.append(of.ofp_action_output(port=outp))
    con.send(msg)

def _handle_ConnectionUp(event):
    dpid = event.dpid

    if dpid == 1:
        rule(event.connection,1,2)
        rule(event.connection,2,1)

    elif dpid == 2:
        rule(event.connection,1,2)
        rule(event.connection,2,1)

    elif dpid == 3:
        rule(event.connection,1,2)
        rule(event.connection,2,1)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
```

---

# 🌐 Custom Topology (`mytopo.py`)

```python
from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, h2)

topos = {'mytopo': MyTopo}
```

---

# 🚀 How to Run the Project

## 1️⃣ Start Controller

Open Terminal 1:

```bash
cd ~/pox
python3 pox.py forwarding.static_routing
```

---

## 2️⃣ Start Mininet

Open Terminal 2:

```bash
sudo mn -c
sudo mn --custom ~/mytopo.py --topo mytopo --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6633
```

---

## 3️⃣ Test Connectivity

Inside Mininet CLI:

```bash
pingall
```

### Expected Output

```text
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped
```

---

# 📸 Proof of Execution

## 🔹 Controller Running

![Controller Running](screenshots/controllerrunning.png)

---

## 🔹 Mininet Topology Running

![Topology Running](screenshots/topologyrunning.png)

---

## 🔹 Flow Table Entries

![Flow Tables](screenshots/flowtables.png)

---

## 🔹 Regression Test

![Regression Test](screenshots/regressiontest1.png)

---
## 🔹 Regression Test

![Regression Test](screenshots/regressiontest2.png)

# 🔄 Routing Behavior

The installed rules force packets to follow:

```text
h1 → s1 → s2 → s3 → h2
```

### Switch-wise Behavior

| Switch | Action                    |
| ------ | ------------------------- |
| s1     | Forward between h1 and s2 |
| s2     | Forward between s1 and s3 |
| s3     | Forward between s2 and h2 |

---

# 📊 Flow Table Verification

Run inside Mininet:

```bash
sh ovs-ofctl dump-flows s1
sh ovs-ofctl dump-flows s2
sh ovs-ofctl dump-flows s3
```

These commands display OpenFlow entries installed by the controller.

---

# 🧪 Regression Testing

## Delete Existing Rules

```bash
sh ovs-ofctl del-flows s1
sh ovs-ofctl del-flows s2
sh ovs-ofctl del-flows s3
```

## Restart Controller and Test Again

```bash
pingall
```

### Expected Result

* Connectivity remains successful
* Same static route is restored

---

# ✅ Results

* Successfully implemented static routing using SDN
* Installed manual OpenFlow rules
* Verified packet delivery
* Validated flow tables
* Performed regression testing successfully

---

# 📚 Concepts Demonstrated

* Software Defined Networking (SDN)
* Control Plane vs Data Plane
* OpenFlow Protocol
* Static Routing
* Flow Rule Installation
* Mininet Network Emulation

---

# 👨‍💻 Author

**Sachin S**
**SRN:** PES2UG24CS422

---

# 📌 Future Enhancements possibilities 

* Dynamic Routing
* Multi-path Routing
* Link Failure Recovery
* QoS-based Traffic Control
* Traffic Monitoring Dashboard

.....
