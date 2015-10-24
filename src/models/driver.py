import rethinkdb as r
from tornado import gen
from tornado import ioloop

# import classes within the same directory
from target import Target

DB = "phishmonger"

r.set_loop_type("tornado")
connection = r.connect(host='localhost', port=28015)

@gen.engine
def init():
    conn = yield connection
    print "Connecting"
    try:
        print "Creating DB"
        yield r.db_create(DB).run(conn)
    except:
        print "database already exists"

    print "Initializing tables"
    conn.use(DB)
    Target().init(conn)


# ioloop.IOLoop().instance().add_callback(init)
