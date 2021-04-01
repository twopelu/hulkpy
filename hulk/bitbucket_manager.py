from bitbucket.bitbucket import Bitbucket

# TODO rename module file to bitbucket and be careful with namespace clashes


class BitbucketManager:
    """
    BitBucket client manager
    """

    def __init__(self, username, password):
        """
        Setup client for Bitbucket API
        """
        self.__username = username
        self.__bb = Bitbucket(username, password)

    def list_repos(self):
        """
        List all repos of the user
        """
        print("HULK BITBUCKET - list repos of the user", self.__username)
        success, repos = self.__bb.repository.all()
        if not success:
            raise Exception("Error in list repos")
        for repo in repos:
            print('HULK list repo: {} {}'.format(repo['name'], repo['last_updated']))
        print("HULK list total: {}".format(len(repos)))
