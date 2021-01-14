# Requires the whirlpool module, which can be downloaded with pip install whirlpool

import whirlpool

# NOTE: The object for whirlpool hash functions must be in bytes or binary,
# hence the "b" before "Hello world"

message = b"Hello world"

pooler = whirlpool.new(message)

digest = pooler.hexdigest()

print(digest)
