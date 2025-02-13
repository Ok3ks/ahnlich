# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: shared/info.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto

from ... import server_types as __server_types__


@dataclass(eq=False, repr=False)
class ServerInfo(betterproto.Message):
    address: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)
    type: "__server_types__.ServerType" = betterproto.enum_field(3)
    limit: int = betterproto.uint32_field(4)
    remaining: int = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class StoreUpsert(betterproto.Message):
    inserted: int = betterproto.uint32_field(1)
    updated: int = betterproto.uint32_field(2)
