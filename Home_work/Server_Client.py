#!/usr/bin/python


class Server(object):

    _MAX_CLIENT_NUM = 200

    def __init__(self):
        self._clients = []

    @property
    def clients(self):
        return self._clients

    def register(self, client):
        assert isinstance(client, Client), "Unexpected object type"
        if len(self._clients) > self._MAX_CLIENT_NUM:
            print("Unable to register client. Max client num {} exceeded.".format(self._MAX_CLIENT_NUM))
        if client not in self._clients:
            self._clients.append(client)

    def unregister(self, client):
        if client in self._clients:
            self._clients.remove(client)

    def reboot(self, client):
        if client in self._clients:
            client.reboot()

    def reboot_all(self):
        for client in self._clients:
            self.reboot(client)


class NetworkSettings(object):

    # _fields = ['ip_address', 'mask', 'gateway', 'os_name', 'drive_space']
    _fields = ['ip_address', 'mask', 'gateway']

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Unexpected number of arguments.")

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

    def reboot(self):
        print("Client {} has been rebooted".format(self.ip_address))


class Client(object):
    # def __init__(self, cls):
    #     self._cls = cls
    #     self._instances = dict()
    #
    # def __call__(self, *args, **kwargs):
    #     return self._instances.setdefault((args, tuple(kwargs.items())), self._cls(*args, **kwargs))

    _unique_clients = {}

    def __new__(cls, *args, **kwargs):
        return cls._unique_clients.setdefault((args, tuple(kwargs.items())), super().__new__(cls))

    def get_network_settings(self):
        return self._network_settings.ip_address, self._network_settings.mask, self._network_settings.gateway

    def set_network_settings(self, *args):
        self._network_settings = NetworkSettings(*args)


if __name__ == '__main__':
    clients_details = [
        ('Windows', '500GB', '192.168.1.35', '0.0.0.0', '192.168.1.255'),
        ('Mac OSX', '750GB', '172.22.171.96', '0.0.0.0', '172.22.171.255'),
        ('Linux', '250GB', '172.22.171.96', '0.0.0.0', '172.22.171.255'),
    ]
    clients = []
    for client in clients_details:
        obj = Client(*client[:2])
        obj.set_network_settings(*client[2:])
        clients.append(obj)

    for f in clients:
        print("id = {}".format(id(f)))
        print("Network settings: {}".format(", ".format(f.get_network_settings())))
