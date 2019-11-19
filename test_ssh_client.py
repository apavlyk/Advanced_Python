#!/usr/bin/python

import unittest
from unittest.mock import patch
from ssh_client import ssh_client


class TestSSHClient(unittest.TestCase):

    def test_call(self):
        cmd1 = 'ls'
        cmd2 = 'notls'
        cmd3 = ''

        with patch("ssh_client.call") as mocked_ssh_call:
            ssh_call = ssh_client.call(cmd1)
            mocked_ssh_call.assert_called_with(cmd1)
            self.assertEqual(ssh_call, 0)

            ssh_call = ssh_client.call(cmd2)
            mocked_ssh_call.assert_called_with(cmd2)
            self.assertEqual(ssh_call, 1)

            with self.assertRaises(RuntimeError):
                ssh_call = ssh_client.call(cmd3)
                mocked_ssh_call.assert_called_with(cmd3)


if __name__ == '__main__':
    unittest.main()
