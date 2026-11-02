# Bit Shifting

Bit shifting moves every bit of a binary number left or right by a fixed number of positions. For unsigned integers it is the same as multiplying or dividing by a power of 2, which is why it is used for fast arithmetic, bit masks and packing data.

## 1. Left shift (`<<`)

- Every bit moves `k` positions to the left.
- The empty positions on the right are filled with `0`.
- For an unsigned number: `x << k = x × 2^k`

**Example 1**

```text
x      = 00101101   (45)
x << 2 = 10110100   (180)
```

45 × 2² = 45 × 4 = 180.

**Example 2**

```text
5      = 00000101
5 << 1 = 00001010   (10)
```

## 2. Right shift (`>>`)

There are two kinds of right shift:

| Kind | Fills the left side with | Usually used for |
|---|---|---|
| Logical | `0` | unsigned numbers |
| Arithmetic | the sign bit | signed (two's complement) numbers |

For an unsigned number: `x >> k = floor(x / 2^k)`

**Example 1**

```text
x      = 00101101   (45)
x >> 2 = 00001011   (11)
```

floor(45 / 4) = 11.

**Example 2**

```text
128      = 10000000
128 >> 3 = 00010000   (16)
```

128 / 8 = 16.

## 3. Points to remember

### Bits can be lost

A left shift drops bits off the left end and a right shift drops bits off the right end.

```text
11110000 << 2 = 11000000   (the two leftmost 1s are lost)
```

### Signed numbers and right shift

With an arithmetic right shift the sign is kept.

```text
-4      = 11111100
-4 >> 1 = 11111110   (-2)
```

```text
x      = 11110000
x >> 1 = 11111000   (left filled with 1, the sign bit)
```

The result is rounded toward negative infinity. The exact rule for negative numbers depends on the language, so be careful when using shifts as division.

### A shift does not wrap around

In a right shift, bits from the left are **not** moved to the right. Every bit moves one place right, the new left bit is filled (with `0` or the sign bit) and the rightmost bit is discarded.

```text
x      = 10110010
x >> 1 = 01011001   (logical)
```

## 4. Shift vs rotate

Moving the bit that falls off one end back in at the other end is called **rotation** (circular shift). In a rotation no bits are lost.

```text
x          = 10110010
rotate L 1 = 01100101   (leftmost bit goes to the right end)
rotate R 1 = 01011001   (rightmost bit goes to the left end)
```

## 5. Quick reference

| Operation | Result |
|---|---|
| `x << k` (unsigned) | `x × 2^k` |
| `x >> k` (unsigned) | `floor(x / 2^k)` |
| `x >> k` (signed) | sign bit is copied in (arithmetic shift) |
| shift | bits that fall off are lost |
| rotate | bits wrap around to the other end |
