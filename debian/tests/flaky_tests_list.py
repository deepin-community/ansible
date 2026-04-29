#!/usr/bin/python3

# This is a list of unit tests that currently fail for various reasons.
# This list is skipped in unit-tests-stable.py
# This list is run in unit-tests-flaky.py

flaky_test_dirs = [
    'ansible_collections/amazon/aws',
    'ansible_collections/ansible/netcommon',
    'ansible_collections/ansible/utils',                    # tests matches broken; waiting for upstream fix
    'ansible_collections/cisco/aci',                        # Test likely needs updating; lxml error message on invalid parse changed.
    'ansible_collections/cisco/dnac',                        # TypeError: TestDnacDiscoveryIntent.__init__() takes 1 positional argument but 2 were given
    'ansible_collections/community/aws',
    'ansible_collections/community/ciscosmb',
    'ansible_collections/community/digitalocean',
    'ansible_collections/community/dns',                    # [1]
    'ansible_collections/community/docker',
    'ansible_collections/community/general',                # import broken
    'ansible_collections/community/hrobot',                 # import broken
    'ansible_collections/community/library_inventory_filtering_v1', # [1]
    'ansible_collections/community/proxmox',
    'ansible_collections/community/routeros',
    'ansible_collections/community/sap_libs',
    'ansible_collections/dellemc/enterprise_sonic',
    'ansible_collections/dellemc/openmanage',
    'ansible_collections/ibm/storage_virtualize',
    'ansible_collections/infoblox/nios_modules',            # All tests failing with "RuntimeError: Patch is already started"
    'ansible_collections/junipernetworks/junos',            # test broken
    'ansible_collections/kubernetes/core',
    'ansible_collections/netapp/cloudmanager',
    'ansible_collections/netapp_eseries/santricity',        # [0]
    'ansible_collections/netapp/ontap',                     # missing netapp_lib
    'ansible_collections/netapp/storagegrid',
    'ansible_collections/ngine_io/cloudstack',              # [0]
    'ansible_collections/splunk/es',                        # assert result["changed"] is True
    'ansible_collections/vmware/vmware',                    # depends on libs not packaged in Debian
    'ansible_collections/vultr/cloud',
]

# [0] test/units/compat/mock.py from ansible-core source is not installed
#     in the binary package. Need to check why.
# [1] E   ModuleNotFoundError: No module named 'ansible_collections.community.internal_test_tools'
