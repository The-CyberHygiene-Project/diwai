from repairkit.records import RunStore
from repairkit.shell import Shell
from repairkit.context import Context, RepairFailed


def store(lib_paths):
    return RunStore(lib_paths, Shell(sudo_prefix=[]))


def test_new_run_folder_is_private_and_recorded(lib_paths):
    s = store(lib_paths)
    run = s.new_run("demo-fix")
    s.save(run, {"repair": "demo-fix", "state": "started"})
    assert oct(run.stat().st_mode & 0o777) == "0o700"
    assert s.load(run)["state"] == "started"
    assert s.runs() == [run]


def test_lock_is_exclusive(lib_paths):
    s = store(lib_paths)
    assert s.lock() is True
    assert s.lock() == "held"
    s.unlock()
    assert s.lock() is True


def test_backup_round_trip_keeps_every_byte(lib_paths):
    s = store(lib_paths)
    run = s.new_run("demo-fix")
    data = bytes(range(256))
    ctx = Context(lib_paths, s.shell, s, run)
    ctx.save_backup("blob", data)
    assert ctx.load_backup("blob") == data


def test_lock_folder_is_not_listed_as_a_run(lib_paths):
    s = store(lib_paths)
    s.lock()
    assert s.runs() == []


def test_repair_failed_carries_plain_reason():
    assert str(RepairFailed("demo.txt is not good")) == "demo.txt is not good"
