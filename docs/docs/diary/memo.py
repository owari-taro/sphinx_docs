>>> res=client.describe_network_acls(Filters=[{"Name":"association.subnet-id","Values":["subnet-090111991e7ef425e"]}])
>>> res
{'NetworkAcls': [{'Associations': [{'NetworkAclAssociationId': 'aclassoc-0925cf15a0f90598e', 'NetworkAclId': 'acl-0b3871da6b071f927', 'SubnetId': 'subnet-090111991e7ef425e'}], 'Entries': [{'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}], 'IsDefault': True, 'NetworkAclId': 'acl-0b3871da6b071f927', 'Tags': [], 'VpcId': 'vpc-05c3b9ae3418b01a8', 'OwnerId': '905418223580'}], 'ResponseMetadata': {'RequestId': '8916d26f-f5c3-465d-8062-a5761060a784', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '8916d26f-f5c3-465d-8062-a5761060a784', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '2034', 'date': 'Sun, 26 May 2024 14:55:37 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
>>> res["Associations"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Associations'
>>> res["Association"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Association'
>>> res.keys()
dict_keys(['NetworkAcls', 'ResponseMetadata'])
>>> res["NetworkAcls"]
[{'Associations': [{'NetworkAclAssociationId': 'aclassoc-0925cf15a0f90598e', 'NetworkAclId': 'acl-0b3871da6b071f927', 'SubnetId': 'subnet-090111991e7ef425e'}], 'Entries': [{'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}], 'IsDefault': True, 'NetworkAclId': 'acl-0b3871da6b071f927', 'Tags': [], 'VpcId': 'vpc-05c3b9ae3418b01a8', 'OwnerId': '905418223580'}]
>>> len(res["NetworkAcls"])
1
>>> res["NetworkAcls"]
[{'Associations': [{'NetworkAclAssociationId': 'aclassoc-0925cf15a0f90598e', 'NetworkAclId': 'acl-0b3871da6b071f927', 'SubnetId': 'subnet-090111991e7ef425e'}], 'Entries': [{'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}], 'IsDefault': True, 'NetworkAclId': 'acl-0b3871da6b071f927', 'Tags': [], 'VpcId': 'vpc-05c3b9ae3418b01a8', 'OwnerId': '905418223580'}]