import zmq
addr = 'tcp://127.0.0.1:5555'
con = zmq.Context()
pull = con.socket(zmq.PULL)
pull.bind(addr)
while 1:
    print pull.recv()

