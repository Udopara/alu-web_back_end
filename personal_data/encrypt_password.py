#!/usr/bin/env python3
""" Encrypt password module using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Return a salted, hashed password as a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate that provided password matches hashed password
    """
    if hashed_password is None or password is None:
        return False
    if not isinstance(hashed_password, bytes) or not isinstance(password, str):
        return False
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
