# How to limit resourses by PID with cgoups

## What you need to do before

- have linux
- have root access or `sudo`.
- cgroups v2 (as indicated by the `grep cgroup /proc/filesystems` you must see `nodev   cgroup2`).
- PID of the running process (for example go process, `PID=12345`).

### 1. See if available controllers

Run:

```bash
cat /sys/fs/cgroup/cgroup.controllers
```

You might see a list like `cpu memory io ...`  
so this controllers are available.

### 2. Enable needed controllers in the Root cgroup

Before you can use a controller in a child cgroup, you need to enable it in the parent. The root cgroup is `/sys/fs/cgroup`. To enable CPU and memory controllers, run:

```bash
echo "+cpu +memory" | sudo tee /sys/fs/cgroup/cgroup.subtree_control
```

If you get a "Device or resource busy" error, it may mean your system’s root cgroup already contains processes.

Check if enabled:

```bash
cat /sys/fs/cgroup/cgroup.subtree_control
```

It should show `cpu memory` if successful.

### 3. Create a new cgroup

Create a directory for your cgroup. For example:

```bash
sudo mkdir /sys/fs/cgroup/mygolanggroup
```

This directory represents a new cgroup. By default, it inherits the controllers enabled by the parent.

### 4. Configure resource limits for your cgropup

**Memory Limit:**
1mb max

```bash
echo $((1024*1024)) | sudo tee /sys/fs/cgroup/mygolanggroup/memory.max
```

- `memory.max` specifies the maximum memory usage in bytes.
- If you want no limit, you could write `max` instead of a number.

**CPU Limit:**
Cgroups v2 uses `cpu.max` to limit CPU. The format is `max quota_period_us`.  

- give the cgroup a maximum of half a CPU core worth of time, you could use:

  ```bash
  echo "50000 100000" | sudo tee /sys/fs/cgroup/mygolanggroup/cpu.max
  ```

  Here:
  - `100000` microseconds (100ms) is the default period.
  - `50000` microseconds is the quota, i.e., half of a single CPU core in that 100ms window.
  
  If you wanted to fully utilize one CPU core, you’d use `100000 100000`.
  
  If you wanted no limit (use as much CPU as available), you can write `max 100000`.

### 5. Add any  process into your Cgroup

process (PID=12345) is currently in the root (or some default) cgroup. To apply the limits, you must move it into `mygolanggroup`:

```bash
echo 12345 | sudo tee /sys/fs/cgroup/mygolanggroup/cgroup.procs
```

and immediately all limits will be applyed

### 6. Verify

lets check if your limits witten

```bash
cat /sys/fs/cgroup/mygolanggroup/memory.max
cat /sys/fs/cgroup/mygolanggroup/cpu.max
```

and you can also verify the processes in cgroup:

```bash
cat /sys/fs/cgroup/mygolanggroup/cgroup.procs
```

you can see pid of your service that you added previously

### 7. Check

Run tools `top` , `htop` to see if the CPU usage is limited as expected.  
If the process takes more of the memory limit, it will be killed by the OOM (Out Of Memory) killer.

### 8. Change limits if needed

You can change the limits at any time:

```bash
echo "250000 100000" | sudo tee /sys/fs/cgroup/mygolanggroup/cpu.max
echo $((16*1024)) | sudo tee /sys/fs/cgroup/mygolanggroup/memory.max
```

The changes take effect immediately and see that go application will be shut down because of memory exeed.

### 9. Cleaning Up

When done, move the process out or terminate it, then remove the cgroup directory:

```bash
sudo rmdir /sys/fs/cgroup/mygolanggroup
```
