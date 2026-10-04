"""What a repair gets: the shell, its run folder, backups and a log."""


class RepairFailed(Exception):
    """A step found the system not as it should be. The message is plain words."""


class Context:
    def __init__(self, paths, shell, store, run_dir, options=None, target=None):
        self.paths, self.shell, self.store, self.run_dir = paths, shell, store, run_dir
        self.options = options or {}
        self.target = target      # test hook only; repairs on the real system ignore it
        self.lines = []

    def save_backup(self, name, data):
        self.store.write_file(self.run_dir, "backup-" + name, data)

    def load_backup(self, name):
        return self.store.read_file(self.run_dir, "backup-" + name)

    def log(self, text):
        self.lines.append(text)
