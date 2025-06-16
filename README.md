# Stateful Fuzzing Framework for Industrial Protocols

This repository contains a lightweight Python framework aimed at fuzzing
industrial protocols using a stateful approach. The design is modular so that
protocol parsers, state machines and interaction logic can be extended easily.

## Features

- Parsers for common OT protocols such as Modbus, DNP3, EtherNet/IP and OPC UA
  (currently Modbus parser implemented using **scapy**).
- Representation of protocol state machines using **networkx**.
- Simple mutation-based test case generator.
- Pluggable target interaction engine using sockets.
- Naïve anomaly detection and JSON reporting utilities.

## Usage Example

```python
from sfuzz import protocols, fuzzer

# parse sample packet
pkt = protocols.parse_modbus(b"\x00\x01\x00\x00\x00\x06\x11\x03\x00\x6B\x00\x03")
print(pkt.summary())

# build a trivial state machine
sm = fuzzer.StateMachine()
sm.add_state("start", start=True)
sm.add_state("read")
sm.add_transition("start", "read", "read_holding_registers")

# generate a test case
gen = fuzzer.TestCaseGenerator()
mutated = gen.mutate(b"\x01\x03\x00\x6B\x00\x03")
print(mutated)
```

This example shows how to parse a Modbus packet and build a simple state
machine for fuzzing.
