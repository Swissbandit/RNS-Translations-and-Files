# TODO: 


# I2p Interface:

Neater shutdown of the event loop and better error handling is needed. 
Sometimes errors occur in I2P that leave tunnel setup hanging indefinitely, 
and right now we have no way of catching it. 
Sometimes the server and client tasks are also not cancelled on shutdown, 
which leads to errors dumped to the console. This should also be remedied.

