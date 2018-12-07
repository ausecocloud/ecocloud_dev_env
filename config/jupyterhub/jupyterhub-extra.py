import yaml

from dockerspawner import DockerSpawner


class MyDockerSpawner(DockerSpawner):

    async def start(self):
        profile_name = self.user_options.get('profile', None)
        if profile_name:
            self.user_options['image'] = profile_name
        # still here? that means we have a profile applied
        self.log.info(self.user_options)
        return await super().start()


c.JupyterHub.spawner_class = MyDockerSpawner


def image_whitelist(spawner):
    with open('/etc/jupyterhub/config/profiles.yaml', 'r') as fp:
        profiles = yaml.load(fp)
    return {
        p['display_name']: p['kubespawner_override']['image_spec']
        for p in profiles['profile_list']
    }

c.DockerSpawner.image_whitelist = image_whitelist
# delete container ... so that a new container get's created if we want to change image
c.DockerSpawner.remove = True
