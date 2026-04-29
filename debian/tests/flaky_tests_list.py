#!/usr/bin/python3

# This is a list of unit tests that currently fail for various reasons.
# This list is skipped in unit-tests-stable.py
# This list is run in unit-tests-flaky.py

flaky_test_dirs = [
    'ansible_collections/cisco/aci',                        # Test likely needs updating; lxml error message on invalid parse changed.
    'ansible_collections/cisco/dnac',                        # TypeError: TestDnacDiscoveryIntent.__init__() takes 1 positional argument but 2 were given
    'ansible_collections/community/dns',                    # [1]
    'ansible_collections/community/general',                # import broken
    'ansible_collections/community/hrobot',                 # import broken
    'ansible_collections/community/library_inventory_filtering_v1', # [1]
    'ansible_collections/ibm/qradar',                       # [0]
    'ansible_collections/junipernetworks/junos',            # test broken
    'ansible_collections/kubevirt/core',                    # missing addict
    'ansible_collections/netapp_eseries/santricity',        # [0]
    'ansible_collections/netapp/ontap',                     # missing netapp_lib
    'ansible_collections/ngine_io/cloudstack',              # [0]
    'ansible_collections/sensu/sensu_go',                   # [2]
    'ansible_collections/splunk/es',                        # assert result["changed"] is True
]

# [0] test/units/compat/mock.py from ansible-core source is not installed
#     in the binary package. Need to check why.
# [1] E   ModuleNotFoundError: No module named 'ansible_collections.community.internal_test_tools'
# [2] E   ansible_collections.sensu.sensu_go.tests.unit.plugins.modules.common.utils.AnsibleFailJson: {'msg': "argument 'pool_size' is of type <class 'NoneType'> and we were unable to convert to int: <class 'NoneType'> cannot be converted to an int", 'failed': True}
