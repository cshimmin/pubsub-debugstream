Silly pubsub example
------

Simple example demonstrating proof-of-concept for pubsub as DAQ debug stream.

## Prerequisites
redis-server and its python bindings. if you're on a Mac, I suggest simply running:
```
brew install redis
pip install redis
```

## Usage

To run:

*Terminal 1*
```
redis-server
```

*Terminal 2*
```
./producer.py
```

*Terminal 3*
```
./consumer.py
```

*Terminal 4*
```
./debug_program1.py
```

*Terminal 5*
```
./debug_program2.py chase
```

Initially, you should see nothing coming from the debug programs. This is because we restict the IDs that are allowed to publish (so that subscribing to `debug_stream:*` doesn't become rediculously expensive).
Add a few people you want to listen to, for example:

*Terminal 6*
```
./debug_IDs.py --add chase jared
```

You should now see some data coming in to the debug programs!
Now if you do:

*Terminal 6*
```
./debug_IDs.py --remove chase
```
you should immediately stop seeing `chase` showing up in the debug stream. Hurray!
