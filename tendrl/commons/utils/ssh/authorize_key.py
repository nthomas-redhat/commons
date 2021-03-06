from tendrl.commons.utils import ansible_module_runner
from tendrl.commons.utils import log_utils as logger

ANSIBLE_MODULE_PATH = "system/authorized_key.py"


class AuthorizeKey(object):
    """AuthorizeKey class is used to copy the given ssh-key

    to particular user. A default user is root.
    Here ssh_key is mandatory and user is optional.
    At the time of initalize it will take user and ssh-key as
    parameter.

    input:
        ssh_key
        user(optional)

    output:
        True/False, None/error
    """
    def __init__(self, ssh_key, user="root"):
        self.attributes = {}
        self.attributes["user"] = user
        self.attributes["key"] = ssh_key

    def run(self):
        """This function is used to copy the given authorize ssh-key

        output:
            True/False, error
        """
        try:
            runner = ansible_module_runner.AnsibleRunner(
                ANSIBLE_MODULE_PATH,
                **self.attributes
            )
        except ansible_module_runner.AnsibleModuleNotFound:
            # Backward compat ansible<=2.2
            runner = ansible_module_runner.AnsibleRunner(
                "core/" + ANSIBLE_MODULE_PATH,
                **self.attributes
            )
        try:
            result, err = runner.run()
            if 'failed' in result:
                err = result
            else:
                logger.log(
                    "debug",
                    NS.publisher_id,
                    {"message": "Authorize key: %s" % result}
                )
        except ansible_module_runner.AnsibleExecutableGenerationFailed as e:
            logger.log(
                "debug",
                NS.publisher_id,
                {"message": "Copying authorize key failed %s. "
                 "Error: %s" % (self.attributes["_raw_params"],
                                str(e.message))
                 }
            )
            err = str(e.message)
        if err != "":
            logger.log(
                "debug",
                NS.publisher_id,
                {"message": "Unable to copy authorize key "
                            ".err:%s" % err}
            )
            return False, err
        else:
            return True, err
