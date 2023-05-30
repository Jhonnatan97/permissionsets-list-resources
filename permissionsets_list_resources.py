import boto3

boto3.setup_default_session (profile_name='your-profile', region_name='region_name')

def check_permission(inline_policy, permission_type):
    # Verificar se a permissão especificada está presente no documento da política inline
    if permission_type.lower() in inline_policy.lower():
        return True
    else:
        return False

def list_permission_sets_policies(permission_type):
    roles = []
    sso_admin_client = boto3.client('sso-admin')
    instance_id = 'arn:aws:sso:::instance/<your-instance>'

    # Obter lista de todos os permission sets
    response = sso_admin_client.list_permission_sets(InstanceArn=instance_id)
    roles.extend (response['PermissionSets'])
    while 'NextToken' in response.keys ():
        response = sso_admin_client.list_permission_sets (InstanceArn=instance_id, NextToken=response['NextToken'])
        roles.extend (response['PermissionSets'])

    for permission_set_arn in roles:
        response = sso_admin_client.list_managed_policies_in_permission_set (
            InstanceArn=instance_id,
            PermissionSetArn=permission_set_arn
        )['AttachedManagedPolicies']
        name_policy = response[0]['Name']
        arn_police = response[0]['Arn'] if response else None
        describe_permissionset = sso_admin_client.describe_permission_set(
            InstanceArn=instance_id,
            PermissionSetArn=permission_set_arn
        )['PermissionSet']
        permissionset_name = describe_permissionset['Name']
        print("Name PermissionSet:", permissionset_name, '-', 'Police AWS:',name_policy, 'Arn:', arn_police)

        response = sso_admin_client.get_inline_policy_for_permission_set(
            InstanceArn=instance_id,
            PermissionSetArn=permission_set_arn
        )

        if 'InlinePolicy' in response:
            inline_policy = response['InlinePolicy']
            print(inline_policy)

            # Verificar se a permissão especificada está presente na política inline
            if check_permission(inline_policy, permission_type):
                print(f"A permissão {permission_type} está presente na política inline.")
            else:
                print(f"A permissão {permission_type} não está presente na política inline.")
        else:
            print("Nenhuma política inline encontrada.")

        print()


# Especificar o tipo de permissão desejado (exemplo: "iam", "secrets manager", "dynamodb", etc.)
permission_type = "cloudtrail" #example
list_permission_sets_policies(permission_type)
