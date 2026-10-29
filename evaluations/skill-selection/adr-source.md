# Queue decision: discussion notes

The fictional service exports project reports. One shared worker queue lets a
large project delay smaller projects. The team has chosen a per-project queue
for the reversible prototype. Production scheduling limits remain undecided.

The viable alternatives considered are a shared FIFO queue (least setup,
project contention remains), per-project queues (independent scheduling,
additional coordination), and a priority queue (one queue, priorities require
an agreed policy). A local harness can exercise two concurrent projects, and
the user has authorised the prototype and local tests. Load tests have not run.
The team will choose production limits after measuring the representative load
case. Revisit the prototype decision if the expected workload cannot meet the
agreed latency budget; no numerical budget has yet been agreed. Publication,
deployment and external account changes are outside the requested work.
