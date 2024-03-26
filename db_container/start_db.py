import docker
import docker.errors


class ContainerCreate:

    def __init__(self):
        self.dclient = docker.from_env()
        self.all_volumes = [x.attrs['Name'] for x in self.dclient.volumes.list()]
        self.all_containers = []
        for name in self.dclient.containers.list(all, sparse=True):
            self.all_containers.append(name.attrs['Name'][0].strip('/'))
        self.db_container = ''

    def create_volume(self, volume_name: str):
        """
        Create a volume for container if it doesn't exist.

        Args:
            volume_name (str): Name of the volume to create

        Returns:
            container volume
        """

        if volume_name not in self.all_volumes:
            try:
                self.dclient.volumes.create(name=volume_name,
                                            driver='local')

            except docker.errors.APIError:
                print("docker api was unable to create the volume!".upper())

    def create_db(self, container_name: str, pgpass: str, volume_name: str, local_port=5455):
        """
        Create a container that initializes the database for first use.

        Args:
            volume_name (str): Name of the volume to create
            pgpass (str): Password for the postgres account
            container_name (str): Name of the container
            local_port (5455): Local port which the container attaches to. Default 5455

        Returns:
            container in running state
        """

        # Container not on system
        if container_name not in self.all_containers:

            try:
                self.db_container = self.dclient.containers.run(
                    image='postgres:16',
                    detach=True,
                    ports={5432: local_port},
                    restart_policy={
                        'Name': 'always',
                        'MaximumRetryCount': 3
                    },
                    mem_limit='9g',
                    volumes={
                        volume_name: '/var/lib/postgresql'
                    },
                    environment={
                        'POSTGRES_PASSWORD': pgpass,
                        'POSTGRES_USER': 'postgres',
                        'POSTGRES_DB': 'postgres'
                    },
                    name=container_name
                )

                return self.db_container

            except docker.errors.ContainerError:
                print("Docker exited with a non-zero status. Printing logs:")
                print(self.db_container.logs())
            except docker.errors.APIError:
                print("docker api was unable to create the container".upper())

        # Container already found on system
        else:
            # Perform different actions based on the state of the container
            self.db_container = self.dclient.containers.get(container_name)
            state = self.db_container.attrs['State']['Status']

            try:

                if state == 'running':
                    print("Container is already running!")
                    return self.db_container

                if state == 'exited':
                    self.db_container.start()
                    return self.db_container

            except docker.errors.APIError:
                print("docker was unable to start the existing container".upper())


"""
############################# MAIN #############################
"""

# This module can only be imported
if __name__ == '__main__':
    pass
