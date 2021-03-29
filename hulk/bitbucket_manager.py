from bitbucket.bitbucket import Bitbucket


class BitbucketManager:
    """
    BitBucket client manager
    """

    __bb: Bitbucket  # BitBucket client

    # def __init__(self):

    def setup_client(self, username, password):
        """
        Setup client for Bitbucket API
        """
        self.__bb = Bitbucket(username, password)

    def list_repos(self):
        """
        List all repos of the user
        """
        success, repos = self.__bb.repository.all()
        if not success:
            raise Exception("Error listing repos")
        for repo in repos:
            print('HULK list repo: {} {}'.format(repo['name'], repo['last_updated']))
        print("HULK list total: {}".format(len(repos)))
