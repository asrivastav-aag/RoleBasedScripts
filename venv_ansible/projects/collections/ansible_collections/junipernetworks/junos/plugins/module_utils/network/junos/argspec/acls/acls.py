#
# _*_ coding: utf_8 _*_
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl_3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the junos_acls module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class AclsArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_acls module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "afi": {
                    "required": True,
                    "choices": ["ipv4", "ipv6"],
                    "type": "str",
                },
                "acls": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "name": {"required": True, "type": "str"},
                        "aces": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"},
                                "source": {
                                    "type": "dict",
                                    "options": {
                                        "address": {"type": "raw"},
                                        "prefix_list": {
                                            "elements": "dict",
                                            "type": "list",
                                            "options": {
                                                "name": {"type": "str"},
                                            },
                                        },
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int",
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "destination": {
                                    "type": "dict",
                                    "options": {
                                        "address": {"type": "raw"},
                                        "prefix_list": {
                                            "elements": "dict",
                                            "type": "list",
                                            "options": {
                                                "name": {"type": "str"},
                                            },
                                        },
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int",
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "protocol": {"type": "str"},
                                "protocol_options": {
                                    "type": "dict",
                                    "options": {
                                        "icmp": {
                                            "type": "dict",
                                            "options": {
                                                "dod_host_prohibited": {
                                                    "type": "bool",
                                                },
                                                "dod_net_prohibited": {
                                                    "type": "bool",
                                                },
                                                "echo": {"type": "bool"},
                                                "echo_reply": {"type": "bool"},
                                                "host_tos_unreachable": {
                                                    "type": "bool",
                                                },
                                                "host_redirect": {
                                                    "type": "bool",
                                                },
                                                "host_tos_redirect": {
                                                    "type": "bool",
                                                },
                                                "host_unknown": {
                                                    "type": "bool",
                                                },
                                                "host_unreachable": {
                                                    "type": "bool",
                                                },
                                                "net_redirect": {
                                                    "type": "bool",
                                                },
                                                "net_tos_redirect": {
                                                    "type": "bool",
                                                },
                                                "network_unknown": {
                                                    "type": "bool",
                                                },
                                                "port_unreachable": {
                                                    "type": "bool",
                                                },
                                                "protocol_unreachable": {
                                                    "type": "bool",
                                                },
                                                "reassembly_timeout": {
                                                    "type": "bool",
                                                },
                                                "redirect": {"type": "bool"},
                                                "router_advertisement": {
                                                    "type": "bool",
                                                },
                                                "router_solicitation": {
                                                    "type": "bool",
                                                },
                                                "source_route_failed": {
                                                    "type": "bool",
                                                },
                                                "time_exceeded": {
                                                    "type": "bool",
                                                },
                                                "ttl_exceeded": {
                                                    "type": "bool",
                                                },
                                            },
                                        },
                                    },
                                },
                                "grant": {
                                    "type": "str",
                                    "choices": ["permit", "deny"],
                                },
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
            "type": "str",
        },
    }


# pylint: disable=C0301
