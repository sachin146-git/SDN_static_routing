# SDN_static_routing
# Static Routing using SDN Controller

## 📌 Project Overview

This project demonstrates **Static Routing in Software Defined Networking (SDN)** using the **POX Controller**, **Mininet**, and **Open vSwitch**.
The controller installs predefined flow rules into switches so that packets always follow a fixed path determined by the controller.

Unlike traditional dynamic routing, where routes may change automatically, this implementation ensures that traffic follows a manually configured static route.

---

## 🎯 Problem Statement

Implement static routing paths using controller-installed flow rules.

### Expected Tasks

* Define routing paths
* Install flow rules manually
* Validate packet delivery
* Document routing behavior
* Perform regression testing to ensure the path remains unchanged after rule reinstallation

---

## 🛠️ Tools & Technologies Used

| Component      | Description                                    |
| -------------- | ---------------------------------------------- |
| Ubuntu         | Operating System                               |
| Mininet        | Network emulator for creating virtual topology |
| POX Controller | SDN controller used to install flow rules      |
| Open vSwitch   | Virtual switch supporting OpenFlow             |
| Python         | Used for controller and topology scripts       |
| GitHub         | Version control and project hosting            |

---

## 🧱 Network Topology

```text
h1 ---- s1 ---- s2 ---- s3 ---- h2
```

### Components

* **Hosts:** h1, h2
* **Switches:** s1, s2, s3
* **Controller:** POX

---

## ⚙️ Project Files

| File Name           | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| `static_routing.py` | POX controller logic for installing static flow rules |
| `mytopo.py`         | Custom Mininet topology                               |
| `README.md`         | Project documentation                                 |

---

## 📄 Source Code

### `static_routing.py`

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

### `mytopo.py`

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

## 🚀 How to Run the Project

### 1️⃣ Start the Controller

Open Terminal 1:

```bash
cd ~/pox
python3 pox.py forwarding.static_routing
```

---

### 2️⃣ Start Mininet Topology

Open Terminal 2:

```bash
sudo mn -c
sudo mn --custom ~/mytopo.py --topo mytopo --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6633
```

---

### 3️⃣ Validate Connectivity

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

## 🔄 Routing Behavior

The controller installs the following forwarding rules:

### Switch s1

* Packets from h1 forwarded to s2
* Return packets forwarded back to h1

### Switch s2

* Forwards packets between s1 and s3

### Switch s3

* Packets forwarded to h2
* Return packets sent back to s2

This ensures all traffic follows:

```text
h1 → s1 → s2 → s3 → h2
```

---

## 📊 Flow Table Verification

Run the following commands in Mininet:

```bash
sh ovs-ofctl dump-flows s1
sh ovs-ofctl dump-flows s2
sh ovs-ofctl dump-flows s3
```

These commands display installed OpenFlow rules in each switch.

---

## 🧪 Regression Testing

To verify routing consistency after reinstalling rules:

### Delete Existing Rules

```bash
sh ovs-ofctl del-flows s1
sh ovs-ofctl del-flows s2
sh ovs-ofctl del-flows s3
```

### Restart Controller and Retest

```bash
pingall
```

### Expected Result

* Connectivity remains successful
* Same static path is preserved

---

## ✅ Outcomes

* Successfully implemented static routing using SDN controller
* Installed manual OpenFlow flow rules
* Verified packet delivery between hosts
* Inspected switch flow tables
* Performed regression testing successfully

---

## 📚 Concepts Demonstrated

* Software Defined Networking (SDN)
* Separation of Control Plane and Data Plane
* OpenFlow Protocol
* Static Routing
* Flow Rule Installation
* Network Emulation using Mininet

---

##  Name and SRN

**Sachin S** - **PES2UG24CS422**

---

## 📌 Future Enhancements

* Multi-path static routing
* Dynamic route updates
* Failure recovery mechanisms
* Traffic monitoring dashboard
* QoS-based routing
