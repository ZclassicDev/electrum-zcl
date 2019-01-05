ELECTRUM_VERSION = 'Z!1.0.7' # version of the client package; = '3.1' really
PROTOCOL_VERSION = '1.1'     # protocol version requested; TODO 1.1 compat?

# The hash of the mnemonic seed must begin with this
SEED_PREFIX      = '01'      # Standard wallet
SEED_PREFIX_2FA  = '101'     # Two-factor authentication
SEED_PREFIX_SW   = '100'     # Segwit wallet


def seed_prefix(seed_type):
    if seed_type == 'standard':
        return SEED_PREFIX
    elif seed_type == 'segwit':
        return SEED_PREFIX_SW
    elif seed_type == '2fa':
        return SEED_PREFIX_2FA
