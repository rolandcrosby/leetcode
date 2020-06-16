# Validate IP Address
# Write a function to check whether an ip string is a valid IPv4 address or IPv6
# address or neither.
#
# IPv4 addresses are canonically represented in dot-decimal notation, which consists of
# four decimal numbers, each ranging from 0 to 255, separated by dots ("."),
# e.g.,172.16.254.1;
#
# Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01
# is invalid.
#
# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group
# representing 16 bits. The groups are separated by colons (":"). For example, the
# address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit
# some leading zeros among four hexadecimal digits and some low-case characters in the
# address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6
# address(Omit leading zeros and using upper cases).
#
# However, we don't replace a consecutive group of zero value with a single empty group
# using two consecutive colons (::) to pursue simplicity. For example,
# 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
#
# Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
# 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
#
# Note: You may assume there is no extra space or special characters in the ip
# string.
#
# Example 1:
# ip: "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
#
# Example 2:
# ip: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
#
# Example 3:
# ip: "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.

import testlib


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.valid_ipv4_address(IP):
            return "IPv4"
        if self.valid_ipv6_address(IP):
            return "IPv6"
        return "Neither"

    def valid_ipv4_address(self, ip: str) -> bool:
        if not ip.isascii():
            return False
        idx = 0
        try:
            for _ in range(3):
                idx = self.consume_ipv4_chunk(ip, idx)
                idx = self.consume_literal(".", ip, idx)
            idx = self.consume_ipv4_chunk(ip, idx)
        except ValueError:
            return False
        return idx == len(ip)

    def consume_ipv4_chunk(self, ip: str, start: int) -> int:
        try:
            end = ip.index(".", start)
        except ValueError:
            end = len(ip)
        val = ip[start:end]
        if val.startswith("0") and len(val) > 1:
            raise ValueError("leading 0 at position {}", start)
        if not val.isdecimal():
            raise ValueError("non-numeric chunk at position {}: {}".format(start, val))
        num = int(val, base=10)
        if num > 255:
            raise ValueError("invalid byte at position {}: {}".format(start, val))
        return end

    def consume_literal(self, literal: str, ip: str, idx: int) -> int:
        if idx >= len(ip):
            raise ValueError(
                "expected {} at position {} but string ended", literal, idx
            )
        if ip[idx] == literal:
            return idx + 1
        else:
            raise ValueError(
                "expected {} at position {}, got {}".format(literal, idx, ip[idx])
            )

    def valid_ipv6_address(self, ip: str) -> bool:
        if not ip.isascii():
            return False
        idx = 0
        try:
            for _ in range(7):
                idx = self.consume_ipv6_chunk(ip, idx)
                idx = self.consume_literal(":", ip, idx)
            idx = self.consume_ipv6_chunk(ip, idx)
        except ValueError:
            return False
        return idx == len(ip)

    def consume_ipv6_chunk(self, ip: str, start: int) -> int:
        try:
            end = ip.index(":", start)
        except ValueError:
            end = len(ip)
        if end - start == 0:
            raise ValueError("empty chunk at position {}".format(start))
        if end - start > 4:
            raise ValueError(
                "chunk longer than 4 characters at position {}: {}".format(
                    start, ip[start:end]
                )
            )
        for i in range(start, end):
            char = ip[i]
            if not (char.isdecimal() or char.lower() in "abcdef"):
                raise ValueError("invalid hex digit at position {}: {}".format(i, char))
        return end


if __name__ == "__main__":
    testdata = [
        ("172.16.254.1", "IPv4"),
        ("172.16.254.0", "IPv4"),
        ("172.16.254.03", "Neither"),
        ("172.16.254", "Neither"),
        ("256.256.256.256", "Neither"),
        ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("02001:0db8:85a3:0:0:8A2E:0370:7334", "Neither"),
        ("2001:0db8:85a3::8A2E:0370:7334", "Neither"),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().validIPAddress(tc[0]), tc[1], tc),
        testdata,
    )
