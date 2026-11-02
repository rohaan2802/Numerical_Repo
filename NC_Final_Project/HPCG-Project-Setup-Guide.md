# HPCG Project – Setup and Work Plan

Steps for building and running the HPCG (High Performance Conjugate Gradient) benchmark and for planning the kernel optimisation project.

## 1. Environment (WSL on Windows)

Install Ubuntu under WSL, then install the build tools:

```bash
sudo apt update
sudo apt install -y build-essential cmake git
```

## 2. Get and build HPCG

```bash
git clone https://github.com/hpcg-benchmark/hpcg.git
cd hpcg
mkdir build && cd build
cmake ..
make -j4
```

## 3. Run the benchmark

```bash
cp ../bin/hpcg.dat .
./xhpcg
```

`hpcg.dat` sets the problem size and run time. When the run finishes, the results are written to a file named `HPCG-Benchmark_*.txt` in the same folder.

```bash
ls HPCG-Benchmark_*.txt
cat HPCG-Benchmark_*.txt
```

## 4. Baseline results

Timings from the first (unoptimised) run, used as the baseline:

| Kernel | Time (s) |
|---|---|
| SpMV (sparse matrix–vector product) | 24.69 |
| MG (multigrid preconditioner, SymGS) | 128.49 |
| DDOT (dot product) | 2.21 |
| WAXPBY (vector update) | 2.44 |

The multigrid step, whose main cost is the symmetric Gauss–Seidel smoother, takes most of the time, followed by SpMV. These are the best targets for optimisation.

## 5. Where the kernels are

| Kernel | Source file |
|---|---|
| SpMV | `src/ComputeSPMV_ref.cpp` |
| Symmetric Gauss–Seidel (inside MG) | `src/ComputeSYMGS_ref.cpp` |

## 6. Project phases

1. **Baseline** – build HPCG, run it and record the timings above.
2. **Choose a kernel and a paper** – pick SpMV or SymGS and a research paper on optimising it.
3. **Understand the kernel** – read the reference code, the data structures (sparse matrix storage) and the memory-access pattern.
4. **Design** – plan the optimisation (for example OpenMP threading, better data layout, loop changes, multicolouring for SymGS).
5. **Implement and benchmark** – change the kernel, check the results are still correct and compare the timings with the baseline.
6. **Report and slides** – write up the method, results and speed-up, and prepare the presentation.
