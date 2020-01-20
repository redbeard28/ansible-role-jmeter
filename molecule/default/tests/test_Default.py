import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('pkg', [
    'python3'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.fixture
def get_ansiblevars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])
    print(ansible_vars)
    return ansible_vars


# Verify if terraform_dir exist
def test_terraform_dir_path(host, get_ansiblevars):
    jmeter_root_path = get_ansiblevars['jmeter_root_path']
    jmeter_path =  "%s/apache-jmeter-%s" % (jmeter_root_path, get_ansiblevars['jmeter_version'])
    jmeter_modules_installer_file = "%s/bin/install_jmeter_modules.sh" % (jmeter_path)
    file = host.file(jmeter_modules_installer_file)

    assert file.user == 'root'
    assert file.group == 'root'