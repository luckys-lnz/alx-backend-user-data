#!/usr/bin/env python3
"""hash password method that returns bytes
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Generate a salted hash of the input password.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as bytes.
    """
    if not isinstance(password, str):
        raise TypeError('Password Must be a string')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
