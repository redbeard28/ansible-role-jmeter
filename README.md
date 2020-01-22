ANSIBLE-ROLE-JMETER
===================

Ansible role install Jmeter.


## Howto use this role?
This role need to be include in a playbook. 

Call this **Galaxy** role  like this:

````bash
ansible-galaxy install -r requirements.yml 
````

Inside requirements.yml
````yaml
# from GitHub, overriding the name and specifying a specific tag
- src: git+https://github.com/redbeard28/ansible-role-jmeter.git
  version: master
  name: jmeter
````

or
````yaml
# from GitHub, overriding the name and specifying a specific tag
- src: redbeard28.jmeter
````

More info => [Ansible Docs](https://docs.ansible.com/ansible-container/roles/access.html)

## Requirements

 * Ansible 2.9+


Role Variables
--------------

```yaml
---
# Put role variables
```

Dependencies
------------

  * redbeard28.bootstrap
  * redbeard28.basetools
  * redbeard28.openjdk
  * redbeard28.ant

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: redbeard28.jmeter, tags: mytags }


Molecule testing framework
--------------------------

You can use molecule to test this role.
```bash
namespace=redbeard28 image=debian tag="buster-basetools" molecule converge 
namespace=redbeard28 image=debian tag="buster-basetools" molecule verify 
```

Author Information
------------------

Jeremie CUADRADO[¹](mailto:info@redbeard-consulting.fr) from Redbeard-Consulting
