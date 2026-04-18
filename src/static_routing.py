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
