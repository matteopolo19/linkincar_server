# linkincar_server

export PYTHONPATH=.

## run server

twistd -n web --class=server.resource --listen=tcp:4000

twistd --class=server.resource --listen=tcp:4000