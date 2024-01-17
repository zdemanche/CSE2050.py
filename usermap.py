import random
import string

class PasswordError(Exception):
    """Custom error to be used in UserMap when wrong password is given for a user."""
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return f"PasswordError: {repr(self.message)}"

class UserRecord:
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.password_hash = self._hash_password(self.salt, password)

    def _hash_password(self, salt, password):
        salted_password = salt + password
        return hash(salted_password)

class UserMap:
    def __init__(self, initial_size=8):
        self._size = initial_size
        self._data = [None] * self._size
        self._count = 0
        self._max_load_factor = 0.75

    def __len__(self):
        return self._count

    def _double(self):
        self._size *= 2
        old_data = self._data
        self._data = [None] * self._size
        self._count = 0

        for record in old_data:
            if record is not None:
                self._add_user(record.username, record.password)

    def _add_user(self, username, password):
        if (self._count / self._size) >= self._max_load_factor:
            self._double()

        index = self._get_index(username)

        while self._data[index] is not None:
            if self._data[index].username == username:
                raise RuntimeError("Username already registered.")
            index = (index + 1) % self._size

        self._data[index] = UserRecord(username, password)
        self._count += 1

    def add_user(self, username, password):
        if username in self:
            raise RuntimeError("Username already registered.")
        self._add_user(username, password)

    def update_password(self, username, current_password, new_password):
        if username not in self:
            raise KeyError(username)

        index = self._get_index(username)
        record = self._data[index]

        while record is not None:
            if record.username == username:
                current_password_hash = record._hash_password(record.salt, current_password)
                if current_password_hash == record.password_hash:
                    record.password_hash = record._hash_password(record.salt, new_password)
                else:
                    raise PasswordError("Incorrect password.")
            index = (index + 1) % self._size
            record = self._data[index]

    def _get_index(self, username):
        index = hash(username) % self._size

        while self._data[index] is not None:
            if self._data[index].username == username:
                return index
            index = (index + 1) % self._size

        return index

    def __contains__(self, username):
        return username in [record.username for record in self._data if record is not None]

    def __getitem__(self, username):
        index = self._get_index(username)
        record = self._data[index]

        if record is not None and record.username == username:
            return record
        raise KeyError(username)
