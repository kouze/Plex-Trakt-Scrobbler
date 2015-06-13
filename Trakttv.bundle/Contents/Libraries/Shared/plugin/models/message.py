from plugin.models.core import db

from playhouse.apsw_ext import *


class MessageType(object):
    Generic     = 0x00
    Exception   = 0x01

    # Basic messages
    Info        = 0x02
    Warning     = 0x04
    Error       = 0x08
    Critical    = 0x16

    # Services
    Trakt       = 0x32


class Message(Model):
    Type = MessageType

    class Meta:
        database = db
        db_table = 'message'

    code = IntegerField(null=True)
    type = IntegerField()

    last_seen_at = DateTimeField()

    # Tracking data
    exception_hash = CharField(null=True, unique=True, max_length=32)
    revision = IntegerField(null=True)

    version_base = CharField(max_length=12)
    version_branch = CharField(max_length=42)

    # User-friendly explanation
    summary = CharField(null=True, max_length=160)  # Short single-line summary
    description = TextField(null=True)  # Extra related details
