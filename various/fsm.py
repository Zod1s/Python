cmds = {
    "CLOSED" : lambda x: "LISTEN" if x == "APP_PASSIVE_OPEN" else "SYN_SENT" if x == "APP_ACTIVE_OPEN" else "ERROR",
    "LISTEN" : lambda x: "SYN_RCVD" if x == "RCV_SYN" else "SYN_SENT" if x == "APP_SEND" else "CLOSED" if x == "APP_CLOSE" else "ERROR",
    "SYN_RCVD" : lambda x: "FIN_WAIT_1" if x == "APP_CLOSE" else "ESTABLISHED" if x == "RCV_ACK" else "ERROR",
    "SYN_SENT" : lambda x: "SYN_RCVD" if x == "RCV_SYN" else "ESTABLISHED" if x == "RCV_SYN_ACK" else "CLOSED" if x == "APP_CLOSE" else "ERROR",
    "ESTABLISHED" : lambda x: "FIN_WAIT_1" if x == "APP_CLOSE" else "CLOSE_WAIT" if x == "RCV_FIN" else "ERROR",
    "FIN_WAIT_1" : lambda x: "CLOSING" if x == "RCV_FIN" else "TIME_WAIT" if x == "RCV_FIN_ACK" else "FIN_WAIT_2" if x == "RCV_ACK" else "ERROR",
    "CLOSING" : lambda x: "TIME_WAIT" if x == "RCV_ACK" else "ERROR",
    "FIN_WAIT_2" : lambda x: "TIME_WAIT" if x == "RCV_FIN" else "ERROR",
    "TIME_WAIT" : lambda x: "CLOSED" if x == "APP_TIMEOUT" else "ERROR",
    "CLOSE_WAIT" : lambda x: "LAST_ACK" if x == "APP_CLOSE" else "ERROR",
    "LAST_ACK" : lambda x: "CLOSED" if x == "RCV_ACK" else "ERROR"
}

def traverse_TCP_states(events):
    state = "CLOSED" # initial state, always
    for event in events:
        state = cmds[state](event)
        if (state == "ERROR"):
            return "ERROR"
    return state