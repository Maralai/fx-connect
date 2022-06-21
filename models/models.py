# -*- coding: utf-8 -*-

from odoo import api, fields, models


class reader(models.Model):
    _name = 'rfid.reader'
    _description = 'RFID Reader'

    name = fields.Char(string="Reader Name")
    alias = fields.Char(string="Reader Alias")
    mac_address = fields.Char(string="MAC Address")

    tag_reads = fields.One2many(
        comodel_name="rfid.reads.tag",
        inverse_name="reader"
    )

    heartbeat_reads = fields.One2many(
        comodel_name="rfid.reads.heartbeat",
        inverse_name="reader"
    )

    
class tag_read(models.Model):
    _name = 'rfid.reads.tag'
    _description = "RFID Tag Reads"

    
    name = fields.Char()

    reader = fields.Many2one(
        string="Reader",
        comodel_name="rfid.reader",
        ondelete="set null"
    )

    reader_alias = fields.Char(related='reader.alias', string="Reader Alias")

    epc = fields.Text(
        string="Electronic Product Code",
        help="""The Tag Electronic Product Code (EPC) Data field"""
        )
    
    pc = fields.Text(
        string="Protocol Control",
        help="""Protocol Control (PC) Bits"""
    )

    antennaPort = fields.Integer(
        string="Antenna",
        help="""Antenna ID on which Tag is read."""
    )

    peakRssi = fields.Integer(
        string="Peak RSSI",
        help="""Peak Received Signal Strength Indicator (RSSI)"""
    )

    seenCount = fields.Integer(
        string="Seen Count",
        help="""The number of times the Tag is read (in-case of periodic reporting)."""
    )

    timeStamp = fields.Datetime(
        string="Time Stamp",
        help="""Timestamp when Tag is seen."""
    )

    phase = fields.Float(
        string="Phase",
        help="""Phase information reported by the reader when the tag is seen."""
    )

    channelIndex = fields.Integer(
        string="Channel Index",
        help="""Index of the first channel when the tag is seen."""
    )


class heartbeat_read(models.Model):
    _name = 'rfid.reads.heartbeat'
    _description = "RFID Heartbeat"

    reader = fields.Many2one(
        string="Reader",
        comodel_name="rfid.reader",
        ondelete="set null"
    )

    timeStamp = fields.Datetime(
        string="Time Stamp",
        help="""Timestamp when Tag is seen."""
    )
