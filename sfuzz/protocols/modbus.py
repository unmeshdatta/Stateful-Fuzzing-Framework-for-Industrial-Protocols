"""Modbus TCP parser using scapy."""
from dataclasses import dataclass
from typing import Optional

from scapy.all import Raw, Packet, TCP, bind_layers
from scapy.packet import Packet as ScapyPacket
from scapy.fields import ShortField, ByteField


class ModbusADU(Packet):
    name = "ModbusADU"
    fields_desc = [
        ShortField("transaction_id", 0),
        ShortField("protocol_id", 0),
        ShortField("length", 0),
        ByteField("unit_id", 0),
    ]


class ModbusPDU(Packet):
    name = "ModbusPDU"
    fields_desc = [
        ByteField("function_code", 0),
        # remaining payload handled generically
    ]


bind_layers(TCP, ModbusADU, dport=502)
bind_layers(ModbusADU, ModbusPDU)


def parse_modbus(data: bytes) -> Optional[ScapyPacket]:
    """Parse raw bytes into a Modbus packet."""
    try:
        pkt = ModbusADU(data)
        return pkt
    except Exception:
        return None
