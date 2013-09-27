An interactive shell for XenAPI. Requires ipython.

Usage:

```
./run <hostname> [<username> [<password>]]
```

Example:

```
$ ./run myxenserver

You now have the following objects to play with:
session - an API session object for myxenserver.
api - an API dispatcher for myxenserver (just an alias for session.xenapi).

In [1]: hosts = api.host.get_all()

In [2]: api.host.get_address(hosts[0])
Out[2]: '192.168.1.123'

In [3]: api.host.get_PIFs(hosts[0])
Out[3]:
['OpaqueRef:d6ffc2d8-de83-5958-abe2-6e3c4239708b',
 'OpaqueRef:7fe8a78a-5533-c24e-1dcd-fe7ad87add2d',
 'OpaqueRef:f44b4c44-155a-1bc6-27be-63ed3e45e52b',
 'OpaqueRef:f38a7a96-32de-3bac-12ac-d099c7ddd715']

In [4]: api.host.set_name_label(hosts[0], "foo")
Out[4]: ''
```
