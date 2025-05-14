# Ansible Collection - republic.crypto

The Republic Crypto's Ansible Galaxy collection of roles to configure blockchain infrastructure.

NOTE: These roles currently set up non-validator nodes. Please check the requirements and
an additional configuration at the chain's documentation if the validator or other node
type is required.

## Roles in this Collection

| Name          | Role                                                                                                                 |
|---------------|----------------------------------------------------------------------------------------------------------------------|
| **Aptos**     | [republic.crypto.aptos](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/aptos)         | 
| **Avalanche** | [republic.crypto.avalanche](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/avalanche) | 
| **Berachain** | [republic.crypto.berachain](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/berachain) | 
| **Cosmos**    | [republic.crypto.cosmos](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/cosmos)       | 
| **Mina**      | [republic.crypto.mina](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/mina)           | 
| **Near**      | [republic.crypto.near](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/near)           | 
| **Polygon**   | [republic.crypto.polygon](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/polygon)     | 
| **Solana**    | [republic.crypto.solana](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/solana)       | 
| **Story**     | [republic.crypto.story](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/story)         | 
| **Sui**       | [republic.crypto.sui](https://github.com/republic-crypto/republic-crypto-collection/tree/main/roles/sui)             | 

**More coming soon!**

## Ansible Collection Usage

Install the collection using the following command:

```sh
ansible-galaxy collection install republic.crypto
```

Example setting up a CosmosHub node with the collection role:

```yaml
# playbook.yml
---
- hosts: 'all'
  gather_facts: true
  become: true

  pre_tasks:
    - name: 'Install apt packages'
      ansible.builtin.apt:
        update_cache: true
        cache_valid_time: 86400
        pkg: python3

  roles:
    - role: republic.crypto.cosmos
        cosmos_chain_name: cosmoshub
        data_dir: /mnt/data/.gaiad
```

## Concept

Ansible Roles consists of few phases (not every role contains all phase though):

- load variables
- install binaries
- init blockchain node
- set configuration
- sync chain data from public backup

## Contributing

The best way to submit feedback and report bugs is to [open a GitHub issue](https://github.com/republic-crypto/republic-crypto-collection/issues).

## Development

### Molecule Testing Framework

We have now switched all test execution to run through ephemeral VMs in AWS! This means so long as you have your AWS access keys available you can pretty well clone the repo and run tests from anywhere without any fancy setup and configuration.

#### AWS Credentials

Please contact team lead for getting your AWS molecule testing account setup.
Once you have credentials and have successfully logged in you will need to provision your own `Access Key` under your profile.

**NOTE:** Alternatives do exist to this such as using AWS credentials files and ensuring the correct target account is selected prior to executing molecule. Simply drop the commands notated with `# drop if using aws creds file`

More information on setting up your credentials file if you chose can be found (here)[https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html]

#### Execution

It's recommended to develop inside [Virtual environment](https://virtualenv.pypa.io/en/latest/). This is taken care of in the following example invocation:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ansible-galaxy install -r requirements.yml
export AWS_ACCESS_KEY_ID="..." # drop if using aws creds file
export AWS_SECRET_ACCESS_KEY="..." # drop if using aws creds file
export AWS_DEFAULT_REGION="us-east-2" # drop if using aws creds file
molecule test -s sui # replace sui with your target
```

For each role there is a `/molecule/<role>` directory with configuration files.
**Note**: Making changes to a role's molecule test file requires you to reset the cache for that that role:

```sh
molecule reset -s cosmos
```

#### Troubleshooting

It isn't uncommon to be fighting an issue which can most easily be debugged on the node where the role is running. To make this easy you can ask molecule not to run the `destroy` phase:

```shell
molecule test -s sui --destroy=never
```

Now when your molecule run fails you can easily access the console of the AWS VM. This can be done multiple ways, the easiest (for me) was:
1. Login to the AWS Web Console
2. Navigate to the EC2 portal
3. Select the `Instances` option on the left panel
4. Locate your instance and click on it
5. Click `Connect` and access via the AWS Web Console connection manager

### Build Ansible Galaxy Locally

To build the local version of the Ansible Galaxy collection:

```sh
ansible-galaxy collection build --force
```

The `republic-crypto-x.x.x.tar.gz` file will appear at the root of the project.

It can be installed for local testing by executing the following command:

```sh
ansible-galaxy collection install republic-crypto-0.x.x.tar.gz --force
```

## References

- [Republic Crypto](https://republiccrypto.com) Company page
- [Republic Crypto Collection](https://galaxy.ansible.com/republic/crypto) Ansible Galaxy page
- [Molecule](https://molecule.readthedocs.io/en/latest/index.html) Ansible roles testing framework
- [Testinfra](https://testinfra.readthedocs.io/en/latest/) unit tests in Python to test actual state of the server configured by Ansible/Molecule

## License

Ansible Collection `republic.crypto` is available under the [MIT](LICENSE) license.

## Additional Disclaimer

This disclaimer ("Disclaimer") sets forth the general guidelines, disclosures, and terms of your use of the software ("Software") provided by Republic Node Jersey Limited, a Bailiwick of Jersey company ("Company", "we", "our", "us") under the MIT License. The Software is designed for running blockchain nodes and is made available to you free of charge. By accessing, downloading, or using the Software, you acknowledge that you have read, understood, and agree to be bound by this Disclaimer.

No Warranties

The Software is provided on an "AS IS" and "AS AVAILABLE" basis. The Company expressly disclaims all warranties, whether express, implied, statutory, or otherwise, with respect to the Software, including all implied warranties of merchantability, fitness for a particular purpose, title, and non-infringement. Without limitation, we make no warranty or guarantee that the Software will meet your requirements, achieve any intended results, be compatible, or work with any other software, systems, or services, operate without interruption, or be error-free.

Limitation of Liability

To the fullest extent permitted by applicable law, in no event will the Company, its affiliates, directors, employees, agents, suppliers, or licensors be liable for (a) any indirect, incidental, special, consequential, or punitive damages, including but not limited to, loss of profits, data, use, goodwill, or other intangible losses, resulting from your access to or use of or inability to access or use the Software; (b) any conduct or content of any third party on the Software; (c) any content obtained from the Software; and (d) unauthorized access, use, or alteration of your transmissions or content, whether based on warranty, contract, tort (including negligence) or any other legal theory, whether or not we have been informed of the possibility of such damage, and even if a remedy set forth herein is found to have failed its essential purpose.

Indemnification

You agree to defend, indemnify, and hold harmless the Company and its licensee and licensors, and their employees, contractors, agents, officers, and directors, from and against any and all claims, damages, obligations, losses, liabilities, costs or debt, and expenses (including but not limited to attorney's fees), resulting from or arising out of a) your use and access of the Software, or b) a breach of these terms.

Modifications and Amendments

The Company reserves the right, at its sole discretion, to modify or replace this Disclaimer at any time. If a revision is material, we will provide at least 30 days' notice prior to any new terms taking effect. What constitutes a material change will be determined at our sole discretion.
